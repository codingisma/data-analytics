import pandas as pd
import os

def transform_data():
    monthly_fpath=os.path.join(os.path.dirname(os.path.dirname(__file__)), 'files', "ts_monthly.csv")
    overview_fpath = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'files', "overview.csv")
    bal_sheet_fpath = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'files', "bal_sheet.csv")
    output_fpath = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'files', "output.csv")
    print(monthly_fpath)
    ts=pd.read_csv(monthly_fpath)
    ov=pd.read_csv(overview_fpath)
    bs=pd.read_csv(bal_sheet_fpath)
    df1=pd.DataFrame(bs)
    df2=pd.DataFrame(ov)
    df3=pd.DataFrame(ts)
    result = pd.merge(df3, df2, on='company', how='inner')
    result['date']= pd.to_datetime(result['date'])
    result['year'] = result['date'].dt.year
    df1['fiscalDateEnding']=pd.to_datetime(df1['fiscalDateEnding'])
    df1['year']=df1['fiscalDateEnding'].dt.year
    merged= pd.merge(result,df1, on=['year','company'], how='left')
    merged.fillna('NA', inplace=True)
    merged.to_csv(output_fpath, index=False)
