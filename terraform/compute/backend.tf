terraform {
  backend "s3" {
    bucket         = "terraform-project-bucket-4727-1644-9083-eu"
    key            = "compute/terraform.tfstate" 
    region         = "eu-central-1"
    use_lockfile   = true
    encrypt        = true
  }
}