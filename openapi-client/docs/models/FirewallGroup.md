# openapi_client.model.firewall_group.FirewallGroup

Firewall Group information.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Firewall Group information. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  | A unique ID for the Firewall Group. | [optional] 
**description** | str,  | str,  | User-supplied description of this Firewall Group. | [optional] 
**date_created** | str,  | str,  | Date the Firewall Group was originally created. | [optional] 
**date_modified** | str,  | str,  | Date of the last modification to this Firewall Group. | [optional] 
**instance_count** | decimal.Decimal, int,  | decimal.Decimal,  | The number of instances linked to this Firewall Group. | [optional] 
**rule_count** | decimal.Decimal, int,  | decimal.Decimal,  | The number of rules in this Firewall Group. | [optional] 
**max_rule_count** | decimal.Decimal, int,  | decimal.Decimal,  | The maximum number of rules allowed for this Firewall Group. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../openapi-client/README.md#documentation-for-models) [[Back to API list]](../../openapi-client/README.md#documentation-for-api-endpoints) [[Back to README]](../../openapi-client/README.md)

