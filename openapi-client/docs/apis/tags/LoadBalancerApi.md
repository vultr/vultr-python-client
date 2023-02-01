<a name="__pageTop"></a>
# openapi_client.apis.tags.load_balancer_api.LoadBalancerApi

All URIs are relative to *https://api.vultr.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_load_balancer**](#create_load_balancer) | **post** /load-balancers | Create Load Balancer
[**create_load_balancer_forwarding_rules**](#create_load_balancer_forwarding_rules) | **post** /load-balancers/{load-balancer-id}/forwarding-rules | Create Forwarding Rule
[**delete_load_balancer**](#delete_load_balancer) | **delete** /load-balancers/{load-balancer-id} | Delete Load Balancer
[**delete_load_balancer_forwarding_rule**](#delete_load_balancer_forwarding_rule) | **delete** /load-balancers/{load-balancer-id}/forwarding-rules/{forwarding-rule-id} | Delete Forwarding Rule
[**get_load_balancer**](#get_load_balancer) | **get** /load-balancers/{load-balancer-id} | Get Load Balancer
[**get_load_balancer_forwarding_rule**](#get_load_balancer_forwarding_rule) | **get** /load-balancers/{load-balancer-id}/forwarding-rules/{forwarding-rule-id} | Get Forwarding Rule
[**get_loadbalancer_firewall_rule**](#get_loadbalancer_firewall_rule) | **get** /load-balancers/{loadbalancer-id}/firewall-rules/{firewall-rule-id} | Get Firewall Rule
[**list_load_balancer_forwarding_rules**](#list_load_balancer_forwarding_rules) | **get** /load-balancers/{load-balancer-id}/forwarding-rules | List Forwarding Rules
[**list_load_balancers**](#list_load_balancers) | **get** /load-balancers | List Load Balancers
[**list_loadbalancer_firewall_rules**](#list_loadbalancer_firewall_rules) | **get** /load-balancers/{loadbalancer-id}/firewall-rules | List Firewall Rules
[**update_load_balancer**](#update_load_balancer) | **patch** /load-balancers/{load-balancer-id} | Update Load Balancer

# **create_load_balancer**
<a name="create_load_balancer"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_load_balancer()

Create Load Balancer

Create a new Load Balancer in a particular `region`.

### Example

* Bearer Authentication (APIKey):
```python
import openapi_client
from openapi_client.apis.tags import load_balancer_api
from openapi_client.model.loadbalancer import Loadbalancer
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
    api_instance = load_balancer_api.LoadBalancerApi(api_client)

    # example passing only optional values
    body = dict(
        region="region_example",
        balancing_algorithm="balancing_algorithm_example",
        ssl_redirect=True,
        http2=True,
        proxy_protocol=True,
        health_check=dict(
            protocol="protocol_example",
            port=1,
            path="path_example",
            check_interval=1,
            response_timeout=1,
            unhealthy_threshold=1,
            healthy_threshold=1,
        ),
        forwarding_rules=[
            dict(
                frontend_protocol="frontend_protocol_example",
                frontend_port=1,
                backend_protocol="backend_protocol_example",
                backend_port=1,
            )
        ],
        sticky_session=dict(
            cookie_name="cookie_name_example",
        ),
        ssl=dict(
            private_key="private_key_example",
            certificate="certificate_example",
            chain="chain_example",
        ),
        label="label_example",
        instances=[
            "instances_example"
        ],
        firewall_rules=[
            dict(
                port=1,
                source="source_example",
                ip_type="ip_type_example",
            )
        ],
        private_network="private_network_example",
        vpc="vpc_example",
    )
    try:
        # Create Load Balancer
        api_response = api_instance.create_load_balancer(
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LoadBalancerApi->create_load_balancer: %s\n" % e)
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
**region** | str,  | str,  | The [Region id](#operation/list-regions) to create this Load Balancer. | 
**balancing_algorithm** | str,  | str,  | The balancing algorithm.  * roundrobin (default) * leastconn | [optional] 
**ssl_redirect** | bool,  | BoolClass,  | If &#x60;true&#x60;, this will redirect all HTTP traffic to HTTPS. You must have an HTTPS rule and SSL certificate installed on the load balancer to enable this option.  * true * false | [optional] 
**http2** | bool,  | BoolClass,  | If &#x60;true&#x60;, this will enable HTTP2 traffic. You must have an HTTPS forwarding rule combo (HTTPS -&gt; HTTPS) to enable this option.  * true * false | [optional] 
**proxy_protocol** | bool,  | BoolClass,  | If &#x60;true&#x60;, you must configure backend nodes to accept Proxy protocol.  * true * false (Default) | [optional] 
**[health_check](#health_check)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | The health check configuration. See [Load Balancer documentation](https://www.vultr.com/docs/vultr-load-balancers/#Load_Balancer_Configuration). | [optional] 
**[forwarding_rules](#forwarding_rules)** | list, tuple,  | tuple,  | An array of forwarding rule objects. | [optional] 
**[sticky_session](#sticky_session)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Enables sticky sessions for your load balancer when a cookie_name is provided. | [optional] 
**[ssl](#ssl)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | An SSL certificate to install on the Load Balancer. | [optional] 
**label** | str,  | str,  | Label for your Load Balancer. | [optional] 
**[instances](#instances)** | list, tuple,  | tuple,  | An array of instances IDs that you want attached to the load balancer. | [optional] 
**[firewall_rules](#firewall_rules)** | list, tuple,  | tuple,  | An array of firewall rule objects. | [optional] 
**private_network** | str,  | str,  | Use &#x60;vpc&#x60; instead. ID of the private network you wish to use. If private_network is omitted it will default to the public network. | [optional] 
**vpc** | str,  | str,  | ID of the VPC you wish to use. If a VPC ID is omitted it will default to the public network. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# health_check

The health check configuration. See [Load Balancer documentation](https://www.vultr.com/docs/vultr-load-balancers/#Load_Balancer_Configuration).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The health check configuration. See [Load Balancer documentation](https://www.vultr.com/docs/vultr-load-balancers/#Load_Balancer_Configuration). | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**protocol** | str,  | str,  | The protocol to use for health checks.  * HTTPS * HTTP * TCP | [optional] 
**port** | decimal.Decimal, int,  | decimal.Decimal,  | The port to use for health checks. | [optional] 
**path** | str,  | str,  | HTTP Path to check. Only applies if protocol is HTTP, or HTTPS. | [optional] 
**check_interval** | decimal.Decimal, int,  | decimal.Decimal,  | Interval between health checks. | [optional] 
**response_timeout** | decimal.Decimal, int,  | decimal.Decimal,  | Timeout before health check fails. | [optional] 
**unhealthy_threshold** | decimal.Decimal, int,  | decimal.Decimal,  | Number times a check must fail before becoming unhealthy. | [optional] 
**healthy_threshold** | decimal.Decimal, int,  | decimal.Decimal,  | Number of times a check must succeed before returning to healthy status. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# forwarding_rules

An array of forwarding rule objects.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | An array of forwarding rule objects. | 

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
**frontend_protocol** | str,  | str,  | The protocol on the Load Balancer to forward to the backend.  * HTTP * HTTPS * TCP | [optional] 
**frontend_port** | decimal.Decimal, int,  | decimal.Decimal,  | The port number on the Load Balancer to forward to the backend. | [optional] 
**backend_protocol** | str,  | str,  | The protocol destination on the backend server.  * HTTP * HTTPS * TCP | [optional] 
**backend_port** | decimal.Decimal, int,  | decimal.Decimal,  | The port number destination on the backend server. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# sticky_session

Enables sticky sessions for your load balancer when a cookie_name is provided.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Enables sticky sessions for your load balancer when a cookie_name is provided. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**cookie_name** | str,  | str,  | The cookie name to make sticky. See [Load Balancer documentation](https://www.vultr.com/docs/vultr-load-balancers/#Load_Balancer_Configuration). | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# ssl

An SSL certificate to install on the Load Balancer.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | An SSL certificate to install on the Load Balancer. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**private_key** | str,  | str,  | The private key. | [optional] 
**certificate** | str,  | str,  | The SSL certificate. | [optional] 
**chain** | str,  | str,  | The certificate chain. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# instances

An array of instances IDs that you want attached to the load balancer.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | An array of instances IDs that you want attached to the load balancer. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# firewall_rules

An array of firewall rule objects.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | An array of firewall rule objects. | 

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
**port** | decimal.Decimal, int,  | decimal.Decimal,  | Port for this rule. | [optional] 
**source** | str,  | str,  | If the source string is given a value of \&quot;cloudflare\&quot; then cloudflare IPs will be supplied. Otherwise enter a IP address with subnet size that you wish to permit through the firewall.  Possible values:  |   | Value | Description | | - | ------ | ------------- | |   | \&quot;192.168.1.1/16\&quot; | Ip address with a subnet size. | |   | cloudflare | Allow all of Cloudflare&#x27;s IP space through the firewall | | [optional] 
**ip_type** | str,  | str,  | The type of IP rule.  * v4 * v6 | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
202 | [ApiResponseFor202](#create_load_balancer.ApiResponseFor202) | Accepted
400 | [ApiResponseFor400](#create_load_balancer.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#create_load_balancer.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#create_load_balancer.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#create_load_balancer.ApiResponseFor404) | Not Found

#### create_load_balancer.ApiResponseFor202
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
**load_balancer** | [**Loadbalancer**]({{complexTypePrefix}}Loadbalancer.md) | [**Loadbalancer**]({{complexTypePrefix}}Loadbalancer.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### create_load_balancer.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### create_load_balancer.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### create_load_balancer.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### create_load_balancer.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[APIKey](../../../openapi-client/README.md#APIKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../openapi-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../openapi-client/README.md#documentation-for-models) [[Back to README]](../../../openapi-client/README.md)

# **create_load_balancer_forwarding_rules**
<a name="create_load_balancer_forwarding_rules"></a>
> create_load_balancer_forwarding_rules(load_balancer_id)

Create Forwarding Rule

Create a new forwarding rule for a Load Balancer.

### Example

* Bearer Authentication (APIKey):
```python
import openapi_client
from openapi_client.apis.tags import load_balancer_api
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
    api_instance = load_balancer_api.LoadBalancerApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'load-balancer-id': "load-balancer-id_example",
    }
    try:
        # Create Forwarding Rule
        api_response = api_instance.create_load_balancer_forwarding_rules(
            path_params=path_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling LoadBalancerApi->create_load_balancer_forwarding_rules: %s\n" % e)

    # example passing only optional values
    path_params = {
        'load-balancer-id': "load-balancer-id_example",
    }
    body = dict(
        frontend_protocol="frontend_protocol_example",
        frontend_port=1,
        backend_protocol="backend_protocol_example",
        backend_port=1,
    )
    try:
        # Create Forwarding Rule
        api_response = api_instance.create_load_balancer_forwarding_rules(
            path_params=path_params,
            body=body,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling LoadBalancerApi->create_load_balancer_forwarding_rules: %s\n" % e)
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
**frontend_protocol** | str,  | str,  | The protocol on the Load Balancer to forward to the backend.  * HTTP * HTTPS * TCP | 
**frontend_port** | decimal.Decimal, int,  | decimal.Decimal,  | The port number on the Load Balancer to forward to the backend. | 
**backend_port** | decimal.Decimal, int,  | decimal.Decimal,  | The port number destination on the backend server. | 
**backend_protocol** | str,  | str,  | The protocol destination on the backend server.  * HTTP * HTTPS * TCP | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
load-balancer-id | LoadBalancerIdSchema | | 

# LoadBalancerIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
202 | [ApiResponseFor202](#create_load_balancer_forwarding_rules.ApiResponseFor202) | Accepted
400 | [ApiResponseFor400](#create_load_balancer_forwarding_rules.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#create_load_balancer_forwarding_rules.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#create_load_balancer_forwarding_rules.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#create_load_balancer_forwarding_rules.ApiResponseFor404) | Not Found

#### create_load_balancer_forwarding_rules.ApiResponseFor202
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### create_load_balancer_forwarding_rules.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### create_load_balancer_forwarding_rules.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### create_load_balancer_forwarding_rules.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### create_load_balancer_forwarding_rules.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[APIKey](../../../openapi-client/README.md#APIKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../openapi-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../openapi-client/README.md#documentation-for-models) [[Back to README]](../../../openapi-client/README.md)

# **delete_load_balancer**
<a name="delete_load_balancer"></a>
> delete_load_balancer(load_balancer_id)

Delete Load Balancer

Delete a Load Balancer.

### Example

* Bearer Authentication (APIKey):
```python
import openapi_client
from openapi_client.apis.tags import load_balancer_api
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
    api_instance = load_balancer_api.LoadBalancerApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'load-balancer-id': "load-balancer-id_example",
    }
    try:
        # Delete Load Balancer
        api_response = api_instance.delete_load_balancer(
            path_params=path_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling LoadBalancerApi->delete_load_balancer: %s\n" % e)
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
load-balancer-id | LoadBalancerIdSchema | | 

# LoadBalancerIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#delete_load_balancer.ApiResponseFor204) | No Content
400 | [ApiResponseFor400](#delete_load_balancer.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#delete_load_balancer.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#delete_load_balancer.ApiResponseFor404) | Not Found

#### delete_load_balancer.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_load_balancer.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_load_balancer.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_load_balancer.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[APIKey](../../../openapi-client/README.md#APIKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../openapi-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../openapi-client/README.md#documentation-for-models) [[Back to README]](../../../openapi-client/README.md)

# **delete_load_balancer_forwarding_rule**
<a name="delete_load_balancer_forwarding_rule"></a>
> delete_load_balancer_forwarding_rule(load_balancer_idforwarding_rule_id)

Delete Forwarding Rule

Delete a Forwarding Rule on a Load Balancer.

### Example

* Bearer Authentication (APIKey):
```python
import openapi_client
from openapi_client.apis.tags import load_balancer_api
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
    api_instance = load_balancer_api.LoadBalancerApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'load-balancer-id': "load-balancer-id_example",
        'forwarding-rule-id': "forwarding-rule-id_example",
    }
    try:
        # Delete Forwarding Rule
        api_response = api_instance.delete_load_balancer_forwarding_rule(
            path_params=path_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling LoadBalancerApi->delete_load_balancer_forwarding_rule: %s\n" % e)
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
load-balancer-id | LoadBalancerIdSchema | | 
forwarding-rule-id | ForwardingRuleIdSchema | | 

# LoadBalancerIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ForwardingRuleIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#delete_load_balancer_forwarding_rule.ApiResponseFor204) | No Content
400 | [ApiResponseFor400](#delete_load_balancer_forwarding_rule.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#delete_load_balancer_forwarding_rule.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#delete_load_balancer_forwarding_rule.ApiResponseFor404) | Not Found

#### delete_load_balancer_forwarding_rule.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_load_balancer_forwarding_rule.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_load_balancer_forwarding_rule.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_load_balancer_forwarding_rule.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[APIKey](../../../openapi-client/README.md#APIKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../openapi-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../openapi-client/README.md#documentation-for-models) [[Back to README]](../../../openapi-client/README.md)

# **get_load_balancer**
<a name="get_load_balancer"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_load_balancer(load_balancer_id)

Get Load Balancer

Get information for a Load Balancer.

### Example

* Bearer Authentication (APIKey):
```python
import openapi_client
from openapi_client.apis.tags import load_balancer_api
from openapi_client.model.loadbalancer import Loadbalancer
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
    api_instance = load_balancer_api.LoadBalancerApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'load-balancer-id': "load-balancer-id_example",
    }
    try:
        # Get Load Balancer
        api_response = api_instance.get_load_balancer(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LoadBalancerApi->get_load_balancer: %s\n" % e)
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
load-balancer-id | LoadBalancerIdSchema | | 

# LoadBalancerIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_load_balancer.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#get_load_balancer.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#get_load_balancer.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#get_load_balancer.ApiResponseFor404) | Not Found

#### get_load_balancer.ApiResponseFor200
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
**load_balancer** | [**Loadbalancer**]({{complexTypePrefix}}Loadbalancer.md) | [**Loadbalancer**]({{complexTypePrefix}}Loadbalancer.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### get_load_balancer.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_load_balancer.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_load_balancer.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[APIKey](../../../openapi-client/README.md#APIKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../openapi-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../openapi-client/README.md#documentation-for-models) [[Back to README]](../../../openapi-client/README.md)

# **get_load_balancer_forwarding_rule**
<a name="get_load_balancer_forwarding_rule"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_load_balancer_forwarding_rule(load_balancer_idforwarding_rule_id)

Get Forwarding Rule

Get information for a Forwarding Rule on a Load Balancer.

### Example

* Bearer Authentication (APIKey):
```python
import openapi_client
from openapi_client.apis.tags import load_balancer_api
from openapi_client.model.forwarding_rule import ForwardingRule
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
    api_instance = load_balancer_api.LoadBalancerApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'load-balancer-id': "load-balancer-id_example",
        'forwarding-rule-id': "forwarding-rule-id_example",
    }
    try:
        # Get Forwarding Rule
        api_response = api_instance.get_load_balancer_forwarding_rule(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LoadBalancerApi->get_load_balancer_forwarding_rule: %s\n" % e)
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
load-balancer-id | LoadBalancerIdSchema | | 
forwarding-rule-id | ForwardingRuleIdSchema | | 

# LoadBalancerIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ForwardingRuleIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_load_balancer_forwarding_rule.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#get_load_balancer_forwarding_rule.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#get_load_balancer_forwarding_rule.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#get_load_balancer_forwarding_rule.ApiResponseFor404) | Not Found

#### get_load_balancer_forwarding_rule.ApiResponseFor200
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
**forwarding_rule** | [**ForwardingRule**]({{complexTypePrefix}}ForwardingRule.md) | [**ForwardingRule**]({{complexTypePrefix}}ForwardingRule.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### get_load_balancer_forwarding_rule.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_load_balancer_forwarding_rule.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_load_balancer_forwarding_rule.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[APIKey](../../../openapi-client/README.md#APIKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../openapi-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../openapi-client/README.md#documentation-for-models) [[Back to README]](../../../openapi-client/README.md)

# **get_loadbalancer_firewall_rule**
<a name="get_loadbalancer_firewall_rule"></a>
> LoadbalancerFirewallRule get_loadbalancer_firewall_rule(loadbalancer_idfirewall_rule_id)

Get Firewall Rule

Get a firewall rule for a Load Balancer.

### Example

* Bearer Authentication (APIKey):
```python
import openapi_client
from openapi_client.apis.tags import load_balancer_api
from openapi_client.model.loadbalancer_firewall_rule import LoadbalancerFirewallRule
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
    api_instance = load_balancer_api.LoadBalancerApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'loadbalancer-id': "loadbalancer-id_example",
        'firewall-rule-id': "firewall-rule-id_example",
    }
    try:
        # Get Firewall Rule
        api_response = api_instance.get_loadbalancer_firewall_rule(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LoadBalancerApi->get_loadbalancer_firewall_rule: %s\n" % e)
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
loadbalancer-id | LoadbalancerIdSchema | | 
firewall-rule-id | FirewallRuleIdSchema | | 

# LoadbalancerIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FirewallRuleIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_loadbalancer_firewall_rule.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#get_loadbalancer_firewall_rule.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#get_loadbalancer_firewall_rule.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#get_loadbalancer_firewall_rule.ApiResponseFor404) | Not Found

#### get_loadbalancer_firewall_rule.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**LoadbalancerFirewallRule**](../../models/LoadbalancerFirewallRule.md) |  | 


#### get_loadbalancer_firewall_rule.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_loadbalancer_firewall_rule.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_loadbalancer_firewall_rule.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[APIKey](../../../openapi-client/README.md#APIKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../openapi-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../openapi-client/README.md#documentation-for-models) [[Back to README]](../../../openapi-client/README.md)

# **list_load_balancer_forwarding_rules**
<a name="list_load_balancer_forwarding_rules"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} list_load_balancer_forwarding_rules(load_balancer_id)

List Forwarding Rules

List the fowarding rules for a Load Balancer.

### Example

* Bearer Authentication (APIKey):
```python
import openapi_client
from openapi_client.apis.tags import load_balancer_api
from openapi_client.model.meta import Meta
from openapi_client.model.forwarding_rule import ForwardingRule
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
    api_instance = load_balancer_api.LoadBalancerApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'load-balancer-id': "load-balancer-id_example",
    }
    query_params = {
    }
    try:
        # List Forwarding Rules
        api_response = api_instance.list_load_balancer_forwarding_rules(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LoadBalancerApi->list_load_balancer_forwarding_rules: %s\n" % e)

    # example passing only optional values
    path_params = {
        'load-balancer-id': "load-balancer-id_example",
    }
    query_params = {
        'per_page': 1,
        'cursor': "cursor_example",
    }
    try:
        # List Forwarding Rules
        api_response = api_instance.list_load_balancer_forwarding_rules(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LoadBalancerApi->list_load_balancer_forwarding_rules: %s\n" % e)
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
load-balancer-id | LoadBalancerIdSchema | | 

# LoadBalancerIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_load_balancer_forwarding_rules.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#list_load_balancer_forwarding_rules.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#list_load_balancer_forwarding_rules.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#list_load_balancer_forwarding_rules.ApiResponseFor404) | Not Found

#### list_load_balancer_forwarding_rules.ApiResponseFor200
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
**[forwarding_rules](#forwarding_rules)** | list, tuple,  | tuple,  |  | [optional] 
**meta** | [**Meta**]({{complexTypePrefix}}Meta.md) | [**Meta**]({{complexTypePrefix}}Meta.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# forwarding_rules

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ForwardingRule**]({{complexTypePrefix}}ForwardingRule.md) | [**ForwardingRule**]({{complexTypePrefix}}ForwardingRule.md) | [**ForwardingRule**]({{complexTypePrefix}}ForwardingRule.md) |  | 

#### list_load_balancer_forwarding_rules.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### list_load_balancer_forwarding_rules.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### list_load_balancer_forwarding_rules.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[APIKey](../../../openapi-client/README.md#APIKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../openapi-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../openapi-client/README.md#documentation-for-models) [[Back to README]](../../../openapi-client/README.md)

# **list_load_balancers**
<a name="list_load_balancers"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} list_load_balancers()

List Load Balancers

List the Load Balancers in your account.

### Example

* Bearer Authentication (APIKey):
```python
import openapi_client
from openapi_client.apis.tags import load_balancer_api
from openapi_client.model.loadbalancer import Loadbalancer
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
    api_instance = load_balancer_api.LoadBalancerApi(api_client)

    # example passing only optional values
    query_params = {
        'per_page': 1,
        'cursor': "cursor_example",
    }
    try:
        # List Load Balancers
        api_response = api_instance.list_load_balancers(
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LoadBalancerApi->list_load_balancers: %s\n" % e)
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
200 | [ApiResponseFor200](#list_load_balancers.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#list_load_balancers.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#list_load_balancers.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#list_load_balancers.ApiResponseFor404) | Not Found

#### list_load_balancers.ApiResponseFor200
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
**[load_balancers](#load_balancers)** | list, tuple,  | tuple,  |  | [optional] 
**meta** | [**Meta**]({{complexTypePrefix}}Meta.md) | [**Meta**]({{complexTypePrefix}}Meta.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# load_balancers

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Loadbalancer**]({{complexTypePrefix}}Loadbalancer.md) | [**Loadbalancer**]({{complexTypePrefix}}Loadbalancer.md) | [**Loadbalancer**]({{complexTypePrefix}}Loadbalancer.md) |  | 

#### list_load_balancers.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### list_load_balancers.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### list_load_balancers.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[APIKey](../../../openapi-client/README.md#APIKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../openapi-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../openapi-client/README.md#documentation-for-models) [[Back to README]](../../../openapi-client/README.md)

# **list_loadbalancer_firewall_rules**
<a name="list_loadbalancer_firewall_rules"></a>
> LoadbalancerFirewallRule list_loadbalancer_firewall_rules(loadbalancer_id)

List Firewall Rules

List the firewall rules for a Load Balancer.

### Example

* Bearer Authentication (APIKey):
```python
import openapi_client
from openapi_client.apis.tags import load_balancer_api
from openapi_client.model.loadbalancer_firewall_rule import LoadbalancerFirewallRule
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
    api_instance = load_balancer_api.LoadBalancerApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'loadbalancer-id': "loadbalancer-id_example",
    }
    query_params = {
    }
    try:
        # List Firewall Rules
        api_response = api_instance.list_loadbalancer_firewall_rules(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LoadBalancerApi->list_loadbalancer_firewall_rules: %s\n" % e)

    # example passing only optional values
    path_params = {
        'loadbalancer-id': "loadbalancer-id_example",
    }
    query_params = {
        'per_page': "per_page_example",
        'cursor': "cursor_example",
    }
    try:
        # List Firewall Rules
        api_response = api_instance.list_loadbalancer_firewall_rules(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LoadBalancerApi->list_loadbalancer_firewall_rules: %s\n" % e)
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
str,  | str,  |  | 

# CursorSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
loadbalancer-id | LoadbalancerIdSchema | | 

# LoadbalancerIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_loadbalancer_firewall_rules.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#list_loadbalancer_firewall_rules.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#list_loadbalancer_firewall_rules.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#list_loadbalancer_firewall_rules.ApiResponseFor404) | Not Found

#### list_loadbalancer_firewall_rules.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**LoadbalancerFirewallRule**](../../models/LoadbalancerFirewallRule.md) |  | 


#### list_loadbalancer_firewall_rules.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### list_loadbalancer_firewall_rules.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### list_loadbalancer_firewall_rules.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[APIKey](../../../openapi-client/README.md#APIKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../openapi-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../openapi-client/README.md#documentation-for-models) [[Back to README]](../../../openapi-client/README.md)

# **update_load_balancer**
<a name="update_load_balancer"></a>
> update_load_balancer(load_balancer_id)

Update Load Balancer

Update information for a Load Balancer. All attributes are optional. If not set, the attributes will retain their original values.

### Example

* Bearer Authentication (APIKey):
```python
import openapi_client
from openapi_client.apis.tags import load_balancer_api
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
    api_instance = load_balancer_api.LoadBalancerApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'load-balancer-id': "load-balancer-id_example",
    }
    try:
        # Update Load Balancer
        api_response = api_instance.update_load_balancer(
            path_params=path_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling LoadBalancerApi->update_load_balancer: %s\n" % e)

    # example passing only optional values
    path_params = {
        'load-balancer-id': "load-balancer-id_example",
    }
    body = dict(
        ssl=dict(
            private_key="private_key_example",
            certificate="certificate_example",
            chain="chain_example",
        ),
        sticky_session=dict(
            cookie_name="cookie_name_example",
        ),
        forwarding_rules=[
            dict(
                frontend_protocol="frontend_protocol_example",
                frontend_port=1,
                backend_protocol="backend_protocol_example",
                backend_port=1,
            )
        ],
        health_check=dict(
            protocol="protocol_example",
            port=1,
            path="path_example",
            check_interval="check_interval_example",
            response_timeout="response_timeout_example",
            unhealthy_threshold="unhealthy_threshold_example",
            healthy_threshold="healthy_threshold_example",
        ),
        proxy_protocol=True,
        ssl_redirect=True,
        http2=True,
        balancing_algorithm="balancing_algorithm_example",
        instances=[
            "instances_example"
        ],
        label="label_example",
        private_network="private_network_example",
        vpc="vpc_example",
        firewall_rules=[
            dict(
                port=1,
                source="source_example",
                ip_type="ip_type_example",
            )
        ],
    )
    try:
        # Update Load Balancer
        api_response = api_instance.update_load_balancer(
            path_params=path_params,
            body=body,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling LoadBalancerApi->update_load_balancer: %s\n" % e)
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
**[ssl](#ssl)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | An SSL certificate to install on the Load Balancer. | [optional] 
**[sticky_session](#sticky_session)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Enables sticky sessions for your load balancer when a cookie_name is provided. | [optional] 
**[forwarding_rules](#forwarding_rules)** | list, tuple,  | tuple,  | An array of forwarding rule objects. | [optional] 
**[health_check](#health_check)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | The health check configuration. [See Load Balancer documentation](https://www.vultr.com/docs/vultr-load-balancers/#Load_Balancer_Configuration). | [optional] 
**proxy_protocol** | bool,  | BoolClass,  | If &#x60;true&#x60;, you must configure backend nodes to accept Proxy protocol.  * true * false (Default) | [optional] 
**ssl_redirect** | bool,  | BoolClass,  | If &#x60;true&#x60;, this will redirect all HTTP traffic to HTTPS. You must have an HTTPS rule and SSL certificate installed on the load balancer to enable this option.  * true * false | [optional] 
**http2** | bool,  | BoolClass,  | If &#x60;true&#x60;, this will enable HTTP2 traffic. You must have an HTTPS forwarding rule combo (HTTPS -&gt; HTTPS) to enable this option.  * true * false | [optional] 
**balancing_algorithm** | str,  | str,  | The balancing algorithm.  * roundrobin (default) * leastconn | [optional] 
**[instances](#instances)** | list, tuple,  | tuple,  | Send the complete array of Instances IDs that should be attached to this Load Balancer. Instances will be attached or detached to match your array. For example, if Instances **X**, **Y**, and **Z** are currently attached, and you send [A,B,Z], then Instance **A** and **B** will be attached,  **X** and **Y** will be detached, and **Z** will remain attached. | [optional] 
**label** | str,  | str,  | The label for your Load Balancer | [optional] 
**private_network** | str,  | str,  | Use &#x60;vpc&#x60; instead. ID of the private network you wish to use. If private_network is omitted it will default to the public network. | [optional] 
**vpc** | str,  | str,  | ID of the VPC you wish to use. If a VPC ID is omitted it will default to the public network. | [optional] 
**[firewall_rules](#firewall_rules)** | list, tuple,  | tuple,  | An array of firewall rule objects. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# ssl

An SSL certificate to install on the Load Balancer.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | An SSL certificate to install on the Load Balancer. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**private_key** | str,  | str,  | The private key. | [optional] 
**certificate** | str,  | str,  | The SSL certificate. | [optional] 
**chain** | str,  | str,  | The certificate chain. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# sticky_session

Enables sticky sessions for your load balancer when a cookie_name is provided.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Enables sticky sessions for your load balancer when a cookie_name is provided. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**cookie_name** | str,  | str,  | The cookie name to make sticky. See [Load Balancer documentation](https://www.vultr.com/docs/vultr-load-balancers/#Load_Balancer_Configuration). | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# forwarding_rules

An array of forwarding rule objects.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | An array of forwarding rule objects. | 

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
**frontend_protocol** | str,  | str,  | The protocol on the Load Balancer to forward to the backend.  * HTTP * HTTPS * TCP | [optional] 
**frontend_port** | decimal.Decimal, int,  | decimal.Decimal,  | The port number on the Load Balancer to forward to the backend. | [optional] 
**backend_protocol** | str,  | str,  | The protocol destination on the backend server.  * HTTP * HTTPS * TCP | [optional] 
**backend_port** | decimal.Decimal, int,  | decimal.Decimal,  | The port number destination on the backend server. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# health_check

The health check configuration. [See Load Balancer documentation](https://www.vultr.com/docs/vultr-load-balancers/#Load_Balancer_Configuration).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The health check configuration. [See Load Balancer documentation](https://www.vultr.com/docs/vultr-load-balancers/#Load_Balancer_Configuration). | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**protocol** | str,  | str,  | The protocol to use for health checks.  * HTTPS * HTTP * TCP | [optional] 
**port** | decimal.Decimal, int,  | decimal.Decimal,  | The port to use for health checks. | [optional] 
**path** | str,  | str,  | HTTP Path to check. Only applies if protocol is HTTP, or HTTPS. | [optional] 
**check_interval** | str,  | str,  | Interval between health checks. | [optional] 
**response_timeout** | str,  | str,  | Timeout before health check fails. | [optional] 
**unhealthy_threshold** | str,  | str,  | Number times a check must fail before becoming unhealthy. | [optional] 
**healthy_threshold** | str,  | str,  | Number of times a check must succeed before returning to healthy status. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# instances

Send the complete array of Instances IDs that should be attached to this Load Balancer. Instances will be attached or detached to match your array. For example, if Instances **X**, **Y**, and **Z** are currently attached, and you send [A,B,Z], then Instance **A** and **B** will be attached,  **X** and **Y** will be detached, and **Z** will remain attached.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Send the complete array of Instances IDs that should be attached to this Load Balancer. Instances will be attached or detached to match your array. For example, if Instances **X**, **Y**, and **Z** are currently attached, and you send [A,B,Z], then Instance **A** and **B** will be attached,  **X** and **Y** will be detached, and **Z** will remain attached. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# firewall_rules

An array of firewall rule objects.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | An array of firewall rule objects. | 

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
**port** | decimal.Decimal, int,  | decimal.Decimal,  | Port for this rule. | [optional] 
**source** | str,  | str,  | If the source string is given a value of \&quot;cloudflare\&quot; then cloudflare IPs will be supplied. Otherwise enter a IP address with subnet size that you wish to permit through the firewall.  Possible values:  |   | Value | Description | | - | ------ | ------------- | |   | \&quot;192.168.1.1/16\&quot; | Ip address with a subnet size. | |   | cloudflare | Allow all of Cloudflare&#x27;s IP space through the firewall | | [optional] 
**ip_type** | str,  | str,  | The type of IP rule.  * v4 * v6 | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
load-balancer-id | LoadBalancerIdSchema | | 

# LoadBalancerIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#update_load_balancer.ApiResponseFor204) | No Content
400 | [ApiResponseFor400](#update_load_balancer.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#update_load_balancer.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#update_load_balancer.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#update_load_balancer.ApiResponseFor404) | Not Found

#### update_load_balancer.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### update_load_balancer.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### update_load_balancer.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### update_load_balancer.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### update_load_balancer.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[APIKey](../../../openapi-client/README.md#APIKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../openapi-client/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../openapi-client/README.md#documentation-for-models) [[Back to README]](../../../openapi-client/README.md)

