from client_rpc_factory import ClientRpcFactory
from client_transport_factory import ClientTransportFactory
from client_app import ClientApp

if __name__ == "__main__":
    try:
        # Choose RPC framework and transport protocol to use
        rpc_framework_type = 'dream'  # Currently only 'dream rpc' is supported
        print(f"chosen rpc framework:'{rpc_framework_type}'")
        transport_protocol_type = 'bad_dream_http'  # Currently only 'bad_dream http'  is supported
        print(f"chosen transport protocol:'{transport_protocol_type}'")

        # Get the transport protocol instance
        transport_protocol = ClientTransportFactory.get_transport_protocol(transport_protocol_type)

        # Get the RPC framework instance with the transport protocol
        rpc_framework = ClientRpcFactory.get_rpc_framework(rpc_framework_type, transport_protocol)

        # Initialize the client app with the RPC framework
        client = ClientApp(rpc_framework)
        client.do_operations()

    except ValueError as e:
        # Print the error message and exit
        print(f"Error: {e}")
