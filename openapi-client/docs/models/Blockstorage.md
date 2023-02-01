# openapi_client.model.blockstorage.Blockstorage

Block Storage information.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Block Storage information. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  | A unique ID for the Block Storage. | [optional] 
**cost** | decimal.Decimal, int,  | decimal.Decimal,  | The monthly cost of this Block Storage. | [optional] 
**status** | str,  | str,  | The current status of this Block Storage.  * active | [optional] 
**size_gb** | decimal.Decimal, int,  | decimal.Decimal,  | Size of the Block Storage in GB. | [optional] 
**region** | str,  | str,  | The [Region id](#operation/list-regions) where the Block Storage is located. | [optional] 
**attached_to_instance** | str,  | str,  | The [Instance id](#operation/list-instances) with this Block Storage attached. | [optional] 
**date_created** | str,  | str,  | The date this Block Storage was created. | [optional] 
**label** | str,  | str,  | The user-supplied label. | [optional] 
**mount_id** | str,  | str,  | An ID associated with the instance, when mounted the ID can be found in /dev/disk/by-id prefixed with virtio. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../openapi-client/README.md#documentation-for-models) [[Back to API list]](../../openapi-client/README.md#documentation-for-api-endpoints) [[Back to README]](../../openapi-client/README.md)

