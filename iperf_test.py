import parser

class TestSuite:
    def test_iperf3_client_connection(self, client):
        assert client.stderr == '', f"Error: {client.stderr}"

        parsed_result = parser.parse_iperf_output(client.stdout)

        assert parsed_result is not None, "Parsing failed"

        transfer = parsed_result['Transfer']
        bitrate = parsed_result['Bitrate']

        assert transfer > 2, f"Transfer is too low: {transfer} MB"
        assert bitrate > 20, f"Bitrate is too low: {bitrate} Mbit/s"
