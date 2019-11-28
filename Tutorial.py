# from bokeh.plotting import figure, output_file, show
# import pandas
# from bokeh.models import ColumnDataSource,HoverTool
# from bokeh.palettes import Spectral5
#
#
# df=pandas.read_csv("Bokeh-Data-Visualization/FactoryData.csv")
# # print(df)
# info = ColumnDataSource(data=dict(df,color=Spectral5))
# output_file("lines.html")
#
# p=figure(title="จำนวนโรงงานในประเทศไทย", x_range=df["Region"],toolbar_location=None,plot_height=250)
# p.vbar(x="Region",top="Factory", width=0.5, color='color', legend='Region', source=info)
#
# hover=HoverTool(tooltips=([('ภูมิภาค', '@Region'),('จำนวน', '@Factory')]))
# p.add_tools(hover)
#
# p.legend.orientation="horizontal"
# p.legend.location="top_center"
# show(p)



# กราฟแนวตั้ง
from bokeh.plotting import figure, output_file, show
import pandas
from bokeh.models import ColumnDataSource,HoverTool
from bokeh.palettes import Spectral8


df=pandas.read_csv("Bokeh-Data-Visualization/ThaiData.csv")
# print(df)
info = ColumnDataSource(data=dict(df,color=Spectral8))
output_file("lines.html")

p=figure(title="รายได้ครัวเรือนแต่ละจังหวัด", y_range=df["City"], x_axis_label="รายได้ต่อเดือน", toolbar_location=None, plot_width=800, plot_height=600, tools="")

p.hbar(y='City', right='Salary', height=0.4, color='color', source=info)

hover=HoverTool()
hover.tooltips="""
        <img src='@Image' width='150px'/>
        <h3>@City</h3>
        <p>รายได้ : @Salary</p>
"""
p.add_tools(hover)

show(p)

