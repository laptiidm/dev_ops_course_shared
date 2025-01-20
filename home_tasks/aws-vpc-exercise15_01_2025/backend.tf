terraform {
  backend "s3" {
    bucket         = "terraform-state-danit-devops"
    key            = "laptii.dm/terraform.tfstate"
    region         = "eu-central-1"
    encrypt        = true
  }
}
