import pandas as pd
from sklearn.cluster import AgglomerativeClustering
import plotly.express as px
import os

PATH = os.path.join(os.path.dirname(__file__), "day8_1.txt")

data = pd.read_csv(PATH, header=None, delimiter=",")

model = AgglomerativeClustering(n_clusters=3, linkage="single", metric = "manhattan")
data["cluster"] = model.fit_predict(data)

fig = px.scatter_3d(data, x = 0, y = 1, z=2, color="cluster")
fig.show()
