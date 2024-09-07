from server.fake_server import FakeServer

class BadDreamHTTP:
    def __init__(self):
        print("BadDreamHTTP: __init__: Initialize")
        # Initialize FakeServer as part of BadDreamHTTP
        self.fake_server = FakeServer() 
        print("BadDreamHTTP: Open connection to the Fake server")

    def send_data_bad_dream_http_way(self, request_data: str) -> str:

        print(f"BadDreamHTTP: send_data_badream_way: Sending request data: {request_data}")
        # Interact with the FakeServer to process the request
        response = self.fake_server.process_request(request_data)

        print(f"BadDreamHTTP: send_data_badream_way: Received response from FakeServer: {response}")
        return response
