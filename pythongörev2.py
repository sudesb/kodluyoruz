import numpy as np


points = [(2,3),(1,7),(4,5),(2,0)]


def euclideanDistance(nokta1,nokta2):
    x_fark = (nokta2[0] - nokta1[0])**2
    y_fark = (nokta2[1] - nokta1[1])**2
    return np.sqrt(x_fark + y_fark)

distances = []

for i in range(len(points)):
    for j in range(i+1, len(points)):
        uzaklık = euclideanDistance(points[i],points[j])
        distances.append(uzaklık)


print(distances)

