# openapi_client.model.loadbalancer.Loadbalancer

Load Balancer information.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Load Balancer information. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  | A unique ID for the Load Balancer. | [optional] 
**date_created** | str,  | str,  | Date this Load Balancer was created. | [optional] 
**region** | str,  | str,  | The [Region id](#operation/list-regions) where the Load Balancer is located. | [optional] 
**label** | str,  | str,  | The user-supplied label for this load-balancer. | [optional] 
**status** | str,  | str,  | The current status.  * active | [optional] 
**ipv4** | str,  | str,  | The IPv4 address of this Load Balancer. | [optional] 
**ipv6** | str,  | str,  | The IPv6 address of this Load Balancer. | [optional] 
**[generic_info](#generic_info)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | An object containing additional options. | [optional] 
**[health_check](#health_check)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | The health check object configuration. See [Load Balancer documentation](https://www.vultr.com/docs/vultr-load-balancers/#Load_Balancer_Configuration). | [optional] 
**has_ssl** | bool,  | BoolClass,  | Indicates if this Load Balancer has an SSL certificate installed. | [optional] 
**http2** | bool,  | BoolClass,  | Indicates if this Load Balancer has HTTP2 enabled. | [optional] 
**[forward_rules](#forward_rules)** | list, tuple,  | tuple,  | An array of forwarding rule objects. | [optional] 
**[instances](#instances)** | list, tuple,  | tuple,  | Array of [Instance ids](#operation/list-instances) attached to this Load Balancer. | [optional] 
**[firewall_rules](#firewall_rules)** | list, tuple,  | tuple,  | An array of firewall rule objects. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# generic_info

An object containing additional options.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | An object containing additional options. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**balancing_algorithm** | str,  | str,  | The balancing algorithm.  * roundrobin (default) * leastconn | [optional] 
**ssl_redirect** | bool,  | BoolClass,  | If &#x60;true&#x60;, this will redirect all HTTP traffic to HTTPS. You must have an HTTPS rule and SSL certificate installed on the load balancer to enable this option.  * true * false | [optional] 
**[sticky_sessions](#sticky_sessions)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Array of sticky session cookies. | [optional] 
**proxy_protocol** | bool,  | BoolClass,  | \&quot;If &#x60;true&#x60;, you must configure backend nodes to accept Proxy protocol. \\n\\n* true\\n* false (Default)\&quot; | [optional] 
**private_network** | str,  | str,  | Use &#x60;vpc&#x60; instead. ID of the private network you wish to use. If private_network is omitted it will default to the public network. | [optional] 
**vpc** | str,  | str,  | ID of the VPC you wish to use. If a VPC ID is omitted it will default to the public network. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# sticky_sessions

Array of sticky session cookies.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Array of sticky session cookies. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**cookie_name** | str,  | str,  | The cookie name to make sticky. See [Load Balancer documentation](https://www.vultr.com/docs/vultr-load-balancers/#Load_Balancer_Configuration). | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# health_check

The health check object configuration. See [Load Balancer documentation](https://www.vultr.com/docs/vultr-load-balancers/#Load_Balancer_Configuration).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The health check object configuration. See [Load Balancer documentation](https://www.vultr.com/docs/vultr-load-balancers/#Load_Balancer_Configuration). | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**protocol** | str,  | str,  | The protocol to use for health checks.  * HTTPS * HTTP * TCP | [optional] 
**port** | decimal.Decimal, int,  | decimal.Decimal,  | The port to use for health checks. | [optional] 
**path** | str,  | str,  | HTTP Path to check. Only applies if Protocol is HTTP or HTTPS. | [optional] 
**check_interval** | decimal.Decimal, int,  | decimal.Decimal,  | Interval between health checks. | [optional] 
**response_timeout** | decimal.Decimal, int,  | decimal.Decimal,  | Timeout before health check fails. | [optional] 
**unhealthy_threshold** | decimal.Decimal, int,  | decimal.Decimal,  | Number times a check must fail before becoming unhealthy. | [optional] 
**healthy_threshold** | decimal.Decimal, int,  | decimal.Decimal,  | Number of times a check must succeed before returning to healthy status. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# forward_rules

An array of forwarding rule objects.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | An array of forwarding rule objects. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  | A forwarding rule object. | 

# items

A forwarding rule object.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A forwarding rule object. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  | A unique ID for the forwarding rule. | [optional] 
**frontend_protocol** | str,  | str,  | The protocol on the Load Balancer to forward to the backend.  * HTTP * HTTPS * TCP | [optional] 
**frontend_port** | decimal.Decimal, int,  | decimal.Decimal,  | The port number on the Load Balancer to forward to the backend. | [optional] 
**backend_portocol** | str,  | str,  | The protocol destination on the backend server.  * HTTP * HTTPS * TCP | [optional] 
**backend_port** | decimal.Decimal, int,  | decimal.Decimal,  | The port number destination on the backend server.  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# instances

Array of [Instance ids](#operation/list-instances) attached to this Load Balancer.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Array of [Instance ids](#operation/list-instances) attached to this Load Balancer. | 

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
**id** | str,  | str,  | A unique ID for the firewall rule. | [optional] 
**port** | decimal.Decimal, int,  | decimal.Decimal,  | Port for this rule. | [optional] 
**source** | str,  | str,  | If the source string is given a value of \&quot;cloudflare\&quot; then cloudflare IPs will be supplied. Otherwise enter a IP address with subnet size that you wish to permit through the firewall.    Possible values:    |   | Value | Description |   | - | ------ | ------------- |   |   | \&quot;192.168.1.1/16\&quot; | Ip address with a subnet size. |   |   | cloudflare | Allow all of Cloudflare&#x27;s IP space through the firewall | | [optional] 
**ip_type** | str,  | str,  | The type of IP rule.  * v4 * v6  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../openapi-client/README.md#documentation-for-models) [[Back to API list]](../../openapi-client/README.md#documentation-for-api-endpoints) [[Back to README]](../../openapi-client/README.md)

