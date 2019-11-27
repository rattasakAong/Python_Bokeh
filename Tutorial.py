from bokeh.plotting import figure, output_file, show
import pandas
from bokeh.models import ColumnDataSource
from bokeh.palettes import Spectral5


df=pandas.read_csv("Bokeh-Data-Visualization/FactoryData.csv")

# print(df)
info = ColumnDataSource(data=dict(df,color=Spectral5))
output_file("lines.html")

p=figure(title="จำนวนโรงงานในประเทศไทย", x_range=df["Region"],toolbar_location=None,plot_height=250)
p.vbar(x="Region",top="Factory", width=0.5, color='color', legend='Region', source=info)
p.legend.orientation="horizontal"
p.legend.location="top_center"
show(p)

