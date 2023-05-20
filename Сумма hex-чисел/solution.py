a = "fed"
b = "13"
def conv(n,ri,ro):
    digs="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    acc=0
    for a in n:
        k=digs.find(a)
        acc=acc*ri+k
    res=""
    while(acc>0):
        k=acc%ro
        res=digs[k]+res
        acc=acc//ro
    return res