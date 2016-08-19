import webapp2
#import random

class Index(webapp2.RequestHandler):

	html_head = """
		<!doctype html>
		<html>
		<head>
			<title>FlickListly</title>
		</head>
		<body>

	"""

	html_tail = """
			</body>
		</html>
	"""

#
#     def getRandomMovie(self):
#
#         # list of movies to select from
#         movies = ["The Big Lebowski", "Blue Velvet", "Toy Story", "Star Wars", "Amelie"]
#
#         # randomly choose one of the movies
#         randomIdx = random.randrange(len(movies))
#
#         return movies[randomIdx]
#
#     def get(self):
#         # add Movie of the Day to the response string
#         movie = self.getRandomMovie()
#         response = "<h1>Movie of the Day</h1>"
#         response += "<p>" + movie + "</p>"
#
#         # add Tomorrow's Movie to the response string
#         tomorrow_movie = self.getRandomMovie()
#         response += "<h1>Tomorrow's Movie</h1>"
#         response += "<p>" + tomorrow_movie + "</p>"
#
#         self.response.write(response)

	def get(self):
		html_form = """
			<form id="add_form" action="/addmovie" method="POST">
				<label for="add_form_title">Movie Title</label>
				<input type="text" id="add_form_title" name="movieTitle" />
				<input type="submit" />
			</form>
		"""
		self.response.write(html_head + html_form + html_form)

class AddMovie(webapp2.RequestHandler):
	### handle adding movies
	###

	def post(self):
		self.response.write(str(self.request))


app = webapp2.WSGIApplication([
    ('/', Index),
    ('/addmovie', AddMovie)
], debug=True)
