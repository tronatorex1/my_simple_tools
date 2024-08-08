# These are examples on how to create simple graphs using matplotlib
#   No use of any other venonous lib (eg Seaborn), just matplotlib

# 1
import matplotlib.pyplot as plt 
# data to display on plots 
x = [3, 1, 3] 
y = [3, 2, 1] 

# This will plot a simple line chart with elements of x as x axis and y as y axis
plt.plot(x, y)
plt.title("Line Chart")

# Adding the legends
plt.legend(["This is the legend"])
plt.show()

# This will plot a simple bar chart
plt.plot(x, y)
plt.plot_date(x, y)

# 2 data to display on plots 
x = [3, 1, 3, 12, 2, 4, 4] 
y = [3, 2, 1, 4, 5, 6, 7]
z = [0, 0.7, 0.1, 4, 0.5, 1.6, 0.7]
plt.bar(x, y)
plt.title("Bars")
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.show()

# 3 Stacked! with X, Y, colors value
plt.stackplot(x, y, z, colors =['r', 'b'])
plt.show()

# 4 Pie
plt.title("Pie chart")
plt.pie(x)
plt.show()

#   with explode segments: highlight plots
e  = (0.1, 0, 0, 0, 0.5, 0, 0) # tuple, keep values under 1
plt.pie(x, explode = e)
plt.title("Pie chart")
plt.show()

# 5 3D plots
# Creating the figure object
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]
z = [1, 8, 27, 64, 125]
fig = plt.figure()
ax = plt.axes(projection = '3d')
ax.plot3D(z, y, x) 
plt.show()