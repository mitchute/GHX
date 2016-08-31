
import json


class GHX():
    def __init__(self, inData):
        self.name = inData[0]
        self.location = inData[1]
        self.flowRate = inData[2]
        self.groundCond = inData[3]

def get_input():

    with open("input.json") as json_file:
        json_data = json.load(json_file)

    load_GHX_data(json_data)

def load_GHX_data(data_from_json):
    inData = []

    inData.append(data_from_json['GHXs'][0]['Name'])


    print(inData)


def calc_g_func():

    return 0

def perform_simulation():

    return 0

def main():

    get_input()

    calc_g_func()

    perform_simulation()

main()