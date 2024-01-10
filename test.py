import random
import json

class MaClasse:
    def __init__(self, attribut1, attribut2):
        self.attribut1 = attribut1
        self.attribut2 = attribut2

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__)

    @classmethod
    def fromJSON(cls, json_str):
        json_dict = json.loads(json_str)
        return cls(**json_dict)

# Création d'un objet de la classe MaClasse
objet = MaClasse("valeur1", "valeur2")

# Convertir l'objet en format JSON
json_data = objet.toJSON()

# Écrire les données JSON dans un fichier
with open('objet.json', 'w') as f:
    f.write(json_data)

# Lire les données JSON depuis le fichier et re-créer l'objet
with open('objet.json', 'r') as f:
    loaded_data = f.read()
    nouvel_objet = MaClasse.fromJSON(loaded_data)

# Utilisation du nouvel objet chargé depuis le fichier JSON
print(nouvel_objet.attribut1)
print(nouvel_objet.attribut2)