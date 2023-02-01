# openapi_client.model.plans_metal.PlansMetal

Plans for Bare Metal instances.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Plans for Bare Metal instances. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  | A unique ID for the Bare Metal Plan. | [optional] 
**cpu_count** | decimal.Decimal, int,  | decimal.Decimal,  | The number of CPUs in this Plan. | [optional] 
**cpu_model** | str,  | str,  | The CPU model type for this instance. | [optional] 
**cpu_threads** | decimal.Decimal, int,  | decimal.Decimal,  | The numner of supported threads for this instance. | [optional] 
**ram** | decimal.Decimal, int,  | decimal.Decimal,  | The amount of RAM in MB. | [optional] 
**disk** | str,  | str,  | The disk size in GB. | [optional] 
**bandwidth** | decimal.Decimal, int,  | decimal.Decimal,  | The monthly bandwidth quota in GB. | [optional] 
**[locations](#locations)** | list, tuple,  | tuple,  | An array of Regions where this plan is valid for use. | [optional] 
**type** | str,  | str,  | The plan type.  * SSD | [optional] 
**monthly_cost** | decimal.Decimal, int,  | decimal.Decimal,  | The monthly cost in US Dollars. | [optional] 
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

