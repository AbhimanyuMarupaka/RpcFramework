import json
from client_rpc import ClientRpc
from client_transport import ClientTransport

class DreamRpc(ClientRpc):
    def __init__(self, transport_protocol: ClientTransport):
        print("DreamRpc: Initialize")
        self.transport_protocol = transport_protocol

    def process_request(self, method: str, args: list):
        # Prepare the request
        
        print(f"DreamRpc: Marshalling/Serializing request received '{method}' with args {args}")

        request_data = json.dumps({"method": method, "args": args})

        print(f"DreamRpc: Sending the serialized msg to transport layer {request_data}")        
        
        # Send the request via the transport protocol
        response_data = self.transport_protocol.send_request(request_data)

        print(f"DreamRpc: Received response from transport layer {response_data}")        

        # Parse and return the result
        response = json.loads(response_data)
        
        return response
