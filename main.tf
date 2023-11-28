locals {
  tags = {
    environment = "dev"
    source = "terraformcloud"
    org = "example"
    component = "infrastructure"
  }
}
resource "azurerm_resource_group" "rg" {
  name     = "tf-cloud-${local.tags.environment}-rg"
  location = "uksouth"
  tags =  local.tags
}
