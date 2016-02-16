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

print "Question 1a"
print "Max midterm score is", max(midterm_scores)
print "Min midterm score is", min(midterm_scores), "\n"

print "Question 1b"
print "Q1 is", np.percentile(midterm_scores, 25)
print "Median is", np.percentile(midterm_scores, 50)
print "Q3 is", np.percentile(midterm_scores, 75), "\n"

print "Question 1c"
print "Mean is", round(np.mean(midterm_scores), 3), "\n"

print "Question 1d"
print "Mode is", max(midterm_scores, key=midterm_scores.count), "\n"

print "Question 1e"
print "Sample variance is", round(np.var(midterm_scores), 3), "\n"