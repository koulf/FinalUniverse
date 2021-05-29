import random

points = []

for i in range(10):
    points.append([random.randrange(5, 20), (random.randrange(5, 20))])

print(points)

px = list(points[random.randrange(10)])

print("\n -----------------")
print('px:', px)
print("\n -----------------")

n = 10

for i in range(n):
    for p in points:
        p[0] -= (px[0] / n)
        p[1] -= (px[1] / n)

print(points)
print('\n')

for p in points:
    p[0] = round(p[0])
    p[1] = round(p[1])

print(points)
