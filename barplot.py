#                                            BAR PLOT

# import matplotlib.pyplot as plt

# x = ["python", "c++", "dsa"]
# y = [80, 67, 98]

# plt.xlabel("name",fontsize=20)
# plt.ylabel("number",fontsize=20)
# plt.title("graph",fontsize=20)

# # c = ["r","g","b"]
# # k = ["b","r","y"]

# # plt.bar(x,y,width=0.5,color=c,align="edge",edgecolor=k,linewidth=8,linestyle=":",alpha=0.5)
# plt.bar(x,y,width=0.5,color="r",edgecolor="r",label="graph")
# plt.legend()
# plt.show()



# import matplotlib.pyplot as plt

# x = ["python", "c++", "dsa"]
# y = [80, 67, 98]

# plt.xlabel("name",fontsize=20)
# plt.ylabel("number",fontsize=20)
# plt.title("graph",fontsize=20)

# c = ["r","g","b"]
# k = ["b","r","y"]

# plt.bar(x,y,width=0.5,color=c,align="edge",edgecolor=k,linewidth=8,linestyle=":",alpha=0.5)
# plt.bar(x,y,width=0.5,color="r",edgecolor="r",label="graph")
# plt.legend()
# plt.show()



# import matplotlib.pyplot as plt

# x = ["python", "c++", "dsa"]
# y = [80, 67, 98]
# z = [40,35,67]

# plt.xlabel("name",fontsize=20)
# plt.ylabel("number",fontsize=20)
# plt.title("graph",fontsize=20)

# # c = ["r","g","b"]
# # k = ["b","r","y"]

# plt.bar(x,y,width=0.5,color="g",label="graph1")
# plt.bar(x,z,width=0.5,color="r",label="graph2")
# plt.legend()
# plt.show()



# import matplotlib.pyplot as plt
# import numpy as np

# x = ["python", "c++", "dsa"]
# y = [80, 67, 98]
# z = [40,35,67]

# width=0.2
# p=np.arange(len(x))
# p1=[j+width for j in p]

# plt.xlabel("name",fontsize=20)
# plt.ylabel("number",fontsize=20)
# plt.title("graph",fontsize=20)

# # c = ["r","g","b"]
# # k = ["b","r","y"]

# plt.bar(p,y,width,color="g",label="graph1")
# plt.bar(p1,z,width,color="r",label="graph2")

# plt.xticks(p+width/2,x,rotation=20)
# plt.legend()
# plt.show()



# import matplotlib.pyplot as plt
# import numpy as np

# x = ["python", "c++", "dsa"]
# y = [80, 67, 98]
# z = [40,35,67]

# width=3
# p=np.arange(len(x))
# p1=[j+width for j in p]

# plt.xlabel("name",fontsize=20)
# plt.ylabel("number",fontsize=20)
# plt.title("graph",fontsize=20)

# # c = ["r","g","b"]
# # k = ["b","r","y"]

# plt.barh(p,y,width,color="g",label="graph1")
# plt.bar(p1,z,width,color="r",label="graph2")

# plt.xticks(p+width/2,x,rotation=20)
# plt.legend()
# plt.show()


import matplotlib.pyplot as plt
import numpy as np

x = ["python", "c++", "dsa"]
y = [80, 67, 98]
z = [40,35,67]

width=0.5
p=np.arange(len(x))
p1=[j+width for j in p]

plt.xlabel("name",fontsize=20)
plt.ylabel("number",fontsize=20)
plt.title("graph",fontsize=20)

# c = ["r","g","b"]
# k = ["b","r","y"]

plt.barh(p,y,width,color="g",label="graph1")
plt.barh(p1,z,width,color="r",label="graph2")

plt.xticks(p+width/2,x,rotation=20)
plt.legend()
plt.show()