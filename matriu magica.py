def quadrat_màgic(l1, l2, l3):
    l1 = ()
    l2 = ()
    l3 = ()
    if len(l1) == len(l2) == len(l3):
        return True
    if sum(l1) == sum(l2) == sum(l3):
        return True

l1 = [6,1,8]
l2 = [7,5,3]
l3 = [2,9,4]
quadrat_màgic[l1,l2,l3]
        