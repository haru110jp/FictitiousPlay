from __future__ import division
import matplotlib.pyplot as plt
import random

samples = []


for k in range(1000): # you can change this number if you like

	
	#defining variables concerning player0
	int_0 = random.uniform(0,1)
	belief00 = int_0
	action0 = []


	int_1 = random.uniform(0,1)
	belief10 = int_1
	action1 = []


	# simulating 1's actions
	for i in range(1000):
	
	#calculating expected values
		ev00 = belief00*1 + (1 - belief00)*(-1)
		ev10 = belief10*(-1) + (1 - belief10)*1
	
		if ev00 > 0:
			action0.append(0)
		elif ev00 < 0:
			action0.append(1)
		else:
			action0.append(random.randint(0,1))

		if ev10 > 0:
			action1.append(0)
		elif ev10 < 0:
			action1.append(1)
		else:
			action1.append(random.randint(0,1))
		
	# updating beliefs
		belief10 = belief10 + (action0[i] - belief10) / (i + 2)
		
		belief00 = belief00 + (action1[i] - belief00) / (i + 2)

	samples.append(belief00)

fig, axes = plt.subplots()
axes.hist(samples)

plt.show()



	
	