import plotly
import plotly.graph_objs as go
import numpy as np

N = 10000

x_list = []
y_list = []

for i in range(N):
    x_value = np.random.randint(-500, 500)
    y_value = np.random.randint(-500, 500)
    x_list.append(x_value)
    y_list.append(y_value)

trc = go.Scatter(
    x=x_list,
    y=y_list,
    mode='markers'
)

data = [trc]
plotly.offline.plot(data, filename='Dots')
