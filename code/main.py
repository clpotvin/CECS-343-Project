# IMPORTS
from Classes.user_interface import UserInterface
from Classes.fleet_interface import FleetInterface
import pandas as pd

# GLOBAL VARIABLES

# FUNCTIONS


def main():
    # UI = UserInterface()
    # UI.run()

    FI = FleetInterface()
    FI.run()

    #pwd = hash("helloW0rld!")

    #if hash(input("Input password: ")) == pwd:
    #    print(True)

    # arr = [['a', 'b', 'c'], ['d', 'e'], ['f', 'g', 'h', 'i']]
    # a = pd.DataFrame.from_records(arr)
    # a.to_csv("CECS-343-Project/code/Data/a.csv")

    #print(a)



main()
