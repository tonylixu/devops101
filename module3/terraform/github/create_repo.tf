resource "github_repository" "test-repo" {
  name        = "test-repo"
  description = "Test repo from Terraform"

  visibility = "public"

  template {
    owner      = "tonylixu"
    repository = "python-fastapi-template"
  }
}