import pandas as pd
from pandas import Series,DataFrame

dataFile = r'E:\Sachin\Python\DataVisualization\Titanic\Data\test.csv'
class TitanicAnalysis(object):
    def __init__(self):
        # Set up the Titanic csv file as a DataFrame
        self.titanic_df = pd.read_csv(dataFile)

    @property
    def HEAD(self):
        return self.titanic_df.head()

    @property
    def INFO(self):
        return self.titanic_df.info()


tA = TitanicAnalysis()
print(tA.INFO)