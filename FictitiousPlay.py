from __future__ import division
import matplotlib.pyplot as plt
import random 
import numpy as np



#defining variables and functions that are useful

payoff_0 = np.array([[1,-1],[-1,1]])
payoff_1 = np.array([[-1,1],[1,-1]])

def set_intbelief():
	int_belief = random.uniform(0,1)
	return  np.array([1-int_belief,int_belief])
	 # belief about the opponent's actions

belief0 = set_intbelief()
belief1 = set_intbelief()


def expected_value(payoff,beliefs):
	"""
	payoff is a matrix like np.array([[1,-1][-1,1]])
	beliefs is a vector
	"""
	return np.dot(payoff,beliefs)
	# returns expected values of each action as a vector

def take_action(x): # this takes a vector and a list as  arguments
	 
	if x[0] > x[1]:
		return 0
	elif x[0] < x[1]:
		return 1
	else:
		return random.randint(0,1)

# lists used later to draw the graph
trajectory0 = [belief0[1]]
trajectory1 = [belief0[1]]


# simulating  actions
for i in range(1000):
	
	ev0 = expected_value(payoff_0,belief0)
	ev1 = expected_value(payoff_1,belief1)
	
	action0 = take_action(ev0)
	action1 = take_action(ev1)

	# updating beliefs
	m = belief0[1] + (action1 - belief0[1])/(i + 2)
	n = belief1[1] + (action0 - belief1[1])/(i + 2)
	belief0 = np.array([1-m,m])
	belief1 = np.array([1-n,n])
	
	trajectory0.append(belief0[0])
	trajectory1.append(belief1[0])



plt.plot(trajectory0, 'b-', label='player0')  
plt.plot(trajectory1, 'y-', label='player1')  
plt.legend()
#plt.savefig("fictitious_graph1.0.png",bbox_inches="tight",pad_inches=0)

plt.show()



	
	