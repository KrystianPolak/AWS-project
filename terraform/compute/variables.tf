variable "instance_type" {
  description = "Typ instancji EC2"
  type        = string
  default     = "t3.micro"
}

variable "ami_id" {
  description = "ID obrazu AMI (Ubuntu 24.04 we Frankfurcie)"
  type        = string
  default     = "ami-0084a47cc718c111a"
}

variable "server_name" {
  description = "Nazwa serwera w tagach"
  type        = string
  default     = "My-GitOps-Server"
}