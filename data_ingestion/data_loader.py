from TrainingData import  *
import pandas as pd
filename = 'InputFile.csv'
class load_data:
    def get_data(self):
         data = pd.read_csv("..//TrainingData//"+filename)
         # data = pd.read_csv(filename)
         return data
