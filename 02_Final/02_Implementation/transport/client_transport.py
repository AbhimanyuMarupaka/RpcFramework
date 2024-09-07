from abc import ABC, abstractmethod

class ClientTransport(ABC):
    @abstractmethod
    def send_request(self, request_data: str) -> str:
        """Send the serialized request data through the transport layer."""
        pass
