import pandas as pd
import csv
import plotly.figure_factory as ff
import statistics
import random
import plotly.graph_objects as go

df = pd.read_csv(r"/Users/anshul/Desktop/Class 110/data1.csv")
data = df["Math_score"].tolist()
mean = statistics.mean(data)
stdev = statistics.stdev(data)
#print(mean)
dataset = []
for x in range(0,50):
    random_index = random.randint(0,len(data))
    value = data[random_index]
    dataset.append(value)
mean2 = statistics.mean(dataset)
stdev2 = statistics.stdev(dataset)
print("Mean of sampling distribution is",mean2)
print("Standard deviation of sampling distribution is",stdev2)

mean3 = mean-mean2
zscore = mean3/stdev
print(zscore)

#fig = ff.create_distplot([dataset],["Math_score"])
#fig.add_trace(go.Scatter(x=[mean,mean],y=[0,2],mode="lines",name="mean"))
#fig.show()