from matplotlib.pyplot import axis
import pandas as pd
from requests import delete
winelist_filepath = "pandas/winelist-data-130k.csv"

def columns_change(row):
    row['points'] = row['points']*10
    return row

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
    pd.set_option("display.max_rows", 10)
    
    ## changing all rows

    def change(row):
        row['country'] = 'Teste'
        return row

    def points_times(value):
        return value*100
    
    points_change = df_winelist['points']*100
    mapped = df_winelist['points'].map(lambda points : points * 100) ## for each element it gets the element and returns it times 100
    mapped_second = df_winelist['points'].map(points_times).head(10)

    ## when passing functions as arguments it can't be passed with () they shall be just
    ## referenced so the call back executes it with their own parameters

    ## print(df)
    ## print(df.shape)
    ## print(df_series)
    ## print(df_winelist.loc[df_winelist['country'] == 'Italy','country']) ## loc counts the values from total range, the last one shall be taken as value - 1
    ## print(df_winelist.iloc[-5:,1])
    ## print(df_winelist.loc[df_winelist['points'] > 50, ['country', 'points']])
    ## print(df_winelist.loc[(df_winelist['points'] > 80) & (df_winelist['country'] == 'Brazil'), ['country', 'points']])
    ##print(df_winelist.loc[df_winelist['country'].isin(['France']),['country']])
    ## print(df_winelist.loc[df_winelist['price'].notnull()].shape)
    ## print(df_winelist['points'].describe())
    ## print(df_winelist.loc[df_winelist['points'] > 95, ['country']].value_counts())
    ## print(df_winelist['points'].mean())
    ## print(df_winelist['points'].apply(columns_change(),axis='columns'))
    ## print(mapped.head(10))
    ## print(df_winelist.apply(lambda row : row['points']-100,axis='columns').head(10)) ## recieves another function as parameter to be appllied in each row
    ## print(df_winelist.apply(change, axis='columns').head(10)) ## axis='columns' change the rows
    ## print(mapped_second)
    ## print(df_winelist['variety'].head(5) +""+ df_winelist['winery'].head(5))
    print(df_winelist.groupby('country')['price'].mean()) ## group by a column and defines how much of the other they have

if __name__ == "__main__":
    ## print('started')
    data_manipulation()