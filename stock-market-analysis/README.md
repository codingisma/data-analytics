**Description:** This ETL Project downloads the data from publicly available API and transforms it in Pandas

Steps to run the project:
1. Clone the project in your local
2. Pip install requirements.txt
3. Run the StockMarketDataDump.py 

This will generate an output file 'stock_data_merged.csv' which can be imported in Tableau and visualizations/analysis could be created on top of it.

In this Project we have included a Tableau workbook, which reads this data and creates visualizations on it


**Details on Util Classes and functions:**
1. Constants.py: Stores all the constants 
2. FileDownloader.py: Cleans the existing files and downloads data from API in new files. Three files are created in this
   1. bal_sheet.csv
   2. overview.csv
   3. ts_monthly.csv
 TransformPandas.py: This pandas code picks the downloaded files and joins them together to form an output.csv which is final sink of this project