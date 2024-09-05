import argparse

class ClientApp:
    def __init__(self, rpc_framework):
        print("ClientApp: Initialize")
        self.rpc_framework = rpc_framework

    def parse_arguments(self):
        # Create argument parser inside the ClientApp class
        parser = argparse.ArgumentParser(description="Command Line RPC Client")
        
        # Optional parameters for the add method
        parser.add_argument("--a", type=int, help="First integer for the add method", default=10)
        parser.add_argument("--b", type=int, help="Second integer for the add method", default=20)

        # Parse the arguments directly inside the class
        args = parser.parse_args()
        return args.a, args.b

    def do_operations(self):
        
        # Remote method 1: hello()
        request_type = "hello"  # This could be any dynamically set value
        
        print(f"ClientApp: Request: '{request_type}'")
        
        result = self.rpc_framework.process_request(request_type, [])
        
        print(f"ClientApp: Result: '{result}'")
        
        # Remote method 2: add(a, b)
        request_type = "add"

        # Parse command-line arguments for the add() method
        a, b = self.parse_arguments()        

        print(f"ClientApp: Request: '{request_type}' with arguments ({a}, {b})")

        result = self.rpc_framework.process_request(request_type, [a, b])
        
        print(f"ClientApp: Result: '{result}'")