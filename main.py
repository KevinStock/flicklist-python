import webapp2

def is_integer(canidate_int):
    for c in canidate_int
        if not c.isdigit():
            return False
    return True


# html boilerplate for the top of every page
page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>FlickList</title>
</head>
<body>
    <h1>FlickList</h1>
"""

# html boilerplate for the bottom of every page
page_footer = """
</body>
</html>
"""

class Index(webapp2.RequestHandler):
    """ Handles requests coming in to '/' (the root of our site)
        e.g. www.flicklist.com/
    """

    def get(self):

        edit_header = "<h3>Edit My Watchlist</h3>"

        # a form for adding new movies
        add_form = """
        <form action="/add" method="post">
            <label>
                I want to add
                <input type="text" name="new-movie"/>
                to my watchlist.
            </label>
            <input type="submit" value="Add It"/>
        </form>
        """

        # TODO 1
        # Include another form so the user can "cross off" a movie from their list.
        remove_dropdown = """
        <form action="/remove" method="post">
        	<label>
        		I want to remove
        		<select type="dropdown" name="del-movie">
        			<option>Big</option>
        			<option>Contact</option>
        			<option>Interstellar</option>
        		</select>
        	</label>
        	<input type="submit" value="Remove It" />
        </form>
        """
#
#         remove_form = """
#         <form action="/remove" method="post">
#             <label>
#                 I want to remove
#                 <input type="text" name="del-movie"/>
#                 from my watchlist.
#             </label>
#             <input type="submit" value="Remove It"/>
#         </form>
#         """

        # TODO 4 (Extra Credit)
        # modify your form to use a dropdown (<select>) instead a
        # text box (<input type="text"/>)


        response = page_header + edit_header + add_form + remove_dropdown + page_footer
        self.response.write(response)


class AddMovie(webapp2.RequestHandler):
    """ Handles requests coming in to '/add'
        e.g. www.flicklist.com/add
    """

    def post(self):
        # look inside the request to figure out what the user typed
        new_movie = self.request.get("new-movie")

        # build response content
        new_movie_element = "<strong>" + new_movie + "</strong>"
        sentence = new_movie_element + " has been added to your Watchlist!"

        response = page_header + "<p>" + sentence + "</p>" + page_footer
        self.response.write(response)


# TODO 2
# Create a new RequestHandler class called CrossOffMovie, to receive and
# handle the request from your 'cross-off' form. The user should see a message like:
# "Star Wars has been crossed off your watchlist".

class RemoveMovie(webapp2.RequestHandler):
    """ Handles requests coming in to '/remove'
        e.g. www.flicklist.com/remove
    """

    def post(self):
        del_movie = self.request.get("del-movie")

        del_movie_element = "<strong>" + del_movie + "</strong>"
        sentence = del_movie_element + " has been removed from your Watchlist!"

        response = page_header + "<p>" + sentence + "</p>" + page_footer
        self.response.write(response)


# TODO 3
# Include a route for your cross-off handler, by adding another tuple to the list below.
app = webapp2.WSGIApplication([
    ('/', Index),
    ('/add', AddMovie),
    ('/remove', RemoveMovie)
], debug=True)
