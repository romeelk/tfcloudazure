# Getting started with TFCloud and Azure

## Create SPN

Create SPN to authenticate your TF workspace:

```
az account show
az account set --subscription "sub_guid"
az ad sp create-for-rbac --name "tfcloudazurespn" --role="Contributor" --scopes="/subscriptions/sub_guid"
```


## Set SPN as TF env var in TF Cloud

To get your plan, apply to work set the TF Azure env vars as variables in your workspace in TF Cloud

From the output of the azure ad spn command set the following:

```
$ $Env:ARM_CLIENT_ID = "fda5aed3-5c19-4295-853f-7870bfbd2a1c"
$ $Env:ARM_CLIENT_SECRET = "<PASSWORD_VALUE>"
$ $Env:ARM_SUBSCRIPTION_ID = "<SUBSCRIPTION_ID>"
$ $Env:ARM_TENANT_ID = "<TENANT_VALUE>"

```

## Integrating Gibhub Actions with TFCloud

