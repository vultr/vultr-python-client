# openapi_client.model.object_storage.ObjectStorage

Object Storage information.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Object Storage information. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  | A unique ID for the Object Storage. | [optional] 
**date_created** | str,  | str,  | Date the Object Store was created. | [optional] 
**cluster_id** | decimal.Decimal, int,  | decimal.Decimal,  | The [Cluster id](#operation/list-object-storage-clusters). | [optional] 
**region** | str,  | str,  | The [Region id](#operation/list-regions) for this Object Storage. | [optional] 
**label** | str,  | str,  | The user-supplied label for this Object Storage. | [optional] 
**status** | str,  | str,  | The status of this Object Storage.  * active * pending | [optional] 
**s3_hostname** | str,  | str,  | The [Cluster hostname](#operation/list-object-storage-clusters) for this Object Storage. | [optional] 
**s3_access_key** | str,  | str,  | The Object Storage access key. | [optional] 
**s3_secret_key** | str,  | str,  | The Object Storage secret key. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../openapi-client/README.md#documentation-for-models) [[Back to API list]](../../openapi-client/README.md#documentation-for-api-endpoints) [[Back to README]](../../openapi-client/README.md)

