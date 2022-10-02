from cProfile import label
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

spotify_filepath = "data-analysis/spotify.csv"
museum_filepath = "data-analysis/museum_visitors.csv"

def database_reading():
    spotify_data = pd.read_csv(spotify_filepath, index_col='Date')
    print(spotify_data.columns)

def graphic_show():
    spotify_data = pd.read_csv(spotify_filepath)
    print(spotify_data.head(10))
    plt.figure(figsize=(20,10))
    plt.title('Daily Global Streams of Popular Songs in 2017-2018')
    plt.xlabel('Date')
    sns.lineplot(data=spotify_data['Shape of You'], label='Shape of You')
    sns.lineplot(data=spotify_data['Despacito'], label='Despacito')
    plt.show()

def museum_data_exercise():
    museum_data = pd.read_csv(museum_filepath)
    plt.figure(figsize=(40,20))
    plt.title('Museum Visitors')
    sns.lineplot(data=museum_data['Chinese American Museum'].head(20), label='Chinese American Museum')
    sns.lineplot(data=museum_data['Avila Adobe'].head(20), label='Avila Adobe')
    plt.show()

if __name__ == "__main__":
    print('starting...')
    ## database_reading()
    ##graphic_show()
    museum_data_exercise()