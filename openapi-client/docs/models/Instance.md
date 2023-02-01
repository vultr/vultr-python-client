# openapi_client.model.instance.Instance

Instance information.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Instance information. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  | A unique ID for the VPS Instance. | [optional] 
**os** | str,  | str,  | The [Operating System name](#operation/list-os). | [optional] 
**ram** | decimal.Decimal, int,  | decimal.Decimal,  | The amount of RAM in MB. | [optional] 
**disk** | decimal.Decimal, int,  | decimal.Decimal,  | The size of the disk in GB. | [optional] 
**main_ip** | str,  | str,  | The main IPv4 address. | [optional] 
**vcpu_count** | decimal.Decimal, int,  | decimal.Decimal,  | Number of vCPUs. | [optional] 
**region** | str,  | str,  | The [Region id](#operation/list-regions) where the Instance is located. | [optional] 
**default_password** | str,  | str,  | The default password assigned at deployment. | [optional] 
**date_created** | str,  | str,  | The date this instance was created. | [optional] 
**status** | str,  | str,  | The current status.  * active * pending * suspended * resizing | [optional] 
**power_status** | str,  | str,  | The power-on status.  * running * stopped | [optional] 
**server_status** | str,  | str,  | The server health status.  * none * locked * installingbooting * ok | [optional] 
**allowed_bandwidth** | decimal.Decimal, int,  | decimal.Decimal,  | Monthly bandwidth quota in GB. | [optional] 
**netmask_v4** | str,  | str,  | The IPv4 netmask in dot-decimal notation. | [optional] 
**gateway_v4** | str,  | str,  | The gateway IP address. | [optional] 
**[v6_networks](#v6_networks)** | list, tuple,  | tuple,  | An array of IPv6 objects. | [optional] 
**hostname** | str,  | str,  | The hostname for this instance. | [optional] 
**label** | str,  | str,  | The user-supplied label for this instance. | [optional] 
**tag** | str,  | str,  | Use &#x60;tags&#x60; instead. The user-supplied tag for this instance. | [optional] 
**internal_ip** | str,  | str,  | The internal IP used by this instance, if set. | [optional] 
**kvm** | str,  | str,  | HTTPS link to the Vultr noVNC Web Console. | [optional] 
**os_id** | decimal.Decimal, int,  | decimal.Decimal,  | The [Operating System id](#operation/list-os) used by this instance. | [optional] 
**app_id** | decimal.Decimal, int,  | decimal.Decimal,  | The [Application id](#operation/list-applications) used by this instance. | [optional] 
**image_id** | str,  | str,  | The [Application image_id](#operation/list-applications) used by this instance. | [optional] 
**firewall_group_id** | str,  | str,  | The [Firewall Group id](#operation/list-firewall-groups) linked to this Instance. | [optional] 
**[features](#features)** | list, tuple,  | tuple,  | \&quot;auto_backups\&quot;, \&quot;ipv6\&quot;, \&quot;ddos_protection\&quot; | [optional] 
**plan** | str,  | str,  | A unique ID for the Plan. | [optional] 
**[tags](#tags)** | list, tuple,  | tuple,  | Tags to apply to the instance | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# v6_networks

An array of IPv6 objects.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | An array of IPv6 objects. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  | An IPv6 object. | 

# items

An IPv6 object.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | An IPv6 object. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**network** | str,  | str,  | The IPv6 subnet. | [optional] 
**main_ip** | str,  | str,  | The main IPv6 network address. | [optional] 
**network_size** | decimal.Decimal, int,  | decimal.Decimal,  | The IPv6 network size in bits. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# features

\"auto_backups\", \"ipv6\", \"ddos_protection\"

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | \&quot;auto_backups\&quot;, \&quot;ipv6\&quot;, \&quot;ddos_protection\&quot; | 

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

[[Back to Model list]](../../openapi-client/README.md#documentation-for-models) [[Back to API list]](../../openapi-client/README.md#documentation-for-api-endpoints) [[Back to README]](../../openapi-client/README.md)

