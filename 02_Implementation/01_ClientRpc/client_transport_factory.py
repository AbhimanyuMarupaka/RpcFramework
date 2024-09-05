from bad_dream_http import BadDreamHttp

class ClientTransportFactory:
    @staticmethod
    def get_transport_protocol(transport_type: str):

        # print(f"Request received to get transport protocol for: '{transport_type}'")

        if transport_type == 'bad_dream_http':
            
            print(f"ClientTransportFactory: Creating '{transport_type}' transport instance.")

            return BadDreamHttp()  # BadDreamHttp is derived from HttpTransport
        else:
            raise ValueError(f"Unknown Transport protocol type: '{transport_type}'. Valid option is 'bad_dream_http'.")
