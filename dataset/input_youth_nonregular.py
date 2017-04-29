import pymysql
import pprint
import csv


# Open the connection to the database (must be one you can write to!)
connection = pymysql.connect(host="localhost",            # your host, usually localhost
                             user="jiang",             # your username
                             passwd="21669969abd",   # your password
                             db="jiang_term_project", # name of the db
                             autocommit=True,             # removes a step in queries
                             cursorclass=pymysql.cursors.DictCursor)

cursor = connection.cursor()

# Clean the table before inserting
full_query = "TRUNCATE youth_nonregular_exercises;"
cursor.execute(full_query)
#  Read the CSV, then as we move row by row we can put it into the database
with open('/export/home/u16/jiang/term_project/dataset/youth_nonregular_rate.csv') as csvfile:
    # tell python about the specific csv format
    myCSVReader = csv.DictReader(csvfile, delimiter=",", quotechar='"')

    for row in myCSVReader:
        pprint.pprint(row)
        # sql with placeholders for dict_params
        sql = "INSERT INTO youth_nonregular_exercises(state_id, rate, y_year_id) " \
              "VALUES (%(state_id)s,%(rate)s,%(y_year_id)s)"
        cursor.execute(sql,row)
    print("Done with writing")
