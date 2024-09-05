from dream_rpc import DreamRpc

class ClientRpcFactory:
    @staticmethod
    def get_rpc_framework(rpc_type: str, transport_protocol):

        if rpc_type == 'dream':

            print(f"ClientRpcFactory: Creating '{rpc_type}' RPC instance.")
        
            return DreamRpc(transport_protocol)
        else:
        
            raise ValueError(f"Unknown RPC framework type: '{rpc_type}'. Valid option is 'dream'.")
