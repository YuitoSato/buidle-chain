import json
import sys
from datetime import datetime

import requests

from app.models.transaction_output import TransactionOutput
from app.utils.buidle_chain_decoder import decode_tx_output
from base64 import b64decode, b64encode
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5

URL = 'http://localhost:5001/'
HEADERS = { 'content-type': 'application/json' }
PUBLIC_KEY_STR = "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAznjoHvzCJtQcIYd3yj7vgwaPlyiG6U/Qlw1G89n0bNt5anvRe+e2eKzvpy98aj6ShGu7hARE9SxAFA9bIHCBqdAyPnrUaw7qGkeZNPHBByHe9prJSn0ZwBtfySOSbzdetO5aAwvLj5qMudW2PDz15mP2taGOvXqNnbcH78ZHQLvF6G+SbwuLHU5LEDSZlcy+CnvPqD67cg+QmJLneVmQfOBtbFHz3yDQghNrHWa+UCspUMHVGsDG6OEK7MSpPieY6TzBEYQWsikosQ+V0zBNrSCADe3GBcJ7XzafM/gb+gzJ1eP78F1sA6Ja4ZtqInqN406PwerAXaUJa2twW6529wIDAQAB"
SECRET_KEY_STR = "MIIEogIBAAKCAQEA4JL8ek8HCgS6yvTSjog/pfB7vc693fB1AA+8kBRchj51ktejPrR5mRpoMJwzBcgal9sAgLjj1gOa9pLReCfTRWuO+M0BiRJac1ebtAY5/A3dR52fE7U47/Agmm3qjL1Wqr3dbckrwgAHioA7RqhWqPQCl1m3qL66T9YlmvJxICzWX5+9ZQEcxSSyKT5gSBOoCWpE1aJlf8g6xoYSxRoTkES6AXDlYQh63eNeWIZXrOsf/0GEAlYxmLTh5QvNfIbN+Txck913ZP1DX8oQHJC4NKQNwAB+I0BovgJ71aFt3V7CeUN1+dYLbp/UcILfiZEyrbL1cRX6KHXH4HP/RTyjQwIDAQABAoIBAAdhjV7PviF8Kk+FYG5C2CSyFL8WTnM+9fl8iuwJX0kiQGcFI15qPBzmG0qNt7eW7hjTn96bNRHRqIQ2KyBR3sXHVTmkM0q4CbUEyh9OnRVFt2IlMhdJu4dXUxsARdc+WdzexKpZFFEaAyVwNYKLAd4ntvYWgszPB/ybwzymf0VZZCbJM1oHj2/CJpUT7ywCcd1Gs1JjUvpz9qxnGe32IfaOdzerDYI2hlpqO27A5ZboJxG1uGFHzkJHIN7bfFCbH+2CdAqMyUrC66SGCJ/o6bVuSHgC/qKpIzUOImkFWTv4IBNI89TrSasMJAwsXn97CuuxLJeecJOlwQQ/B/h7hrECgYEA64LjRVsjqD2iQwxhH8nkcIsMDQOkLc7XklDecU60+f/B5o22EHmBbi/FuYR9J8rRAfDfHtIsYQpkoaBS8+aTV+Jvwo/dFoquJcVGP2CyIEs5K4wQfXzU6+z3sMVVdQvwyy3VhkDzXeEVgMWowJ9D/ErK4oNUZUUAj1+HHZh+znUCgYEA9ByEHkfLsPxEl5zr9Z/7psTlomrBcT2LgLh5elqTso9FhuXK2u8hP2+IJn5s+qmPivAaXL/yuUBr7NagOlFStuewm1KUuGEO46vnv90zvAA8yEJDW33M9Ys8xe9JFtlZhMttFzH6YLygikzpfcY56Uj8e2vZzbATcr1LdZSOY9cCgYBRhRvgHP0JtlPdO4K++yZconTIaHNC++74kY99zw2r35Chmnnj1/sqRdT+M1MTHAwezN6ej4eXC37rx1APZsenyxR+V0fjDpvbLR70vybJMOCYJ0Jp/XTCOWM/R/8dpcVyvunDL+ZNn6TOzxxrmHVy9fymTWlAKJNaDWn6n5d9JQKBgFNdTa09nY1CiXYxa8+FJB6uzTErPgabGwIJfcrQFfJ7xSWtYhpkYblVMGzc7gCoWVH8bzRPhOfI3VKTdUKVNScrdn+Esy9IThpoQYufUiSY/CjzoCcljhIoy8dY0WARN+YGxqmOMtBIepbgbzi5sls9xqOrkEUTJYEgrh1obzwfAoGAUTnh1a2JBME7XnhtLIoEFouLSR3YIfqbm6Vfay8+rjfLKZAbvwJhwdjkE3Jqz2Y/WdgXbd9rA55K1ye+vcNq0BXpEMCMlTqvdNYUrxlXvS9HjqobytFFMPDQ3e4tYFatVA4mfAXRIn1t0azSsjwBl6Lh8N5PnJ6fBCIyFunJGz0="


def fetch_utxo():
    data = {
        'address': PUBLIC_KEY_STR
    }
    res = requests.post(URL + 'transactions/utxo', data = json.dumps(data), headers = HEADERS)
    return list(map(lambda tx_o_dict: decode_tx_output(tx_o_dict), res.json()))


def sign(secret_key, data, passphrase = None):
    try:
        secret_key = \
            '-----BEGIN PUBLIC KEY-----\n' \
            + secret_key \
            + '\n-----END PUBLIC KEY-----'
        rsakey = RSA.importKey(secret_key, passphrase = passphrase)
    except ValueError as e:
        print(e)
        sys.exit(1)
    signer = PKCS1_v1_5.new(rsakey)
    digest = SHA256.new()
    encoded = (data + ('/' * (-len(data) % 4))).encode('utf-8')
    b64decoded = b64decode(encoded)
    digest.update(b64decoded)

    sign = signer.sign(digest)
    return b64encode(sign).decode('utf-8')


def create_tx_input_requests(tx_outputs):
    return list(map(lambda tx_o: {
        'transaction_output_id': tx_o.transaction_output_id,
        'unlocking_script': sign(SECRET_KEY_STR, tx_o.transaction_output_id)
    }, tx_outputs))


if __name__ == '__main__':
    if sys.argv is not None and sys.argv[1] is not None:
        amount = int(sys.argv[1])
        recipient_address = sys.argv[2]

        utxo = fetch_utxo()
        target_utxo = TransactionOutput.fetch_tx_outputs_over_amount(amount, utxo)
        tx_input_requests = create_tx_input_requests(target_utxo)
        request = {
            'sender_address': PUBLIC_KEY_STR,
            'recipient_address': recipient_address,
            'amount': amount,
            'timestamp': datetime.now().timestamp(),
            'tx_input_requests': tx_input_requests
        }
        res = requests.post(
            URL + 'transactions',
            data = json.dumps(request),
            headers = HEADERS
        )
        print(res)
