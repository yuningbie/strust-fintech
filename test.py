#!/usr/bin/python3

import sys
import json
import requests
import psycopg2

print("testst")
# baseUrl = "https://xchain.io"
# asset = "btc"
# response = requests.get(baseUrl + "/api/asset/" + asset)
# print(response.status_code)
# print(response.json())

blockchairBaseUrl = "https://api.blockchair.com/"
response = requests.get(blockchairBaseUrl + "/dash/outputs")
print("YUNING")
print(response.status_code)
print(response.json())

try:
    connection = psycopg2.connect(
        user = "yuningbie",
        password = "database123",
        host = "localhost",
        port = "5432",
        database = "strust_db"
    )

    cursor = connection.cursor()

    # Print PostgreSQL Connection properties
    print(connection.get_dsn_parameters(), "\n")

    # Print PostgreSQL version
    cursor.execute("SELECT version();")
    record = cursor.fetchone()

    print("You are connected to - ", record, "\n")
except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)
finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")