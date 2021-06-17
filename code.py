import pandas as pd
import csv
import plotly.figure_factory as ff
import statistics
import random
import plotly.graph_objects as go

df = pd.read_csv(r"/Users/anshul/Desktop/Class 110/data.csv")
data = df["average"].tolist()
mean = statistics.mean(data)
print(mean)
#fig = ff.create_distplot([data],["average"],show_hist=False)
#fig.show()

stdev = statistics.stdev(data)
print(stdev)
dataset = []
for x in range(0,100):
    random_index = random.randint(0,len(data))
    value = data[random_index]
    dataset.append(value)

mean2 = statistics.mean(dataset)
stdev2 = statistics.stdev(dataset)
print(mean2)
print(stdev2)
fig = ff.create_distplot([dataset],["average"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean2,mean2],y=[0,2],mode="lines",name="mean"))
fig.show()