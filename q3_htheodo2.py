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

def mean_score(ls):
    sum = 0.0
    for num in ls:
        sum += num
    return sum / len(ls)

def sample_variance(ls):
    sum = 0.0
    sum_sq = 0.0
    for num in ls:
        sum = sum + num
        sum_sq = sum_sq + num * num
    return (sum_sq - sum * sum / len(ls)) / (len(ls) - 1)

mean = np.mean(midterm_scores)
std = np.std(midterm_scores)

midterm_z = [zscore(score, mean, std) for score in midterm_scores]

print "Question 3a"
print "Mean before normalization is", round(mean_score(midterm_scores), 3)
print "Sample variance before normalization is", round(sample_variance(midterm_scores), 3)
print "Mean after normalization is", round(mean_score(midterm_z), 3)
print "Sample variance after normalization is", round(sample_variance(midterm_z), 3), "\n"

print "Question 3b"
print "Score after normalization", round(zscore(90, mean, std), 3) , "\n\n\n"
