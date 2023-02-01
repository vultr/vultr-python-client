# openapi_client.model.plans.Plans

Plans for VPS instances.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Plans for VPS instances. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  | A unique ID for the Plan. | [optional] 
**name** | str,  | str,  | The Plan name. | [optional] 
**vcpu_count** | decimal.Decimal, int,  | decimal.Decimal,  | The number of vCPUs in this Plan. | [optional] 
**ram** | decimal.Decimal, int,  | decimal.Decimal,  | The amount of RAM in MB. | [optional] 
**disk** | decimal.Decimal, int,  | decimal.Decimal,  | The disk size in GB. | [optional] 
**bandwidth** | decimal.Decimal, int,  | decimal.Decimal,  | The monthly bandwidth quota in GB. | [optional] 
**monthly_cost** | decimal.Decimal, int,  | decimal.Decimal,  | The monthly cost in US Dollars. | [optional] 
**type** | str,  | str,  | The plan type.  |   | Type | Description | | - | ------ | ------------- | |   | vc2 | Cloud Compute | |   | vhf | High Frequency Compute | |   | vdc | Dedicated Cloud | | [optional] 
**[locations](#locations)** | list, tuple,  | tuple,  | An array of Regions where this plan is valid for use. | [optional] 
**disk_count** | decimal.Decimal, int,  | decimal.Decimal,  | The number of disks that this plan offers. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# locations

An array of Regions where this plan is valid for use.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | An array of Regions where this plan is valid for use. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../openapi-client/README.md#documentation-for-models) [[Back to API list]](../../openapi-client/README.md#documentation-for-api-endpoints) [[Back to README]](../../openapi-client/README.md)

