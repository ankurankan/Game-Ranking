import math

def program(player,theta1,theta2):
	prob_arr = []
	sum_arr = []
	for i in (range(len(graph[player]))):
		power = ((theta1*abs((players[player] - players[i])) + theta2* graph[player][i]))/400
		print(power)
		sum_arr.append(math.exp(power))
	print(sum_arr)
	total_sum = sum(sum_arr)
	for i in sum_arr:
		prob_arr.append(i/total_sum)
	print(prob_arr)
	print(sum(prob_arr))






def program(player,theta1,theta2,no_matches):
	prob_arr = []
	sum_arr = []
	for i in (range(len(graph[player]))):
		power = ((theta1*abs((players[player] - players[i])) + theta2* graph[player][i]))/400
		sum_arr.append(math.exp(power))
	print(sum_arr)
	total_sum = sum(sum_arr)
	for i in range(len(sum_arr)):
		temp_li = [players[i],(sum_arr[i]/total_sum)]
		prob_arr.append(temp_li)
	selected,no_matches = inv(prob_arr,no_matches)
	graph[player][players.index(selected[0])] +=1
	graph[players.index(selected[0])][player] +=1
	print(graph)
	return(no_matches)
