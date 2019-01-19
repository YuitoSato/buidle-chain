from app.models.peer_node import PeerNode


class PeerNodeStore:
    nodes = [
        PeerNode(
            url = 'http://node1:5001',
            address = 'MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAznjoHvzCJtQcIYd3yj7vgwaPlyiG6U/Qlw1G89n0bNt5anvRe+e2eKzvpy98aj6ShGu7hARE9SxAFA9bIHCBqdAyPnrUaw7qGkeZNPHBByHe9prJSn0ZwBtfySOSbzdetO5aAwvLj5qMudW2PDz15mP2taGOvXqNnbcH78ZHQLvF6G+SbwuLHU5LEDSZlcy+CnvPqD67cg+QmJLneVmQfOBtbFHz3yDQghNrHWa+UCspUMHVGsDG6OEK7MSpPieY6TzBEYQWsikosQ+V0zBNrSCADe3GBcJ7XzafM/gb+gzJ1eP78F1sA6Ja4ZtqInqN406PwerAXaUJa2twW6529wIDAQAB'
        ),
        PeerNode(
            url = 'http://node2:5002',
            address = 'MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAxnrb17FTtrgfg33ADcbcb2D7mGX+sBIn6jE24ADNKbAvqRuhonnBJxG5W21xMyfP43P4JS8Kb/e6MsdS0D5cwnvRmsgYZdCL9CvzMJ7gYGpaQ174S3ocdTveYVaMnnZExh8OCvfdGFs5O+wdBJF11jhUmKaNAS45LWjYjou3db5oJdd87ISEHOmyB1UOp4bSIvF0EI5zHMS/kXE53t2W95PdsiXStj0HpzBp0C3jwzVLGDuyvALeC6ACg+9R6exBut8mjoDgL47m3/irFy0E2XEhmmRlpxH/hvFkGVvjMIEXBwdc+p1FDNQtGXEUkCWaBiQxNE+TE02qXlsQi6S+IwIDAQAB'
        ),
        PeerNode(
            url = 'http://node3:5003',
            address = 'MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEArb9KkrF/DTQJqiAcBUbKCaBmCl6bcueH1Oqyo62RKWbigalxBHdF2G7zoFWbIE7ko9hwK9CfcDIyeHcW4mFrM5NdlAtkdkh0TUsHoJwEBTbL891xdM/WWD8e0QG98eiHKfzDYprDFvvW79zRE7oUua+iCa2SLloWWx0j3S//KvZI935AzU3X5UfI+JC4+S7NPuv5X9fch38Yv6LfMNNxaOU12CApSbVTyFnIrhQh7zSgj5ezXpS3s8EOmAwFoOyydZWYzigCqBFNygzov1MyqIjovn2PkvKeNrAGC2qRW8X2rT3Nk+YMNAMlHUzIbkX71ovxG/Iqg21nEGXCVCywMwIDAQAB'
        )
    ]

    @classmethod
    def fetch_all_peer_nodes(cls):
        return cls.nodes
