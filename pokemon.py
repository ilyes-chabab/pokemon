import json
class Pokemon: #class qui prends les caractéristique du pokemon
    def __init__(self,nom,vie,niveau,type,puissance,defense,image):
        self.nom=nom
        self.vie=vie 
        self.niveau= niveau 
        self.type= type 
        self.puissance=puissance
        self.defense=defense
        self.image = image
    def setNom(self):
        return self.nom
    def getVie(self,nouvelleVie):
        self.vie = nouvelleVie

poussifeu=Pokemon("Poussifeu",40,1,"feu",14,0.80,"poussifeu.png")
print(poussifeu.setNom())
print(f"Nom : {poussifeu.nom}, Vie : {poussifeu.vie}, Niveau : {poussifeu.niveau}, Type : {poussifeu.type}, "
        f"Puissance : {poussifeu.puissance}, Defense : {poussifeu.defense}, Image : {poussifeu.image}")