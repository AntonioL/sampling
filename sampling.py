
#I rephrase the problem of sampling as a range query
#which can be efficiently solved in O(sqrt(n)) time
#by using a 2-level data-structure. The data structure can be 
#constructed in O(sqrt(N)) time.

#The first level contains sqrt(N) buckets each containing the cumulative
#distribution function of the first index_bucket*sqrt(N) samples.
#The second level contains sqrt(N) buckets, each containing sqrt(N) elements
#(except possibly for the last). The idea is to draw a sample from an uniform
#distribution, then look up on the first level buckets so to find the according
#second level buckets to inspect.

#The complexity of the above procedure is O(2 sqrt(N))

from math import ceil, floor, sqrt
from random import uniform

#Think of this data-structure like a 2-level map
class Sampler:

    def __init__(self, elements):
        self.bucketSize = int(sqrt(len(elements)))
        self.buckets = ceil(len(elements) / self.bucketSize)

        #1. Build the first level data entries
        cumulativeProb = 0.0
        start, end = 0, self.bucketSize
        self.f = []

        for bucket in range(self.buckets - 1):
            self.f.append(cumulativeProb)
            for i in range(start, end): cumulativeProb += elements[i][1]
            start += self.bucketSize
            end += self.bucketSize
        #1.2. Append the last bucket
        self.f.append(cumulativeProb)

        #2. Second level
        self.s = elements

    def sample(self):
        #1. Draw from Uniform(0, 1)
        p = uniform(0, 1)
        #1. Look up on the first level and find the first level bucket
        firstLevel = self.buckets - 1
        for i in range(self.buckets - 1):
            if self.f[i] <= p < self.f[i+1]:
                firstLevel = i
        #2. Look up on the corresponding second level bucket
        cum = self.f[firstLevel]
        start = firstLevel * self.bucketSize
        end = min(len(self.s), start + self.bucketSize)
        #3. Loop until we find the element drawn from the Uniform distribution falling in the desired range
        for i in range(start, end):
            if cum <= p < (cum + self.s[i][1]): return self.s[i][0]
            cum += self.s[i][1]
        #5. The only situation in which we may reach here is when p=1.0
        return self.s[-1][0]
