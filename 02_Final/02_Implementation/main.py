from rpc.dream_rpc_wrapper import DreamRPCWrapper
from transport.bad_dream_http_wrapper import BadDreamHTTPWrapper
from client_application import ClientApp

if __name__ == "__main__":
    # Initialize the transport layer (BadDreamHTTP)
    transport = BadDreamHTTPWrapper()

    # Initialize the RPC layer (DreamRPC)
    rpc_framework = DreamRPCWrapper(transport)

    # Initialize the client app
    client_app = ClientApp(rpc_framework)

    # Perform operations
    client_app.do_operations()
