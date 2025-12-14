#############################################
# CLOUDWATCH LOG GROUP FOR LAMBDA
#############################################

resource "aws_cloudwatch_log_group" "lambda_log_group" {
  name              = "/aws/lambda/${aws_lambda_function.notes_lambda.function_name}"
  retention_in_days = 14

  tags = {
    Project = "serverless-notes-api"
  }
}

#############################################
# CLOUDWATCH ALARM — LAMBDA ERRORS
#############################################

resource "aws_cloudwatch_metric_alarm" "lambda_error_alarm" {
  alarm_name          = "notes-lambda-errors"
  comparison_operator = "GreaterThanThreshold"
  evaluation_periods  = 1
  metric_name         = "Errors"
  namespace           = "AWS/Lambda"
  period              = 60
  statistic           = "Sum"
  threshold           = 1

  dimensions = {
    FunctionName = aws_lambda_function.notes_lambda.function_name
  }

  alarm_description = "Triggers when the Lambda function generates any errors."
  alarm_actions     = [] # Optional: SNS ARN if you add notifications
}

#############################################
# CLOUDWATCH ALARM — API GATEWAY 5xx ERRORS
#############################################

resource "aws_cloudwatch_metric_alarm" "api_5xx_alarm" {
  alarm_name          = "notes-api-5xx-errors"
  comparison_operator = "GreaterThanThreshold"
  evaluation_periods  = 1
  metric_name         = "5xxError"
  namespace           = "AWS/ApiGateway"
  period              = 60
  statistic           = "Sum"
  threshold           = 1

  dimensions = {
    ApiId = aws_apigatewayv2_api.http_api.id
  }

  alarm_description = "Triggers when API Gateway returns 5xx errors."
  alarm_actions     = []
}

#############################################
# CLOUDWATCH ALARM — DYNAMODB THROTTLES
#############################################

resource "aws_cloudwatch_metric_alarm" "dynamodb_throttle_alarm" {
  alarm_name          = "notes-dynamodb-throttles"
  comparison_operator = "GreaterThanThreshold"
  evaluation_periods  = 1
  metric_name         = "ThrottledRequests"
  namespace           = "AWS/DynamoDB"
  period              = 60
  statistic           = "Sum"
  threshold           = 0

  dimensions = {
    TableName = aws_dynamodb_table.notes.name
  }

  alarm_description = "Triggers when DynamoDB throttles requests (should always be zero)."
  alarm_actions     = []
}
