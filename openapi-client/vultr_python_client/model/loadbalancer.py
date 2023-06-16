# coding: utf-8

"""
    Vultr API

    # Introduction  The Vultr API v2 is a set of HTTP endpoints that adhere to RESTful design principles and CRUD actions with predictable URIs. It uses standard HTTP response codes, authentication, and verbs. The API has consistent and well-formed JSON requests and responses with cursor-based pagination to simplify list handling. Error messages are descriptive and easy to understand. All functions of the Vultr customer portal are accessible via the API, enabling you to script complex unattended scenarios with any tool fluent in HTTP.  ## Requests  Communicate with the API by making an HTTP request at the correct endpoint. The chosen method determines the action taken.  | Method | Usage | | ------ | ------------- | | DELETE | Use the DELETE method to destroy a resource in your account. If it is not found, the operation will return a 4xx error and an appropriate message. | | GET | To retrieve information about a resource, use the GET method. The data is returned as a JSON object. GET methods are read-only and do not affect any resources. | | PATCH | Some resources support partial modification with PATCH, which modifies specific attributes without updating the entire object representation. | | POST | Issue a POST method to create a new object. Include all needed attributes in the request body encoded as JSON. | | PUT | Use the PUT method to update information about a resource. PUT will set new values on the item without regard to their current values. |  **Rate Limit:** Vultr safeguards the API against bursts of incoming traffic based on the request's IP address to ensure stability for all users. If your application sends more than 30 requests per second, the API may return HTTP status code 429.  ## Response Codes  We use standard HTTP response codes to show the success or failure of requests. Response codes in the 2xx range indicate success, while codes in the 4xx range indicate an error, such as an authorization failure or a malformed request. All 4xx errors will return a JSON response object with an `error` attribute explaining the error. Codes in the 5xx range indicate a server-side problem preventing Vultr from fulfilling your request.  | Response | Description | | ------ | ------------- | | 200 OK | The response contains your requested information. | | 201 Created | Your request was accepted. The resource was created. | | 202 Accepted | Your request was accepted. The resource was created or updated. | | 204 No Content | Your request succeeded, there is no additional information returned. | | 400 Bad Request | Your request was malformed. | | 401 Unauthorized | You did not supply valid authentication credentials. | | 403 Forbidden | You are not allowed to perform that action. | | 404 Not Found | No results were found for your request. | | 429 Too Many Requests | Your request exceeded the API rate limit. | | 500 Internal Server Error | We were unable to perform the request due to server-side problems. |  ## Meta and Pagination  Many API calls will return a `meta` object with paging information.  ### Definitions  | Term | Description | | ------ | ------------- | | **List** | The items returned from the database for your request (not necessarily shown in a single response depending on the **cursor** size). | | **Page** | A subset of the full **list** of items. Choose the size of a **page** with the `per_page` parameter. | | **Total** | The `total` attribute indicates the number of items in the full **list**.| | **Cursor** | Use the `cursor` query parameter to select a next or previous **page**. | | **Next** & **Prev** | Use the `next` and `prev` attributes of the `links` meta object as `cursor` values. |  ### How to use Paging  If your result **list** total exceeds the default **cursor** size (the default depends on the route, but is usually 100 records) or the value defined by the `per_page` query param (when present) the response will be returned to you paginated.  ### Paging Example  > These examples have abbreviated attributes and sample values. Your actual `cursor` values will be encoded alphanumeric strings.  To return a **page** with the first two plans in the List:      curl \"https://api.vultr.com/v2/plans?per_page=2\" \\       -X GET \\       -H \"Authorization: Bearer ${VULTR_API_KEY}\"  The API returns an object similar to this:      {         \"plans\": [             {                 \"id\": \"vc2-1c-2gb\",                 \"vcpu_count\": 1,                 \"ram\": 2048,                 \"locations\": []             },             {                 \"id\": \"vc2-24c-97gb\",                 \"vcpu_count\": 24,                 \"ram\": 98304,                 \"locations\": []             }         ],         \"meta\": {             \"total\": 19,             \"links\": {                 \"next\": \"WxYzExampleNext\",                 \"prev\": \"WxYzExamplePrev\"             }         }     }  The object contains two plans. The `total` attribute indicates that 19 plans are available in the List. To navigate forward in the **list**, use the `next` value (`WxYzExampleNext` in this example) as your `cursor` query parameter.      curl \"https://api.vultr.com/v2/plans?per_page=2&cursor=WxYzExampleNext\" \\       -X GET       -H \"Authorization: Bearer ${VULTR_API_KEY}\"  Likewise, you can use the example `prev` value `WxYzExamplePrev` to navigate backward.  ## Parameters  You can pass information to the API with three different types of parameters.  ### Path parameters  Some API calls require variable parameters as part of the endpoint path. For example, to retrieve information about a user, supply the `user-id` in the endpoint.      curl \"https://api.vultr.com/v2/users/{user-id}\" \\       -X GET \\       -H \"Authorization: Bearer ${VULTR_API_KEY}\"  ### Query parameters  Some API calls allow filtering with query parameters. For example, the `/v2/plans` endpoint supports a `type` query parameter. Setting `type=vhf` instructs the API only to return High Frequency Compute plans in the list. You'll find more specifics about valid filters in the endpoint documentation below.      curl \"https://api.vultr.com/v2/plans?type=vhf\" \\       -X GET \\       -H \"Authorization: Bearer ${VULTR_API_KEY}\"  You can also combine filtering with paging. Use the `per_page` parameter to retreive a subset of vhf plans.      curl \"https://api.vultr.com/v2/plans?type=vhf&per_page=2\" \\       -X GET \\       -H \"Authorization: Bearer ${VULTR_API_KEY}\"  ### Request Body  PUT, POST, and PATCH methods may include an object in the request body with a content type of **application/json**. The documentation for each endpoint below has more information about the expected object.  ## API Example Conventions  The examples in this documentation use `curl`, a command-line HTTP client, to demonstrate useage. Linux and macOS computers usually have curl installed by default, and it's [available for download](https://curl.se/download.html) on all popular platforms including Windows.  Each example is split across multiple lines with the `\\` character, which is compatible with a `bash` terminal. A typical example looks like this:      curl \"https://api.vultr.com/v2/domains\" \\       -X POST \\       -H \"Authorization: Bearer ${VULTR_API_KEY}\" \\       -H \"Content-Type: application/json\" \\       --data '{         \"domain\" : \"example.com\",         \"ip\" : \"192.0.2.123\"       }'  * The `-X` parameter sets the request method. For consistency, we show the method on all examples, even though it's not explicitly required for GET methods. * The `-H` lines set required HTTP headers. These examples are formatted to expand the VULTR\\_API\\_KEY environment variable for your convenience. * Examples that require a JSON object in the request body pass the required data via the `--data` parameter.  All values in this guide are examples. Do not rely on the OS or Plan IDs listed in this guide; use the appropriate endpoint to retreive values before creating resources.  # Authentication  <!-- ReDoc-Inject: <security-definitions> -->  # noqa: E501

    The version of the OpenAPI document: 2.0
    Contact: opensource@vultr.com
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from vultr_python_client import schemas  # noqa: F401


class Loadbalancer(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Load Balancer information.
    """


    class MetaOapg:
        
        class properties:
            id = schemas.StrSchema
            date_created = schemas.StrSchema
            region = schemas.StrSchema
            label = schemas.StrSchema
            status = schemas.StrSchema
            ipv4 = schemas.StrSchema
            ipv6 = schemas.StrSchema
            
            
            class generic_info(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    class properties:
                        balancing_algorithm = schemas.StrSchema
                        ssl_redirect = schemas.BoolSchema
                        
                        
                        class sticky_sessions(
                            schemas.DictSchema
                        ):
                        
                        
                            class MetaOapg:
                                
                                class properties:
                                    cookie_name = schemas.StrSchema
                                    __annotations__ = {
                                        "cookie_name": cookie_name,
                                    }
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["cookie_name"]) -> MetaOapg.properties.cookie_name: ...
                            
                            @typing.overload
                            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                            
                            def __getitem__(self, name: typing.Union[typing_extensions.Literal["cookie_name", ], str]):
                                # dict_instance[name] accessor
                                return super().__getitem__(name)
                            
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["cookie_name"]) -> typing.Union[MetaOapg.properties.cookie_name, schemas.Unset]: ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                            
                            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["cookie_name", ], str]):
                                return super().get_item_oapg(name)
                            
                        
                            def __new__(
                                cls,
                                *_args: typing.Union[dict, frozendict.frozendict, ],
                                cookie_name: typing.Union[MetaOapg.properties.cookie_name, str, schemas.Unset] = schemas.unset,
                                _configuration: typing.Optional[schemas.Configuration] = None,
                                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                            ) -> 'sticky_sessions':
                                return super().__new__(
                                    cls,
                                    *_args,
                                    cookie_name=cookie_name,
                                    _configuration=_configuration,
                                    **kwargs,
                                )
                        proxy_protocol = schemas.BoolSchema
                        private_network = schemas.StrSchema
                        vpc = schemas.StrSchema
                        __annotations__ = {
                            "balancing_algorithm": balancing_algorithm,
                            "ssl_redirect": ssl_redirect,
                            "sticky_sessions": sticky_sessions,
                            "proxy_protocol": proxy_protocol,
                            "private_network": private_network,
                            "vpc": vpc,
                        }
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["balancing_algorithm"]) -> MetaOapg.properties.balancing_algorithm: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["ssl_redirect"]) -> MetaOapg.properties.ssl_redirect: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["sticky_sessions"]) -> MetaOapg.properties.sticky_sessions: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["proxy_protocol"]) -> MetaOapg.properties.proxy_protocol: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["private_network"]) -> MetaOapg.properties.private_network: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["vpc"]) -> MetaOapg.properties.vpc: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["balancing_algorithm", "ssl_redirect", "sticky_sessions", "proxy_protocol", "private_network", "vpc", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["balancing_algorithm"]) -> typing.Union[MetaOapg.properties.balancing_algorithm, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["ssl_redirect"]) -> typing.Union[MetaOapg.properties.ssl_redirect, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["sticky_sessions"]) -> typing.Union[MetaOapg.properties.sticky_sessions, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["proxy_protocol"]) -> typing.Union[MetaOapg.properties.proxy_protocol, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["private_network"]) -> typing.Union[MetaOapg.properties.private_network, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["vpc"]) -> typing.Union[MetaOapg.properties.vpc, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["balancing_algorithm", "ssl_redirect", "sticky_sessions", "proxy_protocol", "private_network", "vpc", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    balancing_algorithm: typing.Union[MetaOapg.properties.balancing_algorithm, str, schemas.Unset] = schemas.unset,
                    ssl_redirect: typing.Union[MetaOapg.properties.ssl_redirect, bool, schemas.Unset] = schemas.unset,
                    sticky_sessions: typing.Union[MetaOapg.properties.sticky_sessions, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
                    proxy_protocol: typing.Union[MetaOapg.properties.proxy_protocol, bool, schemas.Unset] = schemas.unset,
                    private_network: typing.Union[MetaOapg.properties.private_network, str, schemas.Unset] = schemas.unset,
                    vpc: typing.Union[MetaOapg.properties.vpc, str, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'generic_info':
                    return super().__new__(
                        cls,
                        *_args,
                        balancing_algorithm=balancing_algorithm,
                        ssl_redirect=ssl_redirect,
                        sticky_sessions=sticky_sessions,
                        proxy_protocol=proxy_protocol,
                        private_network=private_network,
                        vpc=vpc,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class health_check(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    class properties:
                        protocol = schemas.StrSchema
                        port = schemas.IntSchema
                        path = schemas.StrSchema
                        check_interval = schemas.IntSchema
                        response_timeout = schemas.IntSchema
                        unhealthy_threshold = schemas.IntSchema
                        healthy_threshold = schemas.IntSchema
                        __annotations__ = {
                            "protocol": protocol,
                            "port": port,
                            "path": path,
                            "check_interval": check_interval,
                            "response_timeout": response_timeout,
                            "unhealthy_threshold": unhealthy_threshold,
                            "healthy_threshold": healthy_threshold,
                        }
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["protocol"]) -> MetaOapg.properties.protocol: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["port"]) -> MetaOapg.properties.port: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["path"]) -> MetaOapg.properties.path: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["check_interval"]) -> MetaOapg.properties.check_interval: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["response_timeout"]) -> MetaOapg.properties.response_timeout: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["unhealthy_threshold"]) -> MetaOapg.properties.unhealthy_threshold: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["healthy_threshold"]) -> MetaOapg.properties.healthy_threshold: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["protocol", "port", "path", "check_interval", "response_timeout", "unhealthy_threshold", "healthy_threshold", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["protocol"]) -> typing.Union[MetaOapg.properties.protocol, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["port"]) -> typing.Union[MetaOapg.properties.port, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["path"]) -> typing.Union[MetaOapg.properties.path, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["check_interval"]) -> typing.Union[MetaOapg.properties.check_interval, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["response_timeout"]) -> typing.Union[MetaOapg.properties.response_timeout, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["unhealthy_threshold"]) -> typing.Union[MetaOapg.properties.unhealthy_threshold, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["healthy_threshold"]) -> typing.Union[MetaOapg.properties.healthy_threshold, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["protocol", "port", "path", "check_interval", "response_timeout", "unhealthy_threshold", "healthy_threshold", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    protocol: typing.Union[MetaOapg.properties.protocol, str, schemas.Unset] = schemas.unset,
                    port: typing.Union[MetaOapg.properties.port, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                    path: typing.Union[MetaOapg.properties.path, str, schemas.Unset] = schemas.unset,
                    check_interval: typing.Union[MetaOapg.properties.check_interval, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                    response_timeout: typing.Union[MetaOapg.properties.response_timeout, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                    unhealthy_threshold: typing.Union[MetaOapg.properties.unhealthy_threshold, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                    healthy_threshold: typing.Union[MetaOapg.properties.healthy_threshold, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'health_check':
                    return super().__new__(
                        cls,
                        *_args,
                        protocol=protocol,
                        port=port,
                        path=path,
                        check_interval=check_interval,
                        response_timeout=response_timeout,
                        unhealthy_threshold=unhealthy_threshold,
                        healthy_threshold=healthy_threshold,
                        _configuration=_configuration,
                        **kwargs,
                    )
            has_ssl = schemas.BoolSchema
            http2 = schemas.BoolSchema
            
            
            class forward_rules(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class items(
                        schemas.DictSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            class properties:
                                id = schemas.StrSchema
                                frontend_protocol = schemas.StrSchema
                                frontend_port = schemas.IntSchema
                                backend_portocol = schemas.StrSchema
                                backend_port = schemas.IntSchema
                                __annotations__ = {
                                    "id": id,
                                    "frontend_protocol": frontend_protocol,
                                    "frontend_port": frontend_port,
                                    "backend_portocol": backend_portocol,
                                    "backend_port": backend_port,
                                }
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["frontend_protocol"]) -> MetaOapg.properties.frontend_protocol: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["frontend_port"]) -> MetaOapg.properties.frontend_port: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["backend_portocol"]) -> MetaOapg.properties.backend_portocol: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["backend_port"]) -> MetaOapg.properties.backend_port: ...
                        
                        @typing.overload
                        def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                        
                        def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "frontend_protocol", "frontend_port", "backend_portocol", "backend_port", ], str]):
                            # dict_instance[name] accessor
                            return super().__getitem__(name)
                        
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["frontend_protocol"]) -> typing.Union[MetaOapg.properties.frontend_protocol, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["frontend_port"]) -> typing.Union[MetaOapg.properties.frontend_port, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["backend_portocol"]) -> typing.Union[MetaOapg.properties.backend_portocol, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["backend_port"]) -> typing.Union[MetaOapg.properties.backend_port, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                        
                        def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "frontend_protocol", "frontend_port", "backend_portocol", "backend_port", ], str]):
                            return super().get_item_oapg(name)
                        
                    
                        def __new__(
                            cls,
                            *_args: typing.Union[dict, frozendict.frozendict, ],
                            id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
                            frontend_protocol: typing.Union[MetaOapg.properties.frontend_protocol, str, schemas.Unset] = schemas.unset,
                            frontend_port: typing.Union[MetaOapg.properties.frontend_port, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                            backend_portocol: typing.Union[MetaOapg.properties.backend_portocol, str, schemas.Unset] = schemas.unset,
                            backend_port: typing.Union[MetaOapg.properties.backend_port, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'items':
                            return super().__new__(
                                cls,
                                *_args,
                                id=id,
                                frontend_protocol=frontend_protocol,
                                frontend_port=frontend_port,
                                backend_portocol=backend_portocol,
                                backend_port=backend_port,
                                _configuration=_configuration,
                                **kwargs,
                            )
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'forward_rules':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class instances(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'instances':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class firewall_rules(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class items(
                        schemas.DictSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            class properties:
                                id = schemas.StrSchema
                                port = schemas.IntSchema
                                source = schemas.StrSchema
                                ip_type = schemas.StrSchema
                                __annotations__ = {
                                    "id": id,
                                    "port": port,
                                    "source": source,
                                    "ip_type": ip_type,
                                }
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["port"]) -> MetaOapg.properties.port: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["source"]) -> MetaOapg.properties.source: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["ip_type"]) -> MetaOapg.properties.ip_type: ...
                        
                        @typing.overload
                        def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                        
                        def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "port", "source", "ip_type", ], str]):
                            # dict_instance[name] accessor
                            return super().__getitem__(name)
                        
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["port"]) -> typing.Union[MetaOapg.properties.port, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["source"]) -> typing.Union[MetaOapg.properties.source, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["ip_type"]) -> typing.Union[MetaOapg.properties.ip_type, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                        
                        def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "port", "source", "ip_type", ], str]):
                            return super().get_item_oapg(name)
                        
                    
                        def __new__(
                            cls,
                            *_args: typing.Union[dict, frozendict.frozendict, ],
                            id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
                            port: typing.Union[MetaOapg.properties.port, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                            source: typing.Union[MetaOapg.properties.source, str, schemas.Unset] = schemas.unset,
                            ip_type: typing.Union[MetaOapg.properties.ip_type, str, schemas.Unset] = schemas.unset,
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'items':
                            return super().__new__(
                                cls,
                                *_args,
                                id=id,
                                port=port,
                                source=source,
                                ip_type=ip_type,
                                _configuration=_configuration,
                                **kwargs,
                            )
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'firewall_rules':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            __annotations__ = {
                "id": id,
                "date_created": date_created,
                "region": region,
                "label": label,
                "status": status,
                "ipv4": ipv4,
                "ipv6": ipv6,
                "generic_info": generic_info,
                "health_check": health_check,
                "has_ssl": has_ssl,
                "http2": http2,
                "forward_rules": forward_rules,
                "instances": instances,
                "firewall_rules": firewall_rules,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["date_created"]) -> MetaOapg.properties.date_created: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["region"]) -> MetaOapg.properties.region: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["label"]) -> MetaOapg.properties.label: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ipv4"]) -> MetaOapg.properties.ipv4: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ipv6"]) -> MetaOapg.properties.ipv6: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["generic_info"]) -> MetaOapg.properties.generic_info: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["health_check"]) -> MetaOapg.properties.health_check: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["has_ssl"]) -> MetaOapg.properties.has_ssl: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["http2"]) -> MetaOapg.properties.http2: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["forward_rules"]) -> MetaOapg.properties.forward_rules: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["instances"]) -> MetaOapg.properties.instances: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["firewall_rules"]) -> MetaOapg.properties.firewall_rules: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "date_created", "region", "label", "status", "ipv4", "ipv6", "generic_info", "health_check", "has_ssl", "http2", "forward_rules", "instances", "firewall_rules", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["date_created"]) -> typing.Union[MetaOapg.properties.date_created, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["region"]) -> typing.Union[MetaOapg.properties.region, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["label"]) -> typing.Union[MetaOapg.properties.label, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ipv4"]) -> typing.Union[MetaOapg.properties.ipv4, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ipv6"]) -> typing.Union[MetaOapg.properties.ipv6, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["generic_info"]) -> typing.Union[MetaOapg.properties.generic_info, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["health_check"]) -> typing.Union[MetaOapg.properties.health_check, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["has_ssl"]) -> typing.Union[MetaOapg.properties.has_ssl, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["http2"]) -> typing.Union[MetaOapg.properties.http2, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["forward_rules"]) -> typing.Union[MetaOapg.properties.forward_rules, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["instances"]) -> typing.Union[MetaOapg.properties.instances, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["firewall_rules"]) -> typing.Union[MetaOapg.properties.firewall_rules, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "date_created", "region", "label", "status", "ipv4", "ipv6", "generic_info", "health_check", "has_ssl", "http2", "forward_rules", "instances", "firewall_rules", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        date_created: typing.Union[MetaOapg.properties.date_created, str, schemas.Unset] = schemas.unset,
        region: typing.Union[MetaOapg.properties.region, str, schemas.Unset] = schemas.unset,
        label: typing.Union[MetaOapg.properties.label, str, schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        ipv4: typing.Union[MetaOapg.properties.ipv4, str, schemas.Unset] = schemas.unset,
        ipv6: typing.Union[MetaOapg.properties.ipv6, str, schemas.Unset] = schemas.unset,
        generic_info: typing.Union[MetaOapg.properties.generic_info, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        health_check: typing.Union[MetaOapg.properties.health_check, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        has_ssl: typing.Union[MetaOapg.properties.has_ssl, bool, schemas.Unset] = schemas.unset,
        http2: typing.Union[MetaOapg.properties.http2, bool, schemas.Unset] = schemas.unset,
        forward_rules: typing.Union[MetaOapg.properties.forward_rules, list, tuple, schemas.Unset] = schemas.unset,
        instances: typing.Union[MetaOapg.properties.instances, list, tuple, schemas.Unset] = schemas.unset,
        firewall_rules: typing.Union[MetaOapg.properties.firewall_rules, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Loadbalancer':
        return super().__new__(
            cls,
            *_args,
            id=id,
            date_created=date_created,
            region=region,
            label=label,
            status=status,
            ipv4=ipv4,
            ipv6=ipv6,
            generic_info=generic_info,
            health_check=health_check,
            has_ssl=has_ssl,
            http2=http2,
            forward_rules=forward_rules,
            instances=instances,
            firewall_rules=firewall_rules,
            _configuration=_configuration,
            **kwargs,
        )
