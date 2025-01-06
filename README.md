# grpc-learn
Experimenting with grpc

Unary
-----

'''bash
python -m grpc_tools.protoc --proto_path=. ./unary.proto --python_out=. --grpc_python_out=.
'''

python -m grpc_tools.protoc --proto_path=.  ./bidirecctional.proto --python_out=. --grpc_python_out=.

Reference :

https://www.velotio.com/engineering-blog/grpc-implementation-using-python