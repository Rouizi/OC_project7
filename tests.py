import unittest
from unittest.mock import patch, Mock
import app


class TestUrl(unittest.TestCase):

    @patch('app.classes.requests')
    # We mock the requests module
    def test_get_data_from_url(self, requests):
        response_mock = Mock()
        response_mock.json.return_value = {'candidates': [{'formatted_address': '7 Cité Paradis, 75010 Paris, France',
                                    'geometry': {'location': {'lat': 48.8748465, 'lng': 2.3504873}}}], 'status': 'OK'}
        requests.get.side_effect = [response_mock]

        assert app.classes.GoogleMap('openclassroom').get_adress_lat_lng() == ('7 Cité Paradis, 75010 Paris, France',
                                                                               48.8748465, 2.3504873)

    @patch('app.classes.wikipedia')
    # We mock the wikipedia module
    def test_get_history(self, wikipedia):
        history_mock = Mock()

        history_mock.return_value = "L'Hôtel Bourrienne (appelé aussi Hôtel de Bourrienne et Petit Hôtel Bourrienne)" \
                                     " est un hôtel particulier du XVIIIe siècle situé au 58 rue d'Hauteville dans le" \
                                     " 10e arrondissement de Paris. Propriété privée, il est classé au titre des" \
                                     " monuments historiques depuis le 20 juin 1927. En juillet 2015, il est acheté" \
                                     " par l'entrepreneur Charles Beigbeder pour en faire le siège de ses activités d'investissement."

        wikipedia.summary.side_effect = history_mock
        assert app.classes.HistoryFromWiki(48.8748465, 2.3504873).get_history_url()[0] == (
               "L'Hôtel Bourrienne (appelé aussi Hôtel de Bourrienne et Petit Hôtel Bourrienne) est un hôtel " 
               "particulier du XVIIIe siècle situé au 58 rue d'Hauteville dans le 10e arrondissement de Paris." 
               " Propriété privée, il est classé au titre des monuments historiques depuis le 20 juin 1927. En" 
               " juillet 2015, il est acheté par l'entrepreneur Charles Beigbeder pour en faire le siège de ses" 
               " activités d'investissement.")

unittest.main()