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
    def ajouterPokemon(self):
        with open('pokemon.json') as file:
            data = json.load(file)
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__)
    def ajouterDansPokedex(self,pokemon):
        json_data = pokemon.toJSON()
        # Écrire les données JSON dans un fichier
        with open("pokedex.json","a") as f:
            f.write(json_data)
            print("ajouté")
    def verif_pokedex(self,pokemon):
        with open("pokedex.json","r") as fichier:  
            if pokemon not in fichier.read():
                self.ajouterDansPokedex(pokemon)


# #pêchage des informations dans le fichier json
# with open('pokemon.json') as file:
#     data = json.load(file)

# # Création des objets Pokemon à partir des données JSON
# liste_pokemons = []
# for pokemon_data in data:
#     pokemon = Pokemon(pokemon_data['nom'], pokemon_data['vie'], pokemon_data['niveau'],
#                       pokemon_data['type'], pokemon_data['puissance'], pokemon_data['defense'],
#                       pokemon_data['image'])
#     liste_pokemons.append(pokemon)
    
pok=Pokemon("Flofo",40,1,"eau",1245, 0.90,"pikachu.png")
pok.verif_pokedex(pok)
# # Affichage des informations de chaque Pokémon créé
# for pokemon in liste_pokemons:
#     print(f"Nom : {pokemon.nom}, Vie : {pokemon.vie}, Niveau : {pokemon.niveau}, Type : {pokemon.type}, "
#           f"Puissance : {pokemon.puissance}, Defense : {pokemon.defense}, Image : {pokemon.image}")