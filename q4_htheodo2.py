from sklearn import decomposition as dec
import matplotlib.pyplot as plt

filename = "./data/iris.data"

with open(filename) as f_in:
    lines = filter(None, (line.rstrip().split(',') for line in f_in))

name = []
data = []
legend = []
versicolor = 0
virginica = 0
idx = 0
for line in lines:
    if line[0] != '':
        data.append([float(line[0]), float(line[1]), float(line[2]), float(line[3])])
        # first_axis.append(float(line[0]))
        # second_axis.append(float(line[1]))
        # third_axis.append(float(line[2]))
        # fourth_axis.append(float(line[3]))
        if line[4] == "Iris-setosa" :
            label = 0
        elif line[4] == "Iris-versicolor":
            if versicolor == 0:
                versicolor = idx
            label = 1
        else:
            if virginica == 0:
                virginica = idx
            label = 2
        name.append(label)
        legend.append(line[4])
        idx += 1


pca = dec.PCA(n_components = 4)
pca.fit(data)
data = pca.transform(data)

x_minq1, x_maxq1 = data[:, 0].min() - .5, data[:, 0].max() + .5
y_minq1, y_maxq1 = data[:, 1].min() - .5, data[:, 1].max() + .5

x_minq2, x_maxq2 = data[:, 1].min() - .5, data[:, 1].max() + .5
y_minq2, y_maxq2 = data[:, 2].min() - .5, data[:, 2].max() + .5

x_minq3, x_maxq3 = data[:, 2].min() - .5, data[:, 2].max() + .5
y_minq3, y_maxq3 = data[:, 3].min() - .5, data[:, 3].max() + .5

x_minq4, x_maxq4 = data[:, 0].min() - .5, data[:, 0].max() + .5
y_minq4, y_maxq4 = data[:, 3].min() - .5, data[:, 3].max() + .5

plt.figure(1).canvas.set_window_title('Question 4a') 
plt.scatter(data[:versicolor, 0], data[:versicolor, 1], color='red', label="Iris-setosa")
plt.scatter(data[versicolor:virginica, 0], data[versicolor:virginica, 1], color='green', label="Iris-versicolor")
plt.scatter(data[virginica:, 0], data[virginica:, 1], color='blue', label="Iris-virgnica")
plt.xlabel('PCA1')
plt.ylabel('PCA2')

plt.figure(2).canvas.set_window_title('Question 4b') 
plt.subplot(221) 
plt.scatter(data[:versicolor, 0], data[:versicolor, 1], color='red', label="Iris-setosa")
plt.scatter(data[versicolor:virginica, 0], data[versicolor:virginica, 1], color='green', label="Iris-versicolor")
plt.scatter(data[virginica:, 0], data[virginica:, 1], color='blue', label="Iris-virgnica")
plt.xlabel('PCA1')
plt.ylabel('PCA2')

plt.xlim(x_minq1, x_maxq1)
plt.ylim(y_minq1, y_maxq1)
plt.xticks(())
plt.yticks(())
plt.legend()

plt.subplot(222) 
plt.scatter(data[:versicolor, 1], data[:versicolor, 2], color='red', label="Iris-setosa")
plt.scatter(data[versicolor:virginica, 1], data[versicolor:virginica, 2], color='green', label="Iris-versicolor")
plt.scatter(data[virginica:, 1], data[virginica:, 2], color='blue', label="Iris-virgnica")
plt.xlabel('PCA2')
plt.ylabel('PCA3')

plt.xlim(x_minq2, x_maxq2)
plt.ylim(y_minq2, y_maxq2)
plt.xticks(())
plt.yticks(())
plt.legend()

plt.subplot(223) 
plt.scatter(data[:versicolor, 2], data[:versicolor, 3], color='red', label="Iris-setosa")
plt.scatter(data[versicolor:virginica, 2], data[versicolor:virginica, 3], color='green', label="Iris-versicolor")
plt.scatter(data[virginica:, 2], data[virginica:, 3], color='blue', label="Iris-virgnica")
plt.xlabel('PCA3')
plt.ylabel('PCA4')

plt.xlim(x_minq3, x_maxq3)
plt.ylim(y_minq3, y_maxq3)
plt.xticks(())
plt.yticks(())
plt.legend()

plt.subplot(224) 
plt.scatter(data[:versicolor, 0], data[:versicolor, 3], color='red', label="Iris-setosa")
plt.scatter(data[versicolor:virginica, 0], data[versicolor:virginica, 3], color='green', label="Iris-versicolor")
plt.scatter(data[virginica:, 0], data[virginica:, 3], color='blue', label="Iris-virgnica")
plt.xlabel('PCA1')
plt.ylabel('PCA4')

plt.xlim(x_minq4, x_maxq4)
plt.ylim(y_minq4, y_maxq4)
plt.xticks(())
plt.yticks(())
plt.legend()

plt.show()
# iris = datasets.load_iris()
# X = iris.data
# y = iris.target

# print X
# print y