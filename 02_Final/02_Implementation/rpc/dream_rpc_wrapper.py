import json
from rpc.client_rpc import ClientRpc
from rpc.dream_rpc import DreamRPC
from transport.client_transport import ClientTransport

class DreamRPCWrapper(ClientRpc):
    def __init__(self, transport: ClientTransport):
        print("DreamRPCWrapper: __init__: Initialize")
        self.dream_rpc = DreamRPC()  # DreamRPC handles the "preparation" of the RPC call
        self.transport = transport  


    def process_request(self, method: str, args: list):        
        # Step 1: Serialize the request data into JSON format 
        # JSON format is chosen as an example, this format can be replaced by any choice format
        # chosen by the 3rd party library.
        request_data = json.dumps({"method": method, "args": args})
        print(f"DreamRPCWrapper: process_request: Serializing request '{method}' with args {args}")

        # Step 2: Let DreamRPC "prepare" the request (e.g., add metadata or RPC-specific headers)
        prepared_request_data = self.dream_rpc.prepare_request_dream_rpc_way(request_data)

        # Step 3: Use the transport layer to send the prepared request data
        response_data = self.transport.send_request(prepared_request_data)

        # Step 4: Deserialize the response data received from the transport layer
        response = json.loads(response_data)
        print(f"DreamRPCWrapper: process_request_rpc_way: Received response from transport")

        return response

