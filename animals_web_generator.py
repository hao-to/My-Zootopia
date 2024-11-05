animals_data = [
  {
    "name": "American Foxhound",
    "taxonomy": {
      "kingdom": "Animalia",
      "phylum": "Chordata",
      "class": "Mammalia",
      "order": "Carnivora",
      "family": "Canidae",
      "genus": "Canis",
      "scientific_name": "Canis lupus"
    },
    "locations": [
      "North-America"
    ],
    "characteristics": {
      "distinctive_feature": "Long legs and wide, flat ears",
      "temperament": "Mix of affectionate, loving, and stubborn",
      "training": "Medium",
      "diet": "Omnivore",
      "average_litter_size": "7",
      "type": "Hound",
      "common_name": "American Foxhound",
      "slogan": "Sweet, kind, loyal, and very loving!",
      "group": "Dog",
      "color": "BlackWhiteTan",
      "skin_type": "Hair",
      "lifespan": "10 to 12 years"
    }
  },
  {
    "name": "Arctic Fox",
    "taxonomy": {
      "kingdom": "Animalia",
      "phylum": "Chordata",
      "class": "Mammalia",
      "order": "Carnivora",
      "family": "Canidae",
      "genus": "Vulpes",
      "scientific_name": "Vulpes lagopus"
    },
    "locations": [
      "Eurasia",
      "Europe",
      "North-America"
    ],
    "characteristics": {
      "main_prey": "Lemmings, voles, hares, other small rodents, berries, insects",
      "name_of_young": "kit",
      "distinctive_feature": "Thick fur that changes colour with season",
      "habitat": "Polar forest regions",
      "predators": "Snowy Owl, Wolf, Polar Bear",
      "diet": "Carnivore",
      "average_litter_size": "5",
      "lifestyle": "Solitary",
      "favorite_food": "Lemmings",
      "type": "Mammal",
      "slogan": "Extremely thick winter fur!",
      "color": "GreyBlackWhite",
      "skin_type": "Fur",
      "top_speed": "30 mph",
      "lifespan": "7 - 10 years",
      "weight": "1.4kg - 9.4kg (3lbs - 21lbs)",
      "length": "70cm - 110cm (28in - 43in)"
    }
  }]


def get_animal_data():
  for animal in animals_data:
    name = animal.get("name")
    characteristics = animal.get("characteristics", {})  # extracting info from characteristics-Dict
    diet = characteristics.get("diet")
    location = animal.get("locations")
    animal_type = characteristics.get("type")  # extracting info from characteristics-Dict
    if name:
      print(f"Name: {name}")
    if diet:
      print(f"Diet: {diet}")
    if location:  # Überprüfen, ob `locations` existiert und nicht leer ist
      print(f"Location: {location[0]}")
    if animal_type:
      print(f"Type: {animal_type}")
    print()  # print new line


get_animal_data()

get_animal_data()

# expected output:
# Name: American
# Foxhound
# Diet: Omnivore
# Location: North - America
# Type: Hound
