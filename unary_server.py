import grpc
from concurrent import futures
import unary.unary_pb2_grpc as pb2_grpc
import unary.unary_pb2 as pb2

class UnaryService(pb2_grpc.UnaryServicer):
    
    def __inti__(self, *args, **kargs):
        pass
    
    def GetServerResponse(self, request, context):
        message = request.message
        result = f'Hello I am up and running recieved the "{message}" message from you'
        result = {'message':result, 'received':True}
        
        return pb2.MessageResponse(**result)
    
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_UnaryServicer_to_server(UnaryService(), server)
    server.add_insecure_port('[::]:50051')
    print('Started Server! Listening at 50051')
    server.start()
    server.wait_for_termination()
    
    
if __name__ == '__main__':
    serve()