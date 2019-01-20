GRPC_FLAGS := \
    -I. \
    -I/usr/local/include \
    -I$(GOPATH)/src \
    -I$(GOPATH)/src/github.com/grpc-ecosystem/grpc-gateway/third_party/googleapis \
	--include_imports \
	--proto_path=./proto

CLIENT_FLAGS := \
    --python_out=./python-server \
    --grpc_python_out=./python-server \
	--go_out=plugins=grpc:./proto/ \
	--swagger_out=./json-proxy/

all:
	mkdir -p json-proxy/config
	python -m grpc_tools.protoc $(GRPC_FLAGS) \
		$(CLIENT_FLAGS) \
		./proto/*.proto

	protoc $(GRPC_FLAGS) \
		--descriptor_set_out=./json-proxy/config/echo_service.pb \
		./proto/*.proto

clean:
	rm -rf python-server/proto
	rm -rf proto/proto
	rm -rf json-proxy/proto
	rm -rf json-proxy/config
