provider "aws" {
  region  = var.aws_region
  profile = "terraform"

  default_tags {
    tags = {
      Project   = "aws-eks-kubernetes-platform"
      ManagedBy = "Terraform"
    }
  }
}