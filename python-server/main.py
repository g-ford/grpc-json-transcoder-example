import grpc
from concurrent import futures
import time

import proto.echo_pb2 as proto
import proto.echo_pb2_grpc as grpc_server

class EchoService(grpc_server.EchoServicer):
    def Echo(self, request, context):
        response = proto.Message()
        response.message = request.message
        return response

    def Reverse(self, request, context):
        response = proto.Message()
        response.message = request.message[::-1]
        return response


def serve():
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

if __name__ == "__main__":
    serve()