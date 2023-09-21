import requests
import Constants
import os
import time

def get_data(input, company, fname):
    api = Constants.api.replace("COMPANY", company).replace("INPUT_TYPE", input)
    print(api)
    response = requests.get(f"{api}")
    if response.status_code == 200:
        print("sucessfully fetched the data")
        response_string = response.json()
        print(response_string)
        handle_data(company, response_string, fname, input)
    else:
        print(response.status_code)
        print(f"Hello person, there's a {response.status_code} error with your request")





def wriite_data(file_name, string):
    file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'files', file_name)

    with open(file_path, "a") as file:
        file.write(string)


def handle_data(company, s, fname, input):
    if (input == "TIME_SERIES_MONTHLY"):
        for i in s["Monthly Time Series"].keys():
            month = i
            open = s["Monthly Time Series"][i]['1. open']
            close = s["Monthly Time Series"][i]['4. close']
            high = s["Monthly Time Series"][i]['2. high']
            low = s["Monthly Time Series"][i]['3. low']
            volume = s["Monthly Time Series"][i]['5. volume']
            string = month + "," + open + "," + close + "," + high + "," + low + "," + volume + "," + company + "\n"
            wriite_data(fname, string)
    elif (input == "OVERVIEW"):
        Exchange = s['Exchange']
        Currency = s["Currency"]
        Country = s["Country"]
        Sector = s["Sector"]
        Industry = s["Industry"]
        Address = s["Address"]

        string = Exchange + "," + Currency + "," + Country + ",\"" + Sector + "\",\"" + Industry + "\",\"" + Address + "\"," + company + "\n"
        wriite_data(fname, string)

    elif (input == "BALANCE_SHEET"):
        # print(type(s))
        for ip in s["annualReports"]:
            fiscalDateEnding = ip["fiscalDateEnding"]
            totalAssets = ip["totalAssets"]
            inventory = ip["inventory"]
            totalLiabilities = ip["totalLiabilities"]

            string = fiscalDateEnding + "," + totalAssets + "," + inventory + "," + totalLiabilities + "," + company + "\n"
            wriite_data(fname, string)
def cleanup_files():

    for j in Constants.input_type.values():
        print(j)
        fpath=os.path.join(os.path.dirname(os.path.dirname(__file__)), 'files', j)
        print(fpath)
        if os.path.exists(fpath):
            print(f"The file {fpath} exists.")
            os.remove(fpath)
        else:
            print(f"The file {fpath} does not exist.")
def write_headers():
    for k in Constants.input_type:
        file_name = Constants.input_type.get(k)
        header = Constants.header.get(k + "_HEADER")
        wriite_data(file_name, header)

def download_data():
    for company in Constants.company:
        for input in Constants.input_type:
            fname = Constants.input_type.get(input)
            print(input, company, fname)
            print(input, company, fname)
            get_data(input, company, fname)
            time.sleep(15)