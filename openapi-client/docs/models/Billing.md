# openapi_client.model.billing.Billing

Invoice

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Invoice | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | decimal.Decimal, int, float,  | decimal.Decimal,  | ID of the billing history item | [optional] 
**date** | str,  | str,  | Date billing history item was generated | [optional] 
**type** | str,  | str,  | Type of billing history item | [optional] 
**description** | str,  | str,  | Description of billing history item | [optional] 
**amount** | decimal.Decimal, int, float,  | decimal.Decimal,  | Amount for the billing history item in dollars | [optional] 
**balance** | decimal.Decimal, int, float,  | decimal.Decimal,  | The accounts balance in dollars | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../openapi-client/README.md#documentation-for-models) [[Back to API list]](../../openapi-client/README.md#documentation-for-api-endpoints) [[Back to README]](../../openapi-client/README.md)

