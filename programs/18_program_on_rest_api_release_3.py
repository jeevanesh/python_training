"""
PUT: Supported Update records
"""

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
@my_rest_api_app.route("/getdbdata", methods=["GET"]) # default it GET
def my_getdbdata():
    import sqlite3
    my_db_connection = sqlite3.connect("my_database.sqlite3")
    my_db_cursor = my_db_connection.cursor()
    my_db_cursor.execute("SELECT * FROM MY_TABLE")
    my_db_result = my_db_cursor.fetchall()
    return flask.jsonify(my_db_result)
###############################

# -----------
# ENDPOINT -2 : URL http://127.0.0.1:5000/postdbdata mapped to route("/postdbdata")
# To Access Use: consume_api.py
#############
@my_rest_api_app.route("/postdbdata", methods=["POST"])
def my_postdbdata():
    # Get data sent by client
    new_record = flask.request.get_json()
    # new_record will be dictionary
    # new_record = {"IP": "" , "DATE": '', "PICS": "", URL:""}

    import sqlite3
    my_db_connection = sqlite3.connect("my_database.sqlite3")
    my_db_cursor = my_db_connection.cursor()

    # Check whether IP is already exists
    my_query = f"""SELECT COUNT(*) FROM MY_TABLE WHERE IP = '{new_record.get("IP")}'"""
    my_db_cursor.execute(my_query)
    my_db_result = my_db_cursor.fetchone()
    # Example: if 10 records then we will get tuple like (10,)
    records_count = my_db_result[0]
    if records_count > 0:
        response = flask.make_response(flask.jsonify("Record Already Present"), 409)
        return response
    else:
        my_query = f"""
        INSERT INTO MY_TABLE VALUES(
        '{new_record.get("IP")}',
        '{new_record.get("DATE")}',
        '{new_record.get("PICS")}',
        '{new_record.get("URL")}'
        )
        """
        my_db_cursor.execute(my_query)
        my_db_connection.commit()
        my_db_connection.close()
        response = flask.make_response(flask.jsonify("New Record Created"), 201)
        return response
###############################

# -----------
# ENDPOINT -3 : URL http://127.0.0.1:5000/putdbdata mapped to route("/putdbdata")
# To Access Use: consume_api.py
#############
@my_rest_api_app.route("/putdbdata", methods=["PUT"])
def my_putdbdata():
    # Get data sent by client
    new_record = flask.request.get_json()
    # new_record will be dictionary
    # new_record = {"IP": "" , "DATE": '', "PICS": "", URL:""}

    import sqlite3
    my_db_connection = sqlite3.connect("my_database.sqlite3")
    my_db_cursor = my_db_connection.cursor()

    # Check whether IP is already exists
    my_query = f"""SELECT COUNT(*) FROM MY_TABLE WHERE IP = '{new_record.get("IP")}'"""
    my_db_cursor.execute(my_query)
    my_db_result = my_db_cursor.fetchone()
    # Example: if 10 records then we will get tuple like (10,)
    records_count = my_db_result[0]
    if records_count == 0:
        response = flask.make_response(flask.jsonify("Record Not Present To Update"), 404)
        return response
    else:
        my_query = f"""
        UPDATE MY_TABLE
        SET
        IP='{new_record.get("IP")}',
        DATE='{new_record.get("DATE")}',
        PICS='{new_record.get("PICS")}',
        URL='{new_record.get("URL")}'
        WHERE
        IP='{new_record.get("IP")}'
        """
        my_db_cursor.execute(my_query)
        my_db_connection.commit()
        my_db_connection.close()
        response = flask.make_response(flask.jsonify("Record Updated"), 201)
        return response
###############################

# -----------
# Run builtin server
#############
my_rest_api_app.run()
# my_rest_api_app.run(host='127.0.0.1', port=1234)

# list of production servers
# https://wsgi.readthedocs.io/en/latest/servers.html
###############################