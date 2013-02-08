def inv (li):
	li.sort()
	rand_value = random.random()
	sumi =0
	i=0
	while i < len(li) and sumi<rand_value:
		sumi += li[i][1]
		i+=1
	print(rand_value)
	return(li[i-1])







def inv (li,no_matches):
	li.sort()
	rand_value = random.random()
	sumi =0
	i=0
	while i < len(li) and sumi<rand_value:
		sumi += li[i][1]
		i+=1
	print(rand_value)
	if players[0] == li[i-1][0]:
		no_matches[0]+=1
	elif players[1] == li[i-1][0]:
		no_matches[1] +=1
	elif players[2] == li[i-1][0]:
		no_matches[2] +=1
	elif players[3] == li[i-1][0]:
		no_matches[3] +=1
	elif players[4] == li[i-1][0]:
		no_matches[4]+=1
	elif players[5] == li[i-1][0]:
		no_matches[5]+=1
	return([li[i-1],no_matches])
