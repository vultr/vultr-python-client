<a name="__pageTop"></a>
# openapi_client.apis.tags.plans_api.PlansApi

All URIs are relative to *https://api.vultr.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_metal_plans**](#list_metal_plans) | **get** /plans-metal | List Bare Metal Plans
[**list_plans**](#list_plans) | **get** /plans | List Plans

# **list_metal_plans**
<a name="list_metal_plans"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} list_metal_plans()

List Bare Metal Plans

Get a list of all Bare Metal plans at Vultr.  The response is an array of JSON `plan` objects, with unique `id` with sub-fields in the general format of:    <type>-<number of cores>-<memory size>-<optional modifier>  For example: `vc2-24c-96gb-sc1`  More about the sub-fields:  * `<type>`: The Vultr type code. For example, `vc2`, `vhf`, `vdc`, etc. * `<number of cores>`: The number of cores, such as `4c` for \"4 cores\", `8c` for \"8 cores\", etc. * `<memory size>`: Size in GB, such as `32gb`. * `<optional modifier>`: Some plans include a modifier for internal identification purposes, such as CPU type or location surcharges.  > Note: This information about plan id format is for general education. Vultr may change the sub-field format or values at any time. You should not attempt to parse the plan ID sub-fields in your code for any specific purpose. 

### Example

```python
import openapi_client
from openapi_client.apis.tags import plans_api
from openapi_client.model.plans_metal import PlansMetal
from openapi_client.model.meta import Meta
from pprint import pprint
# Defining the host is optional and defaults to https://api.vultr.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.vultr.com/v2"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plans_api.PlansApi(api_client)

    # example passing only optional values
    query_params = {
        'per_page': "per_page_example",
        'cursor': "cursor_example",
    }
    try:
        # List Bare Metal Plans
        api_response = api_instance.list_metal_plans(
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PlansApi->list_metal_plans: %s\n" % e)
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
str,  | str,  |  | 

# CursorSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_metal_plans.ApiResponseFor200) | OK

#### list_metal_plans.ApiResponseFor200
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
**[plans](#plans)** | list, tuple,  | tuple,  |  | [optional] 
**meta** | [**Meta**]({{complexTypePrefix}}Meta.md) | [**Meta**]({{complexTypePrefix}}Meta.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# plans

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**PlansMetal**]({{complexTypePrefix}}PlansMetal.md) | [**PlansMetal**]({{complexTypePrefix}}PlansMetal.md) | [**PlansMetal**]({{complexTypePrefix}}PlansMetal.md) |  | 

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../openapi-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../openapi-client/README.md#documentation-for-models) [[Back to README]](../../../openapi-client/README.md)

# **list_plans**
<a name="list_plans"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} list_plans()

List Plans

Get a list of all VPS plans at Vultr.  The response is an array of JSON `plan` objects, with unique `id` with sub-fields in the general format of:    <type>-<number of cores>-<memory size>-<optional modifier>  For example: `vc2-24c-96gb-sc1`  More about the sub-fields:  * `<type>`: The Vultr type code. For example, `vc2`, `vhf`, `vdc`, etc. * `<number of cores>`: The number of cores, such as `4c` for \"4 cores\", `8c` for \"8 cores\", etc. * `<memory size>`: Size in GB, such as `32gb`. * `<optional modifier>`: Some plans include a modifier for internal identification purposes, such as CPU type or location surcharges.  > Note: This information about plan id format is for general education. Vultr may change the sub-field format or values at any time. You should not attempt to parse the plan ID sub-fields in your code for any specific purpose. 

### Example

```python
import openapi_client
from openapi_client.apis.tags import plans_api
from openapi_client.model.meta import Meta
from openapi_client.model.plans import Plans
from pprint import pprint
# Defining the host is optional and defaults to https://api.vultr.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.vultr.com/v2"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plans_api.PlansApi(api_client)

    # example passing only optional values
    query_params = {
        'type': "type_example",
        'per_page': 1,
        'cursor': "cursor_example",
        'os': "os_example",
    }
    try:
        # List Plans
        api_response = api_instance.list_plans(
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PlansApi->list_plans: %s\n" % e)
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
type | TypeSchema | | optional
per_page | PerPageSchema | | optional
cursor | CursorSchema | | optional
os | OsSchema | | optional


# TypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

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

# OsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_plans.ApiResponseFor200) | OK

#### list_plans.ApiResponseFor200
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
**[plans](#plans)** | list, tuple,  | tuple,  |  | [optional] 
**meta** | [**Meta**]({{complexTypePrefix}}Meta.md) | [**Meta**]({{complexTypePrefix}}Meta.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# plans

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Plans**]({{complexTypePrefix}}Plans.md) | [**Plans**]({{complexTypePrefix}}Plans.md) | [**Plans**]({{complexTypePrefix}}Plans.md) |  | 

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../openapi-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../openapi-client/README.md#documentation-for-models) [[Back to README]](../../../openapi-client/README.md)

