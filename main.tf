locals {
  tags = {
    environment = "dev"
    source = "terraformclous"
  }
}
resource "azurerm_resource_group" "rg" {
  name     = "tf-cloud-${local.tags.environment}-rg"
  location = "uksouth"
  tags =  local.tags
}
