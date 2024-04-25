# graph to list and 

edge_list = [ ("a","b",2),("b","d",4),("d","e",5),("c","e",1),("c","d",6),("a","c",3)]
v_set = set()
tot = 0 
for eq in edge_list:
  tot+=eq[2]
  v_set.add(eq[0])
  v_set.add(eq[1])
  
# print("no of vertces :",len(v_set))
print("total  :" , tot)


adj_list = {v:[] for v in v_set}
for eq in edge_list:
  adj_list[eq[0]].append((eq[1],eq[2]))
  adj_list[eq[1]].append((eq[0],eq[2]))
  
print("adj list:" , adj_list )

for x,y in adj_list.items():
  print(x ,":", y)

