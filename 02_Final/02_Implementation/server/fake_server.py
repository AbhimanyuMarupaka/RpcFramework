import json

class FakeServer:
    def __init__(self):
        print("FakeServer: __init__: Initialize")

    def process_request(self, request_data: str) -> str:
        #Process the request and return a response
        print(f"FakeServer: process_request: Received request: {request_data}")
        request = json.loads(request_data)
        method = request.get("method")
        args = request.get("args", [])

        if method == "hello":
            result = "Greetings!"
        elif method == "add" and len(args) == 2:
            result = args[0] + args[1]
        else:
            result = "Method not found"

        response = json.dumps({"response": result})

        print(f"FakeServer: process_request: Sending response: {response}")
        return response
