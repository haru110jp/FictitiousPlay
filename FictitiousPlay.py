from __future__ import division
import matplotlib.pyplot as plt
import random

#defining the belief of player1
int_0 = random.uniform(0,1)
belief00 = int_0
trajectory0 = [int_0]
action1 = []


#for simplicity, we assume 1's belief fixed
belief10 = 0.6
belief11 = 1 - belief10
# simulating 1's actions
for i in range(100):
	if belief10*1 + belief11*(-1) >0:
		action1.append(1)
		
# preparing for drawing the trajectory
for i in action1:
	belief00 = belief00 + (action1[i] - belief00) / (i + 2)
	trajectory0.append(belief00)

fig, ax = plt.subplots()
ax.plot(trajectory0)

plt.show()
	
	