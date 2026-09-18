# import matplotlib.pyplot as pp
# import numpy as np

# f = open("classify_ldiff.dat")
# d = []
# for i in f:
#   d.append([float(x) for x in i.split()])

# d = np.array(d)
# pp.plot(d[:,0])
# pp.plot(d[:,1])
# pp.plot([0,1000], [100, 100])
# pp.show()
# quit()


# import numpy as np
# import matplotlib.pyplot as pp
# j=[]
# s=[]
# with open("files/classify_sdiff.dat", "r") as f:
#     for line in f:
#         if not line.strip():
#             continue
#         j1, s1 = line.split()
#         j.append(int(j1))
#         s.append(int(s1))
# d1=np.array(j)
# d2=np.array(s)
# so1=pp.hist(d1,density=True,cumulative=True,histtype='step',bins=range(-1000,1000))
# so2=pp.hist(d2,density=True,cumulative=-1,histtype='step',bins=range(-1000,1000))
# a1=np.array(so1[0])
# a2=np.array(so2[0])
# c2=np.array(so2[1])
# pp.subplot(2,1,2)
# pp.plot(c2[:-1],a1+a2)
# pp.show()
# idx=np.argmin(a1+a2)
# print(c2[idx])
# quit()


#ДЕРЕВО ПРИНЯТИЯ РЕШЕНИЙ
# import numpy as np
# import matplotlib.pyplot as pp
# f = open("files/binary_rules.dat")
# d = []
# for s in f:
#     d.append([int(x) for x in s.split()])
# d=np.array(d)

# X = d[:,:-1]
# Y=d[:,-1]
# p0=Y.mean()
# print(p0)

# for i in range(5):
#     pi = Y[X[:,i]==1].mean()
#     print(i, pi)

# print('-------------------------------------')

# Y1 = Y[X[:,2]==1]
# X1= X[X[:,2]==1]
# p0=Y1.mean()
# print(p0)

# for i in range(5):
#     pi = Y1[X1[:,i]==1].mean()
#     print(i, pi)


# import numpy as np
# from sklearn.tree import DecisionTreeClassifier

# f = open("files/unknown_data.dat.short")
# d = []
# for l in f:
#     d.append([float(x) for x in l.split()])
# d = np.array(d)
# x = d[:, :-1]
# y = d[:, -1]
# clf = DecisionTreeClassifier()
# clf.fit(x, y)
# import graphviz
# from sklearn import tree

# dot_data = tree.export_graphviz(clf, out_file=None)
# graph = graphviz.Source(dot_data)
# graph.render("mytree")
