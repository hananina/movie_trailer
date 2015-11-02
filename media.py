import webbrowser
import re

class Movie():
	# """This class provides a way to store movie related information"""
	# VALID_RATING = ["G", "PG", "PG-13","R"]

	def __init__(self, movie_title, movie_storyline, poster_image_url, trailer_youtube_id):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image_url
		self.trailer_youtube_url = trailer_youtube_id
	
	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)

