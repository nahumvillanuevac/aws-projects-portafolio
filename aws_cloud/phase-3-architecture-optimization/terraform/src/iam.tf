resource "aws_iam_role" "terraform_deploy" {
  name = "phase3-deploy-role-nahum"
  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
      Effect = "Allow",
      Principal = { Service = "ec2.amazonaws.com" },
      Action = "sts:AssumeRole"
      }
    ]
  })
}

resource "aws_iam_policy" "terraform_policy" {
  name        = "phase3-terraform-policy"
  description = "Least-privilege policy for deploying S3 + Cloudfront"
  policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
    { Action = ["s3:*"], Effect = "Allow", Resource = "*" },
    { Action = ["cloudfront:*"], Effect = "Allow", Resource = "*" },
    ]
  })
}

resource "aws_iam_role_policy_attachment" "attach" {
  role       = aws_iam_role.terraform_deploy.name
  policy_arn = aws_iam_policy.terraform_policy.arn
}
