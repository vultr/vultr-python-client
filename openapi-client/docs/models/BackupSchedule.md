# openapi_client.model.backup_schedule.BackupSchedule

Backup schedule information.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Backup schedule information. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**enabled** | bool,  | BoolClass,  | Indicates if backup is enabled:  * true * false | [optional] 
**type** | str,  | str,  | Type of backup schedule:  |   | Value | Description | | - | ------ | ------------- | |   | daily | Back up once per day at &#x60;hour&#x60;. | |   | weekly | Back up once per week on &#x60;dow&#x60; at &#x60;hour&#x60;. | |   | monthly | Back up each month at &#x60;dom&#x60; at &#x60;hour&#x60;. | |   | daily\\_alt\\_even | Back up on even dates at &#x60;hour&#x60;. | |   | daily\\_alt\\_odd | Back up on odd dates at &#x60;hour&#x60;. | | [optional] 
**next_scheduled_time_utc** | str,  | str,  | Time of next backup run in UTC. | [optional] 
**hour** | decimal.Decimal, int,  | decimal.Decimal,  | Scheduled hour of day in UTC. | [optional] 
**dow** | decimal.Decimal, int,  | decimal.Decimal,  | Day of week to run.  |   | Value | Description | | - | ------ | ------------- | |   | 1 | Sunday | |   | 2 | Monday | |   | 3 | Tuesday | |   | 4 | Wednesday | |   | 5 | Thursday | |   | 6 | Friday | |   | 7 | Saturday | | [optional] 
**dom** | decimal.Decimal, int,  | decimal.Decimal,  | Day of month to run. Use values between 1 and 28. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../openapi-client/README.md#documentation-for-models) [[Back to API list]](../../openapi-client/README.md#documentation-for-api-endpoints) [[Back to README]](../../openapi-client/README.md)

