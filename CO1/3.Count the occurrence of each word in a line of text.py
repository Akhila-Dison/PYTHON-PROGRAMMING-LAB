k="In its most general sense, the term world refers to the totality of entities, to the whole of reality or to everything that is"
h=[]
for i in k.split(" "):
	if i not in h:
		h.append(i)
for i in h:
	print(i,":",k.split(" ").count(i))
