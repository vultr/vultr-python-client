# openapi_client.model.baremetal.Baremetal

Bare Metal information.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Bare Metal information. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  | A unique ID for the Bare Metal instance. | [optional] 
**os** | str,  | str,  | The [Operating System name](#operation/list-os). | [optional] 
**ram** | str,  | str,  | Text description of the instances&#x27; RAM. | [optional] 
**disk** | str,  | str,  | Text description of the instances&#x27; disk configuration. | [optional] 
**main_ip** | str,  | str,  | The main IPv4 address. | [optional] 
**cpu_count** | decimal.Decimal, int,  | decimal.Decimal,  | Number of CPUs. | [optional] 
**region** | str,  | str,  | The [Region id](#operation/list-regions) where the instance is located. | [optional] 
**default_password** | str,  | str,  | The default password assigned at deployment. | [optional] 
**date_created** | str,  | str,  | The date this instance was created. | [optional] 
**status** | str,  | str,  | The current status.  * active * pending * suspended | [optional] 
**netmask_v4** | str,  | str,  | The IPv4 netmask in dot-decimal notation. | [optional] 
**gateway_v4** | str,  | str,  | The IPv4 gateway address. | [optional] 
**plan** | str,  | str,  | The [Bare Metal Plan id](#operation/list-metal-plans) used by this instance. | [optional] 
**label** | str,  | str,  | The user-supplied label for this instance. | [optional] 
**tag** | str,  | str,  | Use &#x60;tags&#x60; instead. The user-supplied tag for this instance. | [optional] 
**os_id** | decimal.Decimal, int,  | decimal.Decimal,  | The [Operating System id](#operation/list-os). | [optional] 
**app_id** | decimal.Decimal, int,  | decimal.Decimal,  | The [Application id](#operation/list-applications). | [optional] 
**image_id** | str,  | str,  | The [Application image_id](#operation/list-applications). | [optional] 
**v6_network** | str,  | str,  | The IPv6 network size in bits. | [optional] 
**v6_main_ip** | str,  | str,  | The main IPv6 network address. | [optional] 
**v6_network_size** | decimal.Decimal, int,  | decimal.Decimal,  | The IPv6 subnet. | [optional] 
**mac_address** | decimal.Decimal, int,  | decimal.Decimal,  | The MAC address for a Bare Metal server | [optional] 
**[tags](#tags)** | list, tuple,  | tuple,  | Tags to apply to the instance | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# tags

Tags to apply to the instance

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Tags to apply to the instance | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../openapi-client/README.md#documentation-for-models) [[Back to API list]](../../openapi-client/README.md#documentation-for-api-endpoints) [[Back to README]](../../openapi-client/README.md)

