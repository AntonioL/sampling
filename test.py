#Example

from sampling import Sampler

#elements is an array of pairs, the first member contains the element
#and the second the probability of that element being picked up

elements = [(i, 1/20) for i in range(10)] + [(10, 1/2)]
s = Sampler(elements)


#Testing correctness of my procedure, with the above elements we expect 7 to appear 50% of the time and
#the others 7% of the time each.
count = [0 for i in range(len(elements))]

for i in range(10000):
    count[s.sample()] += 1

print(count)
