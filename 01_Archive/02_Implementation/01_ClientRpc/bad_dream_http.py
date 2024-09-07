from base_http_transport import BaseHttpTransport
from server import FakeServer

class BadDreamHttp(BaseHttpTransport):
    def __init__(self):
        print("BadDreamHttp: Initialize")
        self.server = FakeServer()
        print("Opened connection to the FakeServer")

    def send_data_badream_way(self, request_data: str) -> str:
        print(f"BadDreamHttp (Internal): Sending request using BadDream's unique way: {request_data}")
        response = self.server.process_request(request_data)
        print(f"BadDreamHttp (Internal): Received response: {response}")
        return response

    # Translation layer: process_request calls send_data_badream_way internally
    def send_request(self, request_data: str) -> str:
        print(f"BadDreamHttp: Translating process_request to BadDream's internal method.")
        return self.send_data_badream_way(request_data)
