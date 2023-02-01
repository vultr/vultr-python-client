# openapi_client.model.vke_cluster.VkeCluster

VKE Cluster

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | VKE Cluster | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  | ID for the VKE cluster | [optional] 
**label** | str,  | str,  | Label for your cluster | [optional] 
**date_created** | str,  | str,  | Date of creation | [optional] 
**cluster_subnet** | str,  | str,  | IP range that your pods will run on in this cluster | [optional] 
**service_subnet** | str,  | str,  | IP range that services will run on this cluster | [optional] 
**ip** | str,  | str,  | IP for your Kubernetes Clusters Control Plane | [optional] 
**endpoint** | str,  | str,  | Domain for your Kubernetes Clusters Control Plane | [optional] 
**version** | str,  | str,  | Version of Kubernetes this cluster is running on | [optional] 
**region** | str,  | str,  | Region this Kubernetes Cluster is running in | [optional] 
**status** | str,  | str,  | Status for VKE cluster | [optional] 
**[node_pools](#node_pools)** | list, tuple,  | tuple,  | NodePools in this cluster | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# node_pools

NodePools in this cluster

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | NodePools in this cluster | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Nodepools**](Nodepools.md) | [**Nodepools**](Nodepools.md) | [**Nodepools**](Nodepools.md) |  | 

[[Back to Model list]](../../openapi-client/README.md#documentation-for-models) [[Back to API list]](../../openapi-client/README.md#documentation-for-api-endpoints) [[Back to README]](../../openapi-client/README.md)

