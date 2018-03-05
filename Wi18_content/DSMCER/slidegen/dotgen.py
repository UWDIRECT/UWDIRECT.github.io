l1 = ["l1_1", "l1_2", "l1_3"]
l2 = ["l2_1", "l2_2", "l2_3", "l2_4"]
o = ["output"]

for i in l1:
    for j in l2:
        print(" %s -> %s" % (i, j))

for i in l2:
    for j in o:
        print(" %s -> %s" % (i, j))

