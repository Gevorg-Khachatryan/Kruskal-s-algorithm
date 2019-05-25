def kruskal(graph):
    assert type(graph)==dict

    nodes = graph.keys()
    visited = set()
    path = []
    next = None

    while len(visited) < len(nodes):

        for s in nodes:
            distance = 4
            for d in nodes:
                if s in visited and d in visited or s == d:
                    continue
                if graph[s][d] < distance:
                    distance = graph[s][d]
                    pre = s
                    next = d

        path.append((pre, next))
        visited.add(pre)
        visited.add(next)

    return path

s1_s2, s1_s3, s1_s4, s1_s5= map(int, input("Enter s1_s2 ,s1_s3, s1_s4 , s1_s5  : ").split())
s2_s3, s2_s4, s2_s5=map(int, input("Enter s2_s5 , s2_s10 , s2_s5 : ").split())
s3_s4,s3_s5=map(int,input("Enter s3_s4 , s3_s5 : ").split())
s4_s5=int(input("Enter s4_s5 : "))

if __name__ == '__main__':
    graph_dict = {  "s1":{"s1": 0, "s2": s1_s2, "s3": s1_s3, "s4": s1_s4, "s5":s1_s5},
                    "s2":{"s1": s1_s2, "s2": 0, "s3": s2_s3, "s4": s2_s4, "s5":s2_s5},
                    "s3":{"s1": s1_s3, "s2": s2_s3, "s3": 0, "s4":s3_s4, "s5":s3_s5},
                    "s4":{"s1": s1_s4, "s2": s2_s4, "s3": s3_s4, "s4":0, "s5":s4_s5},
                    "s5":{"s1": s1_s5, "s2": s2_s5, "s3": s3_s5, "s4":s4_s5, "s5":0},
    }

    path = kruskal(graph_dict)
    print (path)

