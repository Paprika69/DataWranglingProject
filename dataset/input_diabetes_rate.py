import pymysql
import csv
import pprint

connection = pymysql.connect(host="localhost",
                      user="xichen",
                      passwd="3606586",
                      db="xichen_term_project",
                      autocommit=True,
                      cursorclass=pymysql.cursors.DictCursor)
with open('dataset/adults_obesity.csv') as csvfile:
    myCSVReader = csv.DictReader(csvfile)
    with open("dataset/youth_obesity_rate_new.csv") as referCsvfile:
        referCSVReader = csv.DictReader(referCsvfile)
        for item in myCSVReader:
            if item["adult_rate"] == "":
                item["adult_rate"] = 0
            else:
                item["adult_rate"] = float(item["adult_rate"])/100
            #print(type(item["adult_rate"]))
            for key in referCSVReader:
                #print(item['id'])
                if item['id'] == key['id']:
                    if key["youth_rate"] == "":
                        item["youth_rate"] = 0
                    else:
                        item["youth_rate"]= float(key["youth_rate"])/100
                    #print(type(key["youth_rate"]))
                    break
            sql = """INSERT INTO obesity_rates(state_id,adult_rate,youth_rate,o_year_id)
            VALUE (%(state_id)s,%(adult_rate)s,%(youth_rate)s,%(o_year_id)s)"""
            cursor=connection.cursor()
            cursor.execute(sql, item)

    # change names in placeholder to match names in csv file.


    #for row in myCSVReader:
        # use row directly
        #cursor=connection.cursor()
        #cursor.execute(sql, row)

# with open('dataset/o_years.csv') as csvfile:
#     full_query = "TRUNCATE post_events;"
#     cursor.execute(full_query)
#     myCSVReader = csv.DictReader(csvfile)
#
#     # change names in placeholder to match names in csv file.
#     sql = """INSERT INTO o_years(name)
#           VALUE (%(year)s)"""
#
#     for row in myCSVReader:
#         # use row directly
#         cursor=connection.cursor()
#         cursor.execute(sql, row)
