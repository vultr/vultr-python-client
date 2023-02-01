<a name="__pageTop"></a>
# openapi_client.apis.tags.kubernetes_api.KubernetesApi

All URIs are relative to *https://api.vultr.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_kubernetes_cluster**](#create_kubernetes_cluster) | **post** /kubernetes/clusters | Create Kubernetes Cluster
[**create_nodepools**](#create_nodepools) | **post** /kubernetes/clusters/{vke-id}/node-pools | Create NodePool
[**delete_kubernetes_cluster**](#delete_kubernetes_cluster) | **delete** /kubernetes/clusters/{vke-id} | Delete Kubernetes Cluster
[**delete_kubernetes_cluster_vke_id_delete_with_linked_resources**](#delete_kubernetes_cluster_vke_id_delete_with_linked_resources) | **delete** /kubernetes/clusters/{vke-id}/delete-with-linked-resources | Delete VKE Cluster and All Related Resources
[**delete_nodepool**](#delete_nodepool) | **delete** /kubernetes/clusters/{vke-id}/node-pools/{nodepool-id} | Delete Nodepool
[**delete_nodepool_instance**](#delete_nodepool_instance) | **delete** /kubernetes/clusters/{vke-id}/node-pools/{nodepool-id}/nodes/{node-id} | Delete NodePool Instance
[**get_kubernetes_available_upgrades**](#get_kubernetes_available_upgrades) | **get** /kubernetes/clusters/{vke-id}/available-upgrades | Get Kubernetes Available Upgrades
[**get_kubernetes_clusters**](#get_kubernetes_clusters) | **get** /kubernetes/clusters/{vke-id} | Get Kubernetes Cluster
[**get_kubernetes_clusters_config**](#get_kubernetes_clusters_config) | **get** /kubernetes/clusters/{vke-id}/config | Get Kubernetes Cluster Kubeconfig
[**get_kubernetes_resources**](#get_kubernetes_resources) | **get** /kubernetes/clusters/{vke-id}/resources | Get Kubernetes Resources
[**get_kubernetes_versions**](#get_kubernetes_versions) | **get** /kubernetes/versions | Get Kubernetes Versions
[**get_nodepool**](#get_nodepool) | **get** /kubernetes/clusters/{vke-id}/node-pools/{nodepool-id} | Get NodePool
[**get_nodepools**](#get_nodepools) | **get** /kubernetes/clusters/{vke-id}/node-pools | List NodePools
[**list_kubernetes_clusters**](#list_kubernetes_clusters) | **get** /kubernetes/clusters | List all Kubernetes Clusters
[**recycle_nodepool_instance**](#recycle_nodepool_instance) | **post** /kubernetes/clusters/{vke-id}/node-pools/{nodepool-id}/nodes/{node-id}/recycle | Recycle a NodePool Instance
[**start_kubernetes_cluster_upgrade**](#start_kubernetes_cluster_upgrade) | **post** /kubernetes/clusters/{vke-id}/upgrades | Start Kubernetes Cluster Upgrade
[**update_kubernetes_cluster**](#update_kubernetes_cluster) | **put** /kubernetes/clusters/{vke-id} | Update Kubernetes Cluster
[**update_nodepool**](#update_nodepool) | **patch** /kubernetes/clusters/{vke-id}/node-pools/{nodepool-id} | Update Nodepool

# **create_kubernetes_cluster**
<a name="create_kubernetes_cluster"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_kubernetes_cluster()

Create Kubernetes Cluster

Create Kubernetes Cluster

### Example

* Bearer Authentication (APIKey):
```python
import openapi_client
from openapi_client.apis.tags import kubernetes_api
from openapi_client.model.vke_cluster import VkeCluster
from pprint import pprint
# Defining the host is optional and defaults to https://api.vultr.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.vultr.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: APIKey
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kubernetes_api.KubernetesApi(api_client)

    # example passing only optional values
    body = dict(
        label="label_example",
        region="region_example",
        version="version_example",
        node_pools=[
            dict(
                node_quantity=1,
                label="label_example",
                plan="plan_example",
                tag="tag_example",
                auto_scaler=True,
                min_nodes=1,
                max_nodes=1,
            )
        ],
    )
    try:
        # Create Kubernetes Cluster
        api_response = api_instance.create_kubernetes_cluster(
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KubernetesApi->create_kubernetes_cluster: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**region** | str,  | str,  | Region you want to deploy VKE in. See [Regions](#tag/region) for more information. | 
**version** | str,  | str,  | Version of Kubernetes you want to deploy. | 
**label** | str,  | str,  | The label for your Kubernetes cluster. | [optional] 
**[node_pools](#node_pools)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# node_pools

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**node_quantity** | decimal.Decimal, int,  | decimal.Decimal,  | Number of instances to deploy in this nodepool. Minimum of 1 node required, but at least 3 is recommended. | 
**label** | str,  | str,  | Label for this nodepool. You cannot change the label after a nodepool is created. You cannot have duplicate node pool labels in the same cluster. | 
**plan** | str,  | str,  | Plan you want this nodepool to use. Note: minimum plan must be $10 | 
**tag** | str,  | str,  | Tag for node pool | [optional] 
**auto_scaler** | bool,  | BoolClass,  | Option to use the auto scaler with your cluster. Default false. | [optional] 
**min_nodes** | decimal.Decimal, int,  | decimal.Decimal,  | Auto scaler field for minimum nodes you want for your cluster. Default 1. | [optional] 
**max_nodes** | decimal.Decimal, int,  | decimal.Decimal,  | Auto scaler field for maximum nodes you want for your cluster. Default 1. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#create_kubernetes_cluster.ApiResponseFor201) | Created
400 | [ApiResponseFor400](#create_kubernetes_cluster.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#create_kubernetes_cluster.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#create_kubernetes_cluster.ApiResponseFor404) | Not Found

#### create_kubernetes_cluster.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**vke_cluster** | [**VkeCluster**]({{complexTypePrefix}}VkeCluster.md) | [**VkeCluster**]({{complexTypePrefix}}VkeCluster.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### create_kubernetes_cluster.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### create_kubernetes_cluster.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### create_kubernetes_cluster.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[APIKey](../../../openapi-client/README.md#APIKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../openapi-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../openapi-client/README.md#documentation-for-models) [[Back to README]](../../../openapi-client/README.md)

# **create_nodepools**
<a name="create_nodepools"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_nodepools(vke_id)

Create NodePool

Create NodePool for a Existing Kubernetes Cluster

### Example

* Bearer Authentication (APIKey):
```python
import openapi_client
from openapi_client.apis.tags import kubernetes_api
from openapi_client.model.nodepools import Nodepools
from pprint import pprint
# Defining the host is optional and defaults to https://api.vultr.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.vultr.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: APIKey
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kubernetes_api.KubernetesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'vke-id': "vke-id_example",
    }
    try:
        # Create NodePool
        api_response = api_instance.create_nodepools(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KubernetesApi->create_nodepools: %s\n" % e)

    # example passing only optional values
    path_params = {
        'vke-id': "vke-id_example",
    }
    body = dict(
        node_quantity=1,
        label="label_example",
        plan="plan_example",
        tag="tag_example",
        auto_scaler=True,
        min_nodes=1,
        max_nodes=1,
    )
    try:
        # Create NodePool
        api_response = api_instance.create_nodepools(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KubernetesApi->create_nodepools: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**node_quantity** | decimal.Decimal, int,  | decimal.Decimal,  | Number of instances in this nodepool | 
**label** | str,  | str,  | Label for the nodepool. You cannot change the label after a nodepool is created. You cannot have duplicate node pool labels in the same cluster. | 
**plan** | str,  | str,  | Plan that this nodepool will use | 
**tag** | str,  | str,  | Tag for node pool | [optional] 
**auto_scaler** | bool,  | BoolClass,  | Option to use the auto scaler with your cluster. Default false. | [optional] 
**min_nodes** | decimal.Decimal, int,  | decimal.Decimal,  | Auto scaler field for minimum nodes you want for your cluster. Default 1. | [optional] 
**max_nodes** | decimal.Decimal, int,  | decimal.Decimal,  | Auto scaler field for maximum nodes you want for your cluster. Default 1. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
vke-id | VkeIdSchema | | 

# VkeIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#create_nodepools.ApiResponseFor201) | Created
400 | [ApiResponseFor400](#create_nodepools.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#create_nodepools.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#create_nodepools.ApiResponseFor404) | Not Found

#### create_nodepools.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**node_pool** | [**Nodepools**]({{complexTypePrefix}}Nodepools.md) | [**Nodepools**]({{complexTypePrefix}}Nodepools.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### create_nodepools.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### create_nodepools.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### create_nodepools.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[APIKey](../../../openapi-client/README.md#APIKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../openapi-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../openapi-client/README.md#documentation-for-models) [[Back to README]](../../../openapi-client/README.md)

# **delete_kubernetes_cluster**
<a name="delete_kubernetes_cluster"></a>
> delete_kubernetes_cluster(vke_id)

Delete Kubernetes Cluster

Delete Kubernetes Cluster

### Example

* Bearer Authentication (APIKey):
```python
import openapi_client
from openapi_client.apis.tags import kubernetes_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.vultr.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.vultr.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: APIKey
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kubernetes_api.KubernetesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'vke-id': "vke-id_example",
    }
    try:
        # Delete Kubernetes Cluster
        api_response = api_instance.delete_kubernetes_cluster(
            path_params=path_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling KubernetesApi->delete_kubernetes_cluster: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
vke-id | VkeIdSchema | | 

# VkeIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#delete_kubernetes_cluster.ApiResponseFor204) | No Content
400 | [ApiResponseFor400](#delete_kubernetes_cluster.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#delete_kubernetes_cluster.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#delete_kubernetes_cluster.ApiResponseFor404) | Not Found

#### delete_kubernetes_cluster.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_kubernetes_cluster.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_kubernetes_cluster.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_kubernetes_cluster.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[APIKey](../../../openapi-client/README.md#APIKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../openapi-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../openapi-client/README.md#documentation-for-models) [[Back to README]](../../../openapi-client/README.md)

# **delete_kubernetes_cluster_vke_id_delete_with_linked_resources**
<a name="delete_kubernetes_cluster_vke_id_delete_with_linked_resources"></a>
> delete_kubernetes_cluster_vke_id_delete_with_linked_resources(vke_id)

Delete VKE Cluster and All Related Resources

Delete Kubernetes Cluster and all related resources. 

### Example

* Bearer Authentication (APIKey):
```python
import openapi_client
from openapi_client.apis.tags import kubernetes_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.vultr.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.vultr.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: APIKey
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kubernetes_api.KubernetesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'vke-id': "vke-id_example",
    }
    try:
        # Delete VKE Cluster and All Related Resources
        api_response = api_instance.delete_kubernetes_cluster_vke_id_delete_with_linked_resources(
            path_params=path_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling KubernetesApi->delete_kubernetes_cluster_vke_id_delete_with_linked_resources: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
vke-id | VkeIdSchema | | 

# VkeIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#delete_kubernetes_cluster_vke_id_delete_with_linked_resources.ApiResponseFor204) | No Content
400 | [ApiResponseFor400](#delete_kubernetes_cluster_vke_id_delete_with_linked_resources.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#delete_kubernetes_cluster_vke_id_delete_with_linked_resources.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#delete_kubernetes_cluster_vke_id_delete_with_linked_resources.ApiResponseFor404) | Not Found

#### delete_kubernetes_cluster_vke_id_delete_with_linked_resources.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_kubernetes_cluster_vke_id_delete_with_linked_resources.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_kubernetes_cluster_vke_id_delete_with_linked_resources.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_kubernetes_cluster_vke_id_delete_with_linked_resources.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[APIKey](../../../openapi-client/README.md#APIKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../openapi-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../openapi-client/README.md#documentation-for-models) [[Back to README]](../../../openapi-client/README.md)

# **delete_nodepool**
<a name="delete_nodepool"></a>
> delete_nodepool(vke_idnodepool_id)

Delete Nodepool

Delete a NodePool from a Kubernetes Cluster

### Example

* Bearer Authentication (APIKey):
```python
import openapi_client
from openapi_client.apis.tags import kubernetes_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.vultr.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.vultr.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: APIKey
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kubernetes_api.KubernetesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'vke-id': "vke-id_example",
        'nodepool-id': "nodepool-id_example",
    }
    try:
        # Delete Nodepool
        api_response = api_instance.delete_nodepool(
            path_params=path_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling KubernetesApi->delete_nodepool: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
vke-id | VkeIdSchema | | 
nodepool-id | NodepoolIdSchema | | 

# VkeIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# NodepoolIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#delete_nodepool.ApiResponseFor204) | No Content
400 | [ApiResponseFor400](#delete_nodepool.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#delete_nodepool.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#delete_nodepool.ApiResponseFor404) | Not Found

#### delete_nodepool.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_nodepool.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_nodepool.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_nodepool.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[APIKey](../../../openapi-client/README.md#APIKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../openapi-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../openapi-client/README.md#documentation-for-models) [[Back to README]](../../../openapi-client/README.md)

# **delete_nodepool_instance**
<a name="delete_nodepool_instance"></a>
> delete_nodepool_instance(vke_idnodepool_idnode_id)

Delete NodePool Instance

Delete a single nodepool instance from a given Nodepool

### Example

* Bearer Authentication (APIKey):
```python
import openapi_client
from openapi_client.apis.tags import kubernetes_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.vultr.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.vultr.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: APIKey
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kubernetes_api.KubernetesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'vke-id': "vke-id_example",
        'nodepool-id': "nodepool-id_example",
        'node-id': "node-id_example",
    }
    try:
        # Delete NodePool Instance
        api_response = api_instance.delete_nodepool_instance(
            path_params=path_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling KubernetesApi->delete_nodepool_instance: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
vke-id | VkeIdSchema | | 
nodepool-id | NodepoolIdSchema | | 
node-id | NodeIdSchema | | 

# VkeIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# NodepoolIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# NodeIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#delete_nodepool_instance.ApiResponseFor204) | No Content
400 | [ApiResponseFor400](#delete_nodepool_instance.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#delete_nodepool_instance.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#delete_nodepool_instance.ApiResponseFor404) | Not Found

#### delete_nodepool_instance.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_nodepool_instance.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_nodepool_instance.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_nodepool_instance.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[APIKey](../../../openapi-client/README.md#APIKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../openapi-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../openapi-client/README.md#documentation-for-models) [[Back to README]](../../../openapi-client/README.md)

# **get_kubernetes_available_upgrades**
<a name="get_kubernetes_available_upgrades"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_kubernetes_available_upgrades(vke_id)

Get Kubernetes Available Upgrades

Get the available upgrades for the specified Kubernetes cluster.

### Example

* Bearer Authentication (APIKey):
```python
import openapi_client
from openapi_client.apis.tags import kubernetes_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.vultr.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.vultr.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: APIKey
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kubernetes_api.KubernetesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'vke-id': "vke-id_example",
    }
    try:
        # Get Kubernetes Available Upgrades
        api_response = api_instance.get_kubernetes_available_upgrades(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KubernetesApi->get_kubernetes_available_upgrades: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
vke-id | VkeIdSchema | | 

# VkeIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_kubernetes_available_upgrades.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#get_kubernetes_available_upgrades.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#get_kubernetes_available_upgrades.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#get_kubernetes_available_upgrades.ApiResponseFor404) | Not Found

#### get_kubernetes_available_upgrades.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[available_upgrades](#available_upgrades)** | list, tuple,  | tuple,  | Array of available upgrade version strings | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# available_upgrades

Array of available upgrade version strings

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Array of available upgrade version strings | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

#### get_kubernetes_available_upgrades.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_kubernetes_available_upgrades.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_kubernetes_available_upgrades.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[APIKey](../../../openapi-client/README.md#APIKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../openapi-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../openapi-client/README.md#documentation-for-models) [[Back to README]](../../../openapi-client/README.md)

# **get_kubernetes_clusters**
<a name="get_kubernetes_clusters"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_kubernetes_clusters(vke_id)

Get Kubernetes Cluster

Get Kubernetes Cluster

### Example

* Bearer Authentication (APIKey):
```python
import openapi_client
from openapi_client.apis.tags import kubernetes_api
from openapi_client.model.vke_cluster import VkeCluster
from pprint import pprint
# Defining the host is optional and defaults to https://api.vultr.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.vultr.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: APIKey
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kubernetes_api.KubernetesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'vke-id': "vke-id_example",
    }
    try:
        # Get Kubernetes Cluster
        api_response = api_instance.get_kubernetes_clusters(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KubernetesApi->get_kubernetes_clusters: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
vke-id | VkeIdSchema | | 

# VkeIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_kubernetes_clusters.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#get_kubernetes_clusters.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#get_kubernetes_clusters.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#get_kubernetes_clusters.ApiResponseFor404) | Not Found

#### get_kubernetes_clusters.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**vke_cluster** | [**VkeCluster**]({{complexTypePrefix}}VkeCluster.md) | [**VkeCluster**]({{complexTypePrefix}}VkeCluster.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### get_kubernetes_clusters.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_kubernetes_clusters.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_kubernetes_clusters.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[APIKey](../../../openapi-client/README.md#APIKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../openapi-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../openapi-client/README.md#documentation-for-models) [[Back to README]](../../../openapi-client/README.md)

# **get_kubernetes_clusters_config**
<a name="get_kubernetes_clusters_config"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_kubernetes_clusters_config(vke_id)

Get Kubernetes Cluster Kubeconfig

Get Kubernetes Cluster Kubeconfig

### Example

* Bearer Authentication (APIKey):
```python
import openapi_client
from openapi_client.apis.tags import kubernetes_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.vultr.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.vultr.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: APIKey
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kubernetes_api.KubernetesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'vke-id': "vke-id_example",
    }
    try:
        # Get Kubernetes Cluster Kubeconfig
        api_response = api_instance.get_kubernetes_clusters_config(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KubernetesApi->get_kubernetes_clusters_config: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
vke-id | VkeIdSchema | | 

# VkeIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_kubernetes_clusters_config.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#get_kubernetes_clusters_config.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#get_kubernetes_clusters_config.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#get_kubernetes_clusters_config.ApiResponseFor404) | Not Found

#### get_kubernetes_clusters_config.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**kube_config** | str,  | str,  | Base64 encoded KubeConfig | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### get_kubernetes_clusters_config.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_kubernetes_clusters_config.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_kubernetes_clusters_config.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[APIKey](../../../openapi-client/README.md#APIKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../openapi-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../openapi-client/README.md#documentation-for-models) [[Back to README]](../../../openapi-client/README.md)

# **get_kubernetes_resources**
<a name="get_kubernetes_resources"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_kubernetes_resources(vke_id)

Get Kubernetes Resources

Get the block storage volumes and load balancers deployed by the specified Kubernetes cluster.

### Example

* Bearer Authentication (APIKey):
```python
import openapi_client
from openapi_client.apis.tags import kubernetes_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.vultr.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.vultr.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: APIKey
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kubernetes_api.KubernetesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'vke-id': "vke-id_example",
    }
    try:
        # Get Kubernetes Resources
        api_response = api_instance.get_kubernetes_resources(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KubernetesApi->get_kubernetes_resources: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
vke-id | VkeIdSchema | | 

# VkeIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_kubernetes_resources.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#get_kubernetes_resources.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#get_kubernetes_resources.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#get_kubernetes_resources.ApiResponseFor404) | Not Found

#### get_kubernetes_resources.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[resources](#resources)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# resources

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[block_storage](#block_storage)** | list, tuple,  | tuple,  |  | [optional] 
**[load_balancer](#load_balancer)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# block_storage

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  | Unique identifier for the block storage volume | [optional] 
**label** | str,  | str,  | Label given to the block storage volume | [optional] 
**date_created** | str,  | str,  | Date the block storage volume was created | [optional] 
**status** | str,  | str,  | Status of the block storage volume | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# load_balancer

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  | Unique identifier for the load balancer | [optional] 
**label** | str,  | str,  | Label given to the load balancer | [optional] 
**date_created** | str,  | str,  | Date the load balancer was created | [optional] 
**status** | str,  | str,  | Status of the load balancer | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### get_kubernetes_resources.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_kubernetes_resources.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_kubernetes_resources.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[APIKey](../../../openapi-client/README.md#APIKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../openapi-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../openapi-client/README.md#documentation-for-models) [[Back to README]](../../../openapi-client/README.md)

# **get_kubernetes_versions**
<a name="get_kubernetes_versions"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_kubernetes_versions()

Get Kubernetes Versions

Get a list of supported Kubernetes versions

### Example

```python
import openapi_client
from openapi_client.apis.tags import kubernetes_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.vultr.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.vultr.com/v2"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kubernetes_api.KubernetesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Kubernetes Versions
        api_response = api_instance.get_kubernetes_versions()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KubernetesApi->get_kubernetes_versions: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_kubernetes_versions.ApiResponseFor200) | OK
404 | [ApiResponseFor404](#get_kubernetes_versions.ApiResponseFor404) | Not Found

#### get_kubernetes_versions.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[versions](#versions)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# versions

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

#### get_kubernetes_versions.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../openapi-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../openapi-client/README.md#documentation-for-models) [[Back to README]](../../../openapi-client/README.md)

# **get_nodepool**
<a name="get_nodepool"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_nodepool(vke_idnodepool_id)

Get NodePool

Get Nodepool from a Kubernetes Cluster

### Example

* Bearer Authentication (APIKey):
```python
import openapi_client
from openapi_client.apis.tags import kubernetes_api
from openapi_client.model.nodepools import Nodepools
from pprint import pprint
# Defining the host is optional and defaults to https://api.vultr.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.vultr.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: APIKey
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kubernetes_api.KubernetesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'vke-id': "vke-id_example",
        'nodepool-id': "nodepool-id_example",
    }
    try:
        # Get NodePool
        api_response = api_instance.get_nodepool(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KubernetesApi->get_nodepool: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
vke-id | VkeIdSchema | | 
nodepool-id | NodepoolIdSchema | | 

# VkeIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# NodepoolIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_nodepool.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#get_nodepool.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#get_nodepool.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#get_nodepool.ApiResponseFor404) | Not Found

#### get_nodepool.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**node_pool** | [**Nodepools**]({{complexTypePrefix}}Nodepools.md) | [**Nodepools**]({{complexTypePrefix}}Nodepools.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### get_nodepool.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_nodepool.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_nodepool.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[APIKey](../../../openapi-client/README.md#APIKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../openapi-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../openapi-client/README.md#documentation-for-models) [[Back to README]](../../../openapi-client/README.md)

# **get_nodepools**
<a name="get_nodepools"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_nodepools(vke_id)

List NodePools

List all available NodePools on a Kubernetes Cluster

### Example

* Bearer Authentication (APIKey):
```python
import openapi_client
from openapi_client.apis.tags import kubernetes_api
from openapi_client.model.nodepools import Nodepools
from pprint import pprint
# Defining the host is optional and defaults to https://api.vultr.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.vultr.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: APIKey
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kubernetes_api.KubernetesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'vke-id': "vke-id_example",
    }
    try:
        # List NodePools
        api_response = api_instance.get_nodepools(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KubernetesApi->get_nodepools: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
vke-id | VkeIdSchema | | 

# VkeIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_nodepools.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#get_nodepools.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#get_nodepools.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#get_nodepools.ApiResponseFor404) | Not Found

#### get_nodepools.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[node_pools](#node_pools)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# node_pools

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Nodepools**]({{complexTypePrefix}}Nodepools.md) | [**Nodepools**]({{complexTypePrefix}}Nodepools.md) | [**Nodepools**]({{complexTypePrefix}}Nodepools.md) |  | 

#### get_nodepools.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_nodepools.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_nodepools.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[APIKey](../../../openapi-client/README.md#APIKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../openapi-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../openapi-client/README.md#documentation-for-models) [[Back to README]](../../../openapi-client/README.md)

# **list_kubernetes_clusters**
<a name="list_kubernetes_clusters"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} list_kubernetes_clusters()

List all Kubernetes Clusters

List all Kubernetes clusters currently deployed

### Example

* Bearer Authentication (APIKey):
```python
import openapi_client
from openapi_client.apis.tags import kubernetes_api
from openapi_client.model.vke_cluster import VkeCluster
from pprint import pprint
# Defining the host is optional and defaults to https://api.vultr.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.vultr.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: APIKey
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kubernetes_api.KubernetesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List all Kubernetes Clusters
        api_response = api_instance.list_kubernetes_clusters()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KubernetesApi->list_kubernetes_clusters: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_kubernetes_clusters.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#list_kubernetes_clusters.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#list_kubernetes_clusters.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#list_kubernetes_clusters.ApiResponseFor404) | Not Found

#### list_kubernetes_clusters.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[vke_clusters](#vke_clusters)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# vke_clusters

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**VkeCluster**]({{complexTypePrefix}}VkeCluster.md) | [**VkeCluster**]({{complexTypePrefix}}VkeCluster.md) | [**VkeCluster**]({{complexTypePrefix}}VkeCluster.md) |  | 

#### list_kubernetes_clusters.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### list_kubernetes_clusters.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### list_kubernetes_clusters.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[APIKey](../../../openapi-client/README.md#APIKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../openapi-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../openapi-client/README.md#documentation-for-models) [[Back to README]](../../../openapi-client/README.md)

# **recycle_nodepool_instance**
<a name="recycle_nodepool_instance"></a>
> recycle_nodepool_instance(vke_idnodepool_idnode_id)

Recycle a NodePool Instance

Recycle a specific NodePool Instance

### Example

* Bearer Authentication (APIKey):
```python
import openapi_client
from openapi_client.apis.tags import kubernetes_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.vultr.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.vultr.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: APIKey
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kubernetes_api.KubernetesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'vke-id': "vke-id_example",
        'nodepool-id': "nodepool-id_example",
        'node-id': "node-id_example",
    }
    try:
        # Recycle a NodePool Instance
        api_response = api_instance.recycle_nodepool_instance(
            path_params=path_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling KubernetesApi->recycle_nodepool_instance: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
vke-id | VkeIdSchema | | 
nodepool-id | NodepoolIdSchema | | 
node-id | NodeIdSchema | | 

# VkeIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# NodepoolIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# NodeIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#recycle_nodepool_instance.ApiResponseFor204) | No Content
400 | [ApiResponseFor400](#recycle_nodepool_instance.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#recycle_nodepool_instance.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#recycle_nodepool_instance.ApiResponseFor404) | Not Found

#### recycle_nodepool_instance.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### recycle_nodepool_instance.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### recycle_nodepool_instance.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### recycle_nodepool_instance.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[APIKey](../../../openapi-client/README.md#APIKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../openapi-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../openapi-client/README.md#documentation-for-models) [[Back to README]](../../../openapi-client/README.md)

# **start_kubernetes_cluster_upgrade**
<a name="start_kubernetes_cluster_upgrade"></a>
> start_kubernetes_cluster_upgrade(vke_id)

Start Kubernetes Cluster Upgrade

Start a Kubernetes cluster upgrade.

### Example

* Bearer Authentication (APIKey):
```python
import openapi_client
from openapi_client.apis.tags import kubernetes_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.vultr.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.vultr.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: APIKey
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kubernetes_api.KubernetesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'vke-id': "vke-id_example",
    }
    try:
        # Start Kubernetes Cluster Upgrade
        api_response = api_instance.start_kubernetes_cluster_upgrade(
            path_params=path_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling KubernetesApi->start_kubernetes_cluster_upgrade: %s\n" % e)

    # example passing only optional values
    path_params = {
        'vke-id': "vke-id_example",
    }
    body = dict(
        upgrade_version="upgrade_version_example",
    )
    try:
        # Start Kubernetes Cluster Upgrade
        api_response = api_instance.start_kubernetes_cluster_upgrade(
            path_params=path_params,
            body=body,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling KubernetesApi->start_kubernetes_cluster_upgrade: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**upgrade_version** | str,  | str,  | The version you&#x27;re upgrading to. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
vke-id | VkeIdSchema | | 

# VkeIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
202 | [ApiResponseFor202](#start_kubernetes_cluster_upgrade.ApiResponseFor202) | Accepted
400 | [ApiResponseFor400](#start_kubernetes_cluster_upgrade.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#start_kubernetes_cluster_upgrade.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#start_kubernetes_cluster_upgrade.ApiResponseFor404) | Not Found

#### start_kubernetes_cluster_upgrade.ApiResponseFor202
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### start_kubernetes_cluster_upgrade.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### start_kubernetes_cluster_upgrade.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### start_kubernetes_cluster_upgrade.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[APIKey](../../../openapi-client/README.md#APIKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../openapi-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../openapi-client/README.md#documentation-for-models) [[Back to README]](../../../openapi-client/README.md)

# **update_kubernetes_cluster**
<a name="update_kubernetes_cluster"></a>
> update_kubernetes_cluster(vke_id)

Update Kubernetes Cluster

Update Kubernetes Cluster

### Example

* Bearer Authentication (APIKey):
```python
import openapi_client
from openapi_client.apis.tags import kubernetes_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.vultr.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.vultr.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: APIKey
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kubernetes_api.KubernetesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'vke-id': "vke-id_example",
    }
    try:
        # Update Kubernetes Cluster
        api_response = api_instance.update_kubernetes_cluster(
            path_params=path_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling KubernetesApi->update_kubernetes_cluster: %s\n" % e)

    # example passing only optional values
    path_params = {
        'vke-id': "vke-id_example",
    }
    body = dict(
        label="label_example",
    )
    try:
        # Update Kubernetes Cluster
        api_response = api_instance.update_kubernetes_cluster(
            path_params=path_params,
            body=body,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling KubernetesApi->update_kubernetes_cluster: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**label** | str,  | str,  | Label for the Kubernetes cluster | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
vke-id | VkeIdSchema | | 

# VkeIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#update_kubernetes_cluster.ApiResponseFor204) | No Content
400 | [ApiResponseFor400](#update_kubernetes_cluster.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#update_kubernetes_cluster.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#update_kubernetes_cluster.ApiResponseFor404) | Not Found

#### update_kubernetes_cluster.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### update_kubernetes_cluster.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### update_kubernetes_cluster.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### update_kubernetes_cluster.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[APIKey](../../../openapi-client/README.md#APIKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../openapi-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../openapi-client/README.md#documentation-for-models) [[Back to README]](../../../openapi-client/README.md)

# **update_nodepool**
<a name="update_nodepool"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} update_nodepool(vke_idnodepool_id)

Update Nodepool

Update a Nodepool on a Kubernetes Cluster

### Example

* Bearer Authentication (APIKey):
```python
import openapi_client
from openapi_client.apis.tags import kubernetes_api
from openapi_client.model.nodepools import Nodepools
from pprint import pprint
# Defining the host is optional and defaults to https://api.vultr.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.vultr.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: APIKey
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kubernetes_api.KubernetesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'vke-id': "vke-id_example",
        'nodepool-id': "nodepool-id_example",
    }
    try:
        # Update Nodepool
        api_response = api_instance.update_nodepool(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KubernetesApi->update_nodepool: %s\n" % e)

    # example passing only optional values
    path_params = {
        'vke-id': "vke-id_example",
        'nodepool-id': "nodepool-id_example",
    }
    body = dict(
        node_quantity=1,
        tag="tag_example",
        auto_scaler=True,
        min_nodes=1,
        max_nodes=1,
    )
    try:
        # Update Nodepool
        api_response = api_instance.update_nodepool(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KubernetesApi->update_nodepool: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, SchemaForRequestBodyApplicationXml, Unset] | optional, default is unset |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**node_quantity** | decimal.Decimal, int,  | decimal.Decimal,  | Number of instances in the NodePool. Minimum of 1 is required, but at least 3 is recommended. | [optional] 
**tag** | str,  | str,  | Tag for your node pool | [optional] 
**auto_scaler** | bool,  | BoolClass,  | Option to use the auto scaler for your cluster. Default false. | [optional] 
**min_nodes** | decimal.Decimal, int,  | decimal.Decimal,  | Auto scaler field for minimum nodes you want for your cluster. Default 1. | [optional] 
**max_nodes** | decimal.Decimal, int,  | decimal.Decimal,  | Auto scaler field for maximum nodes you want for your cluster. Default 1. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# SchemaForRequestBodyApplicationXml

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**node_quantity** | decimal.Decimal, int,  | decimal.Decimal,  | Number of instances in the nodepool. Minimum of 1 is required, but at least 3 is recommended. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
vke-id | VkeIdSchema | | 
nodepool-id | NodepoolIdSchema | | 

# VkeIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# NodepoolIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
202 | [ApiResponseFor202](#update_nodepool.ApiResponseFor202) | Accepted
400 | [ApiResponseFor400](#update_nodepool.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#update_nodepool.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#update_nodepool.ApiResponseFor404) | Not Found

#### update_nodepool.ApiResponseFor202
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor202ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor202ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**node_pool** | [**Nodepools**]({{complexTypePrefix}}Nodepools.md) | [**Nodepools**]({{complexTypePrefix}}Nodepools.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### update_nodepool.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### update_nodepool.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### update_nodepool.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[APIKey](../../../openapi-client/README.md#APIKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../openapi-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../openapi-client/README.md#documentation-for-models) [[Back to README]](../../../openapi-client/README.md)

