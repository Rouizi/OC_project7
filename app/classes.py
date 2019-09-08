import requests
import wikipedia
from app import app

adress_found = [
            "Bien sûr mon poussin ! Voici l'adresse: ",
            "Mais oui mon p'tit, tiens mon neurone vient de démarrer, voici l'adresse: ",
            "Oh oui, je m'en souviens bien, et hop, l'adresse: ",
            "Aussitôt demandé, aussitôt trouvé ! Ce que tu cherches est au ",
            "Ouh, ça fait un bail ! Mais si ma mémoire est bonne l'adresse est celle ci: "
        ]
adress_not_foud = [
            "Oh, j'ai beau réfléchir, je ne me souviens plus de cette adresse ...",
            "Oh la la ! Je suis un peu confus. Tu peux me faire une demande plus claire et directe ?",
            "Dis-moi ça plus clairement s'il te plait !",
            "Ça ne me dit rien, pourrais-tu être plus clair ?",
            "Je n'ai pas compris ! Que dis-tu ?"
            ]
relate = [
        "En parlant de ça, j'avais une petite chose à te raconter ... ",
        "D'ailleurs, cela me rappelle quelque chose ... ",
        "Souvenir, souvenir ! Je me souviens de cet endroit. En voici l'histoire: ",
        "Je connais très bien ce lieu. GrandPy Bot va te conter son histoire... ",
        "Sa te dirais une petite histoire sur ce lieu ... "
        ]
no_relate = [
            "Oh ! Je n'ai plus les idées claires, j'ai oublié l'histoire à ce sujet.",
            "Désolé mais je n'ai pas d'histoire intéressante à ce sujet.",
            "Pardon mais je connais mal l'histoire de cet endroit.",
            "Euh je crois avoir oublié l'histoire sur cet endroit !",
            "Je devrais réviser un peu les cours d'histoires..."
            ]


class GoogleMap:

    def __init__(self, content):
        self.content = content #"Salut GrandPy ! Est-ce que tu connais l'adresse d'openclassroom?"

    def get_adress_lat_lng(self):
        content = self.content.split(' ') #['GrandPy', '!', 'Est-ce', 'que', 'tu', 'connais', "l'adresse", "d'OpenClassrooms", '?']
        payload = {
            "input": self.content,
            "inputtype": "textquery",
            "fields": "formatted_address,geometry/location",
            "key": app.config['GOOGLE_MAP_KEY']
        }
        url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json"

        index = 0
        check = True
        while check:
            r = requests.get(url, params=payload)
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
                    return None
                if len(content) == 0:
                    index = -1
                    content = self.content.split(' ')
                payload = {
                    "input": ' '.join(content),
                    "inputtype": "textquery",
                    "fields": "formatted_address,geometry/location",
                    "key": app.config['GOOGLE_MAP_KEY']
                }
                url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json"


class HistoryFromWiki:

    def __init__(self, lat, lng):
        self.lat = lat
        self.lng = lng

    def get_history_url(self):
        wikipedia.set_lang("fr")

        try:
            place = wikipedia.geosearch(latitude=self.lat, longitude=self.lng, results=1)
            url = wikipedia.page(place[0]).url
            history = wikipedia.summary(place[0])
            return history, url
        except wikipedia.exceptions.PageError:
            return
        except wikipedia.exceptions.DisambiguationError:
            return
        except wikipedia.exceptions.WikipediaException:
            return
        except IndexError:
            return

"""28.033886, 1.659626
g = GoogleMap("papay")
results = g.get_adress_lat_lng()
print(results)"""
"""h = HistoryFromWiki(28.033886, 1.659626)
print(h.get_history_url())"""


