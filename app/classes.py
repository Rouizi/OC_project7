import requests


class GoogleMap:

    def __init__(self, url, content):
        self.url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=" + self.content +\
                          "&inputtype=textquery&fields=formatted_address,geometry/location&key=AIzaSyDqAzPXNIxR8TB9qhpda8MsnLj5JCDPiqs"
        self.content = "Salut GrandPy ! Est-ce que tu connais l'adresse d'openclassroom?"

    def get_lat_lng(self):
        content = self.content
        self.content = self.content.split(' ')

        r = requests.get(self.url)
        r_json = r.json()
        status = r_json['status']
        formatted_address = r_json['candidates'][0]['formatted_address']
        lat = r_json['candidates'][0]['geometry']['location']['lat']
        lng = r_json['candidates'][0]['geometry']['location']['lng']