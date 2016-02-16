import numpy as np
import scipy as sp
from scipy import spatial
import sys
from scipy import linalg, mat, dot
# from sklearn.metrics import jaccard_similarity_score

filename = "./data/data.supermarkets.inventories"

with open(filename) as f_in:
    lines = filter(None, (line.rstrip().split('\t') for line in f_in))

table_names = lines[0]
(lines[1]).pop(0)
(lines[2]).pop(0)
sainsbury = [int(x) for x in lines[1]]
kullen = [int(y) for y in lines[2]]

jaccard = 41.0 / (22 + 41 + 58)

a=mat(sainsbury)
b=mat(kullen)
c=dot(a,b.T)/linalg.norm(a)/linalg.norm(b)

print "Question 2a"
print "Jaccard coefficient is", round(jaccard, 3), "\n"

print "Question 2b"
print "Manhattan distance is", round(sp.spatial.distance.minkowski(sainsbury, kullen, 1) , 3)
print "Euclidian distance is", round(sp.spatial.distance.minkowski(sainsbury, kullen, 2) , 3)
print "Supremum distance is", round(sp.spatial.distance.chebyshev(sainsbury, kullen) , 3), "\n"

print "Question 2c"
print "Cosine similarity is", round(c, 3)