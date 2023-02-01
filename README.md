# Python Client Vultr
## Note
In the vultr.com api spec I had to replace the string "API Key" to "APIKey". The OpenAPI format and the generator does not like spaces in the names of security schemes 
## Description
This is a python client for the V2 vultr API. it was generated from the OpenAPI spec at https://www.vultr.com/api/. It was generated using this generator: https://github.com/OpenAPITools/openapi-generator. I have also included a small example in test.py on how to use the client.

## Using the generator
Version 6.2 did not work for another project so I used a snapshot version of 6.3. The jar has been included here for convenience. It is sensitive the java version used, java8 and java11 work, java 17 does not. My OpenAPI spec is called OpenAPI.json but some people may name theirs swagger.json

```
java -jar openapi-generator-cli-6.3.jar generate -i openapi.json -g python -o output_dir

```

## Installation
A new client should be generated in output_dir, the docs folder contains the markdown for documentation. 

To build a wheel run: 
``` 
cd output_dir
python setup.py sdist bdist_wheel
```

you can now use the .whl file in output_dir/dist to install our libary

For poetry you can copy and past the .whl file to the root of you python project and run:

```
poetry add <name_of_file>.whl
```

to install it
## Usage
For the most part, the README and the docs folder in output_dir should be enough documentation to get started. However something not mentioned in the docs is how to properly set the access token.

You can not set the access token like this:
```
configuration = OpenAPI_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
```

You have to manually set it after the configurtation class is initzialed like so:

```
configuration = OpenAPI_client.Configuration()
configuration.access_token = 'YOUR_BEARER_TOKEN'

```

## Support
Tell people where they can go to for help. It can be any combination of an issue tracker, a chat room, an email address, etc.


