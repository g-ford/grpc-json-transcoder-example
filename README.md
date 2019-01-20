# GRPC with JSON Transcoder

This is an example of using GRPC with an Envoy JSON Transcoder so that the same API can be exposed on GRPC and REST endpoints

The example is a very simple echo service that exposes to endpoints:

| GRPC          | REST          | Description   |
| ------------- | ------------- | ------------- |
| echo.Echo/Echo | POST /v1/echo | Returns a copy of the message sent |
| echo.Echo/Reverse | POST /v1/reverse | Returns the same message reversed |

# Pre-requisites

You will need a Docker, Python3 and a golang environment.

    make dependencies

This will install the necessary go and python packages.  A virtual environment will be created for python if required

# Building

Before creating the docker images you will need to generate the GRPC stubs

    make 

# Running

    docker-compose up

This will create two containers, one running the python GRPC server on port 9000, the other running the Envoy JSON transcoder on port 8080.

# Testing

To test the REST endpoints:

    curl -d '{"message":"Test Message"}' \ 
         -H "Content-Type: application/json" 
         -X POST http://localhost:8080/v1/echo

To test the GRPC endpoint

    go run go-client/main.go

