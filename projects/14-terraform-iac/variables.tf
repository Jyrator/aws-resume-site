variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "us-east-1"
}

variable "ses_email" {
  description = "Verified SES email address"
  type        = string
  default     = "ejirosaks@gmail.com"
}

variable "project_name" {
  description = "Project name prefix for all resources"
  type        = string
  default     = "ejiro-tf-contact"
}
