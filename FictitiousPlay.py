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


def expected_value(payoff,beliefs):
	"""
	payoff is a matrix like np.array([[1,-1][-1,1]])
	beliefs is a vector
	"""
	return np.dot(payoff,beliefs)
	# returns expected values of each action as a vector

def take_action(x,y): # this takes a vector and a list as  arguments
	 
	if x[0] > x[1]:
		y.append(0)
	elif x[0] < x[1]:
		y.append(1)
	else:
		y.append(random.randint(0,1))

# lists used later to draw the histogram
action0 = []
action1 = []
histo0 = []


# simulating  actions
for x in range(100):
	
	action0 = []
	action1 = []
	belief0 = set_intbelief()
	belief1 = set_intbelief()
	
	for i in range(1000):
		
		ev0 = expected_value(payoff_0,belief0)
		ev1 = expected_value(payoff_1,belief1)
	
		take_action(x = ev0,y = action0)
		take_action(x = ev1,y = action1)

		# updating beliefs
		m = belief0[1] + (action1[i] - belief0[1])/(i + 2)
		n = belief1[1] + (action0[i] - belief1[1])/(i + 2)
		belief0 = np.array([1-m,m])
		belief1 = np.array([1-n,n])
	
	histo0.append(belief0[1])


fig, axes = plt.subplots()
axes.hist(histo0)

plt.savefig("fictitious_histo1.0.png",bbox_inches="tight",pad_inches=0)

plt.show()



	
	