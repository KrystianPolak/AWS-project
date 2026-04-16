terraform {
  backend "s3" {
    bucket         = "terraform-project-bucket-4727-1644-9083-eu " 
    key            = "state/terraform.tfstate"
    region         = "eu-central-1"
    dynamodb_table = "terraform-lock"               
    encrypt        = true
  }
}