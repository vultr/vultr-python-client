# openapi_client.model.dns_record.DnsRecord

DNS Record information.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | DNS Record information. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  | A unique ID for the DNS Record. | [optional] 
**type** | str,  | str,  | The DNS record type.  * A * AAAA * CNAME * NS * MX * SRV * TXT * CAA * SSHFP | [optional] 
**name** | str,  | str,  | The hostname for this DNS record. | [optional] 
**data** | str,  | str,  | The DNS data for this record type. | [optional] 
**priority** | decimal.Decimal, int,  | decimal.Decimal,  | DNS priority. Does not apply to all record types. | [optional] 
**ttl** | decimal.Decimal, int,  | decimal.Decimal,  | Time to Live in seconds. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../openapi-client/README.md#documentation-for-models) [[Back to API list]](../../openapi-client/README.md#documentation-for-api-endpoints) [[Back to README]](../../openapi-client/README.md)

