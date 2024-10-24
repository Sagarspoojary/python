from bokeh.plotting import figure,output_file,show
p=figure(min_width=800,min_height=200)
p.patch(x=[1,3,2,4],y=[2,3,5,7],color='green')
output_file('patch.html')
show(p)