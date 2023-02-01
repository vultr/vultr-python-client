# openapi_client.model.baremetal_ipv4.BaremetalIpv4

Bare Metal IPv4 information.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Bare Metal IPv4 information. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**ip** | str,  | str,  | The IPv4 address. | [optional] 
**netmask** | str,  | str,  | The IPv4 netmask in dot-decimal notation. | [optional] 
**gateway** | str,  | str,  | The gateway IP address. | [optional] 
**type** | str,  | str,  | The type of IP address.  * main_ip | [optional] 
**reverse** | str,  | str,  | The reverse DNS information for this IP address. | [optional] 
**mac_address** | str,  | str,  | The MAC address associated with this IP address. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../openapi-client/README.md#documentation-for-models) [[Back to API list]](../../openapi-client/README.md#documentation-for-api-endpoints) [[Back to README]](../../openapi-client/README.md)

