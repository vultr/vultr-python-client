# openapi_client.model.nodepools.Nodepools

NodePool

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | NodePool | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  | The [NodePool ID](#operation/get-nodepools). | [optional] 
**date_created** | str,  | str,  | Date of creation | [optional] 
**label** | str,  | str,  | Label for nodepool | [optional] 
**tag** | str,  | str,  | Tag for node pool | [optional] 
**plan** | str,  | str,  | Plan used for nodepool | [optional] 
**status** | str,  | str,  | Status for nodepool | [optional] 
**node_quantity** | decimal.Decimal, int,  | decimal.Decimal,  | Number of nodes in nodepool | [optional] 
**[nodes](#nodes)** | list, tuple,  | tuple,  |  | [optional] 
**date_updated** | str,  | str,  | Date the nodepool was updated. | [optional] 
**auto_scaler** | bool,  | BoolClass,  | Displays if the auto scaler is enabled or disabled for your cluster. | [optional] 
**min_nodes** | decimal.Decimal, int,  | decimal.Decimal,  | Auto scaler field that displays the minimum nodes you want for your cluster. | [optional] 
**max_nodes** | decimal.Decimal, int,  | decimal.Decimal,  | Auto scaler field that displays the maximum nodes you want for your cluster. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# nodes

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**NodepoolInstances**](NodepoolInstances.md) | [**NodepoolInstances**](NodepoolInstances.md) | [**NodepoolInstances**](NodepoolInstances.md) |  | 

[[Back to Model list]](../../openapi-client/README.md#documentation-for-models) [[Back to API list]](../../openapi-client/README.md#documentation-for-api-endpoints) [[Back to README]](../../openapi-client/README.md)

