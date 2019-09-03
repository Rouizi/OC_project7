import unittest
from unittest.mock import patch, Mock
import app


class TestUrl(unittest.TestCase):

    @patch('app.classes.requests')
    def test_get_data_from_url(self, requests):
        response_mock = Mock()
        response_mock.json.return_value = {'candidates': [{'formatted_address': '7 Cité Paradis, 75010 Paris, France',
                                    'geometry': {'location': {'lat': 48.8748465, 'lng': 2.3504873}}}], 'status': 'OK'}
        requests.get.side_effect = [response_mock]

        assert app.classes.GoogleMap('openclassroom').get_adress_lat_lng() == ('7 Cité Paradis, 75010 Paris, France',
                                                                               48.8748465, 2.3504873)

unittest.main()