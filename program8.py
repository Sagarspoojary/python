from bokeh.plotting import figure,output_file,show
x=[1,2,3,4,5]
y=[2,4,6,8,10]
output_file('line.html')
fig=figure(title='Line plot',x_axis_label='x',y_axis_label='y')
fig.line(x,y)
show(fig)