"""
plot using seaborn library
"""

print("iris_data")
print("-"*20)
# -------------

import pandas as pd

iris_data = pd.read_csv("Iris.csv")
print(iris_data.head(5)) # Top 5 rows

print("#"*40, end="\n\n")
#########################

print("Graph-1")
print("-"*20)
# -------------

import seaborn as sns
import matplotlib.pyplot as plt
sns.lineplot(x='SepalLengthCm', y='SepalWidthCm', data=iris_data)
plt.show()
print("#"*40, end="\n\n")
#########################

print("Graph-2")
print("-"*20)
# -------------

import seaborn as sns
import matplotlib.pyplot as plt
sns.violinplot(x='SepalLengthCm', y='SepalWidthCm', data=iris_data)
plt.show()

print("#"*40, end="\n\n")
#########################

print("Graph-3")
print("-"*20)
# -------------

import seaborn as sns
import matplotlib.pyplot as plt
sns.lineplot(x='SepalLengthCm', y='SepalWidthCm', data=iris_data)
plt.savefig("mygraph_1.png")
print("""
Graph saved in
mygraph_1.png
please check
""")
print("#"*40, end="\n\n")
#########################

print("Graph-4")
print("-"*20)
# -------------

import seaborn as sns
import matplotlib.pyplot as plt
my_graph = sns.FacetGrid(iris_data, col="Species")
my_graph.map(plt.plot, "SepalWidthCm")
plt.show()

print("#"*40, end="\n\n")
#########################


print("Graph-5")
print("-"*20)
# -------------

import seaborn as sns
import matplotlib.pyplot as plt
my_graph = sns.PairGrid(iris_data)
my_graph.map(plt.plot)
plt.show()

print("#"*40, end="\n\n")
#########################