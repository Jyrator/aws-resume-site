output "api_endpoint" {
  description = "Contact form API endpoint"
  value       = "${aws_api_gateway_stage.contact_stage.invoke_url}/contact"
}

output "s3_bucket_name" {
  description = "Frontend S3 bucket name"
  value       = aws_s3_bucket.frontend.bucket
}

output "lambda_function_name" {
  description = "Lambda function name"
  value       = aws_lambda_function.contact_form.function_name
}
