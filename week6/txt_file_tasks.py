# import csv
#
# with open("data.csv") as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=",", quotechar='"')
#     for row in csv_reader:
#         print(row[0])
import os


# import jason
#
# with open("data.json", "w") as jason_file:
#     data = jason.load(jason_file)
#
# print(data)


# import jason
#
# jason_data = {"name": "Prins", "job": "Lecturer"}
#
# jason_file = open("output.jason", "w")
# jason.dump(jason_data, jason_file, indent=4)
#
# jason_file.close()


# import json
# import requests
#
# data = {"name": "Prins", "job": "Lecturer"}
#
# json_data = json.dumps(data)
# requests.post("https://somesite.com/post", json=json_data)


# import os
#
# path = os.getcwd()  # get current working directory
# print(f"Current working directory: {path}")
#
#
# for file in os.listdir(path):
#     print(file)
#
import os


def cwd():
    path = os.getcwd()
    print(f"The current working directory is: {path}")
    print(f"The directory contain the files ")
    for file in os.listdir(path):
        print(file)


def run():
    print(f"Processing....")
    cwd()


if __name__ == "__main__":
    run()
