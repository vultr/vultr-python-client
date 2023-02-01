# openapi_client.model.startup.Startup

Startup Script information.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Startup Script information. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  | A unique ID for the Startup Script. | [optional] 
**date_created** | str,  | str,  | The date the Startup Script was created. | [optional] 
**date_modified** | str,  | str,  | The date the Startup Script was last modified. | [optional] 
**name** | str,  | str,  | The user-supplied name of the Startup Script. | [optional] 
**script** | str,  | str,  | The base-64 encoded Startup Script. | [optional] 
**type** | str,  | str,  | The Startup Script type.  * boot * pxe | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../openapi-client/README.md#documentation-for-models) [[Back to API list]](../../openapi-client/README.md#documentation-for-api-endpoints) [[Back to README]](../../openapi-client/README.md)

