import json

class CreerPokemon:
    def __init__(self):
        self.nom=""
        self.vie =0
        self.niveau=0
        self.type=" " 
        self.puissance=0
        self.defense=0
        self.image =""
        self.cree=True
        self.liste_creation=[]

    def creation(self):
        if self.cree:
            self.nom=input("Nom : ")
            self.vie=input("vie: ")
            self.niveau= input("niveau: ") 
            self.type= input("type: ") 
            self.puissance=input("puissance: ")
            self.defense=input("defense: ")
            self.image = input("image: ")

            with open("pokedex.json","a")as file:
                json.dump (print(f"Nom : {self.nom}, Vie : {self.vie}, Niveau : {self.niveau}, Type : {self.type}, " f"Puissance : {self.puissance}, Defense : {self.defense}, Image : {self.image}"),file)
fef=CreerPokemon()
fef.creation()


    


        