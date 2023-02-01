# openapi_client.model.loadbalancer_firewall_rule.LoadbalancerFirewallRule

Load Balancer firewall rule information.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Load Balancer firewall rule information. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  | The unique ID for the firewall rule | [optional] 
**port** | decimal.Decimal, int,  | decimal.Decimal,  | Port for this rule.  | [optional] 
**source** | str,  | str,  | If the source string is given a value of \&quot;cloudflare\&quot; then cloudflare IPs will be supplied. Otherwise enter a IP address with subnet size that you wish to permit through the firewall.  Possible values:  |   | Value | Description | | - | ------ | ------------- | |   | \&quot;192.168.1.1/16\&quot; | Ip address with a subnet size. | |   | cloudflare | Allow all of Cloudflare&#x27;s IP space through the firewall | | [optional] 
**ip_type** | str,  | str,  | The type of IP rule.  * v4 * v6  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../openapi-client/README.md#documentation-for-models) [[Back to API list]](../../openapi-client/README.md#documentation-for-api-endpoints) [[Back to README]](../../openapi-client/README.md)

