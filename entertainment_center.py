import media_udacity
import fresh_tomatoes
import os
import json

def create_movies_list():
    mcu = []

    # opens the json file with the stored movies in it.
    with open("movies_db.json", "r") as file:
        # loads the json file and outputs it as a dict
        movies_dict = json.load(file)

        # iterates over the json file and creates a Movie object. It then
        # appends the object to the mcu empty list.
        for m in movies_dict['movies_db']:
            mcu.append(media_udacity.Movie(str(m['title']),
                                           m['poster_image_url'],
                                           str(m['storyline']).encode('utf-8'),
                                           m['youtube_url']))

        file.close()

        # uses the open_movies_page method in the fresh_tomatoes module. This
        # takes the mcu list and adds it to the HTML page.
        fresh_tomatoes.open_movies_page(mcu)

create_movies_list()
