import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

animals_data = load_data('animals_data.json')


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
    if location:  # checking if `locations` exists and is not empty
      print(f"Location: {location[0]}")
    if animal_type:
      print(f"Type: {animal_type}")
    print()  # print new line for better readability


get_animal_data()