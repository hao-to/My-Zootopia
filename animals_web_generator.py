import json


def load_json_data(file_path):
    """loads JSON-data from specified file path"""
    with open(file_path, "r") as handle:
        return json.load(handle)


def load_file_content(file_path):
    """loads the content of a text file and returns it as a string."""
    with open(file_path, "r") as file:
        return file.read()


def save_text_to_file(output_path, content):
    """saves text content to a specified file path."""
    with open(output_path, "w") as file:
        file.write(content)


def generate_animal_html(data):
    """loads html template, generates/inserts animal data as html and saves result in new HTML file."""

    # load html template using load_file_content function
    html_template = load_file_content('animals_template.html')

    # create html string for animal data to put in placeholder
    output = ""
    for animal in data:
        # start a new list item with the appropriate class
        output += '<li class="cards__item">\n'

        name = animal.get("name")
        characteristics = animal.get("characteristics", {})
        diet = characteristics.get("diet")
        locations = animal.get("locations")
        animal_type = characteristics.get("type")

        # add name as card title
        if name:
            output += f'<div class="card__title"> {name}</div>\n'

        # add other characteristics in card text
        output += '<p class="card__text">\n'

        if diet:
            output += f'<strong>Diet:</strong> {diet}<br/>\n'
        if locations:
            output += f'<strong>Location:</strong> {locations[0]}<br/>\n'
        if animal_type:
            output += f'<strong>Type: </strong>{animal_type}<br/>\n'
        output += '  </p>\n'

        # close the list item for this animal
        output += '</li>\n'

    # replace placeholder in HTML template with new string (output)
    print(output)
    html_content = html_template.replace('__REPLACE_ANIMALS_INFO__', output)

    # save generated HTML content to the specified output file
    save_text_to_file('animals.html', html_content)


def main():
    """Main function to load data, generate HTML, and save output."""
    # Load animal data from JSON file
    animals_data = load_json_data('animals_data.json')

    # Generate HTML and save it to a file
    generate_animal_html(animals_data)


# Run the main function only if this script is executed directly
if __name__ == "__main__":
    main()
