#bfs-Uninformed search
grp={"14":["12","16"],
     "12":["10","13"],
     "16":["15","17"],
     "10":["2"],
     "13":["11"],
     "15":["1"],
     "17":["16"],
     "2":[],
     "11":[],
     "1":[]
     }
vis=[]
que=[]
def bfs(grp,node,vis):
  vis.append(node)
  que.append(node)
  while que:
    s=que.pop(0)
    print(s,end=" ")
    for neighbour in grp[s]:
      if neighbour not in vis:
        vis.append(neighbour)
        que.append(neighbour)
print("THE RESULT OF UN-INFORMEND SEARCH IS : ")  
bfs(grp,"14",vis)
