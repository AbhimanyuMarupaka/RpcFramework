import json

class FakeServer:
    def __init__(self):
        print("FakeServer: Initialize")
        pass

    def process_request(self, request_data: str) -> str:
        print(f"FakeServer: Received request: {request_data}")
        request = json.loads(request_data)
        method_name = request.get("method")
        args = request.get("args", [])

        # Fake implementation of the remote methods
        if method_name == "hello":
            result = "Greetings!"
        elif method_name == "add" and len(args) == 2:
            result = args[0] + args[1]
        else:
            result = "Method not found"

        response = json.dumps({"result": result})
        print(f"FakeServer: Sending response: {response}")
        return response
