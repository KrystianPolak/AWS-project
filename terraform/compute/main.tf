data "terraform_remote_state" "network" {
  backend = "s3"
  config = {
    bucket = "terraform-project-bucket-4727-1644-9083-eu"
    key    = "network/terraform.tfstate" 
    region = "eu-central-1"
  }
}

resource "aws_security_group" "allow_ssh_http" {
  name        = "allow_ssh_http"
  description = "Pozwol na SSH i HTTP"
  vpc_id      = data.terraform_remote_state.network.outputs.vpc_id

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_key_pair" "deployer" {
  key_name   = "aws-key"
  public_key = file(pathexpand("~/.ssh/id_ed25519.pub"))
}

resource "aws_instance" "web_server" {
  ami           = var.ami_id           
  instance_type = var.instance_type    
  
  subnet_id              = data.terraform_remote_state.network.outputs.subnet_id
  vpc_security_group_ids = [aws_security_group.allow_ssh_http.id]
  key_name               = aws_key_pair.deployer.key_name

  tags = {
    Name = var.server_name             
  }
}


output "server_public_ip" {
  value = aws_instance.web_server.public_ip
}