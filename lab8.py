
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
