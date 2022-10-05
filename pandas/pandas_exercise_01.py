import pandas as pd
from requests import delete
winelist_filepath = "pandas/winelist-data-130k.csv"

def data_manipulation():
    df = pd.DataFrame(
        {
            'A':[10,20,30],
            'B':[20,40,60,],
            'C':[30,80,120]
        },
        index=['First', 'Second', 'Third']
    )

    df_series = pd.Series([1,2,3,4,5], index=['a','b','c','d','e'])

    df_winelist = pd.read_csv(winelist_filepath)
    

    ## print(df)
    ## print(df.shape)
    ## print(df_series)
    ## print(df_winelist.loc[df_winelist['country'] == 'Italy','country']) ## loc counts the values from total range, the last one shall be taken as value - 1
    ## print(df_winelist.iloc[-5:,1])
    ## print(df_winelist.loc[df_winelist['points'] > 50, ['country', 'points']])
    ## print(df_winelist.loc[(df_winelist['points'] > 80) & (df_winelist['country'] == 'Brazil'), ['country', 'points']])
    print(df_winelist.loc[df_winelist['country'].isin(['France']),['country']])

if __name__ == "__main__":
    print('started')
    data_manipulation()