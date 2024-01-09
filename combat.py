from pokemon import Pokemon
import random
class Combat:   
    def typePuissance(self,joueur,ennemi): 
        #methode qui augmente ou diminue la puissance d'attaque du pokemon en fonction des types des 2 pokemon
        if joueur.type == "eau":
            if ennemi.type == "eau":
                return joueur.puissance * 1
            if ennemi.type == "feu":
                return joueur.puissance * 2
            if ennemi.type == "sol":
                return joueur.puissance * 0.5
            if ennemi.type == "normal":
                return joueur.puissance * 1
        if joueur.type == "feu":
            if ennemi.type == "eau":
               return joueur.puissance * 0.5
            if ennemi.type == "feu":
                return joueur.puissance * 1
            if ennemi.type == "sol":
                return joueur.puissance * 2
            if ennemi.type == "normal":
                return joueur.puissance * 1
        if joueur.type == "sol":
            if ennemi.type == "eau":
                return joueur.puissance * 2
            if ennemi.type == "feu":
                return joueur.puissance * 0.5
            if ennemi.type == "sol":
                return joueur.puissance * 1
            if ennemi.type == "normal":
                return joueur.puissance * 1
        if joueur.type == "normal":
            if ennemi.type == "eau":
                return joueur.puissance * 1
            if ennemi.type == "feu":
                return joueur.puissance * 1
            if ennemi.type == "sol":
                return joueur.puissance * 1
            if ennemi.type == "normal":
                return joueur.puissance * 1 
    def attaqueLouper(self):
        chiffre=random.randint(1,20)#5% de chance de louper son attaque
        print(chiffre)
        return chiffre
    def attaque(self,joueur,ennemi):  #methode qui diminue la puissance d'attaque vis-a-vis de la defense de l'ennemi

        if self.attaqueLouper() == 1: # il y a 1 chance sur 20 de louper son attaque
            print(f"{joueur.nom} a loupé son attaque .")
        else: #sinon le script prend l'attaque en fonction des deux type et le multiplier a la defense de l'ennemi (c'est un nombre inferieur a 1)
            attaque= self.typePuissance(joueur,ennemi) * ennemi.defense
            attaque =round(attaque) # ca arrondi l'attaque. (ex: 1,75 --> 2)
            ennemi.vie -= attaque #ca deduit les pv en fonction de la puissance
            Pokemon.getVie(self,ennemi.vie)#ca met a jour les pv du pokemon en temps reel
            print(f"{ennemi.nom} a perdu {attaque} pv. total des pv :{ennemi.vie}")
    def gagnant(self,joueur,ennemi):
        #Methode qui regard a chaque fin de tour si l'un des pokemon n'a plus de pv pour annoncer le gagnant et le perdant
        if joueur.vie <= 0:
            print(f"{ennemi.nom} a gagné.")
            print(f"vous avez perdu :( ")
        if ennemi.vie <= 0:
            print(f"vous avez gagné ! :)")
            print(f"{ennemi.nom} a perdu. ")
    
    def lancerCombat(self):
        joueur1=Pokemon("pika",20,1,"sol",5,0.80)
        joueur2=Pokemon("sabelette",20,1,"feu",6,0.70)
        while True:
            if joueur2.vie >0:
                if joueur1.vie >0:
                    self.attaque(joueur1,joueur2)
                else:             
                    self.gagnant(joueur1,joueur2)
                    break
            if joueur1.vie >0:
                if joueur2.vie >0:
                    self.attaque(joueur2,joueur1)
                else:             
                    self.gagnant(joueur1,joueur2)
                    break
            
combat = Combat()
combat.lancerCombat()


