import urllib.parse
import requests
from prettytable import PrettyTable
from colorama import Fore, Style

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "GZhxy49gaCdw82j6bLpcFTXE3A7MMvJ7"

myTable = PrettyTable(["\033[1;31mOrigin\033[0m", "\033[1;32mDestination\033[0m","Distance (Miles)", "Distance (Kilometers)", "Fuel Used (Gal)", "Fuel Used (Ltr)"])

while True:
    # gets user input starting location
    print(Fore.YELLOW)
    orig = input("Starting Location: ")
    if orig == "quit" or orig == "q":
        break
    # gets user input destination
    print(Fore.CYAN)
    dest = input("Destination: ")
    if dest == "quit" or dest == "q":
        break
    url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})
    print(Fore.GREEN)
    print("URL: " + (url))
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]
    # print the output if successful
    if json_status == 0:
        orig = "\033[1;31m%s\033[0m" %orig
        dest = "\033[1;32m%s\033[0m" %dest
        print("API Status: " + str(json_status) + " = A successful route call.\n")
        print("=============================================")
        # Outputs the information into a table
        myTable.add_row([(orig), (dest), str(json_data["route"]["distance"]), str("{:.2f}".format((json_data["route"]["distance"])*1.61)), str(json_data["route"]["fuelUsed"]), str("{:.2f}".format((json_data["route"]["fuelUsed"])*3.78))])
        print(myTable)
        print(Fore.MAGENTA)
        print("=============================================")
        print("Directions:")
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
        print("=============================================\n")
        #hahahah
    # for errors
    elif json_status == 402:
        print(Fore.RED)
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Invalid user inputs for one or both locations.")
        print("**********************************************\n")
    elif json_status == 611:
        print(Fore.RED)
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Missing an entry for one or both locations.")
        print("**********************************************\n")
    else:
        print(Fore.RED)
        print("************************************************************************")
        print("For Staus Code: " + str(json_status) + "; Refer to:")
        print("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print("************************************************************************\n")
        print("************************************************************************\n")
