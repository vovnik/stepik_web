bind = "0.0.0.0:8080"

def app(environ, start_response):
    query_string = environ['QUERY_STRING']
    data = [bytes((param+'\n').encode("UTF-8")) \
            for param in query_string.split('&')]
    start_response("200 OK", [
        ("Content-Type", "text/plain")  
    ])
    print(type(data))
    return iter(data)

