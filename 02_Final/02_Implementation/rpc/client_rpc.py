from abc import ABC, abstractmethod

class ClientRpc(ABC):
    @abstractmethod
    def process_request(self, method: str, args: list):
        """Process the request by serializing data and prepare to send it to the transport layer"""
        pass
