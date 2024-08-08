# These are examples on how to use Seaborn
#   Seaborn is based on matplotlib (as base to display graphs) and adds better looking representations of data, less control yet

# 1
# importing packages 
import seaborn as sns 
import matplotlib.pyplot as plt 

# loading dataset 
data = sns.load_dataset("iris") 

# draw lineplot 
sns.lineplot(x="sepal_length", y="sepal_width", data=data) 
sns.set_style("ticks") # this sets the background's grid style (more or less defined, not colors)
sns.set_context("talk") # minor styles changes relates to graph size (???)
# setting the title using Matplotlib 
plt.title('Title using Matplotlib Function') 
plt.show() # THIS IS THE KEY COMMAND TO SHOW THE ACTUAL GRAPH!!!


# 2
# importing packages  
import seaborn as sns  
# loading dataset  
data = sns.load_dataset("iris")  
# draw lineplot  
sns.lineplot(x="sepal_length", y="sepal_width", data=data)

# setting the default color palette 
sns.set_palette('vlag') 

plt.title('') 
plt.show() # THIS IS THE KEY COMMAND TO SHOW THE ACTUAL GRAPH!!!

# 3 Multi graphs on top
# importing packages 
import seaborn as sns 
import matplotlib.pyplot as plt 
# loading dataset 
data = sns.load_dataset("iris") 
def graph(): 
	sns.lineplot(x="sepal_length", y="sepal_width", data=data) 
# adding the subplots 
axes1 = plt.subplot2grid ( 
(7, 1), (0, 0), rowspan = 2, colspan = 1) 
graph()
axes2 = plt.subplot2grid ( 
(7, 1), (2, 0), rowspan = 2, colspan = 1) 
graph() 
axes3 = plt.subplot2grid ( 
(7, 1), (4, 0), rowspan = 2, colspan = 1) 
graph()
plt.show()


# 4 Multi graphs concatenated
# importing packages 
import seaborn as sns 
import matplotlib.pyplot as plt 
# loading dataset 
data = sns.load_dataset("iris") 
plot = sns.FacetGrid(data, col="species") 
plot.map(plt.plot, "sepal_width") 
plt.show()
