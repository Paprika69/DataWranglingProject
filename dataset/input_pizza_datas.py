import pymysql
import pprint
import csv

############################
# Moving from a csv to mysql
############################

# First you need to go to class_music_festival --> operations and copy just the
# database structure to <yourusername>_empty_music_festival


# Open the connection to the database (must be one you can write to!)
connection = pymysql.connect(host="localhost",            # your host, usually localhost
                             user="jiang",             # your username
                             passwd="21669969abd",   # your password
                             db="jiang_term_project", # name of the db
                             autocommit=True,             # removes a step in queries
                             cursorclass=pymysql.cursors.DictCursor)

cursor = connection.cursor()
full_query = "TRUNCATE pizza_data;"
cursor.execute(full_query)


#  Read the CSV, then as we move row by row we can put it into the database
with open('/export/home/u16/jiang/term_project/dataset/pizzadata.csv') as csvfile:
    # tell python about the specific csv format
    myCSVReader = csv.DictReader(csvfile, delimiter=",", quotechar='"')

    for row in myCSVReader:
        pprint.pprint(row)
        # sql with placeholders for dict_params
        sql = """INSERT INTO pizza_data(id, state_id, pizza_consumption, pizza_store_per_10000_people, p_year_id)
              VALUES (%(id)s,%(state_id)s,%(pizza_consumption)s,%(pizza_store_per_10000_people)s,%(p_year_id)s)"""
        cursor.execute(sql,row)
