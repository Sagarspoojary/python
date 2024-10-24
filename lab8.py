
from bokeh.plotting import figure,output_file,show
x=[1,2,3,4,5]
y=[2,4,6,8,10]
output_file('line.html')
fig=figure(title='line plot',x_axis_label='x',y_axis_label='y')
fig.line(x,y)
show(fig)
from bokeh.plotting import figure,output_file,show
fig=figure(min_width=800,min_height=200)
fig.hbar(y=[2,4,6],height=1,left=0,right=[1,2,3],color='Cyan')
output_file('bar.html')
show(fig)
from bokeh.plotting import figure,output_file,show
fig=figure(min_width=800,min_height=200)
fig.vbar(x=[2,4,6],width=1,bottom=0,top=[10,8,4],color='Cyan')
output_file('vbar.html')
show(fig)
from bokeh.plotting import figure,output_file,show
p=figure(min_width=800,min_height=200)
p.patch(x=[1,3,2,4],y=[2,3,5,7],color='green')
output_file('patch.html')
show(p)
from bokeh.plotting import figure,output_file,show
p=figure(min_width=800,min_height=400)
p.scatter([1,4,3,2,5],[6,5,2,4,7],marker='circle',size=20,fill_color='green')
output_file('scatter.html')
show(p)
from bokeh.plotting import figure,output_file,show
p=figure(min_width=800,min_height=400)
x=[1,2,5,7,9]
y1=[2,5,4,6,8]
y2=[5,9,11,12,15]
p.varea(x=x,y1=y1,y2=y2)
output_file ('area.html')
show(p)
from bokeh.plotting import figure,output_file,show
from math import pi
p=figure(min_width=400,min_height=400)
p.rect(x=[1,2,3],y=[1,2,3],width=0.2,height=40,color='Green',angle=pi/3,height_units='screen')
output_file ('Rectangle.html')
show(p)
import numpy as np
from bokeh.plotting import figure,output_file,show
from math import pi
x=np.linspace(0,4*np.pi,100)
y=np.sin(x)
p=figure()
p.circle(x,y,legend_label="sin(x)")
p.line(x,y,legend_label="sin(x)")
p.line(x,2*y,legend_label="2*sin(x)",line_dash=[10,5],line_color='orange',line_width=2)
p.square(x,3*y,legend_label="3*sin(x)",fill_color=None,line_color='Green')
p.line(x,3*y,legend_label="3*sin(x)",line_color='green')
p.legend.location='bottom_left'
output_file ('Rectangle.html')
show(p)
