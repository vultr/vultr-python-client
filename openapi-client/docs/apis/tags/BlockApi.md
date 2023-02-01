<a name="__pageTop"></a>
# openapi_client.apis.tags.block_api.BlockApi

All URIs are relative to *https://api.vultr.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attach_block**](#attach_block) | **post** /blocks/{block-id}/attach | Attach Block Storage
[**create_block**](#create_block) | **post** /blocks | Create Block Storage
[**delete_block**](#delete_block) | **delete** /blocks/{block-id} | Delete Block Storage
[**detach_block**](#detach_block) | **post** /blocks/{block-id}/detach | Detach Block Storage
[**get_block**](#get_block) | **get** /blocks/{block-id} | Get Block Storage
[**list_blocks**](#list_blocks) | **get** /blocks | List Block storages
[**update_block**](#update_block) | **patch** /blocks/{block-id} | Update Block Storage

# **attach_block**
<a name="attach_block"></a>
> attach_block(block_id)

Attach Block Storage

Attach Block Storage to Instance `instance_id`.

### Example

* Bearer Authentication (APIKey):
```python
import openapi_client
from openapi_client.apis.tags import block_api
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
    api_instance = block_api.BlockApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'block-id': "block-id_example",
    }
    try:
        # Attach Block Storage
        api_response = api_instance.attach_block(
            path_params=path_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling BlockApi->attach_block: %s\n" % e)

    # example passing only optional values
    path_params = {
        'block-id': "block-id_example",
    }
    body = dict(
        instance_id="instance_id_example",
        live=True,
    )
    try:
        # Attach Block Storage
        api_response = api_instance.attach_block(
            path_params=path_params,
            body=body,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling BlockApi->attach_block: %s\n" % e)
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
**instance_id** | str,  | str,  | Attach the Block Storage to this [Instance id](#operation/list-instances). | 
**live** | bool,  | BoolClass,  | Attach Block Storage without restarting the Instance.  |   | Value | Description | | - | ----- | ----------- | |   | true | Attach live, do not restart the instance. | |   | false | Restart the instance and attach the Block Storage. | | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
block-id | BlockIdSchema | | 

# BlockIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#attach_block.ApiResponseFor204) | No Content
400 | [ApiResponseFor400](#attach_block.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#attach_block.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#attach_block.ApiResponseFor404) | Not Found

#### attach_block.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### attach_block.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### attach_block.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### attach_block.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[APIKey](../../../openapi-client/README.md#APIKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../openapi-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../openapi-client/README.md#documentation-for-models) [[Back to README]](../../../openapi-client/README.md)

# **create_block**
<a name="create_block"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_block()

Create Block Storage

Create new Block Storage in a `region` with a size of `size_gb`. Size may range between 10 and 40000 depending on the `block_type`.

### Example

* Bearer Authentication (APIKey):
```python
import openapi_client
from openapi_client.apis.tags import block_api
from openapi_client.model.blockstorage import Blockstorage
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
    api_instance = block_api.BlockApi(api_client)

    # example passing only optional values
    body = dict(
        region="region_example",
        size_gb=1,
        label="label_example",
        block_type="block_type_example",
    )
    try:
        # Create Block Storage
        api_response = api_instance.create_block(
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling BlockApi->create_block: %s\n" % e)
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
**size_gb** | decimal.Decimal, int,  | decimal.Decimal,  | Size in GB may range between 10 and 40000, depending on the &#x60;block_type&#x60;. | 
**region** | str,  | str,  | The [Region id](#operation/list-regions) where the Block Storage will be created. | 
**label** | str,  | str,  | The user-supplied label. | [optional] 
**block_type** | str,  | str,  | An optional parameter, that determines on the type of block storage volume that will be created. Soon to become a required parameter.  * &#x60;high_perf&#x60; from 10GB to 10,000GB * &#x60;storage_opt&#x60; from 40GB to 40,000GB | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
202 | [ApiResponseFor202](#create_block.ApiResponseFor202) | Accepted
400 | [ApiResponseFor400](#create_block.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#create_block.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#create_block.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#create_block.ApiResponseFor404) | Not Found

#### create_block.ApiResponseFor202
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
**block** | [**Blockstorage**]({{complexTypePrefix}}Blockstorage.md) | [**Blockstorage**]({{complexTypePrefix}}Blockstorage.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### create_block.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### create_block.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### create_block.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### create_block.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[APIKey](../../../openapi-client/README.md#APIKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../openapi-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../openapi-client/README.md#documentation-for-models) [[Back to README]](../../../openapi-client/README.md)

# **delete_block**
<a name="delete_block"></a>
> delete_block(block_id)

Delete Block Storage

Delete Block Storage.

### Example

* Bearer Authentication (APIKey):
```python
import openapi_client
from openapi_client.apis.tags import block_api
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
    api_instance = block_api.BlockApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'block-id': "block-id_example",
    }
    try:
        # Delete Block Storage
        api_response = api_instance.delete_block(
            path_params=path_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling BlockApi->delete_block: %s\n" % e)
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
block-id | BlockIdSchema | | 

# BlockIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#delete_block.ApiResponseFor204) | No Content
400 | [ApiResponseFor400](#delete_block.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#delete_block.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#delete_block.ApiResponseFor404) | Not Found

#### delete_block.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_block.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_block.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_block.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[APIKey](../../../openapi-client/README.md#APIKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../openapi-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../openapi-client/README.md#documentation-for-models) [[Back to README]](../../../openapi-client/README.md)

# **detach_block**
<a name="detach_block"></a>
> detach_block(block_id)

Detach Block Storage

Detach Block Storage.

### Example

* Bearer Authentication (APIKey):
```python
import openapi_client
from openapi_client.apis.tags import block_api
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
    api_instance = block_api.BlockApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'block-id': "block-id_example",
    }
    try:
        # Detach Block Storage
        api_response = api_instance.detach_block(
            path_params=path_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling BlockApi->detach_block: %s\n" % e)

    # example passing only optional values
    path_params = {
        'block-id': "block-id_example",
    }
    body = dict(
        live=True,
    )
    try:
        # Detach Block Storage
        api_response = api_instance.detach_block(
            path_params=path_params,
            body=body,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling BlockApi->detach_block: %s\n" % e)
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
**live** | bool,  | BoolClass,  | Detach Block Storage without restarting the Instance.  |   | Value | Description | | - | ----- | ----------- | |   | true | Detach live, do not restart the instance. | |   | false | Restart the instance and detach the Block Storage. | | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
block-id | BlockIdSchema | | 

# BlockIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#detach_block.ApiResponseFor204) | No Content
400 | [ApiResponseFor400](#detach_block.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#detach_block.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#detach_block.ApiResponseFor404) | Not Found

#### detach_block.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### detach_block.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### detach_block.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### detach_block.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[APIKey](../../../openapi-client/README.md#APIKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../openapi-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../openapi-client/README.md#documentation-for-models) [[Back to README]](../../../openapi-client/README.md)

# **get_block**
<a name="get_block"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_block(block_id)

Get Block Storage

Get information for Block Storage.

### Example

* Bearer Authentication (APIKey):
```python
import openapi_client
from openapi_client.apis.tags import block_api
from openapi_client.model.blockstorage import Blockstorage
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
    api_instance = block_api.BlockApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'block-id': "block-id_example",
    }
    try:
        # Get Block Storage
        api_response = api_instance.get_block(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling BlockApi->get_block: %s\n" % e)
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
block-id | BlockIdSchema | | 

# BlockIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_block.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#get_block.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#get_block.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#get_block.ApiResponseFor403) | Forbidden

#### get_block.ApiResponseFor200
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
**block** | [**Blockstorage**]({{complexTypePrefix}}Blockstorage.md) | [**Blockstorage**]({{complexTypePrefix}}Blockstorage.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### get_block.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_block.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_block.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[APIKey](../../../openapi-client/README.md#APIKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../openapi-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../openapi-client/README.md#documentation-for-models) [[Back to README]](../../../openapi-client/README.md)

# **list_blocks**
<a name="list_blocks"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} list_blocks()

List Block storages

List all Block Storage in your account.

### Example

* Bearer Authentication (APIKey):
```python
import openapi_client
from openapi_client.apis.tags import block_api
from openapi_client.model.meta import Meta
from openapi_client.model.blockstorage import Blockstorage
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
    api_instance = block_api.BlockApi(api_client)

    # example passing only optional values
    query_params = {
        'per_page': 1,
        'cursor': "cursor_example",
    }
    try:
        # List Block storages
        api_response = api_instance.list_blocks(
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling BlockApi->list_blocks: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
per_page | PerPageSchema | | optional
cursor | CursorSchema | | optional


# PerPageSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# CursorSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_blocks.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#list_blocks.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#list_blocks.ApiResponseFor401) | Unauthorized
500 | [ApiResponseFor500](#list_blocks.ApiResponseFor500) | Internal Server Error

#### list_blocks.ApiResponseFor200
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
**[blocks](#blocks)** | list, tuple,  | tuple,  |  | [optional] 
**meta** | [**Meta**]({{complexTypePrefix}}Meta.md) | [**Meta**]({{complexTypePrefix}}Meta.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# blocks

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Blockstorage**]({{complexTypePrefix}}Blockstorage.md) | [**Blockstorage**]({{complexTypePrefix}}Blockstorage.md) | [**Blockstorage**]({{complexTypePrefix}}Blockstorage.md) |  | 

#### list_blocks.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### list_blocks.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### list_blocks.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[APIKey](../../../openapi-client/README.md#APIKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../openapi-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../openapi-client/README.md#documentation-for-models) [[Back to README]](../../../openapi-client/README.md)

# **update_block**
<a name="update_block"></a>
> update_block(block_id)

Update Block Storage

Update information for Block Storage. 

### Example

* Bearer Authentication (APIKey):
```python
import openapi_client
from openapi_client.apis.tags import block_api
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
    api_instance = block_api.BlockApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'block-id': "block-id_example",
    }
    try:
        # Update Block Storage
        api_response = api_instance.update_block(
            path_params=path_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling BlockApi->update_block: %s\n" % e)

    # example passing only optional values
    path_params = {
        'block-id': "block-id_example",
    }
    body = dict(
        label="label_example",
        size_gb=1,
    )
    try:
        # Update Block Storage
        api_response = api_instance.update_block(
            path_params=path_params,
            body=body,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling BlockApi->update_block: %s\n" % e)
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
**label** | str,  | str,  | The user-supplied label. | [optional] 
**size_gb** | decimal.Decimal, int,  | decimal.Decimal,  | New size of the Block Storage in GB. Size may range between 10 and 40000 depending on the &#x60;block_type&#x60;. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
block-id | BlockIdSchema | | 

# BlockIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#update_block.ApiResponseFor204) | No Content
400 | [ApiResponseFor400](#update_block.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#update_block.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#update_block.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#update_block.ApiResponseFor404) | Not Found

#### update_block.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### update_block.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### update_block.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### update_block.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### update_block.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[APIKey](../../../openapi-client/README.md#APIKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../openapi-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../openapi-client/README.md#documentation-for-models) [[Back to README]](../../../openapi-client/README.md)

