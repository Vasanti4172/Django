import cherrypy
class WebApp:
    @cherrypy.expose
    def text(self):
        return "This is a plain text response!"
    @cherrypy.expose
    def index(self):
        return """
            <html>
                <head>
                    <title>Welcome to CherryPy</title>
                </head>
                <body>
                    <h1>Hey! There, Experience my  CherryPy web application!</h1>
                    <p>This HTML page is created by using CherryPy.</p>
                </body>
            </html>
        """
    @cherrypy.expose
    def external_html(self):
        return open('external_page.html').read()
if __name__ == '__main__':
    cherrypy.config.update({'server.socket_port': 8081})  
    cherrypy.quickstart(WebApp())