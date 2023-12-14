import os
import sys
from azure.identity import AzureCliCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.resource.resources.models import TagsResource

print("Authenticating with Azure RM")
credential = AzureCliCredential()

subscription_id = os.environ["AZURE_SUBSCRIPTION_ID"]

if len(subscription_id) == 0:
    print("please set the AZURE_SUBSCRIPTION_ID env var")
    sys.exit(-1)

def create_resource_group(resource_group_name:str):
    try:

        tags = {
            "environment": "dev",
            "author": "romeel"
        }
        tag_resource = TagsResource(properties={'tags': tags})

        resource_client = ResourceManagementClient(credential, subscription_id)

        print("Attempting to create resource group")
        resource_client.resource_groups.create_or_update(resource_group_name, {"location": "centralus"})

        resource_group = resource_client.resource_groups.get(resource_group_name)
        
        print(f"Attempting to tag resource group with Id {resource_group.id}")
      
        resource_client.tags.begin_create_or_update_at_scope(resource_group.id, tag_resource)
    except:
        print("An error occured authenticating to Azure")

def check_if_resource_group_exists(resource_group_name:str):

    resource_client = ResourceManagementClient(credential, subscription_id)

    print("Attempting to check resource group")
    exists = resource_client.resource_groups.check_existence(resource_group_name)
    return exists

def list_tags(resource_group_name):
    resource_client = ResourceManagementClient(credential, subscription_id)

    resource_group = resource_client.resource_groups.get(resource_group_name)
    resource_tags = resource_client.tags.get_at_scope(resource_group.id)
    print(f"No of tags found in resource group: {(len(resource_tags.properties.tags))}")


resource_group_name = "python_test_rg"
create_resource_group(resource_group_name)
exists = check_if_resource_group_exists("python_test_rg")
print(f"Resource group exists: {exists} ")
list_tags(resource_group_name)