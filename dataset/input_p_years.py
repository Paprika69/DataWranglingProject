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
                             user="ID",             # your username
                             passwd="Pw",   # your password
                             db="ID_term_project", # name of the db
                             autocommit=True,             # removes a step in queries
                             cursorclass=pymysql.cursors.DictCursor)

cursor = connection.cursor()

#  Read the CSV, then as we move row by row we can put it into the database
with open('/export/home/u17/yoomi/term_project/dataset/p_years.csv') as csvfile:
    # tell python about the specific csv format
    myCSVReader = csv.DictReader(csvfile, delimiter=",", quotechar='"')

    for row in myCSVReader:
        pprint.pprint(row)
        # sql with placeholders for dict_params
        sql = "INSERT INTO p_years(id, name) VALUES (%(id)s,%(name)s)"
        cursor.execute(sql,row)
