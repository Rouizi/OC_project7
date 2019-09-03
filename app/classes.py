import requests


"""def get_data_from_url():
    r = requests.get("https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input="
                     "openclassroom?&inputtype=textquery&fields=formatted_address,"
                     "geometry/location&key=AIzaSyDqAzPXNIxR8TB9qhpda8MsnLj5JCDPiqs")
    r_json = r.json()
    formatted_address = r_json['candidates'][0]['formatted_address']
    lat = r_json['candidates'][0]['geometry']['location']['lat']
    lng = r_json['candidates'][0]['geometry']['location']['lng']
    return formatted_address, lat, lng"""

class GoogleMap:

    def __init__(self, content):
        self.content = content #"Salut GrandPy ! Est-ce que tu connais l'adresse d'openclassroom?"

    def get_adress_lat_lng(self):
        content = self.content.split(' ') #['GrandPy', '!', 'Est-ce', 'que', 'tu', 'connais', "l'adresse", "d'OpenClassrooms", '?']
        url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=" + self.content +\
                          "&inputtype=textquery&fields=formatted_address,geometry/location&key=AIzaSyDqAzPXNIxR8TB9qhpda8MsnLj5JCDPiqs"

        index = 0
        check = True
        while check:
            r = requests.get(url)
            print(type(r))
            r_json = r.json()
            if r_json['status'] == 'OK':
                formatted_address = r_json['candidates'][0]['formatted_address']
                lat = r_json['candidates'][0]['geometry']['location']['lat']
                lng = r_json['candidates'][0]['geometry']['location']['lng']
                return formatted_address, lat, lng
            if len(content) > 0:
                #if the url does not give any result we remove the first word and then we retest then the second and so
                # on. If no result is found by removing all the words we start again but we remove the last one and so on
                content.pop(index)
                if len(content) == 0 and index == -1:
                    return ("Je n'ai trouvé aucun resultat pour ton adresse")
                if len(content) == 0:
                    index = -1
                    content = self.content.split(' ')
                url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=" + ' '.join(content) +\
                          "&inputtype=textquery&fields=formatted_address,geometry/location&key=AIzaSyDqAzPXNIxR8TB9qhpda8MsnLj5JCDPiqs"

"""requests = Mock()


class TestUrl(unittest.TestCase):
    def test_get_data_from_url(self):
        response_mock = Mock()
        response_mock.json.return_value = {'candidates': [{'formatted_address': '7 Cité Paradis, 75010 Paris, France', 'geometry': {'location': {'lat': 48.8748465, 'lng': 2.3504873}}}], 'status': 'OK'}
        requests.get.side_effect = [response_mock]

        assert GoogleMap('openclassroom').get_adress_lat_lng() == ('7 Cité Paradis, 75010 Paris, France', 48.8748465, 2.3504873)

unittest.main()"""


g = GoogleMap("Salut GrandPy ! Est-ce que tu connais l'adresse d'openclassroom?")
a = g.get_adress_lat_lng()
print(a)
