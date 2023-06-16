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


class Baremetal(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Bare Metal information.
    """


    class MetaOapg:
        
        class properties:
            id = schemas.StrSchema
            os = schemas.StrSchema
            ram = schemas.StrSchema
            disk = schemas.StrSchema
            main_ip = schemas.StrSchema
            cpu_count = schemas.IntSchema
            region = schemas.StrSchema
            default_password = schemas.StrSchema
            date_created = schemas.StrSchema
            status = schemas.StrSchema
            netmask_v4 = schemas.StrSchema
            gateway_v4 = schemas.StrSchema
            plan = schemas.StrSchema
            label = schemas.StrSchema
            tag = schemas.StrSchema
            os_id = schemas.IntSchema
            app_id = schemas.IntSchema
            image_id = schemas.StrSchema
            v6_network = schemas.StrSchema
            v6_main_ip = schemas.StrSchema
            v6_network_size = schemas.IntSchema
            mac_address = schemas.IntSchema
            
            
            class tags(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'tags':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            __annotations__ = {
                "id": id,
                "os": os,
                "ram": ram,
                "disk": disk,
                "main_ip": main_ip,
                "cpu_count": cpu_count,
                "region": region,
                "default_password": default_password,
                "date_created": date_created,
                "status": status,
                "netmask_v4": netmask_v4,
                "gateway_v4": gateway_v4,
                "plan": plan,
                "label": label,
                "tag": tag,
                "os_id": os_id,
                "app_id": app_id,
                "image_id": image_id,
                "v6_network": v6_network,
                "v6_main_ip": v6_main_ip,
                "v6_network_size": v6_network_size,
                "mac_address": mac_address,
                "tags": tags,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["os"]) -> MetaOapg.properties.os: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ram"]) -> MetaOapg.properties.ram: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["disk"]) -> MetaOapg.properties.disk: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["main_ip"]) -> MetaOapg.properties.main_ip: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cpu_count"]) -> MetaOapg.properties.cpu_count: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["region"]) -> MetaOapg.properties.region: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["default_password"]) -> MetaOapg.properties.default_password: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["date_created"]) -> MetaOapg.properties.date_created: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["netmask_v4"]) -> MetaOapg.properties.netmask_v4: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["gateway_v4"]) -> MetaOapg.properties.gateway_v4: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["plan"]) -> MetaOapg.properties.plan: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["label"]) -> MetaOapg.properties.label: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tag"]) -> MetaOapg.properties.tag: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["os_id"]) -> MetaOapg.properties.os_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["app_id"]) -> MetaOapg.properties.app_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["image_id"]) -> MetaOapg.properties.image_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["v6_network"]) -> MetaOapg.properties.v6_network: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["v6_main_ip"]) -> MetaOapg.properties.v6_main_ip: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["v6_network_size"]) -> MetaOapg.properties.v6_network_size: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mac_address"]) -> MetaOapg.properties.mac_address: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tags"]) -> MetaOapg.properties.tags: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "os", "ram", "disk", "main_ip", "cpu_count", "region", "default_password", "date_created", "status", "netmask_v4", "gateway_v4", "plan", "label", "tag", "os_id", "app_id", "image_id", "v6_network", "v6_main_ip", "v6_network_size", "mac_address", "tags", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["os"]) -> typing.Union[MetaOapg.properties.os, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ram"]) -> typing.Union[MetaOapg.properties.ram, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["disk"]) -> typing.Union[MetaOapg.properties.disk, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["main_ip"]) -> typing.Union[MetaOapg.properties.main_ip, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cpu_count"]) -> typing.Union[MetaOapg.properties.cpu_count, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["region"]) -> typing.Union[MetaOapg.properties.region, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["default_password"]) -> typing.Union[MetaOapg.properties.default_password, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["date_created"]) -> typing.Union[MetaOapg.properties.date_created, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["netmask_v4"]) -> typing.Union[MetaOapg.properties.netmask_v4, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["gateway_v4"]) -> typing.Union[MetaOapg.properties.gateway_v4, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["plan"]) -> typing.Union[MetaOapg.properties.plan, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["label"]) -> typing.Union[MetaOapg.properties.label, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tag"]) -> typing.Union[MetaOapg.properties.tag, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["os_id"]) -> typing.Union[MetaOapg.properties.os_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["app_id"]) -> typing.Union[MetaOapg.properties.app_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["image_id"]) -> typing.Union[MetaOapg.properties.image_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["v6_network"]) -> typing.Union[MetaOapg.properties.v6_network, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["v6_main_ip"]) -> typing.Union[MetaOapg.properties.v6_main_ip, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["v6_network_size"]) -> typing.Union[MetaOapg.properties.v6_network_size, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mac_address"]) -> typing.Union[MetaOapg.properties.mac_address, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tags"]) -> typing.Union[MetaOapg.properties.tags, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "os", "ram", "disk", "main_ip", "cpu_count", "region", "default_password", "date_created", "status", "netmask_v4", "gateway_v4", "plan", "label", "tag", "os_id", "app_id", "image_id", "v6_network", "v6_main_ip", "v6_network_size", "mac_address", "tags", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        os: typing.Union[MetaOapg.properties.os, str, schemas.Unset] = schemas.unset,
        ram: typing.Union[MetaOapg.properties.ram, str, schemas.Unset] = schemas.unset,
        disk: typing.Union[MetaOapg.properties.disk, str, schemas.Unset] = schemas.unset,
        main_ip: typing.Union[MetaOapg.properties.main_ip, str, schemas.Unset] = schemas.unset,
        cpu_count: typing.Union[MetaOapg.properties.cpu_count, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        region: typing.Union[MetaOapg.properties.region, str, schemas.Unset] = schemas.unset,
        default_password: typing.Union[MetaOapg.properties.default_password, str, schemas.Unset] = schemas.unset,
        date_created: typing.Union[MetaOapg.properties.date_created, str, schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        netmask_v4: typing.Union[MetaOapg.properties.netmask_v4, str, schemas.Unset] = schemas.unset,
        gateway_v4: typing.Union[MetaOapg.properties.gateway_v4, str, schemas.Unset] = schemas.unset,
        plan: typing.Union[MetaOapg.properties.plan, str, schemas.Unset] = schemas.unset,
        label: typing.Union[MetaOapg.properties.label, str, schemas.Unset] = schemas.unset,
        tag: typing.Union[MetaOapg.properties.tag, str, schemas.Unset] = schemas.unset,
        os_id: typing.Union[MetaOapg.properties.os_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        app_id: typing.Union[MetaOapg.properties.app_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        image_id: typing.Union[MetaOapg.properties.image_id, str, schemas.Unset] = schemas.unset,
        v6_network: typing.Union[MetaOapg.properties.v6_network, str, schemas.Unset] = schemas.unset,
        v6_main_ip: typing.Union[MetaOapg.properties.v6_main_ip, str, schemas.Unset] = schemas.unset,
        v6_network_size: typing.Union[MetaOapg.properties.v6_network_size, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        mac_address: typing.Union[MetaOapg.properties.mac_address, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        tags: typing.Union[MetaOapg.properties.tags, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Baremetal':
        return super().__new__(
            cls,
            *_args,
            id=id,
            os=os,
            ram=ram,
            disk=disk,
            main_ip=main_ip,
            cpu_count=cpu_count,
            region=region,
            default_password=default_password,
            date_created=date_created,
            status=status,
            netmask_v4=netmask_v4,
            gateway_v4=gateway_v4,
            plan=plan,
            label=label,
            tag=tag,
            os_id=os_id,
            app_id=app_id,
            image_id=image_id,
            v6_network=v6_network,
            v6_main_ip=v6_main_ip,
            v6_network_size=v6_network_size,
            mac_address=mac_address,
            tags=tags,
            _configuration=_configuration,
            **kwargs,
        )
