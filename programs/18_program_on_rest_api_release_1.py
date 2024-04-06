"""

Also Refer: consume_api.py

Python for web development

We have many web frameworks in python,
- bottle framework
- flask framework # POPULAR: Micro framework
- django framework # POPULAR: MVT(Model View Template)
- pyramid framework
- web2py framework
- falcon framework
- fastapi framework  # POPULAR
Many More
"""

"""
We are discussing flask framework
- Using flask, we can develop websites
- Using flask, we can create RESTFul web services like RESTAPI, Microservices
"""

"""
We will discuss on using flask to develop RESTAPI
"""

"""
Suppose, if we want to provide access to our database with others/public
then how to provide?
OPTION-1:
    provide all credentials like username, password, host, db etc

OPTION-1 will not work because we can't share all details with others

OPTION-1 is like
our-db/our-app  <-- DIRECT ENTRY -->  others/public

"""

"""
We got 2 solutions

1) SOAP, Simple Object Access Protocol
2) REST, REpresentational State Transfer

both are called styles/designs/architecture

both tells best way to provide access to others?

our-db/our-app  <-- INTERFACE -->  others/public
APPLICATION PROGRAMMING INTERFACE (API)

both tells how to write INTERFACE

SOAP-API
REST-API

REST came after SOAP
- REST is easy to implement
- REST is popular
"""

'''
Then using REST 
Suppose, if we want to provide access to our database with others/public
then how to provide?

- No need to implement REST architecture from scratch
- Because, flask is already implemented REST
- So, we can use flask framework to develop RESTAPI 
'''

'''
HTTP Methods
GET : Reading
POST: Creating/sending data to server
PUT: update
PATCH: partial update
DELETE: delete
'''

# -----------
# Create App For Our REST API
#############
import flask
# my_rest_api_app = flask.Flask("MyRESTAPIApp")
my_rest_api_app = flask.Flask(__name__)
###############################

# -----------
# ENDPOINT -1 : URL http://127.0.0.1:5000/getdbdata mapped to route("/getdbdata")
# To Access Use: consume_api.py
#############
@my_rest_api_app.route("/getdbdata")
def my_getdbdata():
    import sqlite3
    my_db_connection = sqlite3.connect("my_database.sqlite3")
    my_db_cursor = my_db_connection.cursor()
    my_db_cursor.execute("SELECT * FROM MY_TABLE")
    my_db_result = my_db_cursor.fetchall()
    return flask.jsonify(my_db_result)

###############################


# -----------
# Run builtin server
#############
my_rest_api_app.run()
# my_rest_api_app.run(host='127.0.0.1', port=1234)

# list of production servers
# https://wsgi.readthedocs.io/en/latest/servers.html
###############################