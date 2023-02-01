# openapi_client.model.firewall_rule.FirewallRule

Firewall rule information.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Firewall rule information. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | decimal.Decimal, int,  | decimal.Decimal,  | A unique ID for the Firewall Rule. | [optional] 
**type** | str,  | str,  | This field is deprecated. Use &#x60;ip_type&#x60; instead.  The type of IP rule.  * v4 * v6 | [optional] 
**ip_type** | str,  | str,  | The type of IP rule.  * v4 * v6 | [optional] 
**action** | str,  | str,  | Action to take when this rule is met.  * accept | [optional] 
**protocol** | str,  | str,  | The protocol for this rule.  * ICMP * TCP * UDP * GRE  | [optional] 
**port** | str,  | str,  | Port or port range for this rule. | [optional] 
**subnet** | str,  | str,  | IP address representing a subnet. The IP address format must match with the \&quot;ip_type\&quot; parameter value. | [optional] 
**subnet_size** | decimal.Decimal, int,  | decimal.Decimal,  | The number of bits for the netmask in CIDR notation. Example: 24 | [optional] 
**source** | str,  | str,  | If the source string is given a value of \&quot;cloudflare\&quot; subnet and subnet_size will both be ignored. Possible values:  |   | Value | Description | | - | ------ | ------------- | |   | \&quot;\&quot; | Use the value from &#x60;subnet&#x60; and &#x60;subnet_size&#x60;. | |   | cloudflare | Allow all of Cloudflare&#x27;s IP space through the firewall | | [optional] 
**notes** | str,  | str,  | User-supplied notes for this rule. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../openapi-client/README.md#documentation-for-models) [[Back to API list]](../../openapi-client/README.md#documentation-for-api-endpoints) [[Back to README]](../../openapi-client/README.md)

