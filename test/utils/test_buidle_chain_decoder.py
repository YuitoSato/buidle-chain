from unittest import TestCase

from app.utils.buidle_chain_decoder import decode_block_receive_request


class TestTransactionService(TestCase):
    def test_decode_block_receive_request(self):
        r1 = {
            'block': {
                'block_id': 'test_block_id',
                'block_number': 1,
                'previous_block_hash': 'test',
                'timestamp': 0,
                'merkle_root': 'test',
                'difficulty_target': 0,
                'nonce': 0,
                'transactions': []
            },
            'proof_result': {
                'result_hash_int': 0,
                'target_hash_int': 0,
                'nonce': 0
            },
            'sender_node_url': 'test',
            'tx_to_miner': {
                'transaction_id': 'test_tx_id',
                'tx_outputs': [],
                'tx_inputs': []
            }
        }

        r = {
            'sender_node_url': 'MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAznjoHvzCJtQcIYd3yj7vgwaPlyiG6U/Qlw1G89n0bNt5anvRe+e2eKzvpy98aj6ShGu7hARE9SxAFA9bIHCBqdAyPnrUaw7qGkeZNPHBByHe9prJSn0ZwBtfySOSbzdetO5aAwvLj5qMudW2PDz15mP2taGOvXqNnbcH78ZHQLvF6G+SbwuLHU5LEDSZlcy+CnvPqD67cg+QmJLneVmQfOBtbFHz3yDQghNrHWa+UCspUMHVGsDG6OEK7MSpPieY6TzBEYQWsikosQ+V0zBNrSCADe3GBcJ7XzafM/gb+gzJ1eP78F1sA6Ja4ZtqInqN406PwerAXaUJa2twW6529wIDAQAB',
            'block': { 'block_id': 'afb0d261079e9c96fe49f600748e3681bb17331f74cec08334884337e12e304a', 'transactions': [
                { 'tx_outputs': [{ 'amount': 99.0,
                    'transaction_output_id': '9b591161021fd1a857b70f63528b21ea8216b618fd4117289b5af6a8cfde3453',
                    'locking_script': '\r\x1cg\x88F¶UÏ»\x13\x9ev:;$úNR?a¶\x83#}\x17\x88»ÞI\x05kÏòiF@I»¬åJË\x8e¬\x1c\x9cÈò«\x80ìQ±@Aæµ%"\x10¿\x0btÑNfU\x1awýXðÀÃ5âÕ\'óÐ\\9\x8f¢Ù\xadsJ\x98î\x90ô\x10¹Z²OmÿS\x10ôÆúÐH¬\x98¶re\x84ZíËJ\x0bÛ³h_²ÏÛæÖ\x88\x9bZjsu\x12éV&=\x1ed²\\²Û¥ù,Íî¬!r³|\x10\x9e\tüSo¶=ºô5]\x9cQz\x06µZ*=|Ã\x85÷&JÅôÈ\x1a%Ùî)\x17.z\x85Pd\x14ÿyÂ#\r\x1exáé\x1eç\x0bG\x0b\x0c\x88\x03w\x9e-d³¤ \x82-¢\x1f+C2é¡Ü\x12ø«\x8fêd\x18ý¶\x15\x00NcüPµÓ\x8az¸\x98Ë>NÙ¡\x1e^',
                    'recipient_address': 'MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAxnrb17FTtrgfg33ADcbcb2D7mGX+sBIn6jE24ADNKbAvqRuhonnBJxG5W21xMyfP43P4JS8Kb/e6MsdS0D5cwnvRmsgYZdCL9CvzMJ7gYGpaQ174S3ocdTveYVaMnnZExh8OCvfdGFs5O+wdBJF11jhUmKaNAS45LWjYjou3db5oJdd87ISEHOmyB1UOp4bSIvF0EI5zHMS/kXE53t2W95PdsiXStj0HpzBp0C3jwzVLGDuyvALeC6ACg+9R6exBut8mjoDgL47m3/irFy0E2XEhmmRlpxH/hvFkGVvjMIEXBwdc+p1FDNQtGXEUkCWaBiQxNE+TE02qXlsQi6S+IwIDAQAB',
                    'sender_address': 'MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAznjoHvzCJtQcIYd3yj7vgwaPlyiG6U/Qlw1G89n0bNt5anvRe+e2eKzvpy98aj6ShGu7hARE9SxAFA9bIHCBqdAyPnrUaw7qGkeZNPHBByHe9prJSn0ZwBtfySOSbzdetO5aAwvLj5qMudW2PDz15mP2taGOvXqNnbcH78ZHQLvF6G+SbwuLHU5LEDSZlcy+CnvPqD67cg+QmJLneVmQfOBtbFHz3yDQghNrHWa+UCspUMHVGsDG6OEK7MSpPieY6TzBEYQWsikosQ+V0zBNrSCADe3GBcJ7XzafM/gb+gzJ1eP78F1sA6Ja4ZtqInqN406PwerAXaUJa2twW6529wIDAQAB' },
                    { 'amount': 1.0,
                        'transaction_output_id': 'de6332bf37cd847564de645cce1877ec7e9acd59408bbb1bc8acc787a8e6ef52',
                        'locking_script': 'coinbase_address', 'recipient_address': 'coinbase_address',
                        'sender_address': 'MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAznjoHvzCJtQcIYd3yj7vgwaPlyiG6U/Qlw1G89n0bNt5anvRe+e2eKzvpy98aj6ShGu7hARE9SxAFA9bIHCBqdAyPnrUaw7qGkeZNPHBByHe9prJSn0ZwBtfySOSbzdetO5aAwvLj5qMudW2PDz15mP2taGOvXqNnbcH78ZHQLvF6G+SbwuLHU5LEDSZlcy+CnvPqD67cg+QmJLneVmQfOBtbFHz3yDQghNrHWa+UCspUMHVGsDG6OEK7MSpPieY6TzBEYQWsikosQ+V0zBNrSCADe3GBcJ7XzafM/gb+gzJ1eP78F1sA6Ja4ZtqInqN406PwerAXaUJa2twW6529wIDAQAB' },
                    { 'amount': 9999900,
                        'transaction_output_id': '8a8f0b2b77afc72a66964bf40f062fbc7fcca64ef4ff5205aa2a35041d92318a',
                        'locking_script': "\x16\x84-\x0c\x97à\x89ëà\x1a^¡\\øùê?°2JÅ8\xa0s\x02z\x8e]PaûX¦?ðq¡t\x7fR\x99\x99ËxKô'Êèéw<\x9ahHÉ^êr\x88\x16\x88sM\x91vN\x9bµo¢3\x88@\x8f W~Õ\x1b¡£÷\x0b\x1c\x8a\x01f\x99\x9a\x8f3{Ü\x8fq\x900ø¢UKÖô¦(bv<Õ¸\x92wªd\x93Jñ\x12\x14¡\x89Ôä\x00'Î\x04*¡\x1dr¢68\x0b\x13·/\x9d3@y\x18ú\x0c7\x028\x98ÚBr6Jm±é1\x1a\x01©¡+ïBL\x04xw©ûÒ]\x8f¦ñ\\\x9aû\x8fÌ\rÕi(ù\x15d.\x1f,r8ZÕ¿½/\x1c\x93\x90gß0Iÿ¦P}W~\x8d\x1d<U¢%SU)\x14¾i\x9c\x9e¾\x9aµ\x05]I\\JÉ\x9c}\x81Ýw¼SìÝ&\x01$êu\x9b\x9dì\x06èÕ1",
                        'recipient_address': 'MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAznjoHvzCJtQcIYd3yj7vgwaPlyiG6U/Qlw1G89n0bNt5anvRe+e2eKzvpy98aj6ShGu7hARE9SxAFA9bIHCBqdAyPnrUaw7qGkeZNPHBByHe9prJSn0ZwBtfySOSbzdetO5aAwvLj5qMudW2PDz15mP2taGOvXqNnbcH78ZHQLvF6G+SbwuLHU5LEDSZlcy+CnvPqD67cg+QmJLneVmQfOBtbFHz3yDQghNrHWa+UCspUMHVGsDG6OEK7MSpPieY6TzBEYQWsikosQ+V0zBNrSCADe3GBcJ7XzafM/gb+gzJ1eP78F1sA6Ja4ZtqInqN406PwerAXaUJa2twW6529wIDAQAB',
                        'sender_address': 'MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAznjoHvzCJtQcIYd3yj7vgwaPlyiG6U/Qlw1G89n0bNt5anvRe+e2eKzvpy98aj6ShGu7hARE9SxAFA9bIHCBqdAyPnrUaw7qGkeZNPHBByHe9prJSn0ZwBtfySOSbzdetO5aAwvLj5qMudW2PDz15mP2taGOvXqNnbcH78ZHQLvF6G+SbwuLHU5LEDSZlcy+CnvPqD67cg+QmJLneVmQfOBtbFHz3yDQghNrHWa+UCspUMHVGsDG6OEK7MSpPieY6TzBEYQWsikosQ+V0zBNrSCADe3GBcJ7XzafM/gb+gzJ1eP78F1sA6Ja4ZtqInqN406PwerAXaUJa2twW6529wIDAQAB' }],
                    'tx_inputs': [{
                        'unlocking_script': 'a79HlQg8wbMhVVYlpQpPu+81Wbjjdqfo32JuLTQFBP+mLQzxu3I8MN4q/8n+WMPcII653Wzp0NM/j7kevip4GlRBWG4al1DrlcaUc2/cNv1mPNWG2gMCTTG6HAIzw8TU5zVRKTdXtewHpSjw28i2IzM0NeZZyZCQwxslDKn128xFKrTT49zjI0/tE0JmZarCENW6cYI6oYRReCCsafgtVMBuwzFN2vEX1WMrIdAF8N944buQIitJ4tBwS8jTgyHQlZ8zr1DWPaGyEtFXbHeAx59COQwcuQPazF3K2sWd/o6DmxuqRyo59TM4Hk84p2tQvJen+TUZEZwXMEy1MpNouw==',
                        'amount': 10000000,
                        'transaction_output_id': '38927c5472ba46709f43a750e666ddb1f218fb6b8ec3227a931328e119f8d6a7',
                        'transaction_input_id': '95836e4c1bfd11e9baaa0242ac140003' }],
                    'transaction_id': 'b53b531d5cf0e71e7fad116a54ad3b0bcbb06142680779c8139615c5e886c528' }],
                'nonce': 995617,
                'previous_block_hash': 'b5b3fa3f30c94d673bb255b7e755e5a58dcdce52e30544e40ca5f23f02ec2c95',
                'timestamp': 1547911162.000693, 'block_number': 2, 'difficulty_target': 20, 'merkle_root': ''
            },
            'proof_result': { 'nonce': 995617,
                'result_hash_int': 57625841494000262633660371648045959368632072447096640707399335526420641,
                'target_hash_int': 110427941548649020598956093796432407239217743554726184882600387580788736 },
            'tx_to_miner': { 'tx_outputs': [{ 'amount': 9900000.0,
                'transaction_output_id': '27496edc11383b2b3cacf20c3f49dcba241cf1ab2210b9073b84444a763dd1bf',
                'locking_script': "~÷p½ç\x90¸9ÿ`7¼ßV]¼N1\x1c×MÌ\x86ÔÎ»ºHi\x02ý!\x89\x1f_\x8evn\x94B«zò7+Õ@\x9dq\x1f9\x13¯6\tÈ×yÙwÁÝÙý\x13ne*Q\x0fô\x91ÏE8^ÏO®Tá×Üë\x1aN®\n\x0f\x97±\x87\x10BCrO8D°\x03\x90\x03N,Z\x9a\\Cm\x8fh\x1c4Ñu³\x931\x19)\x18u\x9e¶iç\x9ba\x9a\x1aü\x9eÅ3Åü¹7fû³¯p?øô\x0e çJ\x1b`tP\tn{\x13\x1aðn\x86F\x89ê¾!D¬Òù\x0cá·\x14t\x92?xí,\x82PJ'¯n>%/\x07t3!\x194á©2\x86ª\x07\x8bgWÌ\x86ÚÐx²%ÂºRsJ7«®\x1cæÔ´_Æ·ªx\x17¦¿\x99Ë.Ð×Ûy\x90F\nü\x8eØÔ\x9b\x8cü\x96\x85êJôQ",
                'recipient_address': 'MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAznjoHvzCJtQcIYd3yj7vgwaPlyiG6U/Qlw1G89n0bNt5anvRe+e2eKzvpy98aj6ShGu7hARE9SxAFA9bIHCBqdAyPnrUaw7qGkeZNPHBByHe9prJSn0ZwBtfySOSbzdetO5aAwvLj5qMudW2PDz15mP2taGOvXqNnbcH78ZHQLvF6G+SbwuLHU5LEDSZlcy+CnvPqD67cg+QmJLneVmQfOBtbFHz3yDQghNrHWa+UCspUMHVGsDG6OEK7MSpPieY6TzBEYQWsikosQ+V0zBNrSCADe3GBcJ7XzafM/gb+gzJ1eP78F1sA6Ja4ZtqInqN406PwerAXaUJa2twW6529wIDAQAB',
                'sender_address': 'coinbase_address' }], 'tx_inputs': [],
                'transaction_id': '1a1a5a57da2c7077720c762bf3867940a359ffd8775a9d771d387fbd639dcc5b'
            }
        }

        block_receive_request = decode_block_receive_request(r1)
        self.assertIsNotNone(block_receive_request.block.block_id)
