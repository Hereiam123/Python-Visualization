from bokeh.plotting import figure, output_file, show, ColumnDataSource, save
from bokeh.models.tools import HoverTool
import pandas

# Read in csv
df = pandas.read_csv('cars.csv')

# Create ColumnDataSource from data frame
source = ColumnDataSource(df)

# output to static HTML file
output_file("lines.html", title="line plot example")

# Car list
car_list = source.data['Car'].tolist()

# create a new plot with a title and axis labels
p = figure(y_range=car_list, plot_width=800, plot_height=600, title="Cars with Top Horsepower",
           x_axis_label='Horsepower', tools="pan, box_select, zoom_in, zoom_out, save, reset")

# add a line renderer with legend and line thickness
p.hbar(
    y="Car", right="Horsepower", left=0, height=0.4, color='orange', fill_alpha=0.5, source=source
)

# Add Tooltips
hover = HoverTool()
hover.tooltips = """
    <div>
    <h3>@Car</h3>
        <div><strong>Price: </strong>@Price</div>
        <div><strong>HP: </strong>@Horsepower</div>
        <div><img src="@Image" alt="" width="200"/></div>
    </div>
"""
p.add_tools(hover)
# show the results
# show(p)

# Save file
save(p)
