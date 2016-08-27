import webapp2
import cgi
import jinja2
import os


# set up jinja
template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir))


# load some templates
t_page_header = jinja_env.get_template("page-header.html")
t_page_footer = jinja_env.get_template("page-footer.html")


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
        t_edit = jinja_env.get_template("edit.html")

        main_content = t_edit.render(
                        watchlist = getCurrentWatchlist(),
                        error = self.request.get("error"))
        page_header = t_page_header.render(title="FlickList")
        page_footer = t_page_footer.render()

        response = page_header + main_content + page_footer
        self.response.write(response)


class AddMovie(webapp2.RequestHandler):
    """ Handles requests coming in to '/add'
        e.g. www.flicklist.com/add
    """

    def post(self):
        new_movie = self.request.get("new-movie")

        # if the user typed nothing at all, redirect and yell at them
        if (not new_movie) or (new_movie.strip() == ""):
            error = "Please specify the movie you want to add."
            self.redirect("/?error=" + cgi.escape(error))

        # if the user wants to add a terrible movie, redirect and yell at them
        if new_movie in terrible_movies:
            error = "Trust me, you don't want to add '{0}' to your Watchlist.".format(new_movie)
            self.redirect("/?error=" + cgi.escape(error, quote=True))

        # 'escape' the user's input so that if they typed HTML, it doesn't mess up our site
        new_movie_escaped = cgi.escape(new_movie, quote=True)

        # TODO 1
        # Use a template to render the confirmation message
        t_add = jinja_env.get_template("add.html")
        main_content = t_add.render(movie=new_movie_escaped)
        page_header = t_page_header.render(title="FlickList: " + new_movie_escaped + " has been added to your WatchList")
        page_footer = t_page_footer.render()
        
        response = page_header + main_content + page_footer
        self.response.write(response)



class CrossOffMovie(webapp2.RequestHandler):
    """ Handles requests coming in to '/cross-off'
        e.g. www.flicklist.com/cross-off
    """

    def post(self):
        crossed_off_movie = self.request.get("crossed-off-movie")

        if not crossed_off_movie or crossed_off_movie.strip() == "":
            error = "Please specify a movie to cross off."
            self.redirect("/?error=", cgi.escape(error))

        # if user tried to cross off a movie that is not in their list, reject
        if not (crossed_off_movie in getCurrentWatchlist()):
            # make a helpful error message
            error = "'{0}' is not in your Watchlist, so you can't cross it off!".format(crossed_off_movie)
            error_escaped = cgi.escape(error, quote=True)

            # redirect to homepage, and include error as a query parameter in the URL
            self.redirect("/?error=" + error_escaped)

        # render confirmation page
        t_cross_off = jinja_env.get_template("cross-off.html")
        main_content = t_cross_off.render(movie=crossed_off_movie)
        page_header = t_page_header.render(
                        title="FlickList: " + crossed_off_movie
                        + " has been crossed off your Watchlist")
        page_footer = t_page_footer.render()

        response = page_header + main_content + page_footer
        self.response.write(response)


app = webapp2.WSGIApplication([
    ('/', Index),
    ('/add', AddMovie),
    ('/cross-off', CrossOffMovie)
], debug=True)
