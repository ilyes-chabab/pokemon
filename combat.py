from pokemon import Pokemon
class Combat:   
    def typePuissance(self,joueur,ennemi):
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
    def attaque(self,joueur,ennemi):
        attaque= self.typePuissance(joueur,ennemi) * ennemi.defense
        ennemi.vie -= attaque
        Pokemon.getVie(self,ennemi.vie)
        print(f"{ennemi.nom} a perdu {attaque} pv")
        print(f"{ennemi.nom} a {ennemi.vie}")
    def gagnant(self,joueur,ennemi):
        if joueur.vie < 0:
            print(f"{ennemi.nom} a gagné.")
            print(f"vous avez perdu :( ")
        if ennemi.vie < 0:
            print(f"vous avez gagné ! :)")
            print(f"{ennemi.nom} a perdu. ")

    def lancerCombat(self):
        joueur1=Pokemon("pika",20,1,"feu",5,0.80)
        joueur2=Pokemon("pi",20,1,"sol",6,0.70)
        while True:
            if joueur2.vie >0:
                self.attaque(joueur1,joueur2)
            if joueur1.vie >0:
                self.attaque(joueur1,joueur2)
            else:             
                self.gagnant(joueur1,joueur2)
                break
combat = Combat()
combat.lancerCombat()


