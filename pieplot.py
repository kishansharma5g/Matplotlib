#                                  *** PIE PLOT ***

# import matplotlib.pyplot as plt

# x= [10,35,67,30,56,88]

# plt.title("PIE PLOT",fontsize = 20)
# plt.pie(x)
# plt.show()



# use of labels :->

# import matplotlib.pyplot as plt

# x= [10,20,30,40]
# y = ["c","c++","java","python"]
# c = ["g","k","b","y"]

# plt.title("PIE PLOT",fontsize = 20)
# plt.pie(x,labels = y,colors = c)
# plt.show()



# use of explode :->

# import matplotlib.pyplot as plt

# x= [10,20,30,40]
# y = ["c","c++","java","python"]
# c = ["g","k","b","y"]
# ex = [0.4,0.0,0.0,0.0]

# plt.title("PIE PLOT",fontsize = 20)
# plt.pie(x,labels = y,colors = c,explode = ex)
# plt.show()



# use of autopct :->

# import matplotlib.pyplot as plt

# x= [10,20,30,40]
# y = ["c","c++","java","python"]
# c = ["g","r","b","y"]
# ex = [0.4,0.0,0.0,0.0]

# plt.title("PIE PLOT",fontsize = 20)
# plt.pie(x,labels = y,colors = c,explode = ex,autopct = "%0.1f%%")
# plt.show()



# use of shadow :->

# import matplotlib.pyplot as plt

# x= [10,20,30,40]
# y = ["c","c++","java","python"]
# c = ["g","r","b","y"]
# ex = [0.4,0.0,0.0,0.0]

# plt.title("PIE PLOT",fontsize = 20)
# plt.pie(x,labels = y,colors = c,explode = ex,autopct = "%0.1f%%",shadow = True)
# plt.show()



# use of radius :->

# import matplotlib.pyplot as plt

# x= [10,20,30,40]
# y = ["c","c++","java","python"]
# c = ["g","r","b","y"]
# ex = [0.4,0.0,0.0,0.0]

# plt.title("PIE PLOT",fontsize = 20)
# plt.pie(x,labels = y,colors = c,explode = ex,
#         autopct = "%0.1f%%",shadow = True,radius = 1.3)
# plt.show()



# use of labeldistance :->

# import matplotlib.pyplot as plt

# x= [10,20,30,40]
# y = ["c","c++","java","python"]
# ex = [0.4,0.0,0.0,0.0]

# plt.title("PIE PLOT",fontsize = 20)
# plt.pie(x,labels = y,explode = ex,
#         autopct = "%0.1f%%",labeldistance = 1.4)
# plt.show()



# use of startangle :->

# import matplotlib.pyplot as plt

# x= [10,20,30,40]
# y = ["c","c++","java","python"]
# ex = [0.4,0.0,0.0,0.0]

# plt.title("PIE PLOT",fontsize = 20)
# plt.pie(x,labels = y,explode = ex,
#         autopct = "%0.1f%%",startangle = 180)
# plt.show()



# use of textprops :->

# import matplotlib.pyplot as plt

# x= [10,20,30,40]
# y = ["c","c++","java","python"]
# ex = [0.4,0.0,0.0,0.0]

# plt.title("PIE PLOT",fontsize = 20)
# plt.pie(x,labels = y,explode = ex,
#         autopct = "%0.1f%%",textprops = {"fontsize":20})
# plt.show()



# use of counterlock :->

# import matplotlib.pyplot as plt

# x= [10,20,30,40]
# y = ["c","c++","java","python"]
# ex = [0.4,0.0,0.0,0.0]

# plt.title("PIE PLOT",fontsize = 20)
# # plt.pie(x,labels = y,explode = ex,
# #         autopct = "%0.1f%%",textprops = {"fontsize":20},counterclock = True)

# plt.pie(x,labels = y,explode = ex,
#         autopct = "%0.1f%%",textprops = {"fontsize":20},
#         counterclock = False)
# plt.show()



# use of wedgeprops :->

# import matplotlib.pyplot as plt

# x= [10,20,30,40]
# y = ["c","c++","java","python"]
# ex = [0.4,0.0,0.0,0.0]

# plt.title("PIE PLOT",fontsize = 20)

# # plt.pie(x,labels = y,explode = ex,
# #         autopct = "%0.1f%%",textprops = {"fontsize":20},
# #         counterclock = False,wedgeprops = {"linewidth": 100})

# # plt.pie(x,labels = y,explode = ex,
# #         autopct = "%0.1f%%",textprops = {"fontsize":20},
# #         counterclock = False,wedgeprops = {"linewidth": 100,"width":4})

# plt.pie(x,labels = y,explode = ex,
#         autopct = "%0.1f%%",textprops = {"fontsize":20},
#         counterclock = False,wedgeprops = {"linewidth":4,"edgecolor":"m"})
# plt.show()




# use of rotatelabel :->

# import matplotlib.pyplot as plt

# x= [10,20,30,40]
# y = ["c","c++","java","python"]
# ex = [0.4,0.0,0.0,0.0]

# # plt.title("PIE PLOT",fontsize = 20)
# # plt.pie(x,labels = y,explode = ex,
# #         autopct = "%0.1f%%",textprops = {"fontsize":20},rotatelabels = True)

# plt.title("PIE PLOT",fontsize = 20)
# plt.pie(x,labels = y,explode = ex,
#         autopct = "%0.1f%%",textprops = {"fontsize":20},rotatelabels = False)

# plt.show()



# use of legend() function :->

# import matplotlib.pyplot as plt

# x= [10,20,30,40]
# y = ["c","c++","java","python"]
# ex = [0.4,0.0,0.0,0.0]

# plt.title("PIE PLOT",fontsize = 20)
# plt.pie(x,labels = y,explode = ex,
#         autopct = "%0.1f%%",textprops = {"fontsize":20},rotatelabels = False)

# plt.legend(loc = 2)
# plt.show()



# dot pychart :->

import matplotlib.pyplot as plt

x= [10,20,30,40]
plt.pie([1])
plt.show()

