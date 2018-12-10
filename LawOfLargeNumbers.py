import numpy
from numpy.random import rand

N = 10
result = 0
counter = 0;
for i in rand(N):
	if(i > -1 and i < 1):
		counter = counter +1
		result = i / 100;
		print (result)


