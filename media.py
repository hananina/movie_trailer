import webbrowser
import re

class Video():
	"""This class is parent class of Movie and Drama"""

	def __init__(self, release_date, valid_raitng):
		# Constant allways need to be capitarized
		self.release_date = release_date
		self.valid_raitng = valid_raitng

class Movie(Video):
	"""This class provides a way to store movie related information"""

	def __init__(self, release_date, valid_raitng, movie_title, movie_storyline, poster_image_url, trailer_youtube_id):
		Video.__init__(self, release_date, valid_raitng)
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image_url
		self.trailer_youtube_url = trailer_youtube_id
	

class Drama(Video):
	"""This class provides a way to store drama related information"""

	def __init__(self, release_date, valid_raitng, drama_title, drama_storyline, poster_image_url, trailer_youtube_id):
		Video.__init__(self, release_date, valid_raitng)
		self.title = drama_title
		self.storyline = drama_storyline
		self.poster_image_url = poster_image_url
		self.trailer_youtube_url = trailer_youtube_id
