class Pokemon: #class qui prends les caractéristique du pokemon
    def __init__(self,nom,vie,niveau,type,puissance,defense):
        self.nom=nom
        self.vie=vie 
        self.niveau= niveau 
        self.type= type 
        self.puissance=puissance
        self.defense=defense
    def setNom(self):
        return self.nom
    def getVie(self,nouvelleVie):
        self.vie = nouvelleVie
        