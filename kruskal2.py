
def Dict(NumOfPeak):
    x = []
    z=[]
    for i in range(NumOfPeak):
        y = 's' + str(i + 1)
        x.append(y)
    for i in range(NumOfPeak):
        y = 's' + str(i + 1)
        z.append([y,dict.fromkeys(x)])
    dic=dict(z)
    return dic
def DictPrint(x):
    for peak in x.keys():
            print (peak,x[peak])
def kruskal(graph):
    assert type(graph)==dict
    nodes = graph.keys()
    visited = set()
    path = []
    next = None
    while len(path) < len(nodes)-1:
        for s in nodes:
            distance = 0
            for d in sum[s]:
                if s==d:
                    sum[s][d]=0
                if sum[s][d]==None:
                    print("Enter ",s,d)
                    sum[s][d]=int(input(":"))
                    sum[d][s]=sum[s][d]
                pathx = (s, d)
                pathy = (d, s)
                if pathx in path or pathy in path or s == d:
                    continue
                if graph[s][d] > distance and distance!=0:
                    continue

                distance = graph[s][d]
                pre = s
                next = d
            if len(path)==len(nodes)-1:
                continue
            path.append((pre, next))
            visited.add(pre)
            visited.add(next)

    return path
num=int(input("Enter num of peak:"))
sum=Dict(num)
DictPrint(sum)
path = kruskal(sum)
print('***********')
print (path)
DictPrint(sum)
