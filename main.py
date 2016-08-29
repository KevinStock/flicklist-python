import webapp2
import cgi
import os
import jinja2

# Creating Jinja Environment
template_dir = os.path.join(
        os.path.dirname(__file__),
        "templates"
)
jinja_env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(template_dir)
)

# html boilerplate for the top of every page
# page_header = """
# <!DOCTYPE html>
# <html>
# <head>
#     <title>FlickList</title>
#     <style type="text/css">
#         .error {
#             color: red;
#         }
#     </style>
# </head>
# <body>
#     <h1>
#         <a href="/">FlickList</a>
#     </h1>
# """

# html boilerplate for the bottom of every page
# page_footer = """
# </body>
# </html>
# """


# a list of movies that nobody should be allowed to watch
terrible_movies = [
    "Gigli",
    "Star Wars Episode 1: Attack of the Clones",
    "Paul Blart: Mall Cop 2",
    "Nine Lives"
]


def getCurrentWatchlist():
    """ Returns the user's current watchlist """

    # for now, we are just pretending
    return [ "Star Wars", "Minions", "Freaky Friday", "My Favorite Martian" ]


class Index(webapp2.RequestHandler):
    """ Handles requests coming in to '/' (the root of our site)
        e.g. www.flicklist.com/
    """

    def get(self):
        movies = getCurrentWatchlist()
        template = jinja_env.get_template("edit.html")
        response = template.render(movies=movies)
        self.response.write(response)


class AddMovie(webapp2.RequestHandler):
    """ Handles requests coming in to '/add'
        e.g. www.flicklist.com/add
    """

    def post(self):
        # look inside the request to figure out what the user typed
        new_movie = self.request.get("new-movie")

        # if the user typed nothing at all, redirect and yell at them
        if (not new_movie) or (new_movie.strip() == ""):
            error = "Please specify the movie you want to add."
            self.redirect("/?error=" + cgi.escape(error, quote=True))

        # if the user wants to add a terrible movie, redirect and yell at them
        if new_movie in terrible_movies:
            error = "Trust me, you don't want to add '{0}' to your Watchlist".format(new_movie)
            self.redirect("/?error=" + cgi.escape(error, quote=True))

        # 'escape' the user's input so that if they typed HTML, it doesn't mess up our site
        new_movie_escaped = cgi.escape(new_movie, quote=True)

        # build response content
        new_movie_element = "<strong>" + new_movie_escaped + "</strong>"
        sentence = new_movie_element + " has been added to your Watchlist!"
        response = page_header + "<p>" + sentence + "</p>" + page_footer
        self.response.write(response)


class CrossOffMovie(webapp2.RequestHandler):
    """ Handles requests coming in to '/cross-off'
        e.g. www.flicklist.com/cross-off
    """

    def post(self):
        # look inside the request to figure out what the user typed
        crossed_off_movie = self.request.get("crossed-off-movie")

        if (crossed_off_movie in getCurrentWatchlist()) == False:
            # the user tried to cross off a movie that isn't in their list,
            # so we redirect back to the front page and yell at them

            # make a helpful error message
            error = "'{0}' is not in your Watchlist, so you can't cross it off!".format(crossed_off_movie)
            error_escaped = cgi.escape(error, quote=True)

            # redirect to homepage, and include error as a query parameter in the URL
            self.redirect("/?error=" + error_escaped)

        # if we didn't redirect by now, then all is well
        crossed_off_movie_element = "<strike>" + crossed_off_movie + "</strike>"
        confirmation = crossed_off_movie_element + " has been crossed off your Watchlist."
        response = page_header + "<p>" + confirmation + "</p>" + page_footer
        self.response.write(response)


app = webapp2.WSGIApplication([
    ('/', Index),
    ('/add', AddMovie),
    ('/cross-off', CrossOffMovie)
], debug=True)
