<a name="__pageTop"></a>
# openapi_client.apis.tags.reserved_ip_api.ReservedIpApi

All URIs are relative to *https://api.vultr.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attach_reserved_ip**](#attach_reserved_ip) | **post** /reserved-ips/{reserved-ip}/attach | Attach Reserved IP
[**convert_reserved_ip**](#convert_reserved_ip) | **post** /reserved-ips/convert | Convert Instance IP to Reserved IP
[**create_reserved_ip**](#create_reserved_ip) | **post** /reserved-ips | Create Reserved IP
[**delete_reserved_ip**](#delete_reserved_ip) | **delete** /reserved-ips/{reserved-ip} | Delete Reserved IP
[**detach_reserved_ip**](#detach_reserved_ip) | **post** /reserved-ips/{reserved-ip}/detach | Detach Reserved IP
[**get_reserved_ip**](#get_reserved_ip) | **get** /reserved-ips/{reserved-ip} | Get Reserved IP
[**list_reserved_ips**](#list_reserved_ips) | **get** /reserved-ips | List Reserved IPs
[**patch_reserved_ips_reserved_ip**](#patch_reserved_ips_reserved_ip) | **patch** /reserved-ips/{reserved-ip} | Update Reserved IP

# **attach_reserved_ip**
<a name="attach_reserved_ip"></a>
> attach_reserved_ip(reserved_ip)

Attach Reserved IP

Attach a Reserved IP to an compute instance or a baremetal instance - `instance_id`.

### Example

* Bearer Authentication (APIKey):
```python
import openapi_client
from openapi_client.apis.tags import reserved_ip_api
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
    api_instance = reserved_ip_api.ReservedIpApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'reserved-ip': "reserved-ip_example",
    }
    try:
        # Attach Reserved IP
        api_response = api_instance.attach_reserved_ip(
            path_params=path_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling ReservedIpApi->attach_reserved_ip: %s\n" % e)

    # example passing only optional values
    path_params = {
        'reserved-ip': "reserved-ip_example",
    }
    body = dict(
        instance_id="instance_id_example",
    )
    try:
        # Attach Reserved IP
        api_response = api_instance.attach_reserved_ip(
            path_params=path_params,
            body=body,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling ReservedIpApi->attach_reserved_ip: %s\n" % e)
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
**instance_id** | str,  | str,  | Attach the Reserved IP to a [Compute Instance id](#operation/list-instances) or a [Bare Metal Instance id](#operation/list-baremetals). | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
reserved-ip | ReservedIpSchema | | 

# ReservedIpSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#attach_reserved_ip.ApiResponseFor204) | No Content
400 | [ApiResponseFor400](#attach_reserved_ip.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#attach_reserved_ip.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#attach_reserved_ip.ApiResponseFor404) | Not Found

#### attach_reserved_ip.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### attach_reserved_ip.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### attach_reserved_ip.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### attach_reserved_ip.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[APIKey](../../../openapi-client/README.md#APIKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../openapi-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../openapi-client/README.md#documentation-for-models) [[Back to README]](../../../openapi-client/README.md)

# **convert_reserved_ip**
<a name="convert_reserved_ip"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} convert_reserved_ip()

Convert Instance IP to Reserved IP

Convert the `ip_address` of an existing [instance](#operation/list-instances) into a Reserved IP.

### Example

* Bearer Authentication (APIKey):
```python
import openapi_client
from openapi_client.apis.tags import reserved_ip_api
from openapi_client.model.reserved_ip import ReservedIp
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
    api_instance = reserved_ip_api.ReservedIpApi(api_client)

    # example passing only optional values
    body = dict(
        ip_address="ip_address_example",
        label="label_example",
    )
    try:
        # Convert Instance IP to Reserved IP
        api_response = api_instance.convert_reserved_ip(
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ReservedIpApi->convert_reserved_ip: %s\n" % e)
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
**ip_address** | str,  | str,  | The IP address to convert. | 
**label** | str,  | str,  | A user-supplied label for this IP address. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#convert_reserved_ip.ApiResponseFor201) | Created
400 | [ApiResponseFor400](#convert_reserved_ip.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#convert_reserved_ip.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#convert_reserved_ip.ApiResponseFor404) | Not Found

#### convert_reserved_ip.ApiResponseFor201
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
**reserved_ip** | [**ReservedIp**]({{complexTypePrefix}}ReservedIp.md) | [**ReservedIp**]({{complexTypePrefix}}ReservedIp.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### convert_reserved_ip.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### convert_reserved_ip.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### convert_reserved_ip.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[APIKey](../../../openapi-client/README.md#APIKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../openapi-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../openapi-client/README.md#documentation-for-models) [[Back to README]](../../../openapi-client/README.md)

# **create_reserved_ip**
<a name="create_reserved_ip"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_reserved_ip()

Create Reserved IP

Create a new Reserved IP. The `region` and `ip_type` attributes are required.

### Example

* Bearer Authentication (APIKey):
```python
import openapi_client
from openapi_client.apis.tags import reserved_ip_api
from openapi_client.model.reserved_ip import ReservedIp
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
    api_instance = reserved_ip_api.ReservedIpApi(api_client)

    # example passing only optional values
    body = dict(
        region="region_example",
        ip_type="ip_type_example",
        label="label_example",
    )
    try:
        # Create Reserved IP
        api_response = api_instance.create_reserved_ip(
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ReservedIpApi->create_reserved_ip: %s\n" % e)
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
**ip_type** | str,  | str,  | The type of IP address.  * v4 * v6 | 
**region** | str,  | str,  | The [Region id](#operation/list-regions) where the Reserved IP will be created. | 
**label** | str,  | str,  | The user-supplied label. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#create_reserved_ip.ApiResponseFor201) | Created
400 | [ApiResponseFor400](#create_reserved_ip.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#create_reserved_ip.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#create_reserved_ip.ApiResponseFor404) | Not Found

#### create_reserved_ip.ApiResponseFor201
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
**reserved_ip** | [**ReservedIp**]({{complexTypePrefix}}ReservedIp.md) | [**ReservedIp**]({{complexTypePrefix}}ReservedIp.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### create_reserved_ip.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### create_reserved_ip.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### create_reserved_ip.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[APIKey](../../../openapi-client/README.md#APIKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../openapi-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../openapi-client/README.md#documentation-for-models) [[Back to README]](../../../openapi-client/README.md)

# **delete_reserved_ip**
<a name="delete_reserved_ip"></a>
> delete_reserved_ip(reserved_ip)

Delete Reserved IP

Delete a Reserved IP.

### Example

* Bearer Authentication (APIKey):
```python
import openapi_client
from openapi_client.apis.tags import reserved_ip_api
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
    api_instance = reserved_ip_api.ReservedIpApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'reserved-ip': "reserved-ip_example",
    }
    try:
        # Delete Reserved IP
        api_response = api_instance.delete_reserved_ip(
            path_params=path_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling ReservedIpApi->delete_reserved_ip: %s\n" % e)
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
reserved-ip | ReservedIpSchema | | 

# ReservedIpSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#delete_reserved_ip.ApiResponseFor204) | No Content
400 | [ApiResponseFor400](#delete_reserved_ip.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#delete_reserved_ip.ApiResponseFor401) | Unauthorized

#### delete_reserved_ip.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_reserved_ip.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_reserved_ip.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[APIKey](../../../openapi-client/README.md#APIKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../openapi-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../openapi-client/README.md#documentation-for-models) [[Back to README]](../../../openapi-client/README.md)

# **detach_reserved_ip**
<a name="detach_reserved_ip"></a>
> detach_reserved_ip(reserved_ip)

Detach Reserved IP

Detach a Reserved IP.

### Example

* Bearer Authentication (APIKey):
```python
import openapi_client
from openapi_client.apis.tags import reserved_ip_api
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
    api_instance = reserved_ip_api.ReservedIpApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'reserved-ip': "reserved-ip_example",
    }
    try:
        # Detach Reserved IP
        api_response = api_instance.detach_reserved_ip(
            path_params=path_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling ReservedIpApi->detach_reserved_ip: %s\n" % e)
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
reserved-ip | ReservedIpSchema | | 

# ReservedIpSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#detach_reserved_ip.ApiResponseFor204) | No Content
400 | [ApiResponseFor400](#detach_reserved_ip.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#detach_reserved_ip.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#detach_reserved_ip.ApiResponseFor404) | Not Found

#### detach_reserved_ip.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### detach_reserved_ip.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### detach_reserved_ip.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### detach_reserved_ip.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[APIKey](../../../openapi-client/README.md#APIKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../openapi-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../openapi-client/README.md#documentation-for-models) [[Back to README]](../../../openapi-client/README.md)

# **get_reserved_ip**
<a name="get_reserved_ip"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_reserved_ip(reserved_ip)

Get Reserved IP

Get information about a Reserved IP.

### Example

* Bearer Authentication (APIKey):
```python
import openapi_client
from openapi_client.apis.tags import reserved_ip_api
from openapi_client.model.reserved_ip import ReservedIp
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
    api_instance = reserved_ip_api.ReservedIpApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'reserved-ip': "reserved-ip_example",
    }
    try:
        # Get Reserved IP
        api_response = api_instance.get_reserved_ip(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ReservedIpApi->get_reserved_ip: %s\n" % e)
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
reserved-ip | ReservedIpSchema | | 

# ReservedIpSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_reserved_ip.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#get_reserved_ip.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#get_reserved_ip.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#get_reserved_ip.ApiResponseFor404) | Not Found

#### get_reserved_ip.ApiResponseFor200
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
**reserved_ip** | [**ReservedIp**]({{complexTypePrefix}}ReservedIp.md) | [**ReservedIp**]({{complexTypePrefix}}ReservedIp.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### get_reserved_ip.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_reserved_ip.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_reserved_ip.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[APIKey](../../../openapi-client/README.md#APIKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../openapi-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../openapi-client/README.md#documentation-for-models) [[Back to README]](../../../openapi-client/README.md)

# **list_reserved_ips**
<a name="list_reserved_ips"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} list_reserved_ips()

List Reserved IPs

List all Reserved IPs in your account.

### Example

* Bearer Authentication (APIKey):
```python
import openapi_client
from openapi_client.apis.tags import reserved_ip_api
from openapi_client.model.meta import Meta
from openapi_client.model.reserved_ip import ReservedIp
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
    api_instance = reserved_ip_api.ReservedIpApi(api_client)

    # example passing only optional values
    query_params = {
        'per_page': 1,
        'cursor': "cursor_example",
    }
    try:
        # List Reserved IPs
        api_response = api_instance.list_reserved_ips(
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ReservedIpApi->list_reserved_ips: %s\n" % e)
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
200 | [ApiResponseFor200](#list_reserved_ips.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#list_reserved_ips.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#list_reserved_ips.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#list_reserved_ips.ApiResponseFor404) | Not Found

#### list_reserved_ips.ApiResponseFor200
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
**[reserved_ips](#reserved_ips)** | list, tuple,  | tuple,  |  | [optional] 
**meta** | [**Meta**]({{complexTypePrefix}}Meta.md) | [**Meta**]({{complexTypePrefix}}Meta.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# reserved_ips

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ReservedIp**]({{complexTypePrefix}}ReservedIp.md) | [**ReservedIp**]({{complexTypePrefix}}ReservedIp.md) | [**ReservedIp**]({{complexTypePrefix}}ReservedIp.md) |  | 

#### list_reserved_ips.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### list_reserved_ips.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### list_reserved_ips.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[APIKey](../../../openapi-client/README.md#APIKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../openapi-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../openapi-client/README.md#documentation-for-models) [[Back to README]](../../../openapi-client/README.md)

# **patch_reserved_ips_reserved_ip**
<a name="patch_reserved_ips_reserved_ip"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} patch_reserved_ips_reserved_ip(reserved_ip)

Update Reserved IP

Update information on a Reserved IP.

### Example

* Bearer Authentication (APIKey):
```python
import openapi_client
from openapi_client.apis.tags import reserved_ip_api
from openapi_client.model.reserved_ip import ReservedIp
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
    api_instance = reserved_ip_api.ReservedIpApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'reserved-ip': "reserved-ip_example",
    }
    try:
        # Update Reserved IP
        api_response = api_instance.patch_reserved_ips_reserved_ip(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ReservedIpApi->patch_reserved_ips_reserved_ip: %s\n" % e)

    # example passing only optional values
    path_params = {
        'reserved-ip': "reserved-ip_example",
    }
    body = dict(
        label="label_example",
    )
    try:
        # Update Reserved IP
        api_response = api_instance.patch_reserved_ips_reserved_ip(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ReservedIpApi->patch_reserved_ips_reserved_ip: %s\n" % e)
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
**label** | str,  | str,  |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
reserved-ip | ReservedIpSchema | | 

# ReservedIpSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#patch_reserved_ips_reserved_ip.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#patch_reserved_ips_reserved_ip.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#patch_reserved_ips_reserved_ip.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#patch_reserved_ips_reserved_ip.ApiResponseFor404) | Not Found

#### patch_reserved_ips_reserved_ip.ApiResponseFor200
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
**reserved_ip** | [**ReservedIp**]({{complexTypePrefix}}ReservedIp.md) | [**ReservedIp**]({{complexTypePrefix}}ReservedIp.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### patch_reserved_ips_reserved_ip.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### patch_reserved_ips_reserved_ip.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### patch_reserved_ips_reserved_ip.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[APIKey](../../../openapi-client/README.md#APIKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../openapi-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../openapi-client/README.md#documentation-for-models) [[Back to README]](../../../openapi-client/README.md)

