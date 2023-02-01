# openapi_client.model.application.Application

Application information.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Application information. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | decimal.Decimal, int,  | decimal.Decimal,  | A unique ID for the application. | [optional] 
**name** | str,  | str,  | The application name. | [optional] 
**short_name** | str,  | str,  | The short application name. | [optional] 
**deploy_name** | str,  | str,  | A long description of the application. | [optional] 
**type** | str,  | str,  | The type of application.  * one-click - use app_id to deploy one-click applications. * marketplace - use image_id to deploy marketplace applications. | [optional] 
**vendor** | str,  | str,  | The application vendor name. | [optional] 
**image_id** | str,  | str,  | A unique ID for marketplace applications. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../openapi-client/README.md#documentation-for-models) [[Back to API list]](../../openapi-client/README.md#documentation-for-api-endpoints) [[Back to README]](../../openapi-client/README.md)

