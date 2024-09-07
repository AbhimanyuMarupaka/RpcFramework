from abc import ABC, abstractmethod

class ClientTransport(ABC):
    @abstractmethod
    def send_request(self, request_data: str) -> str:
        """Send a request and return the response."""
        pass
