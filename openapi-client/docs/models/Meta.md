# openapi_client.model.meta.Meta

The meta information object. See [Meta and Pagination](#section/Introduction/Meta-and-Pagination) for more information.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The meta information object. See [Meta and Pagination](#section/Introduction/Meta-and-Pagination) for more information. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**total** | decimal.Decimal, int,  | decimal.Decimal,  | Total objects available in the list. This value may be greater than the number of objects returned if &#x60;per_page&#x60; is set. | [optional] 
**[links](#links)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Cursor values for pagination. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# links

Cursor values for pagination.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Cursor values for pagination. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**next** | str,  | str,  | Cursor value for the next page. | [optional] 
**prev** | str,  | str,  | Cursor value for the previous page. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../openapi-client/README.md#documentation-for-models) [[Back to API list]](../../openapi-client/README.md#documentation-for-api-endpoints) [[Back to README]](../../openapi-client/README.md)

