import pandas as pd

def summary_df(details):
    for key in details.keys():
        if details[key]==0:
            details[key]="No issue"
        else:
            details[key]="Check system"

    df=pd.DataFrame(details.items(),columns=["Check","Status"])
    print(df)

