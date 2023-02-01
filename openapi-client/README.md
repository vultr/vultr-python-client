# openapi-client
# Introduction

The Vultr API v2 is a set of HTTP endpoints that adhere to RESTful design principles and CRUD actions with predictable URIs. It uses standard HTTP response codes, authentication, and verbs. The API has consistent and well-formed JSON requests and responses with cursor-based pagination to simplify list handling. Error messages are descriptive and easy to understand. All functions of the Vultr customer portal are accessible via the API, enabling you to script complex unattended scenarios with any tool fluent in HTTP.

## Requests

Communicate with the API by making an HTTP request at the correct endpoint. The chosen method determines the action taken.

| Method | Usage |
| ------ | ------------- |
| DELETE | Use the DELETE method to destroy a resource in your account. If it is not found, the operation will return a 4xx error and an appropriate message. |
| GET | To retrieve information about a resource, use the GET method. The data is returned as a JSON object. GET methods are read-only and do not affect any resources. |
| PATCH | Some resources support partial modification with PATCH, which modifies specific attributes without updating the entire object representation. |
| POST | Issue a POST method to create a new object. Include all needed attributes in the request body encoded as JSON. |
| PUT | Use the PUT method to update information about a resource. PUT will set new values on the item without regard to their current values. |

**Rate Limit:** Vultr safeguards the API against bursts of incoming traffic based on the request's IP address to ensure stability for all users. If your application sends more than 30 requests per second, the API may return HTTP status code 429.

## Response Codes

We use standard HTTP response codes to show the success or failure of requests. Response codes in the 2xx range indicate success, while codes in the 4xx range indicate an error, such as an authorization failure or a malformed request. All 4xx errors will return a JSON response object with an `error` attribute explaining the error. Codes in the 5xx range indicate a server-side problem preventing Vultr from fulfilling your request.

| Response | Description |
| ------ | ------------- |
| 200 OK | The response contains your requested information. |
| 201 Created | Your request was accepted. The resource was created. |
| 202 Accepted | Your request was accepted. The resource was created or updated. |
| 204 No Content | Your request succeeded, there is no additional information returned. |
| 400 Bad Request | Your request was malformed. |
| 401 Unauthorized | You did not supply valid authentication credentials. |
| 403 Forbidden | You are not allowed to perform that action. |
| 404 Not Found | No results were found for your request. |
| 429 Too Many Requests | Your request exceeded the API rate limit. |
| 500 Internal Server Error | We were unable to perform the request due to server-side problems. |

## Meta and Pagination

Many API calls will return a `meta` object with paging information.

### Definitions

| Term | Description |
| ------ | ------------- |
| **List** | The items returned from the database for your request (not necessarily shown in a single response depending on the **cursor** size). |
| **Page** | A subset of the full **list** of items. Choose the size of a **page** with the `per_page` parameter. |
| **Total** | The `total` attribute indicates the number of items in the full **list**.|
| **Cursor** | Use the `cursor` query parameter to select a next or previous **page**. |
| **Next** & **Prev** | Use the `next` and `prev` attributes of the `links` meta object as `cursor` values. |

### How to use Paging

If your result **list** total exceeds the default **cursor** size (the default depends on the route, but is usually 100 records) or the value defined by the `per_page` query param (when present) the response will be returned to you paginated.

### Paging Example

> These examples have abbreviated attributes and sample values. Your actual `cursor` values will be encoded alphanumeric strings.

To return a **page** with the first two plans in the List:

    curl \"https://api.vultr.com/v2/plans?per_page=2\" \\
      -X GET \\
      -H \"Authorization: Bearer ${VULTR_API_KEY}\"

The API returns an object similar to this:

    {
        \"plans\": [
            {
                \"id\": \"vc2-1c-2gb\",
                \"vcpu_count\": 1,
                \"ram\": 2048,
                \"locations\": []
            },
            {
                \"id\": \"vc2-24c-97gb\",
                \"vcpu_count\": 24,
                \"ram\": 98304,
                \"locations\": []
            }
        ],
        \"meta\": {
            \"total\": 19,
            \"links\": {
                \"next\": \"WxYzExampleNext\",
                \"prev\": \"WxYzExamplePrev\"
            }
        }
    }

The object contains two plans. The `total` attribute indicates that 19 plans are available in the List. To navigate forward in the **list**, use the `next` value (`WxYzExampleNext` in this example) as your `cursor` query parameter.

    curl \"https://api.vultr.com/v2/plans?per_page=2&cursor=WxYzExampleNext\" \\
      -X GET
      -H \"Authorization: Bearer ${VULTR_API_KEY}\"

Likewise, you can use the example `prev` value `WxYzExamplePrev` to navigate backward.

## Parameters

You can pass information to the API with three different types of parameters.

### Path parameters

Some API calls require variable parameters as part of the endpoint path. For example, to retrieve information about a user, supply the `user-id` in the endpoint.

    curl \"https://api.vultr.com/v2/users/{user-id}\" \\
      -X GET \\
      -H \"Authorization: Bearer ${VULTR_API_KEY}\"

### Query parameters

Some API calls allow filtering with query parameters. For example, the `/v2/plans` endpoint supports a `type` query parameter. Setting `type=vhf` instructs the API only to return High Frequency Compute plans in the list. You'll find more specifics about valid filters in the endpoint documentation below.

    curl \"https://api.vultr.com/v2/plans?type=vhf\" \\
      -X GET \\
      -H \"Authorization: Bearer ${VULTR_API_KEY}\"

You can also combine filtering with paging. Use the `per_page` parameter to retreive a subset of vhf plans.

    curl \"https://api.vultr.com/v2/plans?type=vhf&per_page=2\" \\
      -X GET \\
      -H \"Authorization: Bearer ${VULTR_API_KEY}\"

### Request Body

PUT, POST, and PATCH methods may include an object in the request body with a content type of **application/json**. The documentation for each endpoint below has more information about the expected object.

## API Example Conventions

The examples in this documentation use `curl`, a command-line HTTP client, to demonstrate useage. Linux and macOS computers usually have curl installed by default, and it's [available for download](https://curl.se/download.html) on all popular platforms including Windows.

Each example is split across multiple lines with the `\\` character, which is compatible with a `bash` terminal. A typical example looks like this:

    curl \"https://api.vultr.com/v2/domains\" \\
      -X POST \\
      -H \"Authorization: Bearer ${VULTR_API_KEY}\" \\
      -H \"Content-Type: application/json\" \\
      --data '{
        \"domain\" : \"example.com\",
        \"ip\" : \"192.0.2.123\"
      }'

* The `-X` parameter sets the request method. For consistency, we show the method on all examples, even though it's not explicitly required for GET methods.
* The `-H` lines set required HTTP headers. These examples are formatted to expand the VULTR\\_API\\_KEY environment variable for your convenience.
* Examples that require a JSON object in the request body pass the required data via the `--data` parameter.

All values in this guide are examples. Do not rely on the OS or Plan IDs listed in this guide; use the appropriate endpoint to retreive values before creating resources.

# Authentication

<!-- ReDoc-Inject: <security-definitions> -->

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 2.0
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://www.vultr.com](https://www.vultr.com)

## Requirements.

Python &gt;&#x3D;3.7

## Migration from other generators like python and python-legacy

### Changes
1. This generator uses spec case for all (object) property names and parameter names.
    - So if the spec has a property name like camelCase, it will use camelCase rather than camel_case
    - So you will need to update how you input and read properties to use spec case
2. Endpoint parameters are stored in dictionaries to prevent collisions (explanation below)
    - So you will need to update how you pass data in to endpoints
3. Endpoint responses now include the original response, the deserialized response body, and (todo)the deserialized headers
    - So you will need to update your code to use response.body to access deserialized data
4. All validated data is instantiated in an instance that subclasses all validated Schema classes and Decimal/str/list/tuple/frozendict/NoneClass/BoolClass/bytes/io.FileIO
    - This means that you can use isinstance to check if a payload validated against a schema class
    - This means that no data will be of type None/True/False
        - ingested None will subclass NoneClass
        - ingested True will subclass BoolClass
        - ingested False will subclass BoolClass
        - So if you need to check is True/False/None, instead use instance.is_true_oapg()/.is_false_oapg()/.is_none_oapg()
5. All validated class instances are immutable except for ones based on io.File
    - This is because if properties were changed after validation, that validation would no longer apply
    - So no changing values or property values after a class has been instantiated
6. String + Number types with formats
    - String type data is stored as a string and if you need to access types based on its format like date,
    date-time, uuid, number etc then you will need to use accessor functions on the instance
    - type string + format: See .as_date_oapg, .as_datetime_oapg, .as_decimal_oapg, .as_uuid_oapg
    - type number + format: See .as_float_oapg, .as_int_oapg
    - this was done because openapi/json-schema defines constraints. string data may be type string with no format
    keyword in one schema, and include a format constraint in another schema
    - So if you need to access a string format based type, use as_date_oapg/as_datetime_oapg/as_decimal_oapg/as_uuid_oapg
    - So if you need to access a number format based type, use as_int_oapg/as_float_oapg
7. Property access on AnyType(type unset) or object(dict) schemas
    - Only required keys with valid python names are properties like .someProp and have type hints
    - All optional keys may not exist, so properties are not defined for them
    - One can access optional values with dict_instance['optionalProp'] and KeyError will be raised if it does not exist
    - Use get_item_oapg if you need a way to always get a value whether or not the key exists
        - If the key does not exist, schemas.unset is returned from calling dict_instance.get_item_oapg('optionalProp')
        - All required and optional keys have type hints for this method, and @typing.overload is used
        - A type hint is also generated for additionalProperties accessed using this method
    - So you will need to update you code to use some_instance['optionalProp'] to access optional property
    and additionalProperty values
8. The location of the api classes has changed
    - Api classes are located in your_package.apis.tags.some_api
    - This change was made to eliminate redundant code generation
    - Legacy generators generated the same endpoint twice if it had > 1 tag on it
    - This generator defines an endpoint in one class, then inherits that class to generate
      apis by tags and by paths
    - This change reduces code and allows quicker run time if you use the path apis
        - path apis are at your_package.apis.paths.some_path
    - Those apis will only load their needed models, which is less to load than all of the resources needed in a tag api
    - So you will need to update your import paths to the api classes

### Why are Oapg and _oapg used in class and method names?
Classes can have arbitrarily named properties set on them
Endpoints can have arbitrary operationId method names set
For those reasons, I use the prefix Oapg and _oapg to greatly reduce the likelihood of collisions
on protected + public classes/methods.
oapg stands for OpenApi Python Generator.

### Object property spec case
This was done because when payloads are ingested, they can be validated against N number of schemas.
If the input signature used a different property name then that has mutated the payload.
So SchemaA and SchemaB must both see the camelCase spec named variable.
Also it is possible to send in two properties, named camelCase and camel_case in the same payload.
That use case should be support so spec case is used.

### Parameter spec case
Parameters can be included in different locations including:
- query
- path
- header
- cookie

Any of those parameters could use the same parameter names, so if every parameter
was included as an endpoint parameter in a function signature, they would collide.
For that reason, each of those inputs have been separated out into separate typed dictionaries:
- query_params
- path_params
- header_params
- cookie_params

So when updating your code, you will need to pass endpoint parameters in using those
dictionaries.

### Endpoint responses
Endpoint responses have been enriched to now include more information.
Any response reom an endpoint will now include the following properties:
response: urllib3.HTTPResponse
body: typing.Union[Unset, Schema]
headers: typing.Union[Unset, TODO]
Note: response header deserialization has not yet been added


## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import openapi_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import openapi_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import openapi_client
from pprint import pprint
from openapi_client.apis.tags import vpcs_api
from openapi_client.model.meta import Meta
from openapi_client.model.vpc import Vpc
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
    api_instance = vpcs_api.VPCsApi(api_client)
    any_type = dict(
        region="region_example",
        description="description_example",
        v4_subnet="v4_subnet_example",
        v4_subnet_mask=1,
    ) # anyType | Include a JSON object in the request body with a content type of **application/json**. (optional)

    try:
        # Create a VPC
        api_response = api_instance.create_vpc(any_type=any_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling VPCsApi->create_vpc: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://api.vultr.com/v2*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*VPCsApi* | [**create_vpc**](../docs/apis/tags/VPCsApi.md#create_vpc) | **post** /vpcs | Create a VPC
*VPCsApi* | [**delete_vpc**](../docs/apis/tags/VPCsApi.md#delete_vpc) | **delete** /vpcs/{vpc-id} | Delete a VPC
*VPCsApi* | [**get_vpc**](../docs/apis/tags/VPCsApi.md#get_vpc) | **get** /vpcs/{vpc-id} | Get a VPC
*VPCsApi* | [**list_vpcs**](../docs/apis/tags/VPCsApi.md#list_vpcs) | **get** /vpcs | List VPCs
*VPCsApi* | [**update_vpc**](../docs/apis/tags/VPCsApi.md#update_vpc) | **put** /vpcs/{vpc-id} | Update a VPC
*AccountApi* | [**get_account**](../docs/apis/tags/AccountApi.md#get_account) | **get** /account | Get Account Info
*ApplicationApi* | [**list_applications**](../docs/apis/tags/ApplicationApi.md#list_applications) | **get** /applications | List Applications
*BackupApi* | [**get_backup**](../docs/apis/tags/BackupApi.md#get_backup) | **get** /backups/{backup-id} | Get a Backup
*BackupApi* | [**list_backups**](../docs/apis/tags/BackupApi.md#list_backups) | **get** /backups | List Backups
*BaremetalApi* | [**create_baremetal**](../docs/apis/tags/BaremetalApi.md#create_baremetal) | **post** /bare-metals | Create Bare Metal Instance
*BaremetalApi* | [**delete_baremetal**](../docs/apis/tags/BaremetalApi.md#delete_baremetal) | **delete** /bare-metals/{baremetal-id} | Delete Bare Metal
*BaremetalApi* | [**get_bandwidth_baremetal**](../docs/apis/tags/BaremetalApi.md#get_bandwidth_baremetal) | **get** /bare-metals/{baremetal-id}/bandwidth | Bare Metal Bandwidth
*BaremetalApi* | [**get_bare_metal_userdata**](../docs/apis/tags/BaremetalApi.md#get_bare_metal_userdata) | **get** /bare-metals/{baremetal-id}/user-data | Get Bare Metal User Data
*BaremetalApi* | [**get_bare_metal_vnc**](../docs/apis/tags/BaremetalApi.md#get_bare_metal_vnc) | **get** /bare-metals/{baremetal-id}/vnc | Get VNC URL for a Bare Metal
*BaremetalApi* | [**get_bare_metals_upgrades**](../docs/apis/tags/BaremetalApi.md#get_bare_metals_upgrades) | **get** /bare-metals/{baremetal-id}/upgrades | Get Available Bare Metal Upgrades
*BaremetalApi* | [**get_baremetal**](../docs/apis/tags/BaremetalApi.md#get_baremetal) | **get** /bare-metals/{baremetal-id} | Get Bare Metal
*BaremetalApi* | [**get_ipv4_baremetal**](../docs/apis/tags/BaremetalApi.md#get_ipv4_baremetal) | **get** /bare-metals/{baremetal-id}/ipv4 | Bare Metal IPv4 Addresses
*BaremetalApi* | [**get_ipv6_baremetal**](../docs/apis/tags/BaremetalApi.md#get_ipv6_baremetal) | **get** /bare-metals/{baremetal-id}/ipv6 | Bare Metal IPv6 Addresses
*BaremetalApi* | [**halt_baremetal**](../docs/apis/tags/BaremetalApi.md#halt_baremetal) | **post** /bare-metals/{baremetal-id}/halt | Halt Bare Metal
*BaremetalApi* | [**halt_baremetals**](../docs/apis/tags/BaremetalApi.md#halt_baremetals) | **post** /bare-metals/halt | Halt Bare Metals
*BaremetalApi* | [**list_baremetals**](../docs/apis/tags/BaremetalApi.md#list_baremetals) | **get** /bare-metals | List Bare Metal Instances
*BaremetalApi* | [**reboot_bare_metals**](../docs/apis/tags/BaremetalApi.md#reboot_bare_metals) | **post** /bare-metals/reboot | Reboot Bare Metals
*BaremetalApi* | [**reboot_baremetal**](../docs/apis/tags/BaremetalApi.md#reboot_baremetal) | **post** /bare-metals/{baremetal-id}/reboot | Reboot Bare Metal
*BaremetalApi* | [**reinstall_baremetal**](../docs/apis/tags/BaremetalApi.md#reinstall_baremetal) | **post** /bare-metals/{baremetal-id}/reinstall | Reinstall Bare Metal
*BaremetalApi* | [**start_bare_metals**](../docs/apis/tags/BaremetalApi.md#start_bare_metals) | **post** /bare-metals/start | Start Bare Metals
*BaremetalApi* | [**start_baremetal**](../docs/apis/tags/BaremetalApi.md#start_baremetal) | **post** /bare-metals/{baremetal-id}/start | Start Bare Metal
*BaremetalApi* | [**update_baremetal**](../docs/apis/tags/BaremetalApi.md#update_baremetal) | **patch** /bare-metals/{baremetal-id} | Update Bare Metal
*BillingApi* | [**get_invoice**](../docs/apis/tags/BillingApi.md#get_invoice) | **get** /billing/invoices/{invoice-id} | Get Invoice
*BillingApi* | [**get_invoice_items**](../docs/apis/tags/BillingApi.md#get_invoice_items) | **get** /billing/invoices/{invoice-id}/items | Get Invoice Items
*BillingApi* | [**list_billing_history**](../docs/apis/tags/BillingApi.md#list_billing_history) | **get** /billing/history | List Billing History
*BillingApi* | [**list_invoices**](../docs/apis/tags/BillingApi.md#list_invoices) | **get** /billing/invoices | List Invoices
*BlockApi* | [**attach_block**](../docs/apis/tags/BlockApi.md#attach_block) | **post** /blocks/{block-id}/attach | Attach Block Storage
*BlockApi* | [**create_block**](../docs/apis/tags/BlockApi.md#create_block) | **post** /blocks | Create Block Storage
*BlockApi* | [**delete_block**](../docs/apis/tags/BlockApi.md#delete_block) | **delete** /blocks/{block-id} | Delete Block Storage
*BlockApi* | [**detach_block**](../docs/apis/tags/BlockApi.md#detach_block) | **post** /blocks/{block-id}/detach | Detach Block Storage
*BlockApi* | [**get_block**](../docs/apis/tags/BlockApi.md#get_block) | **get** /blocks/{block-id} | Get Block Storage
*BlockApi* | [**list_blocks**](../docs/apis/tags/BlockApi.md#list_blocks) | **get** /blocks | List Block storages
*BlockApi* | [**update_block**](../docs/apis/tags/BlockApi.md#update_block) | **patch** /blocks/{block-id} | Update Block Storage
*DnsApi* | [**create_dns_domain**](../docs/apis/tags/DnsApi.md#create_dns_domain) | **post** /domains | Create DNS Domain
*DnsApi* | [**create_dns_domain_record**](../docs/apis/tags/DnsApi.md#create_dns_domain_record) | **post** /domains/{dns-domain}/records | Create Record
*DnsApi* | [**delete_dns_domain**](../docs/apis/tags/DnsApi.md#delete_dns_domain) | **delete** /domains/{dns-domain} | Delete Domain
*DnsApi* | [**delete_dns_domain_record**](../docs/apis/tags/DnsApi.md#delete_dns_domain_record) | **delete** /domains/{dns-domain}/records/{record-id} | Delete Record
*DnsApi* | [**get_dns_domain**](../docs/apis/tags/DnsApi.md#get_dns_domain) | **get** /domains/{dns-domain} | Get DNS Domain
*DnsApi* | [**get_dns_domain_dnssec**](../docs/apis/tags/DnsApi.md#get_dns_domain_dnssec) | **get** /domains/{dns-domain}/dnssec | Get DNSSec Info
*DnsApi* | [**get_dns_domain_record**](../docs/apis/tags/DnsApi.md#get_dns_domain_record) | **get** /domains/{dns-domain}/records/{record-id} | Get Record
*DnsApi* | [**get_dns_domain_soa**](../docs/apis/tags/DnsApi.md#get_dns_domain_soa) | **get** /domains/{dns-domain}/soa | Get SOA information
*DnsApi* | [**list_dns_domain_records**](../docs/apis/tags/DnsApi.md#list_dns_domain_records) | **get** /domains/{dns-domain}/records | List Records
*DnsApi* | [**list_dns_domains**](../docs/apis/tags/DnsApi.md#list_dns_domains) | **get** /domains | List DNS Domains
*DnsApi* | [**update_dns_domain**](../docs/apis/tags/DnsApi.md#update_dns_domain) | **put** /domains/{dns-domain} | Update a DNS Domain
*DnsApi* | [**update_dns_domain_record**](../docs/apis/tags/DnsApi.md#update_dns_domain_record) | **patch** /domains/{dns-domain}/records/{record-id} | Update Record
*DnsApi* | [**update_dns_domain_soa**](../docs/apis/tags/DnsApi.md#update_dns_domain_soa) | **patch** /domains/{dns-domain}/soa | Update SOA information
*FirewallApi* | [**create_firewall_group**](../docs/apis/tags/FirewallApi.md#create_firewall_group) | **post** /firewalls | Create Firewall Group
*FirewallApi* | [**delete_firewall_group**](../docs/apis/tags/FirewallApi.md#delete_firewall_group) | **delete** /firewalls/{firewall-group-id} | Delete Firewall Group
*FirewallApi* | [**delete_firewall_group_rule**](../docs/apis/tags/FirewallApi.md#delete_firewall_group_rule) | **delete** /firewalls/{firewall-group-id}/rules/{firewall-rule-id} | Delete Firewall Rule
*FirewallApi* | [**get_firewall_group**](../docs/apis/tags/FirewallApi.md#get_firewall_group) | **get** /firewalls/{firewall-group-id} | Get Firewall Group
*FirewallApi* | [**get_firewall_group_rule**](../docs/apis/tags/FirewallApi.md#get_firewall_group_rule) | **get** /firewalls/{firewall-group-id}/rules/{firewall-rule-id} | Get Firewall Rule
*FirewallApi* | [**list_firewall_group_rules**](../docs/apis/tags/FirewallApi.md#list_firewall_group_rules) | **get** /firewalls/{firewall-group-id}/rules | List Firewall Rules
*FirewallApi* | [**list_firewall_groups**](../docs/apis/tags/FirewallApi.md#list_firewall_groups) | **get** /firewalls | List Firewall Groups
*FirewallApi* | [**post_firewalls_firewall_group_id_rules**](../docs/apis/tags/FirewallApi.md#post_firewalls_firewall_group_id_rules) | **post** /firewalls/{firewall-group-id}/rules | Create Firewall Rules
*FirewallApi* | [**update_firewall_group**](../docs/apis/tags/FirewallApi.md#update_firewall_group) | **put** /firewalls/{firewall-group-id} | Update Firewall Group
*InstancesApi* | [**attach_instance_iso**](../docs/apis/tags/InstancesApi.md#attach_instance_iso) | **post** /instances/{instance-id}/iso/attach | Attach ISO to Instance
*InstancesApi* | [**attach_instance_network**](../docs/apis/tags/InstancesApi.md#attach_instance_network) | **post** /instances/{instance-id}/private-networks/attach | Attach Private Network to Instance
*InstancesApi* | [**attach_instance_vpc**](../docs/apis/tags/InstancesApi.md#attach_instance_vpc) | **post** /instances/{instance-id}/vpcs/attach | Attach VPC to Instance
*InstancesApi* | [**create_instance**](../docs/apis/tags/InstancesApi.md#create_instance) | **post** /instances | Create Instance
*InstancesApi* | [**create_instance_backup_schedule**](../docs/apis/tags/InstancesApi.md#create_instance_backup_schedule) | **post** /instances/{instance-id}/backup-schedule | Set Instance Backup Schedule
*InstancesApi* | [**create_instance_ipv4**](../docs/apis/tags/InstancesApi.md#create_instance_ipv4) | **post** /instances/{instance-id}/ipv4 | Create IPv4
*InstancesApi* | [**create_instance_reverse_ipv4**](../docs/apis/tags/InstancesApi.md#create_instance_reverse_ipv4) | **post** /instances/{instance-id}/ipv4/reverse | Create Instance Reverse IPv4
*InstancesApi* | [**create_instance_reverse_ipv6**](../docs/apis/tags/InstancesApi.md#create_instance_reverse_ipv6) | **post** /instances/{instance-id}/ipv6/reverse | Create Instance Reverse IPv6
*InstancesApi* | [**delete_instance**](../docs/apis/tags/InstancesApi.md#delete_instance) | **delete** /instances/{instance-id} | Delete Instance
*InstancesApi* | [**delete_instance_ipv4**](../docs/apis/tags/InstancesApi.md#delete_instance_ipv4) | **delete** /instances/{instance-id}/ipv4/{ipv4} | Delete IPv4 Address
*InstancesApi* | [**delete_instance_reverse_ipv6**](../docs/apis/tags/InstancesApi.md#delete_instance_reverse_ipv6) | **delete** /instances/{instance-id}/ipv6/reverse/{ipv6} | Delete Instance Reverse IPv6
*InstancesApi* | [**detach_instance_iso**](../docs/apis/tags/InstancesApi.md#detach_instance_iso) | **post** /instances/{instance-id}/iso/detach | Detach ISO from instance
*InstancesApi* | [**detach_instance_network**](../docs/apis/tags/InstancesApi.md#detach_instance_network) | **post** /instances/{instance-id}/private-networks/detach | Detach Private Network from Instance.
*InstancesApi* | [**detach_instance_vpc**](../docs/apis/tags/InstancesApi.md#detach_instance_vpc) | **post** /instances/{instance-id}/vpcs/detach | Detach VPC from Instance
*InstancesApi* | [**get_instance**](../docs/apis/tags/InstancesApi.md#get_instance) | **get** /instances/{instance-id} | Get Instance
*InstancesApi* | [**get_instance_backup_schedule**](../docs/apis/tags/InstancesApi.md#get_instance_backup_schedule) | **get** /instances/{instance-id}/backup-schedule | Get Instance Backup Schedule
*InstancesApi* | [**get_instance_bandwidth**](../docs/apis/tags/InstancesApi.md#get_instance_bandwidth) | **get** /instances/{instance-id}/bandwidth | Instance Bandwidth
*InstancesApi* | [**get_instance_ipv4**](../docs/apis/tags/InstancesApi.md#get_instance_ipv4) | **get** /instances/{instance-id}/ipv4 | List Instance IPv4 Information
*InstancesApi* | [**get_instance_ipv6**](../docs/apis/tags/InstancesApi.md#get_instance_ipv6) | **get** /instances/{instance-id}/ipv6 | Get Instance IPv6 Information
*InstancesApi* | [**get_instance_iso_status**](../docs/apis/tags/InstancesApi.md#get_instance_iso_status) | **get** /instances/{instance-id}/iso | Get Instance ISO Status
*InstancesApi* | [**get_instance_neighbors**](../docs/apis/tags/InstancesApi.md#get_instance_neighbors) | **get** /instances/{instance-id}/neighbors | Get Instance neighbors
*InstancesApi* | [**get_instance_upgrades**](../docs/apis/tags/InstancesApi.md#get_instance_upgrades) | **get** /instances/{instance-id}/upgrades | Get Available Instance Upgrades
*InstancesApi* | [**get_instance_userdata**](../docs/apis/tags/InstancesApi.md#get_instance_userdata) | **get** /instances/{instance-id}/user-data | Get Instance User Data
*InstancesApi* | [**halt_instance**](../docs/apis/tags/InstancesApi.md#halt_instance) | **post** /instances/{instance-id}/halt | Halt Instance
*InstancesApi* | [**halt_instances**](../docs/apis/tags/InstancesApi.md#halt_instances) | **post** /instances/halt | Halt Instances
*InstancesApi* | [**list_instance_ipv6_reverse**](../docs/apis/tags/InstancesApi.md#list_instance_ipv6_reverse) | **get** /instances/{instance-id}/ipv6/reverse | List Instance IPv6 Reverse
*InstancesApi* | [**list_instance_private_networks**](../docs/apis/tags/InstancesApi.md#list_instance_private_networks) | **get** /instances/{instance-id}/private-networks | List instance Private Networks
*InstancesApi* | [**list_instance_vpcs**](../docs/apis/tags/InstancesApi.md#list_instance_vpcs) | **get** /instances/{instance-id}/vpcs | List instance VPCs
*InstancesApi* | [**list_instances**](../docs/apis/tags/InstancesApi.md#list_instances) | **get** /instances | List Instances
*InstancesApi* | [**post_instances_instance_id_ipv4_reverse_default**](../docs/apis/tags/InstancesApi.md#post_instances_instance_id_ipv4_reverse_default) | **post** /instances/{instance-id}/ipv4/reverse/default | Set Default Reverse DNS Entry
*InstancesApi* | [**reboot_instance**](../docs/apis/tags/InstancesApi.md#reboot_instance) | **post** /instances/{instance-id}/reboot | Reboot Instance
*InstancesApi* | [**reboot_instances**](../docs/apis/tags/InstancesApi.md#reboot_instances) | **post** /instances/reboot | Reboot instances
*InstancesApi* | [**reinstall_instance**](../docs/apis/tags/InstancesApi.md#reinstall_instance) | **post** /instances/{instance-id}/reinstall | Reinstall Instance
*InstancesApi* | [**restore_instance**](../docs/apis/tags/InstancesApi.md#restore_instance) | **post** /instances/{instance-id}/restore | Restore Instance
*InstancesApi* | [**start_instance**](../docs/apis/tags/InstancesApi.md#start_instance) | **post** /instances/{instance-id}/start | Start instance
*InstancesApi* | [**start_instances**](../docs/apis/tags/InstancesApi.md#start_instances) | **post** /instances/start | Start instances
*InstancesApi* | [**update_instance**](../docs/apis/tags/InstancesApi.md#update_instance) | **patch** /instances/{instance-id} | Update Instance
*IsoApi* | [**create_iso**](../docs/apis/tags/IsoApi.md#create_iso) | **post** /iso | Create ISO
*IsoApi* | [**delete_iso**](../docs/apis/tags/IsoApi.md#delete_iso) | **delete** /iso/{iso-id} | Delete ISO
*IsoApi* | [**iso_get**](../docs/apis/tags/IsoApi.md#iso_get) | **get** /iso/{iso-id} | Get ISO
*IsoApi* | [**list_isos**](../docs/apis/tags/IsoApi.md#list_isos) | **get** /iso | List ISOs
*IsoApi* | [**list_public_isos**](../docs/apis/tags/IsoApi.md#list_public_isos) | **get** /iso-public | List Public ISOs
*KubernetesApi* | [**create_kubernetes_cluster**](../docs/apis/tags/KubernetesApi.md#create_kubernetes_cluster) | **post** /kubernetes/clusters | Create Kubernetes Cluster
*KubernetesApi* | [**create_nodepools**](../docs/apis/tags/KubernetesApi.md#create_nodepools) | **post** /kubernetes/clusters/{vke-id}/node-pools | Create NodePool
*KubernetesApi* | [**delete_kubernetes_cluster**](../docs/apis/tags/KubernetesApi.md#delete_kubernetes_cluster) | **delete** /kubernetes/clusters/{vke-id} | Delete Kubernetes Cluster
*KubernetesApi* | [**delete_kubernetes_cluster_vke_id_delete_with_linked_resources**](../docs/apis/tags/KubernetesApi.md#delete_kubernetes_cluster_vke_id_delete_with_linked_resources) | **delete** /kubernetes/clusters/{vke-id}/delete-with-linked-resources | Delete VKE Cluster and All Related Resources
*KubernetesApi* | [**delete_nodepool**](../docs/apis/tags/KubernetesApi.md#delete_nodepool) | **delete** /kubernetes/clusters/{vke-id}/node-pools/{nodepool-id} | Delete Nodepool
*KubernetesApi* | [**delete_nodepool_instance**](../docs/apis/tags/KubernetesApi.md#delete_nodepool_instance) | **delete** /kubernetes/clusters/{vke-id}/node-pools/{nodepool-id}/nodes/{node-id} | Delete NodePool Instance
*KubernetesApi* | [**get_kubernetes_available_upgrades**](../docs/apis/tags/KubernetesApi.md#get_kubernetes_available_upgrades) | **get** /kubernetes/clusters/{vke-id}/available-upgrades | Get Kubernetes Available Upgrades
*KubernetesApi* | [**get_kubernetes_clusters**](../docs/apis/tags/KubernetesApi.md#get_kubernetes_clusters) | **get** /kubernetes/clusters/{vke-id} | Get Kubernetes Cluster
*KubernetesApi* | [**get_kubernetes_clusters_config**](../docs/apis/tags/KubernetesApi.md#get_kubernetes_clusters_config) | **get** /kubernetes/clusters/{vke-id}/config | Get Kubernetes Cluster Kubeconfig
*KubernetesApi* | [**get_kubernetes_resources**](../docs/apis/tags/KubernetesApi.md#get_kubernetes_resources) | **get** /kubernetes/clusters/{vke-id}/resources | Get Kubernetes Resources
*KubernetesApi* | [**get_kubernetes_versions**](../docs/apis/tags/KubernetesApi.md#get_kubernetes_versions) | **get** /kubernetes/versions | Get Kubernetes Versions
*KubernetesApi* | [**get_nodepool**](../docs/apis/tags/KubernetesApi.md#get_nodepool) | **get** /kubernetes/clusters/{vke-id}/node-pools/{nodepool-id} | Get NodePool
*KubernetesApi* | [**get_nodepools**](../docs/apis/tags/KubernetesApi.md#get_nodepools) | **get** /kubernetes/clusters/{vke-id}/node-pools | List NodePools
*KubernetesApi* | [**list_kubernetes_clusters**](../docs/apis/tags/KubernetesApi.md#list_kubernetes_clusters) | **get** /kubernetes/clusters | List all Kubernetes Clusters
*KubernetesApi* | [**recycle_nodepool_instance**](../docs/apis/tags/KubernetesApi.md#recycle_nodepool_instance) | **post** /kubernetes/clusters/{vke-id}/node-pools/{nodepool-id}/nodes/{node-id}/recycle | Recycle a NodePool Instance
*KubernetesApi* | [**start_kubernetes_cluster_upgrade**](../docs/apis/tags/KubernetesApi.md#start_kubernetes_cluster_upgrade) | **post** /kubernetes/clusters/{vke-id}/upgrades | Start Kubernetes Cluster Upgrade
*KubernetesApi* | [**update_kubernetes_cluster**](../docs/apis/tags/KubernetesApi.md#update_kubernetes_cluster) | **put** /kubernetes/clusters/{vke-id} | Update Kubernetes Cluster
*KubernetesApi* | [**update_nodepool**](../docs/apis/tags/KubernetesApi.md#update_nodepool) | **patch** /kubernetes/clusters/{vke-id}/node-pools/{nodepool-id} | Update Nodepool
*LoadBalancerApi* | [**create_load_balancer**](../docs/apis/tags/LoadBalancerApi.md#create_load_balancer) | **post** /load-balancers | Create Load Balancer
*LoadBalancerApi* | [**create_load_balancer_forwarding_rules**](../docs/apis/tags/LoadBalancerApi.md#create_load_balancer_forwarding_rules) | **post** /load-balancers/{load-balancer-id}/forwarding-rules | Create Forwarding Rule
*LoadBalancerApi* | [**delete_load_balancer**](../docs/apis/tags/LoadBalancerApi.md#delete_load_balancer) | **delete** /load-balancers/{load-balancer-id} | Delete Load Balancer
*LoadBalancerApi* | [**delete_load_balancer_forwarding_rule**](../docs/apis/tags/LoadBalancerApi.md#delete_load_balancer_forwarding_rule) | **delete** /load-balancers/{load-balancer-id}/forwarding-rules/{forwarding-rule-id} | Delete Forwarding Rule
*LoadBalancerApi* | [**get_load_balancer**](../docs/apis/tags/LoadBalancerApi.md#get_load_balancer) | **get** /load-balancers/{load-balancer-id} | Get Load Balancer
*LoadBalancerApi* | [**get_load_balancer_forwarding_rule**](../docs/apis/tags/LoadBalancerApi.md#get_load_balancer_forwarding_rule) | **get** /load-balancers/{load-balancer-id}/forwarding-rules/{forwarding-rule-id} | Get Forwarding Rule
*LoadBalancerApi* | [**get_loadbalancer_firewall_rule**](../docs/apis/tags/LoadBalancerApi.md#get_loadbalancer_firewall_rule) | **get** /load-balancers/{loadbalancer-id}/firewall-rules/{firewall-rule-id} | Get Firewall Rule
*LoadBalancerApi* | [**list_load_balancer_forwarding_rules**](../docs/apis/tags/LoadBalancerApi.md#list_load_balancer_forwarding_rules) | **get** /load-balancers/{load-balancer-id}/forwarding-rules | List Forwarding Rules
*LoadBalancerApi* | [**list_load_balancers**](../docs/apis/tags/LoadBalancerApi.md#list_load_balancers) | **get** /load-balancers | List Load Balancers
*LoadBalancerApi* | [**list_loadbalancer_firewall_rules**](../docs/apis/tags/LoadBalancerApi.md#list_loadbalancer_firewall_rules) | **get** /load-balancers/{loadbalancer-id}/firewall-rules | List Firewall Rules
*LoadBalancerApi* | [**update_load_balancer**](../docs/apis/tags/LoadBalancerApi.md#update_load_balancer) | **patch** /load-balancers/{load-balancer-id} | Update Load Balancer
*OsApi* | [**list_os**](../docs/apis/tags/OsApi.md#list_os) | **get** /os | List OS
*PlansApi* | [**list_metal_plans**](../docs/apis/tags/PlansApi.md#list_metal_plans) | **get** /plans-metal | List Bare Metal Plans
*PlansApi* | [**list_plans**](../docs/apis/tags/PlansApi.md#list_plans) | **get** /plans | List Plans
*PrivateNetworksApi* | [**create_network**](../docs/apis/tags/PrivateNetworksApi.md#create_network) | **post** /private-networks | Create a Private Network
*PrivateNetworksApi* | [**delete_network**](../docs/apis/tags/PrivateNetworksApi.md#delete_network) | **delete** /private-networks/{network-id} | Delete a private network
*PrivateNetworksApi* | [**get_network**](../docs/apis/tags/PrivateNetworksApi.md#get_network) | **get** /private-networks/{network-id} | Get a private network
*PrivateNetworksApi* | [**list_networks**](../docs/apis/tags/PrivateNetworksApi.md#list_networks) | **get** /private-networks | List Private Networks
*PrivateNetworksApi* | [**update_network**](../docs/apis/tags/PrivateNetworksApi.md#update_network) | **put** /private-networks/{network-id} | Update a Private Network
*RegionApi* | [**list_available_plans_region**](../docs/apis/tags/RegionApi.md#list_available_plans_region) | **get** /regions/{region-id}/availability | List available plans in region
*RegionApi* | [**list_regions**](../docs/apis/tags/RegionApi.md#list_regions) | **get** /regions | List Regions
*ReservedIpApi* | [**attach_reserved_ip**](../docs/apis/tags/ReservedIpApi.md#attach_reserved_ip) | **post** /reserved-ips/{reserved-ip}/attach | Attach Reserved IP
*ReservedIpApi* | [**convert_reserved_ip**](../docs/apis/tags/ReservedIpApi.md#convert_reserved_ip) | **post** /reserved-ips/convert | Convert Instance IP to Reserved IP
*ReservedIpApi* | [**create_reserved_ip**](../docs/apis/tags/ReservedIpApi.md#create_reserved_ip) | **post** /reserved-ips | Create Reserved IP
*ReservedIpApi* | [**delete_reserved_ip**](../docs/apis/tags/ReservedIpApi.md#delete_reserved_ip) | **delete** /reserved-ips/{reserved-ip} | Delete Reserved IP
*ReservedIpApi* | [**detach_reserved_ip**](../docs/apis/tags/ReservedIpApi.md#detach_reserved_ip) | **post** /reserved-ips/{reserved-ip}/detach | Detach Reserved IP
*ReservedIpApi* | [**get_reserved_ip**](../docs/apis/tags/ReservedIpApi.md#get_reserved_ip) | **get** /reserved-ips/{reserved-ip} | Get Reserved IP
*ReservedIpApi* | [**list_reserved_ips**](../docs/apis/tags/ReservedIpApi.md#list_reserved_ips) | **get** /reserved-ips | List Reserved IPs
*ReservedIpApi* | [**patch_reserved_ips_reserved_ip**](../docs/apis/tags/ReservedIpApi.md#patch_reserved_ips_reserved_ip) | **patch** /reserved-ips/{reserved-ip} | Update Reserved IP
*S3Api* | [**create_object_storage**](../docs/apis/tags/S3Api.md#create_object_storage) | **post** /object-storage | Create Object Storage
*S3Api* | [**delete_object_storage**](../docs/apis/tags/S3Api.md#delete_object_storage) | **delete** /object-storage/{object-storage-id} | Delete Object Storage
*S3Api* | [**get_object_storage**](../docs/apis/tags/S3Api.md#get_object_storage) | **get** /object-storage/{object-storage-id} | Get Object Storage
*S3Api* | [**list_object_storage_clusters**](../docs/apis/tags/S3Api.md#list_object_storage_clusters) | **get** /object-storage/clusters | Get All Clusters
*S3Api* | [**list_object_storages**](../docs/apis/tags/S3Api.md#list_object_storages) | **get** /object-storage | List Object Storages
*S3Api* | [**regenerate_object_storage_keys**](../docs/apis/tags/S3Api.md#regenerate_object_storage_keys) | **post** /object-storage/{object-storage-id}/regenerate-keys | Regenerate Object Storage Keys
*S3Api* | [**update_object_storage**](../docs/apis/tags/S3Api.md#update_object_storage) | **put** /object-storage/{object-storage-id} | Update Object Storage
*SnapshotApi* | [**create_snapshot**](../docs/apis/tags/SnapshotApi.md#create_snapshot) | **post** /snapshots | Create Snapshot
*SnapshotApi* | [**create_snapshot_create_from_url**](../docs/apis/tags/SnapshotApi.md#create_snapshot_create_from_url) | **post** /snapshots/create-from-url | Create Snapshot from URL
*SnapshotApi* | [**delete_snapshot**](../docs/apis/tags/SnapshotApi.md#delete_snapshot) | **delete** /snapshots/{snapshot-id} | Delete Snapshot
*SnapshotApi* | [**get_snapshot**](../docs/apis/tags/SnapshotApi.md#get_snapshot) | **get** /snapshots/{snapshot-id} | Get Snapshot
*SnapshotApi* | [**list_snapshots**](../docs/apis/tags/SnapshotApi.md#list_snapshots) | **get** /snapshots | List Snapshots
*SnapshotApi* | [**put_snapshots_snapshot_id**](../docs/apis/tags/SnapshotApi.md#put_snapshots_snapshot_id) | **put** /snapshots/{snapshot-id} | Update Snapshot
*SshApi* | [**create_ssh_key**](../docs/apis/tags/SshApi.md#create_ssh_key) | **post** /ssh-keys | Create SSH key
*SshApi* | [**delete_ssh_key**](../docs/apis/tags/SshApi.md#delete_ssh_key) | **delete** /ssh-keys/{ssh-key-id} | Delete SSH Key
*SshApi* | [**get_ssh_key**](../docs/apis/tags/SshApi.md#get_ssh_key) | **get** /ssh-keys/{ssh-key-id} | Get SSH Key
*SshApi* | [**list_ssh_keys**](../docs/apis/tags/SshApi.md#list_ssh_keys) | **get** /ssh-keys | List SSH Keys
*SshApi* | [**update_ssh_key**](../docs/apis/tags/SshApi.md#update_ssh_key) | **patch** /ssh-keys/{ssh-key-id} | Update SSH Key
*StartupApi* | [**create_startup_script**](../docs/apis/tags/StartupApi.md#create_startup_script) | **post** /startup-scripts | Create Startup Script
*StartupApi* | [**delete_startup_script**](../docs/apis/tags/StartupApi.md#delete_startup_script) | **delete** /startup-scripts/{startup-id} | Delete Startup Script
*StartupApi* | [**get_startup_script**](../docs/apis/tags/StartupApi.md#get_startup_script) | **get** /startup-scripts/{startup-id} | Get Startup Script
*StartupApi* | [**list_startup_scripts**](../docs/apis/tags/StartupApi.md#list_startup_scripts) | **get** /startup-scripts | List Startup Scripts
*StartupApi* | [**update_startup_script**](../docs/apis/tags/StartupApi.md#update_startup_script) | **patch** /startup-scripts/{startup-id} | Update Startup Script
*UsersApi* | [**create_user**](../docs/apis/tags/UsersApi.md#create_user) | **post** /users | Create User
*UsersApi* | [**delete_user**](../docs/apis/tags/UsersApi.md#delete_user) | **delete** /users/{user-id} | Delete User
*UsersApi* | [**get_user**](../docs/apis/tags/UsersApi.md#get_user) | **get** /users/{user-id} | Get User
*UsersApi* | [**list_users**](../docs/apis/tags/UsersApi.md#list_users) | **get** /users | Get Users
*UsersApi* | [**update_user**](../docs/apis/tags/UsersApi.md#update_user) | **patch** /users/{user-id} | Update User

## Documentation For Models

 - [Account](../docs/models/Account.md)
 - [Application](../docs/models/Application.md)
 - [Backup](../docs/models/Backup.md)
 - [BackupSchedule](../docs/models/BackupSchedule.md)
 - [Bandwidth](../docs/models/Bandwidth.md)
 - [Baremetal](../docs/models/Baremetal.md)
 - [BaremetalIpv4](../docs/models/BaremetalIpv4.md)
 - [BaremetalIpv6](../docs/models/BaremetalIpv6.md)
 - [Billing](../docs/models/Billing.md)
 - [Blockstorage](../docs/models/Blockstorage.md)
 - [Clusters](../docs/models/Clusters.md)
 - [DnsRecord](../docs/models/DnsRecord.md)
 - [DnsSoa](../docs/models/DnsSoa.md)
 - [Domain](../docs/models/Domain.md)
 - [FirewallGroup](../docs/models/FirewallGroup.md)
 - [FirewallRule](../docs/models/FirewallRule.md)
 - [ForwardingRule](../docs/models/ForwardingRule.md)
 - [Instance](../docs/models/Instance.md)
 - [Invoice](../docs/models/Invoice.md)
 - [Iso](../docs/models/Iso.md)
 - [IsoPublic](../docs/models/IsoPublic.md)
 - [Loadbalancer](../docs/models/Loadbalancer.md)
 - [LoadbalancerFirewallRule](../docs/models/LoadbalancerFirewallRule.md)
 - [Meta](../docs/models/Meta.md)
 - [Network](../docs/models/Network.md)
 - [NodepoolInstances](../docs/models/NodepoolInstances.md)
 - [Nodepools](../docs/models/Nodepools.md)
 - [ObjectStorage](../docs/models/ObjectStorage.md)
 - [Os](../docs/models/Os.md)
 - [Plans](../docs/models/Plans.md)
 - [PlansMetal](../docs/models/PlansMetal.md)
 - [PrivateNetworks](../docs/models/PrivateNetworks.md)
 - [Region](../docs/models/Region.md)
 - [ReservedIp](../docs/models/ReservedIp.md)
 - [Snapshot](../docs/models/Snapshot.md)
 - [Ssh](../docs/models/Ssh.md)
 - [Startup](../docs/models/Startup.md)
 - [User](../docs/models/User.md)
 - [VkeCluster](../docs/models/VkeCluster.md)
 - [Vpc](../docs/models/Vpc.md)

## Documentation For Authorization

 Authentication schemes defined for the API:
## APIKey

- **Type**: Bearer authentication


## Author

opensource@vultr.com
opensource@vultr.com
opensource@vultr.com
opensource@vultr.com
opensource@vultr.com
opensource@vultr.com
opensource@vultr.com
opensource@vultr.com
opensource@vultr.com
opensource@vultr.com
opensource@vultr.com
opensource@vultr.com
opensource@vultr.com
opensource@vultr.com
opensource@vultr.com
opensource@vultr.com
opensource@vultr.com
opensource@vultr.com
opensource@vultr.com
opensource@vultr.com
opensource@vultr.com
opensource@vultr.com
opensource@vultr.com

## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in openapi_client.apis and openapi_client.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from openapi_client.apis.default_api import DefaultApi`
- `from openapi_client.model.pet import Pet`

Solution 1:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import openapi_client
from openapi_client.apis import *
from openapi_client.models import *
```
