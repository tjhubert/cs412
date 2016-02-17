filename = "./data/data.supermarkets.inventories"

with open(filename) as f_in:
    lines = filter(None, (line.rstrip().split('\t') for line in f_in))

table_names = lines[0]
(lines[1]).pop(0)
(lines[2]).pop(0)
sainsbury = [int(x) for x in lines[1]]
kullen = [int(y) for y in lines[2]]

jaccard = 41.0 / (22 + 41 + 58)

def minkowski(ls1, ls2, h):
    sum = 0.0
    for x in range(0, len(ls1)):
        sum = sum + (abs(ls1[x] - ls2[x]) ** h)
    return sum ** (1.0 / h)

def supremum(ls1, ls2):
    max_diff = 0.0
    diff = 0.0
    for x in range(0, len(ls1)):
        diff = abs(ls1[x] - ls2[x])
        if diff > max_diff:
            max_diff = diff
    return max_diff

def cosine_similarity(a, b):
    sum_ab = 0.0
    sum_a = 0.0
    sum_b = 0.0
    for x in range(0, len(a)):
        sum_ab = sum_ab + a[x] * b[x]
        sum_a = sum_a + a[x] * a[x]
        sum_b = sum_b + b[x] * b[x]
    return sum_ab / ( (sum_a ** 0.5) * (sum_b ** 0.5) )

print "Question 2a"
print "Jaccard coefficient is", round(jaccard, 3), "\n"

print "Question 2b"
print "Manhattan distance is", round(minkowski(sainsbury, kullen, 1) , 3)
print "Euclidian distance is", round(minkowski(sainsbury, kullen, 2) , 3)
print "Supremum distance is", round(supremum(sainsbury, kullen) , 3), "\n"

print "Question 2c"
print "Cosine similarity is", round(cosine_similarity(sainsbury, kullen), 3), "\n\n\n"