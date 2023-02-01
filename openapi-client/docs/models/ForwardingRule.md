# openapi_client.model.forwarding_rule.ForwardingRule

Forwarding Rule information.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Forwarding Rule information. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  | A unique ID for the Forwarding Rule. | [optional] 
**frontend_protocol** | str,  | str,  | The protocol on the Load Balancer to forward to the backend.  * HTTP * HTTPS * TCP | [optional] 
**frontend_port** | decimal.Decimal, int,  | decimal.Decimal,  | The port number on the Load Balancer to forward to the backend. | [optional] 
**backend_protocol** | str,  | str,  | The protocol destination on the backend server.  * HTTP * HTTPS * TCP | [optional] 
**backend_port** | decimal.Decimal, int,  | decimal.Decimal,  | The port number destination on the backend server. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../openapi-client/README.md#documentation-for-models) [[Back to API list]](../../openapi-client/README.md#documentation-for-api-endpoints) [[Back to README]](../../openapi-client/README.md)

