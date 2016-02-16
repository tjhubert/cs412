import numpy as np
import scipy as sp
import statistics as st

filename = "./data/data.online.scores"

with open(filename) as f_in:
    lines = filter(None, (line.rstrip().split('\t') for line in f_in))

student_ids = []
midterm_scores = []
final_scores = []

for line in lines:
    student_ids.append(line[0])
    midterm_scores.append(int(line[1]))
    final_scores.append(int(line[2]))

def zscore(data, mean, std):
    return (data - mean) / std

mean = np.mean(midterm_scores)
std = np.std(midterm_scores)

midterm_z = [zscore(score, mean, std) for score in midterm_scores]

print "Question 3a"
print "Mean before normalization is", round(np.mean(midterm_scores), 3)
print "Sample variance before normalization is", round(np.var(midterm_scores), 3)
print "Mean after normalization is", round(np.mean(midterm_z), 3)
print "Sample variance after normalization is", round(np.var(midterm_z), 3), "\n"

print "Question 3b"
print "Score after normalization", round(zscore(90, mean, std), 3) 
