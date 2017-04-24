import pymysql
import csv
import pprint

connection = pymysql.connect(host="localhost",
                      user="xichen",
                      passwd="3606586",
                      db="xichen_term_project",
                      autocommit=True,
                      cursorclass=pymysql.cursors.DictCursor)
with open('dataset/adults diabetes rate by state_term_1.csv') as csvfile:
    myCSVReader = csv.DictReader(csvfile)

    # change names in placeholder to match names in csv file.
    sql = """INSERT INTO obesity_rates(state_id,adult_rate,youth_rate,o_year_id)
          VALUE (%(state_id)s,%(adult_rate)s,%(youth_rate)s,%(o_year_id)s)"""

    for row in myCSVReader:
        # use row directly
        cursor=connection.cursor()
        cursor.execute(sql, row)

with open('dataset/o_years.csv') as csvfile:
    myCSVReader = csv.DictReader(csvfile)

    # change names in placeholder to match names in csv file.
    sql = """INSERT INTO o_years(name)
          VALUE (%(year)s)"""

    for row in myCSVReader:
        # use row directly
        cursor=connection.cursor()
        cursor.execute(sql, row)
