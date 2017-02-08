# sampling
Design and implementation of an algorithm for sampling from a list of elements with each one having its own probability.
The complexity of the sampling algorithm is O(sqrt(N)).

This relies on a data-structure built ad-hoc for the task which construction takes O(N) time. The data-structure is a simple two level array.

The idea is to have sqrt(N) first-level buckets each containing the cumulative probability of the previous elements.
First bucket is going to be always 0.0.

Then we have a second level field which contains the elements alongside with their probability.
The idea is that once we find the right bucket then we have to scan for a maximum sqrt(N) elements.

In the worst-case scenario both the first-leve and second-leve scan visit sqrt(N) elements yielding O(2 * sqrt(N)) complexity hence O(sqrt(N)).

In general the underlying idea is to rephrase the sampling problem as a range query.
