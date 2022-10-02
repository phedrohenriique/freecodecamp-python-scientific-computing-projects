import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import seaborn as sns
fifa_filepath = "data-analysis/fifa.csv"

def database_reading():
    
    fifa_data = pd.read_csv(fifa_filepath, index_col='Date', parse_dates=True)
    ##print(fifa_data.head(5))
    plt.figure(figsize=(16,6))
    sns.lineplot(data=fifa_data)
    plt.show()  ## had to install backend GUI interface pyqt5

if __name__ == "__main__":

    ##print('Setup Completed')
    database_reading()