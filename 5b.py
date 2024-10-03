import matplotlib.pyplot as plt
exp_vals=[1400,600,300,410,250]
exp_labels=['home rent','food','phone/internet bill','car','other utilities']
plt.pie(exp_vals,labels=exp_labels,shadow=True)
plt.show()
plt.pie(exp_vals,labels=exp_labels,shadow=True,autopct='%0.1f%%,radius=1.5')
plt.show()
plt.pie(exp_vals,labels=exp_labels,shadow=True,autopct='%1.1f%%,radius=1.5',explode=[0,0,0,0.2,0.1])
plt.show()
plt.pie(exp_vals,labels=exp_labels,shadow=True,autopct='%1.1f%%,radius=1.5',explode=[0,0,0,0.1,0.2],counterclock=False,startangle=30)
plt.show()
