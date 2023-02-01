# openapi_client.model.invoice.Invoice

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | decimal.Decimal, int,  | decimal.Decimal,  | ID of the invoice | [optional] 
**date** | str,  | str,  | Date invoice was generated | [optional] 
**description** | str,  | str,  | description of item | [optional] 
**amount** | decimal.Decimal, int, float,  | decimal.Decimal,  | Amount due in dollars | [optional] 
**balance** | decimal.Decimal, int, float,  | decimal.Decimal,  | Account balance amount in dollars | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../openapi-client/README.md#documentation-for-models) [[Back to API list]](../../openapi-client/README.md#documentation-for-api-endpoints) [[Back to README]](../../openapi-client/README.md)

