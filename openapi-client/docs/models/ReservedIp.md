# openapi_client.model.reserved_ip.ReservedIp

Reserved IP information.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Reserved IP information. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  | A unique ID for the Reserved IP. | [optional] 
**region** | str,  | str,  | The [Region id](#operation/list-regions) where the Reserved IP is located. | [optional] 
**ip_type** | str,  | str,  | The type of IP address.  * v4 * v6 | [optional] 
**subnet** | str,  | str,  | The IP subnet. | [optional] 
**subnet_size** | decimal.Decimal, int,  | decimal.Decimal,  | The IP network size in bits. | [optional] 
**label** | str,  | str,  | The user-supplied label. | [optional] 
**instance_id** | str,  | str,  | The [Instance id](#operation/list-instances) attached to this Reserved IP. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../openapi-client/README.md#documentation-for-models) [[Back to API list]](../../openapi-client/README.md#documentation-for-api-endpoints) [[Back to README]](../../openapi-client/README.md)

