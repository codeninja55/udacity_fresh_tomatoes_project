#
#
# Class Movie
# Constructor:
# __init__(self)
# Instance Variables:
# title, storyline, poster_image_url, youtube_trailer_url
# Instance Methods:
# show_trailer
#

import webbrowser

# Parent class
class Motion_Picture():
    __module__ = "media_udacity"
    """ This parent class provides a way to store motion picture related
    information """

    # Class constructor which initializes the picture title, post image url
    # and the duration of film/show.
    def __init__(self, title, poster_image_url):
        self.title = title
        self.poster_image_url = poster_image_url

    def show_info(self):
        print("Title: " + self.title)
        print("Poster: " + self.poster_image_url)


class Movie(Motion_Picture):
    """ This child class of Motion_Picture provides a way to store movie
    related information

    This class further adds instance variables to the class that includes:
    - storyline: a storyline about the movie
    - trailer_youtube_url: A URL link to the trailer from YouTube.

    Instance methods include:
    - show_info(): overrides the parent class method show_info() and
    further prints the storyline instance variable.
    - show_trailer(): opens a web browser and follows the url link of the
    instance variable trailer_youtube_url. """

    VALID_RATINGS = ["G", "PG", "M", "MA", "R"]

    # Constructor inheritance - the child class constructor that inherits
    # class variables from the parent such as title, poster image url,
    # and duration.
    def __init__(self, title, poster_image_url,
                 storyline, trailer_youtube_url):
        Motion_Picture.__init__(self, title, poster_image_url)
        self.storyline = storyline
        self.trailer_youtube_url = trailer_youtube_url

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

    # @Override parent method
    def show_info(self):
        print("Title: " + str(self.title))
        print("Poster: " + self.poster_image_url)
        print("Storyline: " + str(self.storyline))


        # class Tv_Show(Motion_Picture):
        # def __init__ (self)
        # Motion_Picture.__init__(self, title, poster_image_url)
        #
