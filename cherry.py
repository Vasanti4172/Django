import cherrypy
cherrypy.config.update({
 'server.socket_host': '127.0.0.1',
 'server.socket_port': 8082 
})
class MyApp:
    @cherrypy.expose
    def index(self):
        return("This is a simple text response!")
    @cherrypy.expose
    def op_html(self):
        return open('op.html').read()
    @cherrypy.expose
    def html(self):
        return"""
        <html>
            <head>
                <title>Greetings from Cherrypy</title>
            </head>
            <body>
                <h1>Hey There!Experience CherryPy!</h1>
                <p>This is an HTML page created by using CherryPy.</p>
            </body>
        </html>
        """
if __name__ == '__main__':
    cherrypy.quickstart(MyApp())