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

def max_score(ls):
    max = ls[0]
    for num in ls:
        if num > max :
            max = num
    return max

def min_score(ls):
    min = ls[0]
    for num in ls:
        if num < min :
            min = num
    return min

def quartile(ls, quartile):
    sorted_list = ls[:]
    sorted_list.sort()
    index_to_find = quartile / 4.0 * len(ls)
    rounded_index = int(index_to_find)
    number_dec = index_to_find - rounded_index
    if number_dec == 0.0:
        return ls[rounded_index]
    elif number_dec == 0.25:
        return (ls[rounded_index] * 3 + ls[rounded_index + 1]) / 4
    elif number_dec == 0.5:
        return (ls[rounded_index] + ls[rounded_index + 1]) / 2
    elif number_dec == 0.25:
        return (ls[rounded_index] + ls[rounded_index + 1] * 3) / 4

def mean_score(ls):
    sum = 0.0
    for num in ls:
        sum += num
    return sum / len(ls)

def mode_score(ls):
    sorted_list = ls[:]
    sorted_list.sort()
    prev_num = sorted_list[0]
    count_num = -1
    mode_num = prev_num
    mode_freq = -1
    for num in sorted_list:
        if (num == prev_num):
            count_num = count_num + 1
            if count_num >= mode_freq:
                mode_num = num
                mode_freq = count_num
        else:
            prev_num = num
            count_num = 0 
    return mode_num

def sample_variance(ls):
    sum = 0.0
    sum_sq = 0.0
    for num in ls:
        sum = sum + num
        sum_sq = sum_sq + num * num
    return (sum_sq - sum * sum / len(ls)) / (len(ls) - 1)

print "Question 1a"
print "Max midterm score is", max_score(midterm_scores)
print "Min midterm score is", min_score(midterm_scores), "\n"

print "Question 1b"
print "Q1 is", quartile(midterm_scores, 1)
print "Median is", quartile(midterm_scores, 2)
print "Q3 is", quartile(midterm_scores, 3), "\n"

print "Question 1c"
print "Mean is", round(mean_score(midterm_scores), 3), "\n"

print "Question 1d"
print "Mode is", mode_score(midterm_scores), "\n"

print "Question 1e"
print "Sample variance is", round(sample_variance(midterm_scores), 3), "\n\n\n"