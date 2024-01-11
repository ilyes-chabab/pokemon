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
#pêchage des informations dans le fichier json
with open('pokedex.json') as file:
    data = json.load(file)

# Création des objets Pokemon à partir des données JSON
liste_pokemons = []
for pokemon_data in data:
    pokemon = Pokemon(pokemon_data['nom'], pokemon_data['vie'], pokemon_data['niveau'],
                      pokemon_data['type'], pokemon_data['puissance'], pokemon_data['defense'],
                      pokemon_data['image'])
    liste_pokemons.append(pokemon)
# Affichage des informations de chaque Pokémon créé
for pokemon in liste_pokemons:
    print(f"Nom : {pokemon.nom}, Vie : {pokemon.vie}, Niveau : {pokemon.niveau}, Type : {pokemon.type}, "
          f"Puissance : {pokemon.puissance}, Defense : {pokemon.defense}, Image : {pokemon.image}")