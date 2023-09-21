api ="https://www.alphavantage.co/query?function=INPUT_TYPE&symbol=COMPANY&apikey=9QBF0T4CAU5XGCL8"
company=["IBM","AAPL","UBER"]
input_type={"BALANCE_SHEET":"bal_sheet.csv","OVERVIEW":"overview.csv","TIME_SERIES_MONTHLY":"ts_monthly.csv"}
header={"BALANCE_SHEET_HEADER": "fiscalDateEnding,"+"totalAssets,"+"inventory,"+"totalLiabilities,"+"company"+"\n",
        "OVERVIEW_HEADER":"Exchange,"+"Currency,"+"Country,"+"Sector,"+"Industry,"+"Address,"+"company"+"\n",
        "TIME_SERIES_MONTHLY_HEADER":"date,"+"open,"+"close,"+"high,"+"low,"+"volume,"+"company"+"\n"}
file_dir="files/"