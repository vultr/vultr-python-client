# openapi_client.model.vpc.Vpc

VPC information.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | VPC information. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  | A unique ID for the VPC. | 
**region** | str,  | str,  | The [Region id](#operation/list-regions) where the VPC is located. | [optional] 
**date_created** | str,  | str,  | Date the VPC was created. | [optional] 
**description** | str,  | str,  | A description of the VPC. | [optional] 
**v4_subnet** | str,  | str,  | The IPv4 VPC address. For example: 10.99.0.0 | [optional] 
**v4_subnet_mask** | decimal.Decimal, int,  | decimal.Decimal,  | The number of bits for the netmask in CIDR notation. Example: 24 | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../openapi-client/README.md#documentation-for-models) [[Back to API list]](../../openapi-client/README.md#documentation-for-api-endpoints) [[Back to README]](../../openapi-client/README.md)

