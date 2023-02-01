# openapi_client.model.user.User

User information.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | User information. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[user](#user)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | An array of Users. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# user

An array of Users.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | An array of Users. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  | The User&#x27;s id. | [optional] 
**name** | str,  | str,  | The User&#x27;s name. | [optional] 
**api_enabled** | bool,  | BoolClass,  | Permit API access for this User.  * true * false | [optional] 
**email** | str,  | str,  | The User&#x27;s email address. | [optional] 
**password** | str,  | str,  | The User&#x27;s password. | [optional] 
**[acls](#acls)** | list, tuple,  | tuple,  | An array of permission granted.  * abuse * alerts * billing * dns * firewall * loadbalancer * manage\\_users * objstore * provisioning * subscriptions * subscriptions\\_view * support * upgrade | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# acls

An array of permission granted.  * abuse * alerts * billing * dns * firewall * loadbalancer * manage\\_users * objstore * provisioning * subscriptions * subscriptions\\_view * support * upgrade

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | An array of permission granted.  * abuse * alerts * billing * dns * firewall * loadbalancer * manage\\_users * objstore * provisioning * subscriptions * subscriptions\\_view * support * upgrade | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../openapi-client/README.md#documentation-for-models) [[Back to API list]](../../openapi-client/README.md#documentation-for-api-endpoints) [[Back to README]](../../openapi-client/README.md)

