import sys
def Cantor(a,N):
    if len(a) <= 1:
        return a
    else:
        N -= 1
        side = Cantor('-'*3**N,N)
        space = ' '*3**N
        return merge(side,space)
def merge(side,space):
    return(side+space+side)
for line in sys.stdin:
    N = int(line)
    X = '-'*3**N
    print(Cantor(X,N))