# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer 
import time

hostName = "localhost"
serverPort = 8080

#This class inherits from BaseHTTPRequestHandler and provides custom logic for handling HTTP requests
class MyServer(BaseHTTPRequestHandler): 

    #Inside this class, there's a do_GET method which is executed when a GET request is received by the server.
    def do_GET(self):

        self.send_response(200) #server sends an HTTP response with a status code of 200(OK)
        self.send_header("Content-type", "text/html") #indicates that the response is in HTML format
        self.end_headers()

        #use the self.wfile.write() method to write HTML content to the response.
        self.wfile.write(bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8")) 
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>This is an example web server.</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

#take note that DO_GET method runs in chrome or your browser

if __name__ == "__main__":    #The script checks if it's being run as the main program     
    webServer = HTTPServer((hostName, serverPort), MyServer)

    #A message is printed in terminal indicating that the server has started and showing the host and port.
    print("Server started http://%s:%s" % (hostName, serverPort))

    #The server enters a loop, serving incoming requests indefinitely until a keyboard interrupt (Ctrl+C) is received.
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

#Upon interrupt, the server is gracefully shut down using webServer.server_close()
    webServer.server_close()
    print("Server stopped.")