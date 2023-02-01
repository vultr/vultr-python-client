<a name="__pageTop"></a>
# openapi_client.apis.tags.dns_api.DnsApi

All URIs are relative to *https://api.vultr.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_dns_domain**](#create_dns_domain) | **post** /domains | Create DNS Domain
[**create_dns_domain_record**](#create_dns_domain_record) | **post** /domains/{dns-domain}/records | Create Record
[**delete_dns_domain**](#delete_dns_domain) | **delete** /domains/{dns-domain} | Delete Domain
[**delete_dns_domain_record**](#delete_dns_domain_record) | **delete** /domains/{dns-domain}/records/{record-id} | Delete Record
[**get_dns_domain**](#get_dns_domain) | **get** /domains/{dns-domain} | Get DNS Domain
[**get_dns_domain_dnssec**](#get_dns_domain_dnssec) | **get** /domains/{dns-domain}/dnssec | Get DNSSec Info
[**get_dns_domain_record**](#get_dns_domain_record) | **get** /domains/{dns-domain}/records/{record-id} | Get Record
[**get_dns_domain_soa**](#get_dns_domain_soa) | **get** /domains/{dns-domain}/soa | Get SOA information
[**list_dns_domain_records**](#list_dns_domain_records) | **get** /domains/{dns-domain}/records | List Records
[**list_dns_domains**](#list_dns_domains) | **get** /domains | List DNS Domains
[**update_dns_domain**](#update_dns_domain) | **put** /domains/{dns-domain} | Update a DNS Domain
[**update_dns_domain_record**](#update_dns_domain_record) | **patch** /domains/{dns-domain}/records/{record-id} | Update Record
[**update_dns_domain_soa**](#update_dns_domain_soa) | **patch** /domains/{dns-domain}/soa | Update SOA information

# **create_dns_domain**
<a name="create_dns_domain"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_dns_domain()

Create DNS Domain

Create a DNS Domain for `domain`. If no `ip` address is supplied a domain with no records will be created.

### Example

* Bearer Authentication (APIKey):
```python
import openapi_client
from openapi_client.apis.tags import dns_api
from openapi_client.model.domain import Domain
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
    api_instance = dns_api.DnsApi(api_client)

    # example passing only optional values
    body = dict(
        domain="domain_example",
        ip="ip_example",
        dns_sec="dns_sec_example",
    )
    try:
        # Create DNS Domain
        api_response = api_instance.create_dns_domain(
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DnsApi->create_dns_domain: %s\n" % e)
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
**domain** | str,  | str,  | Your registered DNS Domain name. | 
**ip** | str,  | str,  | The default IP address for your DNS Domain. If omitted an empty domain zone will be created. | [optional] 
**dns_sec** | str,  | str,  | Enable or disable DNSSEC.  * enabled * disabled (default) | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#create_dns_domain.ApiResponseFor200) | OK

#### create_dns_domain.ApiResponseFor200
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
**domain** | [**Domain**]({{complexTypePrefix}}Domain.md) | [**Domain**]({{complexTypePrefix}}Domain.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Authorization

[APIKey](../../../openapi-client/README.md#APIKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../openapi-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../openapi-client/README.md#documentation-for-models) [[Back to README]](../../../openapi-client/README.md)

# **create_dns_domain_record**
<a name="create_dns_domain_record"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_dns_domain_record(dns_domain)

Create Record

Create a DNS record.

### Example

* Bearer Authentication (APIKey):
```python
import openapi_client
from openapi_client.apis.tags import dns_api
from openapi_client.model.dns_record import DnsRecord
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
    api_instance = dns_api.DnsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'dns-domain': "dns-domain_example",
    }
    try:
        # Create Record
        api_response = api_instance.create_dns_domain_record(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DnsApi->create_dns_domain_record: %s\n" % e)

    # example passing only optional values
    path_params = {
        'dns-domain': "dns-domain_example",
    }
    body = dict(
        name="name_example",
        type="type_example",
        data="data_example",
        ttl=1,
        priority=1,
    )
    try:
        # Create Record
        api_response = api_instance.create_dns_domain_record(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DnsApi->create_dns_domain_record: %s\n" % e)
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
**data** | str,  | str,  | The DNS data for this record type. | 
**name** | str,  | str,  | The hostname for this DNS record. | 
**type** | str,  | str,  | The DNS record type.  * A * AAAA * CNAME * NS * MX * SRV * TXT * CAA * SSHFP | 
**ttl** | decimal.Decimal, int,  | decimal.Decimal,  | Time to Live in seconds. | [optional] 
**priority** | decimal.Decimal, int,  | decimal.Decimal,  | DNS priority. Does not apply to all record types. (Only required for MX and SRV) | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
dns-domain | DnsDomainSchema | | 

# DnsDomainSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#create_dns_domain_record.ApiResponseFor201) | Created
400 | [ApiResponseFor400](#create_dns_domain_record.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#create_dns_domain_record.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#create_dns_domain_record.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#create_dns_domain_record.ApiResponseFor404) | Not Found

#### create_dns_domain_record.ApiResponseFor201
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
**record** | [**DnsRecord**]({{complexTypePrefix}}DnsRecord.md) | [**DnsRecord**]({{complexTypePrefix}}DnsRecord.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### create_dns_domain_record.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### create_dns_domain_record.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### create_dns_domain_record.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### create_dns_domain_record.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[APIKey](../../../openapi-client/README.md#APIKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../openapi-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../openapi-client/README.md#documentation-for-models) [[Back to README]](../../../openapi-client/README.md)

# **delete_dns_domain**
<a name="delete_dns_domain"></a>
> delete_dns_domain(dns_domain)

Delete Domain

Delete the DNS Domain.

### Example

* Bearer Authentication (APIKey):
```python
import openapi_client
from openapi_client.apis.tags import dns_api
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
    api_instance = dns_api.DnsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'dns-domain': "dns-domain_example",
    }
    try:
        # Delete Domain
        api_response = api_instance.delete_dns_domain(
            path_params=path_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling DnsApi->delete_dns_domain: %s\n" % e)
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
dns-domain | DnsDomainSchema | | 

# DnsDomainSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#delete_dns_domain.ApiResponseFor204) | No Content
400 | [ApiResponseFor400](#delete_dns_domain.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#delete_dns_domain.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#delete_dns_domain.ApiResponseFor404) | Not Found

#### delete_dns_domain.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_dns_domain.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_dns_domain.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_dns_domain.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[APIKey](../../../openapi-client/README.md#APIKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../openapi-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../openapi-client/README.md#documentation-for-models) [[Back to README]](../../../openapi-client/README.md)

# **delete_dns_domain_record**
<a name="delete_dns_domain_record"></a>
> delete_dns_domain_record(dns_domainrecord_id)

Delete Record

Delete the DNS record.

### Example

* Bearer Authentication (APIKey):
```python
import openapi_client
from openapi_client.apis.tags import dns_api
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
    api_instance = dns_api.DnsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'dns-domain': "dns-domain_example",
        'record-id': "record-id_example",
    }
    try:
        # Delete Record
        api_response = api_instance.delete_dns_domain_record(
            path_params=path_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling DnsApi->delete_dns_domain_record: %s\n" % e)
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
dns-domain | DnsDomainSchema | | 
record-id | RecordIdSchema | | 

# DnsDomainSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# RecordIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#delete_dns_domain_record.ApiResponseFor204) | No Content
400 | [ApiResponseFor400](#delete_dns_domain_record.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#delete_dns_domain_record.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#delete_dns_domain_record.ApiResponseFor404) | Not Found

#### delete_dns_domain_record.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_dns_domain_record.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_dns_domain_record.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_dns_domain_record.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[APIKey](../../../openapi-client/README.md#APIKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../openapi-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../openapi-client/README.md#documentation-for-models) [[Back to README]](../../../openapi-client/README.md)

# **get_dns_domain**
<a name="get_dns_domain"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_dns_domain(dns_domain)

Get DNS Domain

Get information for the DNS Domain.

### Example

* Bearer Authentication (APIKey):
```python
import openapi_client
from openapi_client.apis.tags import dns_api
from openapi_client.model.domain import Domain
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
    api_instance = dns_api.DnsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'dns-domain': "dns-domain_example",
    }
    try:
        # Get DNS Domain
        api_response = api_instance.get_dns_domain(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DnsApi->get_dns_domain: %s\n" % e)
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
dns-domain | DnsDomainSchema | | 

# DnsDomainSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_dns_domain.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#get_dns_domain.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#get_dns_domain.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#get_dns_domain.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#get_dns_domain.ApiResponseFor404) | Not Found

#### get_dns_domain.ApiResponseFor200
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
**domain** | [**Domain**]({{complexTypePrefix}}Domain.md) | [**Domain**]({{complexTypePrefix}}Domain.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### get_dns_domain.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_dns_domain.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_dns_domain.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_dns_domain.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[APIKey](../../../openapi-client/README.md#APIKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../openapi-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../openapi-client/README.md#documentation-for-models) [[Back to README]](../../../openapi-client/README.md)

# **get_dns_domain_dnssec**
<a name="get_dns_domain_dnssec"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_dns_domain_dnssec(dns_domain)

Get DNSSec Info

Get the DNSSEC information for the DNS Domain.

### Example

* Bearer Authentication (APIKey):
```python
import openapi_client
from openapi_client.apis.tags import dns_api
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
    api_instance = dns_api.DnsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'dns-domain': "dns-domain_example",
    }
    try:
        # Get DNSSec Info
        api_response = api_instance.get_dns_domain_dnssec(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DnsApi->get_dns_domain_dnssec: %s\n" % e)
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
dns-domain | DnsDomainSchema | | 

# DnsDomainSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_dns_domain_dnssec.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#get_dns_domain_dnssec.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#get_dns_domain_dnssec.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#get_dns_domain_dnssec.ApiResponseFor404) | Not Found

#### get_dns_domain_dnssec.ApiResponseFor200
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
**[dns_sec](#dns_sec)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# dns_sec

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

#### get_dns_domain_dnssec.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_dns_domain_dnssec.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_dns_domain_dnssec.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[APIKey](../../../openapi-client/README.md#APIKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../openapi-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../openapi-client/README.md#documentation-for-models) [[Back to README]](../../../openapi-client/README.md)

# **get_dns_domain_record**
<a name="get_dns_domain_record"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_dns_domain_record(dns_domainrecord_id)

Get Record

Get information for a DNS Record.

### Example

* Bearer Authentication (APIKey):
```python
import openapi_client
from openapi_client.apis.tags import dns_api
from openapi_client.model.dns_record import DnsRecord
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
    api_instance = dns_api.DnsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'dns-domain': "dns-domain_example",
        'record-id': "record-id_example",
    }
    try:
        # Get Record
        api_response = api_instance.get_dns_domain_record(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DnsApi->get_dns_domain_record: %s\n" % e)
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
dns-domain | DnsDomainSchema | | 
record-id | RecordIdSchema | | 

# DnsDomainSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# RecordIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_dns_domain_record.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#get_dns_domain_record.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#get_dns_domain_record.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#get_dns_domain_record.ApiResponseFor404) | Not Found

#### get_dns_domain_record.ApiResponseFor200
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
**record** | [**DnsRecord**]({{complexTypePrefix}}DnsRecord.md) | [**DnsRecord**]({{complexTypePrefix}}DnsRecord.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### get_dns_domain_record.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_dns_domain_record.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_dns_domain_record.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[APIKey](../../../openapi-client/README.md#APIKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../openapi-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../openapi-client/README.md#documentation-for-models) [[Back to README]](../../../openapi-client/README.md)

# **get_dns_domain_soa**
<a name="get_dns_domain_soa"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_dns_domain_soa(dns_domain)

Get SOA information

Get SOA information for the DNS Domain.

### Example

* Bearer Authentication (APIKey):
```python
import openapi_client
from openapi_client.apis.tags import dns_api
from openapi_client.model.dns_soa import DnsSoa
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
    api_instance = dns_api.DnsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'dns-domain': "dns-domain_example",
    }
    try:
        # Get SOA information
        api_response = api_instance.get_dns_domain_soa(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DnsApi->get_dns_domain_soa: %s\n" % e)
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
dns-domain | DnsDomainSchema | | 

# DnsDomainSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_dns_domain_soa.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#get_dns_domain_soa.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#get_dns_domain_soa.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#get_dns_domain_soa.ApiResponseFor404) | Not Found

#### get_dns_domain_soa.ApiResponseFor200
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
**dns_soa** | [**DnsSoa**]({{complexTypePrefix}}DnsSoa.md) | [**DnsSoa**]({{complexTypePrefix}}DnsSoa.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### get_dns_domain_soa.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_dns_domain_soa.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_dns_domain_soa.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[APIKey](../../../openapi-client/README.md#APIKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../openapi-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../openapi-client/README.md#documentation-for-models) [[Back to README]](../../../openapi-client/README.md)

# **list_dns_domain_records**
<a name="list_dns_domain_records"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} list_dns_domain_records(dns_domain)

List Records

Get the DNS records for the Domain.

### Example

* Bearer Authentication (APIKey):
```python
import openapi_client
from openapi_client.apis.tags import dns_api
from openapi_client.model.meta import Meta
from openapi_client.model.dns_record import DnsRecord
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
    api_instance = dns_api.DnsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'dns-domain': "dns-domain_example",
    }
    query_params = {
    }
    try:
        # List Records
        api_response = api_instance.list_dns_domain_records(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DnsApi->list_dns_domain_records: %s\n" % e)

    # example passing only optional values
    path_params = {
        'dns-domain': "dns-domain_example",
    }
    query_params = {
        'per_page': 1,
        'cursor': "cursor_example",
    }
    try:
        # List Records
        api_response = api_instance.list_dns_domain_records(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DnsApi->list_dns_domain_records: %s\n" % e)
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

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
dns-domain | DnsDomainSchema | | 

# DnsDomainSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_dns_domain_records.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#list_dns_domain_records.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#list_dns_domain_records.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#list_dns_domain_records.ApiResponseFor404) | Not Found

#### list_dns_domain_records.ApiResponseFor200
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
**[records](#records)** | list, tuple,  | tuple,  |  | [optional] 
**meta** | [**Meta**]({{complexTypePrefix}}Meta.md) | [**Meta**]({{complexTypePrefix}}Meta.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# records

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**DnsRecord**]({{complexTypePrefix}}DnsRecord.md) | [**DnsRecord**]({{complexTypePrefix}}DnsRecord.md) | [**DnsRecord**]({{complexTypePrefix}}DnsRecord.md) |  | 

#### list_dns_domain_records.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### list_dns_domain_records.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### list_dns_domain_records.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[APIKey](../../../openapi-client/README.md#APIKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../openapi-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../openapi-client/README.md#documentation-for-models) [[Back to README]](../../../openapi-client/README.md)

# **list_dns_domains**
<a name="list_dns_domains"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} list_dns_domains()

List DNS Domains

List all DNS Domains in your account.

### Example

* Bearer Authentication (APIKey):
```python
import openapi_client
from openapi_client.apis.tags import dns_api
from openapi_client.model.meta import Meta
from openapi_client.model.domain import Domain
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
    api_instance = dns_api.DnsApi(api_client)

    # example passing only optional values
    query_params = {
        'per_page': 1,
        'cursor': "cursor_example",
    }
    try:
        # List DNS Domains
        api_response = api_instance.list_dns_domains(
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DnsApi->list_dns_domains: %s\n" % e)
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
200 | [ApiResponseFor200](#list_dns_domains.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#list_dns_domains.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#list_dns_domains.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#list_dns_domains.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#list_dns_domains.ApiResponseFor404) | Not Found

#### list_dns_domains.ApiResponseFor200
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
**[domains](#domains)** | list, tuple,  | tuple,  |  | [optional] 
**meta** | [**Meta**]({{complexTypePrefix}}Meta.md) | [**Meta**]({{complexTypePrefix}}Meta.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# domains

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Domain**]({{complexTypePrefix}}Domain.md) | [**Domain**]({{complexTypePrefix}}Domain.md) | [**Domain**]({{complexTypePrefix}}Domain.md) |  | 

#### list_dns_domains.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### list_dns_domains.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### list_dns_domains.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### list_dns_domains.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[APIKey](../../../openapi-client/README.md#APIKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../openapi-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../openapi-client/README.md#documentation-for-models) [[Back to README]](../../../openapi-client/README.md)

# **update_dns_domain**
<a name="update_dns_domain"></a>
> update_dns_domain(dns_domain)

Update a DNS Domain

Update the DNS Domain. 

### Example

* Bearer Authentication (APIKey):
```python
import openapi_client
from openapi_client.apis.tags import dns_api
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
    api_instance = dns_api.DnsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'dns-domain': "dns-domain_example",
    }
    try:
        # Update a DNS Domain
        api_response = api_instance.update_dns_domain(
            path_params=path_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling DnsApi->update_dns_domain: %s\n" % e)

    # example passing only optional values
    path_params = {
        'dns-domain': "dns-domain_example",
    }
    body = dict(
        dns_sec="dns_sec_example",
    )
    try:
        # Update a DNS Domain
        api_response = api_instance.update_dns_domain(
            path_params=path_params,
            body=body,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling DnsApi->update_dns_domain: %s\n" % e)
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
**dns_sec** | str,  | str,  | Enable or disable DNSSEC.  * enabled * disabled | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
dns-domain | DnsDomainSchema | | 

# DnsDomainSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#update_dns_domain.ApiResponseFor204) | No Content
400 | [ApiResponseFor400](#update_dns_domain.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#update_dns_domain.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#update_dns_domain.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#update_dns_domain.ApiResponseFor404) | Not Found

#### update_dns_domain.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### update_dns_domain.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### update_dns_domain.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### update_dns_domain.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### update_dns_domain.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[APIKey](../../../openapi-client/README.md#APIKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../openapi-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../openapi-client/README.md#documentation-for-models) [[Back to README]](../../../openapi-client/README.md)

# **update_dns_domain_record**
<a name="update_dns_domain_record"></a>
> update_dns_domain_record(dns_domainrecord_id)

Update Record

Update the information for a DNS record. All attributes are optional. If not set, the attributes will retain their original values.

### Example

* Bearer Authentication (APIKey):
```python
import openapi_client
from openapi_client.apis.tags import dns_api
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
    api_instance = dns_api.DnsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'dns-domain': "dns-domain_example",
        'record-id': "record-id_example",
    }
    try:
        # Update Record
        api_response = api_instance.update_dns_domain_record(
            path_params=path_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling DnsApi->update_dns_domain_record: %s\n" % e)

    # example passing only optional values
    path_params = {
        'dns-domain': "dns-domain_example",
        'record-id': "record-id_example",
    }
    body = dict(
        name="name_example",
        data="data_example",
        ttl=1,
        priority=1,
    )
    try:
        # Update Record
        api_response = api_instance.update_dns_domain_record(
            path_params=path_params,
            body=body,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling DnsApi->update_dns_domain_record: %s\n" % e)
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
**name** | str,  | str,  | The hostname for this DNS record. | [optional] 
**data** | str,  | str,  | The DNS data for this record type. | [optional] 
**ttl** | decimal.Decimal, int,  | decimal.Decimal,  | Time to Live in seconds. | [optional] 
**priority** | decimal.Decimal, int,  | decimal.Decimal,  | DNS priority. Does not apply to all record types. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
dns-domain | DnsDomainSchema | | 
record-id | RecordIdSchema | | 

# DnsDomainSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# RecordIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#update_dns_domain_record.ApiResponseFor204) | No Content

#### update_dns_domain_record.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[APIKey](../../../openapi-client/README.md#APIKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../openapi-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../openapi-client/README.md#documentation-for-models) [[Back to README]](../../../openapi-client/README.md)

# **update_dns_domain_soa**
<a name="update_dns_domain_soa"></a>
> update_dns_domain_soa(dns_domain)

Update SOA information

Update the SOA information for the DNS Domain. All attributes are optional. If not set, the attributes will retain their original values.

### Example

* Bearer Authentication (APIKey):
```python
import openapi_client
from openapi_client.apis.tags import dns_api
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
    api_instance = dns_api.DnsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'dns-domain': "dns-domain_example",
    }
    try:
        # Update SOA information
        api_response = api_instance.update_dns_domain_soa(
            path_params=path_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling DnsApi->update_dns_domain_soa: %s\n" % e)

    # example passing only optional values
    path_params = {
        'dns-domain': "dns-domain_example",
    }
    body = dict(
        nsprimary="nsprimary_example",
        email="email_example",
    )
    try:
        # Update SOA information
        api_response = api_instance.update_dns_domain_soa(
            path_params=path_params,
            body=body,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling DnsApi->update_dns_domain_soa: %s\n" % e)
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
**nsprimary** | str,  | str,  | Set the primary nameserver. | [optional] 
**email** | str,  | str,  | Set the contact email address. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
dns-domain | DnsDomainSchema | | 

# DnsDomainSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#update_dns_domain_soa.ApiResponseFor204) | No Content
400 | [ApiResponseFor400](#update_dns_domain_soa.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#update_dns_domain_soa.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#update_dns_domain_soa.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#update_dns_domain_soa.ApiResponseFor404) | Not Found

#### update_dns_domain_soa.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### update_dns_domain_soa.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### update_dns_domain_soa.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### update_dns_domain_soa.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### update_dns_domain_soa.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[APIKey](../../../openapi-client/README.md#APIKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../openapi-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../openapi-client/README.md#documentation-for-models) [[Back to README]](../../../openapi-client/README.md)

