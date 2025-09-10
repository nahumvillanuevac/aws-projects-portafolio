# Create file in a local machine using Terraform
resource "null_resource" "file" {
    provisioner "local-exec" {
        command = "echo 'Message: ${upper("hello world!")}' > hello.txt "
    }
}