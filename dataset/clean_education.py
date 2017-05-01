import csv
import pprint

"""
Function to spread list values left to right.
Used to deal with implicit multiple headers.
["","value","","value2",""] ==> ["","value","value","value2","value2"]
"""
def spread_list(inlist):
    outlist = []
    curr = ""
    for item in inlist:
        if(item): # hit a new one, update
            curr = item
        outlist.append(curr)
    return outlist

with open('/export/home/u16/jiang/term_project/dataset/education_raw.csv') as csvfile:

    myCSVReader = csv.reader(csvfile, delimiter=",", quotechar='"')

    years = spread_list(next(myCSVReader))
    age_ranges = spread_list(next(myCSVReader))

    outrows = []

    for row in myCSVReader:

        if(not any(row)):
            break
        else:
            for row in myCSVReader:
                for index, item in enumerate(row):
                    if(index == 0):
                        state = item
                    else:
                        if(item == ""):
                            item = "NA"

                        outrow = {
                        "state": state,
                        "age_range": age_ranges[index],
                        "year": years[index],
                        "bachelor_rate": item
                                }
                        outrows.append(outrow)

out_headers = ["state", "age_range", "year", "bachelor_rate"]

with open("/export/home/u16/jiang/term_project/dataset/education_clean.csv" ,"w", newline = "") as csvfile:
    myCsvWriter = csv.DictWriter(csvfile, delimiter=',', quotechar='"',fieldnames = out_headers)

    myCsvWriter.writeheader()

    for row_dict in outrows:
        myCsvWriter.writerow(row_dict)
print("Done with wrting")
