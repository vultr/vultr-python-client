<a name="__pageTop"></a>
# openapi_client.apis.tags.baremetal_api.BaremetalApi

All URIs are relative to *https://api.vultr.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_baremetal**](#create_baremetal) | **post** /bare-metals | Create Bare Metal Instance
[**delete_baremetal**](#delete_baremetal) | **delete** /bare-metals/{baremetal-id} | Delete Bare Metal
[**get_bandwidth_baremetal**](#get_bandwidth_baremetal) | **get** /bare-metals/{baremetal-id}/bandwidth | Bare Metal Bandwidth
[**get_bare_metal_userdata**](#get_bare_metal_userdata) | **get** /bare-metals/{baremetal-id}/user-data | Get Bare Metal User Data
[**get_bare_metal_vnc**](#get_bare_metal_vnc) | **get** /bare-metals/{baremetal-id}/vnc | Get VNC URL for a Bare Metal
[**get_bare_metals_upgrades**](#get_bare_metals_upgrades) | **get** /bare-metals/{baremetal-id}/upgrades | Get Available Bare Metal Upgrades
[**get_baremetal**](#get_baremetal) | **get** /bare-metals/{baremetal-id} | Get Bare Metal
[**get_ipv4_baremetal**](#get_ipv4_baremetal) | **get** /bare-metals/{baremetal-id}/ipv4 | Bare Metal IPv4 Addresses
[**get_ipv6_baremetal**](#get_ipv6_baremetal) | **get** /bare-metals/{baremetal-id}/ipv6 | Bare Metal IPv6 Addresses
[**halt_baremetal**](#halt_baremetal) | **post** /bare-metals/{baremetal-id}/halt | Halt Bare Metal
[**halt_baremetals**](#halt_baremetals) | **post** /bare-metals/halt | Halt Bare Metals
[**list_baremetals**](#list_baremetals) | **get** /bare-metals | List Bare Metal Instances
[**reboot_bare_metals**](#reboot_bare_metals) | **post** /bare-metals/reboot | Reboot Bare Metals
[**reboot_baremetal**](#reboot_baremetal) | **post** /bare-metals/{baremetal-id}/reboot | Reboot Bare Metal
[**reinstall_baremetal**](#reinstall_baremetal) | **post** /bare-metals/{baremetal-id}/reinstall | Reinstall Bare Metal
[**start_bare_metals**](#start_bare_metals) | **post** /bare-metals/start | Start Bare Metals
[**start_baremetal**](#start_baremetal) | **post** /bare-metals/{baremetal-id}/start | Start Bare Metal
[**update_baremetal**](#update_baremetal) | **patch** /bare-metals/{baremetal-id} | Update Bare Metal

# **create_baremetal**
<a name="create_baremetal"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_baremetal()

Create Bare Metal Instance

Create a new Bare Metal instance in a `region` with the desired `plan`. Choose one of the following to deploy the instance:  * `os_id` * `snapshot_id` * `app_id` * `image_id`  Supply other attributes as desired.

### Example

* Bearer Authentication (APIKey):
```python
import openapi_client
from openapi_client.apis.tags import baremetal_api
from openapi_client.model.baremetal import Baremetal
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
    api_instance = baremetal_api.BaremetalApi(api_client)

    # example passing only optional values
    body = dict(
        region="region_example",
        plan="plan_example",
        script_id="script_id_example",
        enable_ipv6=True,
        sshkey_id=[
            "sshkey_id_example"
        ],
        user_data="user_data_example",
        label="label_example",
        activation_email=True,
        hostname="hostname_example",
        tag="tag_example",
        reserved_ipv4="reserved_ipv4_example",
        os_id=1,
        snapshot_id="snapshot_id_example",
        app_id=1,
        image_id="image_id_example",
        persistent_pxe=True,
        tags=[
            "tags_example"
        ],
    )
    try:
        # Create Bare Metal Instance
        api_response = api_instance.create_baremetal(
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling BaremetalApi->create_baremetal: %s\n" % e)
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
**region** | str,  | str,  | The [Region id](#operation/list-regions) to create the instance. | 
**plan** | str,  | str,  | The [Bare Metal plan id](#operation/list-metal-plans) to use for this instance. | 
**script_id** | str,  | str,  | The [Startup Script id](#operation/list-startup-scripts) to use for this instance. | [optional] 
**enable_ipv6** | bool,  | BoolClass,  | Enable IPv6.  * true | [optional] 
**[sshkey_id](#sshkey_id)** | list, tuple,  | tuple,  | The [SSH Key id](#operation/list-ssh-keys) to install on this instance. | [optional] 
**user_data** | str,  | str,  | The user-supplied, base64 encoded [user data](https://www.vultr.com/docs/manage-instance-user-data-with-the-vultr-metadata-api/) for this Instance. | [optional] 
**label** | str,  | str,  | The user-supplied label. | [optional] 
**activation_email** | bool,  | BoolClass,  | Notify by email after deployment.  * true * false (default) | [optional] 
**hostname** | str,  | str,  | The user-supplied hostname to use when deploying this instance. | [optional] 
**tag** | str,  | str,  | Use &#x60;tags&#x60; instead. The user-supplied tag. | [optional] 
**reserved_ipv4** | str,  | str,  | The [Reserved IP id](#operation/list-reserved-ips) for this instance. | [optional] 
**os_id** | decimal.Decimal, int,  | decimal.Decimal,  | If supplied, deploy the instance using this [Operating System id](#operation/list-os). | [optional] 
**snapshot_id** | str,  | str,  | If supplied, deploy the instance using this [Snapshot ID](#operation/list-snapshots). | [optional] 
**app_id** | decimal.Decimal, int,  | decimal.Decimal,  | If supplied, deploy the instance using this [Application id](#operation/list-applications). | [optional] 
**image_id** | str,  | str,  | If supplied, deploy the instance using this [Application image_id](#operation/list-applications). | [optional] 
**persistent_pxe** | bool,  | BoolClass,  | Enable persistent PXE.  * true * false (default) | [optional] 
**[tags](#tags)** | list, tuple,  | tuple,  | Tags to apply to the instance | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# sshkey_id

The [SSH Key id](#operation/list-ssh-keys) to install on this instance.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The [SSH Key id](#operation/list-ssh-keys) to install on this instance. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# tags

Tags to apply to the instance

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Tags to apply to the instance | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
202 | [ApiResponseFor202](#create_baremetal.ApiResponseFor202) | Accepted
400 | [ApiResponseFor400](#create_baremetal.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#create_baremetal.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#create_baremetal.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#create_baremetal.ApiResponseFor404) | Not Found

#### create_baremetal.ApiResponseFor202
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
**baremetal** | [**Baremetal**]({{complexTypePrefix}}Baremetal.md) | [**Baremetal**]({{complexTypePrefix}}Baremetal.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### create_baremetal.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### create_baremetal.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### create_baremetal.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### create_baremetal.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[APIKey](../../../openapi-client/README.md#APIKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../openapi-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../openapi-client/README.md#documentation-for-models) [[Back to README]](../../../openapi-client/README.md)

# **delete_baremetal**
<a name="delete_baremetal"></a>
> delete_baremetal(baremetal_id)

Delete Bare Metal

Delete a Bare Metal instance.

### Example

* Bearer Authentication (APIKey):
```python
import openapi_client
from openapi_client.apis.tags import baremetal_api
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
    api_instance = baremetal_api.BaremetalApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'baremetal-id': "baremetal-id_example",
    }
    try:
        # Delete Bare Metal
        api_response = api_instance.delete_baremetal(
            path_params=path_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling BaremetalApi->delete_baremetal: %s\n" % e)
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
baremetal-id | BaremetalIdSchema | | 

# BaremetalIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#delete_baremetal.ApiResponseFor204) | No Content
400 | [ApiResponseFor400](#delete_baremetal.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#delete_baremetal.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#delete_baremetal.ApiResponseFor404) | Not Found

#### delete_baremetal.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_baremetal.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_baremetal.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_baremetal.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[APIKey](../../../openapi-client/README.md#APIKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../openapi-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../openapi-client/README.md#documentation-for-models) [[Back to README]](../../../openapi-client/README.md)

# **get_bandwidth_baremetal**
<a name="get_bandwidth_baremetal"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_bandwidth_baremetal(baremetal_id)

Bare Metal Bandwidth

Get bandwidth information for the Bare Metal instance.<br><br>The `bandwidth` object in a successful response contains objects representing a day in the month. The date is denoted by the nested object keys. Days begin and end in the UTC timezone. Bandwidth utilization data contained within the date object is refreshed periodically. We do not recommend using this endpoint to gather real-time metrics.

### Example

* Bearer Authentication (APIKey):
```python
import openapi_client
from openapi_client.apis.tags import baremetal_api
from openapi_client.model.bandwidth import Bandwidth
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
    api_instance = baremetal_api.BaremetalApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'baremetal-id': "baremetal-id_example",
    }
    try:
        # Bare Metal Bandwidth
        api_response = api_instance.get_bandwidth_baremetal(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling BaremetalApi->get_bandwidth_baremetal: %s\n" % e)
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
baremetal-id | BaremetalIdSchema | | 

# BaremetalIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_bandwidth_baremetal.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#get_bandwidth_baremetal.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#get_bandwidth_baremetal.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#get_bandwidth_baremetal.ApiResponseFor404) | Not Found

#### get_bandwidth_baremetal.ApiResponseFor200
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
**[bandwidth](#bandwidth)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | This object will contain objects that represent days in the month (UTC). The date is denoted by the nested objects keys. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# bandwidth

This object will contain objects that represent days in the month (UTC). The date is denoted by the nested objects keys.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | This object will contain objects that represent days in the month (UTC). The date is denoted by the nested objects keys. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**2020-10-10** | [**Bandwidth**]({{complexTypePrefix}}Bandwidth.md) | [**Bandwidth**]({{complexTypePrefix}}Bandwidth.md) |  | [optional] 
**2020-10-11** | [**Bandwidth**]({{complexTypePrefix}}Bandwidth.md) | [**Bandwidth**]({{complexTypePrefix}}Bandwidth.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### get_bandwidth_baremetal.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_bandwidth_baremetal.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_bandwidth_baremetal.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[APIKey](../../../openapi-client/README.md#APIKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../openapi-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../openapi-client/README.md#documentation-for-models) [[Back to README]](../../../openapi-client/README.md)

# **get_bare_metal_userdata**
<a name="get_bare_metal_userdata"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_bare_metal_userdata(baremetal_id)

Get Bare Metal User Data

Get the user-supplied, base64 encoded [user data](https://www.vultr.com/docs/manage-instance-user-data-with-the-vultr-metadata-api/) for a Bare Metal.

### Example

* Bearer Authentication (APIKey):
```python
import openapi_client
from openapi_client.apis.tags import baremetal_api
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
    api_instance = baremetal_api.BaremetalApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'baremetal-id': "baremetal-id_example",
    }
    try:
        # Get Bare Metal User Data
        api_response = api_instance.get_bare_metal_userdata(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling BaremetalApi->get_bare_metal_userdata: %s\n" % e)
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
baremetal-id | BaremetalIdSchema | | 

# BaremetalIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_bare_metal_userdata.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#get_bare_metal_userdata.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#get_bare_metal_userdata.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#get_bare_metal_userdata.ApiResponseFor404) | Not Found

#### get_bare_metal_userdata.ApiResponseFor200
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
**[user_data](#user_data)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# user_data

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**data** | str,  | str,  | The user-supplied, base64 encoded [user data](https://www.vultr.com/docs/manage-instance-user-data-with-the-vultr-metadata-api/) attached to this bare metal. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### get_bare_metal_userdata.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_bare_metal_userdata.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_bare_metal_userdata.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[APIKey](../../../openapi-client/README.md#APIKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../openapi-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../openapi-client/README.md#documentation-for-models) [[Back to README]](../../../openapi-client/README.md)

# **get_bare_metal_vnc**
<a name="get_bare_metal_vnc"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_bare_metal_vnc(baremetal_id)

Get VNC URL for a Bare Metal

Get the VNC URL for a Bare Metal

### Example

* Bearer Authentication (APIKey):
```python
import openapi_client
from openapi_client.apis.tags import baremetal_api
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
    api_instance = baremetal_api.BaremetalApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'baremetal-id': "baremetal-id_example",
    }
    try:
        # Get VNC URL for a Bare Metal
        api_response = api_instance.get_bare_metal_vnc(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling BaremetalApi->get_bare_metal_vnc: %s\n" % e)
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
baremetal-id | BaremetalIdSchema | | 

# BaremetalIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_bare_metal_vnc.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#get_bare_metal_vnc.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#get_bare_metal_vnc.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#get_bare_metal_vnc.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#get_bare_metal_vnc.ApiResponseFor404) | Not Found

#### get_bare_metal_vnc.ApiResponseFor200
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
**[vnc](#vnc)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | This object will contain the VNC URL for the Bare Metal Instance | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# vnc

This object will contain the VNC URL for the Bare Metal Instance

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | This object will contain the VNC URL for the Bare Metal Instance | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**url** | str,  | str,  | This is the VNC URL for the Bare Metal Instance | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### get_bare_metal_vnc.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_bare_metal_vnc.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_bare_metal_vnc.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_bare_metal_vnc.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[APIKey](../../../openapi-client/README.md#APIKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../openapi-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../openapi-client/README.md#documentation-for-models) [[Back to README]](../../../openapi-client/README.md)

# **get_bare_metals_upgrades**
<a name="get_bare_metals_upgrades"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_bare_metals_upgrades(baremetal_id)

Get Available Bare Metal Upgrades

Get available upgrades for a Bare Metal

### Example

* Bearer Authentication (APIKey):
```python
import openapi_client
from openapi_client.apis.tags import baremetal_api
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
    api_instance = baremetal_api.BaremetalApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'baremetal-id': "baremetal-id_example",
    }
    query_params = {
    }
    try:
        # Get Available Bare Metal Upgrades
        api_response = api_instance.get_bare_metals_upgrades(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling BaremetalApi->get_bare_metals_upgrades: %s\n" % e)

    # example passing only optional values
    path_params = {
        'baremetal-id': "baremetal-id_example",
    }
    query_params = {
        'type': "type_example",
    }
    try:
        # Get Available Bare Metal Upgrades
        api_response = api_instance.get_bare_metals_upgrades(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling BaremetalApi->get_bare_metals_upgrades: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
type | TypeSchema | | optional


# TypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
baremetal-id | BaremetalIdSchema | | 

# BaremetalIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_bare_metals_upgrades.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#get_bare_metals_upgrades.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#get_bare_metals_upgrades.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#get_bare_metals_upgrades.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#get_bare_metals_upgrades.ApiResponseFor404) | Not Found

#### get_bare_metals_upgrades.ApiResponseFor200
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
**[upgrades](#upgrades)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | This object will contain the available Bare Metal Upgrades | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# upgrades

This object will contain the available Bare Metal Upgrades

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | This object will contain the available Bare Metal Upgrades | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[applications](#applications)** | list, tuple,  | tuple,  |  | [optional] 
**[os](#os)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# applications

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

# os

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

#### get_bare_metals_upgrades.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_bare_metals_upgrades.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_bare_metals_upgrades.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_bare_metals_upgrades.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[APIKey](../../../openapi-client/README.md#APIKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../openapi-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../openapi-client/README.md#documentation-for-models) [[Back to README]](../../../openapi-client/README.md)

# **get_baremetal**
<a name="get_baremetal"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_baremetal(baremetal_id)

Get Bare Metal

Get information for a Bare Metal instance.

### Example

* Bearer Authentication (APIKey):
```python
import openapi_client
from openapi_client.apis.tags import baremetal_api
from openapi_client.model.baremetal import Baremetal
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
    api_instance = baremetal_api.BaremetalApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'baremetal-id': "baremetal-id_example",
    }
    try:
        # Get Bare Metal
        api_response = api_instance.get_baremetal(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling BaremetalApi->get_baremetal: %s\n" % e)
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
baremetal-id | BaremetalIdSchema | | 

# BaremetalIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_baremetal.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#get_baremetal.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#get_baremetal.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#get_baremetal.ApiResponseFor404) | Not Found

#### get_baremetal.ApiResponseFor200
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
**bare_metal** | [**Baremetal**]({{complexTypePrefix}}Baremetal.md) | [**Baremetal**]({{complexTypePrefix}}Baremetal.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### get_baremetal.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_baremetal.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_baremetal.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[APIKey](../../../openapi-client/README.md#APIKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../openapi-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../openapi-client/README.md#documentation-for-models) [[Back to README]](../../../openapi-client/README.md)

# **get_ipv4_baremetal**
<a name="get_ipv4_baremetal"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_ipv4_baremetal(baremetal_id)

Bare Metal IPv4 Addresses

Get the IPv4 information for the Bare Metal instance.

### Example

* Bearer Authentication (APIKey):
```python
import openapi_client
from openapi_client.apis.tags import baremetal_api
from openapi_client.model.meta import Meta
from openapi_client.model.baremetal_ipv4 import BaremetalIpv4
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
    api_instance = baremetal_api.BaremetalApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'baremetal-id': "baremetal-id_example",
    }
    try:
        # Bare Metal IPv4 Addresses
        api_response = api_instance.get_ipv4_baremetal(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling BaremetalApi->get_ipv4_baremetal: %s\n" % e)
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
baremetal-id | BaremetalIdSchema | | 

# BaremetalIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_ipv4_baremetal.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#get_ipv4_baremetal.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#get_ipv4_baremetal.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#get_ipv4_baremetal.ApiResponseFor404) | Not Found

#### get_ipv4_baremetal.ApiResponseFor200
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
**[ipv4s](#ipv4s)** | list, tuple,  | tuple,  |  | [optional] 
**meta** | [**Meta**]({{complexTypePrefix}}Meta.md) | [**Meta**]({{complexTypePrefix}}Meta.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# ipv4s

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**BaremetalIpv4**]({{complexTypePrefix}}BaremetalIpv4.md) | [**BaremetalIpv4**]({{complexTypePrefix}}BaremetalIpv4.md) | [**BaremetalIpv4**]({{complexTypePrefix}}BaremetalIpv4.md) |  | 

#### get_ipv4_baremetal.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_ipv4_baremetal.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_ipv4_baremetal.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[APIKey](../../../openapi-client/README.md#APIKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../openapi-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../openapi-client/README.md#documentation-for-models) [[Back to README]](../../../openapi-client/README.md)

# **get_ipv6_baremetal**
<a name="get_ipv6_baremetal"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_ipv6_baremetal(baremetal_id)

Bare Metal IPv6 Addresses

Get the IPv6 information for the Bare Metal instance.

### Example

* Bearer Authentication (APIKey):
```python
import openapi_client
from openapi_client.apis.tags import baremetal_api
from openapi_client.model.baremetal_ipv6 import BaremetalIpv6
from openapi_client.model.meta import Meta
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
    api_instance = baremetal_api.BaremetalApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'baremetal-id': "baremetal-id_example",
    }
    try:
        # Bare Metal IPv6 Addresses
        api_response = api_instance.get_ipv6_baremetal(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling BaremetalApi->get_ipv6_baremetal: %s\n" % e)
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
baremetal-id | BaremetalIdSchema | | 

# BaremetalIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_ipv6_baremetal.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#get_ipv6_baremetal.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#get_ipv6_baremetal.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#get_ipv6_baremetal.ApiResponseFor404) | Not Found

#### get_ipv6_baremetal.ApiResponseFor200
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
**[ipv6s](#ipv6s)** | list, tuple,  | tuple,  |  | [optional] 
**meta** | [**Meta**]({{complexTypePrefix}}Meta.md) | [**Meta**]({{complexTypePrefix}}Meta.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# ipv6s

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**BaremetalIpv6**]({{complexTypePrefix}}BaremetalIpv6.md) | [**BaremetalIpv6**]({{complexTypePrefix}}BaremetalIpv6.md) | [**BaremetalIpv6**]({{complexTypePrefix}}BaremetalIpv6.md) |  | 

#### get_ipv6_baremetal.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_ipv6_baremetal.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_ipv6_baremetal.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[APIKey](../../../openapi-client/README.md#APIKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../openapi-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../openapi-client/README.md#documentation-for-models) [[Back to README]](../../../openapi-client/README.md)

# **halt_baremetal**
<a name="halt_baremetal"></a>
> halt_baremetal(baremetal_id)

Halt Bare Metal

Halt the Bare Metal instance.

### Example

* Bearer Authentication (APIKey):
```python
import openapi_client
from openapi_client.apis.tags import baremetal_api
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
    api_instance = baremetal_api.BaremetalApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'baremetal-id': "baremetal-id_example",
    }
    try:
        # Halt Bare Metal
        api_response = api_instance.halt_baremetal(
            path_params=path_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling BaremetalApi->halt_baremetal: %s\n" % e)
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
baremetal-id | BaremetalIdSchema | | 

# BaremetalIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#halt_baremetal.ApiResponseFor204) | No Content
400 | [ApiResponseFor400](#halt_baremetal.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#halt_baremetal.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#halt_baremetal.ApiResponseFor404) | Not Found

#### halt_baremetal.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### halt_baremetal.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### halt_baremetal.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### halt_baremetal.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[APIKey](../../../openapi-client/README.md#APIKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../openapi-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../openapi-client/README.md#documentation-for-models) [[Back to README]](../../../openapi-client/README.md)

# **halt_baremetals**
<a name="halt_baremetals"></a>
> halt_baremetals()

Halt Bare Metals

Halt Bare Metals.

### Example

* Bearer Authentication (APIKey):
```python
import openapi_client
from openapi_client.apis.tags import baremetal_api
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
    api_instance = baremetal_api.BaremetalApi(api_client)

    # example passing only optional values
    body = dict(
        baremetal_ids=[
            "baremetal_ids_example"
        ],
    )
    try:
        # Halt Bare Metals
        api_response = api_instance.halt_baremetals(
            body=body,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling BaremetalApi->halt_baremetals: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
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
**[baremetal_ids](#baremetal_ids)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# baremetal_ids

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#halt_baremetals.ApiResponseFor204) | No Content
400 | [ApiResponseFor400](#halt_baremetals.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#halt_baremetals.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#halt_baremetals.ApiResponseFor404) | Not Found

#### halt_baremetals.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### halt_baremetals.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### halt_baremetals.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### halt_baremetals.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[APIKey](../../../openapi-client/README.md#APIKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../openapi-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../openapi-client/README.md#documentation-for-models) [[Back to README]](../../../openapi-client/README.md)

# **list_baremetals**
<a name="list_baremetals"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} list_baremetals()

List Bare Metal Instances

List all Bare Metal instances in your account.

### Example

* Bearer Authentication (APIKey):
```python
import openapi_client
from openapi_client.apis.tags import baremetal_api
from openapi_client.model.meta import Meta
from openapi_client.model.baremetal import Baremetal
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
    api_instance = baremetal_api.BaremetalApi(api_client)

    # example passing only optional values
    query_params = {
        'per_page': 1,
        'cursor': "cursor_example",
    }
    try:
        # List Bare Metal Instances
        api_response = api_instance.list_baremetals(
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling BaremetalApi->list_baremetals: %s\n" % e)
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
200 | [ApiResponseFor200](#list_baremetals.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#list_baremetals.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#list_baremetals.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#list_baremetals.ApiResponseFor404) | Not Found

#### list_baremetals.ApiResponseFor200
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
**[bare_metals](#bare_metals)** | list, tuple,  | tuple,  |  | [optional] 
**meta** | [**Meta**]({{complexTypePrefix}}Meta.md) | [**Meta**]({{complexTypePrefix}}Meta.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# bare_metals

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Baremetal**]({{complexTypePrefix}}Baremetal.md) | [**Baremetal**]({{complexTypePrefix}}Baremetal.md) | [**Baremetal**]({{complexTypePrefix}}Baremetal.md) |  | 

#### list_baremetals.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### list_baremetals.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### list_baremetals.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[APIKey](../../../openapi-client/README.md#APIKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../openapi-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../openapi-client/README.md#documentation-for-models) [[Back to README]](../../../openapi-client/README.md)

# **reboot_bare_metals**
<a name="reboot_bare_metals"></a>
> reboot_bare_metals()

Reboot Bare Metals

Reboot Bare Metals.

### Example

* Bearer Authentication (APIKey):
```python
import openapi_client
from openapi_client.apis.tags import baremetal_api
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
    api_instance = baremetal_api.BaremetalApi(api_client)

    # example passing only optional values
    body = dict(
        baremetal_ids=[
            "baremetal_ids_example"
        ],
    )
    try:
        # Reboot Bare Metals
        api_response = api_instance.reboot_bare_metals(
            body=body,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling BaremetalApi->reboot_bare_metals: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
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
**[baremetal_ids](#baremetal_ids)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# baremetal_ids

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#reboot_bare_metals.ApiResponseFor204) | No Content
400 | [ApiResponseFor400](#reboot_bare_metals.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#reboot_bare_metals.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#reboot_bare_metals.ApiResponseFor404) | Not Found

#### reboot_bare_metals.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### reboot_bare_metals.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### reboot_bare_metals.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### reboot_bare_metals.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[APIKey](../../../openapi-client/README.md#APIKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../openapi-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../openapi-client/README.md#documentation-for-models) [[Back to README]](../../../openapi-client/README.md)

# **reboot_baremetal**
<a name="reboot_baremetal"></a>
> reboot_baremetal(baremetal_id)

Reboot Bare Metal

Reboot the Bare Metal instance.

### Example

* Bearer Authentication (APIKey):
```python
import openapi_client
from openapi_client.apis.tags import baremetal_api
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
    api_instance = baremetal_api.BaremetalApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'baremetal-id': "baremetal-id_example",
    }
    try:
        # Reboot Bare Metal
        api_response = api_instance.reboot_baremetal(
            path_params=path_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling BaremetalApi->reboot_baremetal: %s\n" % e)
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
baremetal-id | BaremetalIdSchema | | 

# BaremetalIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#reboot_baremetal.ApiResponseFor204) | No Content
400 | [ApiResponseFor400](#reboot_baremetal.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#reboot_baremetal.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#reboot_baremetal.ApiResponseFor404) | Not Found

#### reboot_baremetal.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### reboot_baremetal.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### reboot_baremetal.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### reboot_baremetal.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[APIKey](../../../openapi-client/README.md#APIKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../openapi-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../openapi-client/README.md#documentation-for-models) [[Back to README]](../../../openapi-client/README.md)

# **reinstall_baremetal**
<a name="reinstall_baremetal"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} reinstall_baremetal(baremetal_id)

Reinstall Bare Metal

Reinstall the Bare Metal instance.  **Note:** This action may take a few extra seconds to complete.

### Example

* Bearer Authentication (APIKey):
```python
import openapi_client
from openapi_client.apis.tags import baremetal_api
from openapi_client.model.baremetal import Baremetal
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
    api_instance = baremetal_api.BaremetalApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'baremetal-id': "baremetal-id_example",
    }
    try:
        # Reinstall Bare Metal
        api_response = api_instance.reinstall_baremetal(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling BaremetalApi->reinstall_baremetal: %s\n" % e)
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
baremetal-id | BaremetalIdSchema | | 

# BaremetalIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
202 | [ApiResponseFor202](#reinstall_baremetal.ApiResponseFor202) | Accepted
400 | [ApiResponseFor400](#reinstall_baremetal.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#reinstall_baremetal.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#reinstall_baremetal.ApiResponseFor404) | Not Found

#### reinstall_baremetal.ApiResponseFor202
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
**bare_metal** | [**Baremetal**]({{complexTypePrefix}}Baremetal.md) | [**Baremetal**]({{complexTypePrefix}}Baremetal.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### reinstall_baremetal.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### reinstall_baremetal.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### reinstall_baremetal.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[APIKey](../../../openapi-client/README.md#APIKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../openapi-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../openapi-client/README.md#documentation-for-models) [[Back to README]](../../../openapi-client/README.md)

# **start_bare_metals**
<a name="start_bare_metals"></a>
> start_bare_metals()

Start Bare Metals

Start Bare Metals.

### Example

* Bearer Authentication (APIKey):
```python
import openapi_client
from openapi_client.apis.tags import baremetal_api
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
    api_instance = baremetal_api.BaremetalApi(api_client)

    # example passing only optional values
    body = dict(
        baremetal_ids=[
            "baremetal_ids_example"
        ],
    )
    try:
        # Start Bare Metals
        api_response = api_instance.start_bare_metals(
            body=body,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling BaremetalApi->start_bare_metals: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
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
**[baremetal_ids](#baremetal_ids)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# baremetal_ids

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#start_bare_metals.ApiResponseFor204) | No Content
400 | [ApiResponseFor400](#start_bare_metals.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#start_bare_metals.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#start_bare_metals.ApiResponseFor404) | Not Found

#### start_bare_metals.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### start_bare_metals.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### start_bare_metals.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### start_bare_metals.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[APIKey](../../../openapi-client/README.md#APIKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../openapi-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../openapi-client/README.md#documentation-for-models) [[Back to README]](../../../openapi-client/README.md)

# **start_baremetal**
<a name="start_baremetal"></a>
> start_baremetal(baremetal_id)

Start Bare Metal

Start the Bare Metal instance.

### Example

* Bearer Authentication (APIKey):
```python
import openapi_client
from openapi_client.apis.tags import baremetal_api
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
    api_instance = baremetal_api.BaremetalApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'baremetal-id': "baremetal-id_example",
    }
    try:
        # Start Bare Metal
        api_response = api_instance.start_baremetal(
            path_params=path_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling BaremetalApi->start_baremetal: %s\n" % e)
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
baremetal-id | BaremetalIdSchema | | 

# BaremetalIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#start_baremetal.ApiResponseFor204) | No Content
400 | [ApiResponseFor400](#start_baremetal.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#start_baremetal.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#start_baremetal.ApiResponseFor404) | Not Found

#### start_baremetal.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### start_baremetal.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### start_baremetal.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### start_baremetal.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[APIKey](../../../openapi-client/README.md#APIKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../openapi-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../openapi-client/README.md#documentation-for-models) [[Back to README]](../../../openapi-client/README.md)

# **update_baremetal**
<a name="update_baremetal"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} update_baremetal(baremetal_id)

Update Bare Metal

Update a Bare Metal instance. All attributes are optional. If not set, the attributes will retain their original values.  **Note:** Changing `os_id`, `app_id` or `image_id` may take a few extra seconds to complete.

### Example

* Bearer Authentication (APIKey):
```python
import openapi_client
from openapi_client.apis.tags import baremetal_api
from openapi_client.model.baremetal import Baremetal
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
    api_instance = baremetal_api.BaremetalApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'baremetal-id': "baremetal-id_example",
    }
    try:
        # Update Bare Metal
        api_response = api_instance.update_baremetal(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling BaremetalApi->update_baremetal: %s\n" % e)

    # example passing only optional values
    path_params = {
        'baremetal-id': "baremetal-id_example",
    }
    body = dict(
        user_data="user_data_example",
        label="label_example",
        tag="tag_example",
        os_id=1,
        app_id=1,
        image_id="image_id_example",
        enable_ipv6=True,
        tags=[
            "tags_example"
        ],
    )
    try:
        # Update Bare Metal
        api_response = api_instance.update_baremetal(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling BaremetalApi->update_baremetal: %s\n" % e)
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
**user_data** | str,  | str,  | The user-supplied, base64 encoded [user data](https://www.vultr.com/docs/manage-instance-user-data-with-the-vultr-metadata-api/) to attach to this instance. | [optional] 
**label** | str,  | str,  | The user-supplied label. | [optional] 
**tag** | str,  | str,  | Use &#x60;tags&#x60; instead. The user-supplied tag. | [optional] 
**os_id** | decimal.Decimal, int,  | decimal.Decimal,  | If supplied, reinstall the instance using this [Operating System id](#operation/list-os). | [optional] 
**app_id** | decimal.Decimal, int,  | decimal.Decimal,  | If supplied, reinstall the instance using this [Application id](#operation/list-applications). | [optional] 
**image_id** | str,  | str,  | If supplied, reinstall the instance using this [Application image_id](#operation/list-applications). | [optional] 
**enable_ipv6** | bool,  | BoolClass,  | Enable IPv6.  * true | [optional] 
**[tags](#tags)** | list, tuple,  | tuple,  | Tags to apply to the instance | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# tags

Tags to apply to the instance

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Tags to apply to the instance | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
baremetal-id | BaremetalIdSchema | | 

# BaremetalIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
202 | [ApiResponseFor202](#update_baremetal.ApiResponseFor202) | Accepted
400 | [ApiResponseFor400](#update_baremetal.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#update_baremetal.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#update_baremetal.ApiResponseFor404) | Not Found

#### update_baremetal.ApiResponseFor202
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
**bare_metal** | [**Baremetal**]({{complexTypePrefix}}Baremetal.md) | [**Baremetal**]({{complexTypePrefix}}Baremetal.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### update_baremetal.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### update_baremetal.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### update_baremetal.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[APIKey](../../../openapi-client/README.md#APIKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../openapi-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../openapi-client/README.md#documentation-for-models) [[Back to README]](../../../openapi-client/README.md)

