variable "aws_region" {
  description = "AWS region used for the EKS platform"
  type        = string
  default     = "us-east-1"
}

variable "project_name" {
  description = "Name used for project resources"
  type        = string
  default     = "eks-kubernetes-platform"
}

variable "kubernetes_version" {
  description = "Kubernetes version for the EKS cluster"
  type        = string
  default     = "1.35"
}