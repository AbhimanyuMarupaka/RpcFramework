from transport.client_transport import ClientTransport
from transport.bad_dream_http import BadDreamHTTP

class BadDreamHTTPWrapper(ClientTransport):
    def __init__(self):
        print("BadDreamHTTPWrapper: __init__: Initialize")
        # Initialize BadDreamHTTP 
        self.bad_dream_http = BadDreamHTTP()

    def send_request(self, request_data: str) -> str:
        print(f"BadDreamHTTPWrapper: send_request: Calling send method of BadDreamHTTP: {request_data}")
        response =  self.bad_dream_http.send_data_bad_dream_http_way(request_data)
        print(f"BadDreamHTTPWrapper: send_request: Received response from BadDreamHTTP: {response}")
        return response
