from abc import ABC, abstractmethod

class ClientRpc(ABC):
    @abstractmethod
    def process_request(self, method: str, args: list):
        pass
