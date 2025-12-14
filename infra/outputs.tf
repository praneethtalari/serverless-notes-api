output "api_url" {
  description = "Base URL of the Notes HTTP API"
  value       = aws_apigatewayv2_api.http_api.api_endpoint
}

output "notes_endpoint" {
  description = "Full /notes endpoint for CRUD operations"
  value       = "${aws_apigatewayv2_api.http_api.api_endpoint}/notes"
}
