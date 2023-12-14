variable "location" {
    description = "Location of the network"
    default     = "uksouth"
}

variable "username" {
    description = "Username for Virtual Machines"
    default     = "azureuser"
}

variable "password" {
    description = "Password for Virtual Machines"
    type = string
    sensitive = true
}

variable "vmsize" {
    description = "Size of the VMs"
    default     = "Standard_DS1_v2"
}

variable "onprem_address_space" {
    type=list(string)
    description = "on prem addresss space"
}