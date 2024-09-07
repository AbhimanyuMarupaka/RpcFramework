from client_transport import ClientTransport

class BaseHttpTransport(ClientTransport):
    # This method is currently overridden by the derived class (BadDreamHttp).
    # However, this base class is designed to hold common methods that can be shared
    # across various HTTP implementations. 
    # By having this method in the base class, we ensure that shared behavior is 
    # easily reusable across all HTTP-based transports, reducing code duplication.
    def send_request(self, request_data: str) -> str:
        print(f"BaseHttpTransport: Sending HTTP request: {request_data}")
        response = '{"result": "Simulated HTTP response"}'
        print(f"BaseHttpTransport: Received HTTP response: {response}")
        return response
