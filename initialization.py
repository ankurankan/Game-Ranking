import math
import random

def omega(a_1, a_2, mu, sigma):
    return(round(a_1*mu + a_2 * sigma, 6))

def match_select(fitness_score):
    prob = [[0 for i in range(5)] for j in range(5)]
    sumi = 0
    for i in range(4):
        for j in range(i+1,5):
            sumi+= math.exp(fitness_score[i][j])
    for i in range(4):
        for j in range(i+1,5):
            prob[i][j] = math.exp(fitness_score[i][j])/sumi
    rand = random.random()
    sumi = 0
    for i in range(0,4):
        for j in range(i+1,5):
            sumi+= prob[i][j]
            if sumi >= rand:
                return([i,j])
    return(i,j)

def match(i,j):
    rand = random.randint(0,2)
    if rand == 1:
        return (j)
    elif rand == 0:
        return (i)
    else:
        return (None)
    
def matchmaking(a_1, a_2, theta_1, theta_2, fitness_score, mu, sigma, no_of_matches):
    for i in range(4):
        for j in range(i+1, 5):
            fitness_score[i][j] = theta_1 * (omega(a_1, a_2, mu[i], sigma[i]) - omega(a_1, a_2, mu[j], sigma[j])) + theta_2 *(no_of_matches[i][j])  
    i,j = match_select(fitness_score)
    return(i,j)

def update(i, j, a_1, a_2, mu, sigma, K, win, history):
    if win == None:
        S_i = 0.5
        S_j = 0.5
    elif win == i:
        S_i = 1
        S_j = 0
    else:
        S_i = 0
        S_j = 1
        
    expectation = math.exp(omega(a_1, a_2, mu[i], sigma[i])) / (math.exp(omega(a_1, a_2, mu[i], sigma[i])) + math.exp(omega(a_1, a_2, mu[j], sigma[j])))
    k_i = K * math.exp(omega(a_1, a_2, mu[i], sigma[i]))
    mu[i] += (k_i*( S_i - expectation))
    t = len(history[i])
    sumi_i = 0
    for x in range(len(history[i])):
        sumi_i+= (history[i][x] - mu[i])**2
    sigma[i] = sumi_i/t 
    print ("new mu of player i", mu[i])
    print("new sigma of player i", sigma[i])
    history[i].append(mu[i])
    
    k_j = K * math.exp(omega(a_1, a_2, mu[j], sigma[j]))
    mu[j] += (k_j* ( S_j + expectation - 1))
    sumi_j = 0
    t = len(history[j])
    for x in range(t):
        sumi_j += (history[j][x] - mu[j])**2
    sigma[j] = sumi_j/t
    print("new mu of player j", mu[j])
    print("new sigma of player j", sigma[j])
    history[j].append(mu[j])
    
def initialize(a_1, a_2, theta_1, theta_2, K):
    no_of_matches = [[0 for i in range(5)] for j in range(5)] ## n_ij
    fitness_score = [[0 for i in range(5)] for j in range(5)] ## delta_ij    
    mu = [5 for i in range(5)] ## mu
    history_players = [[5] for i in range(5)]  ## History set
    sigma = [5/3 for i in range(5)] ## variance list
    total_games = [[0 for i in range(5)] for j in range(5)] ##counting the no of games
    for z in range(1000):
        i,j = matchmaking(a_1, a_2, theta_1, theta_2, fitness_score, mu, sigma, no_of_matches)
        print("match between", i , "and", j)
        total_games[i][j]+=1
        win = match(i,j)
        print(win, "won the match")
        update(i, j, a_1, a_2, mu, sigma, K, win, history_players)
        print()
    print("---------------------------------------------------------------------")
    print("Final Result")
    print("---------------------------------------------------------------------")
    for i in range(5):
        print("Player ",i)
        for j in range(5):
            if j!= i:
                if i>j:
                    max = i
                    min = j
                else:
                    max =j
                    min = i
                print("Games played with",j, "=", total_games[min][max])
##        print("total_games", total_games)
        print("final mu of player", i, "is",  mu[i])
        print("final sigma of player", i, "is" , sigma[i])
        print("-------------------------------------------------------------------")
        
initialize(0.1,-0.3,-0.5,-0.1,1)