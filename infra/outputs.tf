output "api_url" {
  value = aws_apigatewayv2_api.http_api.api_endpoint
}

output "api_url_stage" {
  value = aws_apigatewayv2_stage.default.invoke_url
}
