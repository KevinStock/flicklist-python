import webapp2

class Index(webapp2.RequestHandler):
	def get_random_movie(self):
		# TODO: Make acctually random
		return 'Die Hard'

    def get(self):
        response = '<html><body>'
        response += '<strong>Random Movie:</strong>'
        response += self.get_random_movie()
        response += '</body></html>'

        self.response.write(response)

app = webapp2.WSGIApplication([
    ('/', Index)
], debug=True)
