#                        *** HISTOGRAM PLOT ***

# import matplotlib.pyplot as plt
# x = []

# plt.hist(x,y)
# plt.show()


#without bins parameter graph:->

import matplotlib.pyplot as plt
import numpy as np
import random #data take as randomly usimg random function

x = np.random.randint(10,60,(50))
no = [15,39,39,15,28,58,54,51,27,27,22,45,34,50,16,24,38,28,38,30,27,51,54,40,14,43,34,50,20,43,48,59,52,13,50,53,17,36,57,54,15,49,25,58,59,13,34,46
,17,25]

# print(x)
plt.title("HISTOGRAM",fontsize = 30)
plt.xlabel("x-axis ->",fontsize = 15)
plt.ylabel("y-axis ->",fontsize = 15)
plt.hist(no,color = "g",edgecolor = "k",bins = l)
plt.show()



#using bins parameter graph:->

import matplotlib.pyplot as plt
import numpy as np
import random #data take as randomly usimg random function

x = np.random.randint(10,60,(50))
no = [15,39,39,15,28,58,54,51,27,27,22,45,34,50,16,24,38,28,38,30,27,51,54,40,14,43,34,50,20,43,48,59,52,13,50,53,17,36,57,54,15,49,25,58,59,13,34,46
,17,25]
l = [10,20,30,40,50,60]

# print(x)
plt.title("HISTOGRAM",fontsize = 30)
plt.xlabel("x-axis ->",fontsize = 15)
plt.ylabel("y-axis ->",fontsize = 15)
plt.hist(no,color = "g",edgecolor = "k",bins = l)
plt.show()


import matplotlib.pyplot as plt
import numpy as np
import random #data take as randomly usimg random function

x = np.random.randint(10,60,(50))
no = [15,39,39,15,28,58,54,51,27,27,22,45,34,50,16,24,38,28,38,30,27,51,54,40,14,43,34,50,20,43,48,59,52,13,50,53,17,36,57,54,15,49,25,58,59,13,34,46
,17,25]
# l = [10,20,30,40,50,60]

# print(x)
plt.title("HISTOGRAM",fontsize = 30)
plt.xlabel("x-axis ->",fontsize = 15)
plt.ylabel("y-axis ->",fontsize = 15)
plt.hist(no,"auto",(10,150),color = "g",edgecolor = "k")
plt.show()



#use of cumulative :->

import matplotlib.pyplot as plt
import numpy as np
import random #data take as randomly usimg random function

x = np.random.randint(10,60,(50))
no = [15,39,39,15,28,58,54,51,27,27,22,45,34,50,16,24,38,28,38,30,27,51,54,40,14,43,34,50,20,43,48,59,52,13,50,53,17,36,57,54,15,49,25,58,59,13,34,46
,17,25]
# l = [10,20,30,40,50,60]

# print(x)
plt.title("HISTOGRAM",fontsize = 30)
plt.xlabel("x-axis ->",fontsize = 15)
plt.ylabel("y-axis ->",fontsize = 15)
plt.hist(no,"auto",color = "g",edgecolor = "k",cumulative = -1)
plt.show()



# use of bottom :->

import matplotlib.pyplot as plt
import numpy as np
import random #data take as randomly usimg random function

x = np.random.randint(10,60,(50))
no = [15,39,39,15,28,58,54,51,27,27,22,45,34,50,16,24,38,28,38,30,27,51,54,40,14,43,34,50,20,43,48,59,52,13,50,53,17,36,57,54,15,49,25,58,59,13,34,46
,17,25]
# l = [10,20,30,40,50,60]

# print(x)
plt.title("HISTOGRAM",fontsize = 30)
plt.xlabel("x-axis ->",fontsize = 15)
plt.ylabel("y-axis ->",fontsize = 15)
# plt.hist(no,"auto",color = "g",edgecolor = "k",bottom = 20)
# plt.hist(no,"auto",color = "g",edgecolor = "k",cumulative = -1,bottom = "20")
# plt.hist(no,"auto",color = "g",edgecolor = "k",align = "left")
# plt.hist(no,"auto",color = "g",edgecolor = "k",align = "right")
plt.hist(no,"auto",color = "g",edgecolor = "k",align = "mid")
plt.show()



# types of historam 

import matplotlib.pyplot as plt
import numpy as np
import random #data take as randomly usimg random function

x = np.random.randint(10,60,(50))
no = [15,39,39,15,28,58,54,51,27,27,22,45,34,50,16,24,38,28,38,
    30,27,51,54,40,14,43,34,50,20,43,48,59,52,13,50,53,17,36,57
    ,54,15,49,25,58,59,13,34,46
,17,25]


# print(x)
plt.title("HISTOGRAM",fontsize = 30)
plt.xlabel("x-axis ->",fontsize = 15)
plt.ylabel("y-axis ->",fontsize = 15)

# type - 1 :->
# plt.hist(no,color = "g",edgecolor = "k",histtype = "step")
# plt.hist(no,color = "g",edgecolor = "k",histtype = "stepfilled")

# type - 2 :->

# plt.hist(no,color = "g",edgecolor = "k",histtype = "bar")
# plt.hist(no,color = "g",edgecolor = "k",histtype = "barstacked")
plt.show()



# use of orientation :->

import matplotlib.pyplot as plt
import numpy as np
import random #data take as randomly usimg random function

x = np.random.randint(10,60,(50))
no = [15,39,39,15,28,58,54,51,27,27,22,45,34,50,16,24,38,28,38,30,27,51,54,40,14,43,34,50,20,43,48,59,52,13,50,53,17,36,57,54,15,49,25,58,59,13,34,46
,17,25]
# l = [10,20,30,40,50,60]

# print(x)
plt.title("HISTOGRAM",fontsize = 30)
plt.xlabel("x-axis ->",fontsize = 15)
plt.ylabel("y-axis ->",fontsize = 15)
# plt.hist(no,color = "g",edgecolor = "k",orientation = "vertical")
plt.hist(no,color = "g",edgecolor = "k",orientation = "horizontal")

plt.show()



# use of rwidth :->

import matplotlib.pyplot as plt
import numpy as np
import random #data take as randomly usimg random function

x = np.random.randint(10,60,(50))
no = [15,39,39,15,28,58,54,51,27,27,22,45,34,50,16,24,38,28,38,30,27,51,54,40,14,43,34,50,20,43,48,59,52,13,50,53,17,36,57,54,15,49,25,58,59,13,34,46
,17,25]
# l = [10,20,30,40,50,60]

# print(x)
plt.title("HISTOGRAM",fontsize = 30)
plt.xlabel("x-axis ->",fontsize = 15)
plt.ylabel("y-axis ->",fontsize = 15)
plt.hist(no,color = "g",edgecolor = "k",rwidth = 0.3)
plt.show()



# use of log :-> logrithmic graph

import matplotlib.pyplot as plt
import numpy as np
import random #data take as randomly usimg random function

x = np.random.randint(10,60,(50))
no = [15,39,39,15,28,58,54,51,27,27,22,45,34,50,16,24,38,28,38,30,27,51,54,40,14,43,34,50,20,43,48,59,52,13,50,53,17,36,57,54,15,49,25,58,59,13,34,46
,17,25]
# l = [10,20,30,40,50,60]

# print(x)
plt.title("HISTOGRAM",fontsize = 30)
plt.xlabel("x-axis ->",fontsize = 15)
plt.ylabel("y-axis ->",fontsize = 15)
plt.hist(no,color = "g",edgecolor = "k",log = True)
plt.show()



# use of axvline() function :->

import matplotlib.pyplot as plt
import numpy as np
import random #data take as randomly usimg random function

x = np.random.randint(10,60,(50))
no = [15,39,39,15,28,58,54,51,27,27,22,45,34,50,16,24,38,28,38,30,27,51,54,40,14,43,34,50,20,43,48,59,52,13,50,53,17,36,57,54,15,49,25,58,59,13,34,46
,17,25]

# print(x)
plt.title("HISTOGRAM",fontsize = 30)
plt.xlabel("x-axis ->",fontsize = 15)
plt.ylabel("y-axis ->",fontsize = 15)
plt.hist(no,color = "g",edgecolor = "k",)
plt.axvline(50,color = "r",label = "Axvline")
plt.legend()# use for label prameter
plt.show()



# use of grid() function :->

import matplotlib.pyplot as plt
import numpy as np
import random #data take as randomly usimg random function

x = np.random.randint(10,60,(50))
no = [15,39,39,15,28,58,54,51,27,27,22,45,34,50,16,24,38,28,38,30,27,51,54,40,14,43,34,50,20,43,48,59,52,13,50,53,17,36,57,54,15,49,25,58,59,13,34,46
,17,25]

# print(x)
plt.title("HISTOGRAM",fontsize = 30)
plt.xlabel("x-axis ->",fontsize = 15)
plt.ylabel("y-axis ->",fontsize = 15)
plt.hist(no,color = "g",edgecolor = "k",)
plt.axvline(50,color = "r",label = "Axvline")
plt.legend()# use for label prameter
plt.grid()
plt.show()