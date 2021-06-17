import pandas as pd
import csv
import plotly.figure_factory as ff
import statistics
import random
import plotly.graph_objects as go

df = pd.read_csv(r"/Users/anshul/Desktop/Class 110/data2.csv")
data = df["Math score"].tolist()
popmean = statistics.mean(data)

dataset = []
for x in range(0,50):
    random_index = random.randint(0,len(data))
    value = data[random_index]
    dataset.append(value)
mean = statistics.mean(dataset)
stdev = statistics.stdev(dataset)
print("Mean of sampling data is",mean)
print("Standard deviation of sampling data is",stdev)

zscore = (mean-popmean)

