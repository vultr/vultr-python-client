# openapi_client.model.account.Account

Account information.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Account information. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  | Your user name. | [optional] 
**email** | str,  | str,  | Your email address. | [optional] 
**[acls](#acls)** | list, tuple,  | tuple,  | An array of permission granted. * manage\\_users * subscriptions_view * subscriptions * billing * support * provisioning * dns * abuse * upgrade * firewall * alerts * objstore * loadbalancer | [optional] 
**balance** | decimal.Decimal, int, float,  | decimal.Decimal,  | Your current account balance. | [optional] 
**pending_charges** | decimal.Decimal, int, float,  | decimal.Decimal,  | Unbilled charges for this month. | [optional] 
**last_payment_date** | str,  | str,  | Date of your last payment. | [optional] 
**last_payment_amount** | decimal.Decimal, int, float,  | decimal.Decimal,  | The amount of your last payment. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# acls

An array of permission granted. * manage\\_users * subscriptions_view * subscriptions * billing * support * provisioning * dns * abuse * upgrade * firewall * alerts * objstore * loadbalancer

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | An array of permission granted. * manage\\_users * subscriptions_view * subscriptions * billing * support * provisioning * dns * abuse * upgrade * firewall * alerts * objstore * loadbalancer | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../openapi-client/README.md#documentation-for-models) [[Back to API list]](../../openapi-client/README.md#documentation-for-api-endpoints) [[Back to README]](../../openapi-client/README.md)

