import grpc
from concurrent import futures
import time

import proto.echo_pb2 as proto
import proto.echo_pb2_grpc as grpc_server

class EchoService(grpc_server.EchoServicer):
    def Echo(self, request, context):
        print("Processing request", request)
        response = proto.Message()
        response.message = request.message + ", hissss!"
        return response

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
grpc_server.add_EchoServicer_to_server(EchoService(), server)

print("Starting server on port 9000")
server.add_insecure_port('[::]:9000')
server.start()

try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)