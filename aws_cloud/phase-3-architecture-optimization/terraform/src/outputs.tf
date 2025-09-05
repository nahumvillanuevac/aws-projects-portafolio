output "s3_bucket_terraform_nahum" {
  value = aws_s3_bucket.static_site.id
}

output "cloudfront_url" {
  value = aws_cloudfront_distribution.cdn.domain_name
}
