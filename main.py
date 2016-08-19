import webapp2
import random

class Index(webapp2.RequestHandler):

    def getRandomMovie(self):

        # TODO: make a list with at least 5 movie titles
        movie_list = ['Suicide Squad', 'Batman v Superman', 'Mad Max', 'Star Trek Beyond', 'The Legend of Tarzan', 'The Nice Guy', 'Captain America: Civil War']

        # TODO: randomly choose one of the movies, and return it
        randnum = random.randint(0, len(movie_list) - 1)

        return movie_list[randnum]

    def get(self):
        movie = self.getRandomMovie()
        second_movie = self.getRandomMovie()

        # build the response string
        response = "<h1>Movie of the Day</h1>"
        response += "<p>" + movie + "</p>"

        # TODO: pick a different random movie, and display it under
        # the heading "<h1>Tommorrow's Movie</h1>"
        response += "<h1>Tomorrow's Movie</h1>"
        response += "<p>" + second_movie + "</p>"


        self.response.write(response)

app = webapp2.WSGIApplication([
    ('/', Index)
], debug=True)
