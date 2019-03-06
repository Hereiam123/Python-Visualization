from bokeh.plotting import figure, output_file, show
import pandas

# Read in csv
df = pandas.read_csv('cars.csv')

car = df['Car']
hp = df['Horsepower']

# output to static HTML file
output_file("lines.html", title="line plot example")

# create a new plot with a title and axis labels
p = figure(y_range=car, plot_width=800, plot_height=600, title="Cars with Top Horsepower",
           x_axis_label='Horsepower', tools="")

# add a line renderer with legend and line thickness
p.hbar(
    y=car, right=hp, left=0, height=0.4, color='orange', fill_alpha=0.5
)

# show the results
show(p)
