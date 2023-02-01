# openapi_client.model.snapshot.Snapshot

Snapshot information.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Snapshot information. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  | A unique ID for the Snapshot. | [optional] 
**date_created** | str,  | str,  | The date this snapshot was created. | [optional] 
**description** | str,  | str,  | The user-supplied description of the Snapshot. | [optional] 
**size** | decimal.Decimal, int,  | decimal.Decimal,  | The snapshot size in bytes. | [optional] 
**status** | str,  | str,  | The Snapshot status.  * pending * complete * deleted | [optional] 
**os_id** | decimal.Decimal, int,  | decimal.Decimal,  | The [Operating System id](#operation/list-os) for this Snapshot. | [optional] 
**app_id** | decimal.Decimal, int,  | decimal.Decimal,  | The [Application id](#operation/list-applications) for this snapshot. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../openapi-client/README.md#documentation-for-models) [[Back to API list]](../../openapi-client/README.md#documentation-for-api-endpoints) [[Back to README]](../../openapi-client/README.md)

