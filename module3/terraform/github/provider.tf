terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 4.0"
    }
  }
}

data "aws_ssm_parameter" "github_personal_token" {
  name = "tony-github-personal-token"
}

provider "aws" {
  region = "us-east-1"
  profile = "tomo"
}

# Configure the Github provider
provider "github" {
  token = "${data.aws_ssm_parameter.github_personal_token.value}"
}
