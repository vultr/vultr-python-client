import openapi_client
from openapi_client.apis.tags import account_api
from openapi_client.model.account import Account
from pprint import pprint
# Defining the host is optional and defaults to https://api.vultr.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.vultr.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: APIKey
configuration = openapi_client.Configuration()

configuration.access_token = input("Enter Bearer Token: ")
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = account_api.AccountApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Account Info
        api_response = api_instance.get_account()

        account = Account(api_response.body)
        pprint(account)
    except openapi_client.ApiException as e:
        print("Exception when calling AccountApi->get_account: %s\n" % e)