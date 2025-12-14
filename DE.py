import random
import math
import numpy as np
import matplotlib.pyplot as plt

A = 10
n = 10

# vector = [random.randint(1,100) for _ in range(10)]
# vector = [27, 75, 5, 14, 34, 51, 11, 16, 90, 88]
# vector = [14, 83, 49, 93, 44, 92, 74, 87, 29, 19]
vector = [random.uniform(0,10) for _ in range(10)]
print(vector)

vec = [0] * 50
vec2 = [0] * 50
vec3 = [0] * 50
vec4 = [0] * 50
vec5 = [0] * 50
vec6 = [0] * 50
vec7 = [0] * 50
vec8 = [0] * 50
def sum(size,x) : 
    a = 0
    for i in range(size) :
        b = 2 * math.pi
        b *= x[i]
        a += pow(x[i],2) - A * math.cos(b)
    return a + size * A
a = [[]]

for i in range(50):
    b = []
    a.append(b)
    for y in range(i + 50):
        b = np.random.uniform(low = 0,high = 10,size = 10)
        a[i].append(b)


def DE (size,NP,F,CR,vector,a) :
     for i in range(5 * size,10 * size) :
        for y in range(500):
            b = np.random.choice(np.arange(i, dtype=np.int32), size=(3), replace=False)
            q = np.random.randint(10)
            v = [random.uniform(0,10) for _ in range(10)]
            for z in range(10):
                m = np.random.rand()
                if (m <= CR or q == z) :
                    n = a[i - size * 5][b[0]][z] + F * (a[i - size * 5][b[1]][z] - a[i - size * 5][b[2]][z])
                    # n = a[b[0]][z] + (F / 2) * (a[b[0]][z] - a[b[1]][z] - a[b[2]][z])
                    # n = a[b[0]][z] + F * (a[b[1]][z] - a[b[2]][z]) + F * (a[b[3]][z] - a[b[4]][z])
                else :
                    n = vector[z]
                v[z] = n
            if(sum(10,vector) > sum(10,v)):
                vector = v
        l = sum(10,vector)
        print(l)
        vec[i - 50] = l
def DE1 (size,NP,F,CR,vector,a) :
     for i in range(5 * size,10 * size) :
        # a = np.random.uniform(low = 0,high = 10,size = (i,size))
        for y in range(500):
            b = np.random.choice(np.arange(i, dtype=np.int32), size=(3), replace=False)
            q = np.random.randint(10)
            v = [random.uniform(0,10) for _ in range(10)]
            for z in range(10):
                m = np.random.rand()
                if (m <= CR or q == z) :
                    # n = a[b[0]][z] + F * (a[b[1]][z] - a[b[2]][z])
                    n = a[i - size * 5][b[0]][z] + (F / 2) * (a[i - size * 5][b[0]][z] - a[i - size * 5][b[1]][z] - a[i - size * 5][b[2]][z])
                    # n = a[b[0]][z] + F * (a[b[1]][z] - a[b[2]][z]) + F * (a[b[3]][z] - a[b[4]][z])
                else :
                    n = vector[z]
                v[z] = n
            if(sum(10,vector) > sum(10,v)):
                vector = v
        l = sum(10,vector)
        print(l)
        vec2[i - 50] = l
def DE2 (size,NP,F,CR,vector,a) :
     for i in range(5 * size,10 * size) :
        # a = np.random.uniform(low = 0,high = 10,size = (i,size))
        for y in range(500):
            b = np.random.choice(np.arange(i, dtype=np.int32), size=(5), replace=False)
            q = np.random.randint(10)
            v = [random.uniform(0,10) for _ in range(10)]
            for z in range(10):
                m = np.random.rand()
                if (m <= CR or q == z) :
                    # n = a[b[0]][z] + F * (a[b[1]][z] - a[b[2]][z])
                    # n = a[b[0]][z] + (F / 2) * (a[b[0]][z] - a[b[1]][z] - a[b[2]][z])
                    n = a[i - size * 5][b[0]][z] + F * (a[i - size * 5][b[1]][z] - a[i - size * 5][b[2]][z]) + F * (a[i - size * 5][b[3]][z] - a[i - size * 5][b[4]][z])
                else :
                    n = vector[z]
                v[z] = n
            if(sum(10,vector) > sum(10,v)):
                vector = v
        l = sum(10,vector)
        print(l)
        vec3[i - 50] = l
def DEb (size,NP,F,CR,vector,a) :
     for i in range(5 * size,10 * size) :
        # a = np.random.uniform(low = 0,high = 10,size = (i,size))
        for y in range(1000):
            b = np.random.choice(np.arange(i, dtype=np.int32), size=(2), replace=False)
            q = np.random.randint(10)
            v = [random.uniform(0,10) for _ in range(10)]
            min = -10000
            mark = 0
            for z in range(1,i):
                if(sum(10,a[i -size * 5][z]) < min):
                    min = sum(10,a[z])
                    mark = z
            for d in range(10):
                m = np.random.rand()
                if (m <= CR or q == z) :
                    n = vector[d] + F * (a[i - size * 5][mark][d] - vector[d]) + F * (a[i - size * 5][b[0]][d] - a[i - size * 5][b[1]][d])
                    # n = a[mark][d] + F * (a[b[0]][d] - a[b[1]][d])
                    # n = a[mark][d] + F * (a[b[0]][d] - a[b[1]][d]) + F * (a[b[2]][d] - a[b[3]][d])
                else :
                    n = vector[d]
                v[d] = n
            if(sum(10,vector) > sum(10,v)):
                vector = v
        l = sum(10,vector)
        print(l)
        vec4[i - 50] = l
def DEb2 (size,NP,F,CR,vector,a) :
     for i in range(5 * size,10 * size) :
        # a = np.random.uniform(low = 0,high = 10,size = (i,size))
        for y in range(500):
            b = np.random.choice(np.arange(i, dtype=np.int32), size=(2), replace=False)
            q = np.random.randint(10)
            v = [random.uniform(0,10) for _ in range(10)]
            min = -10000
            mark = 0
            for z in range(1,i):
                if(sum(10,a[i -size * 5][z]) < min):
                    min = sum(10,a[z])
                    mark = z
            for d in range(10):
                m = np.random.rand()
                if (m <= CR or q == z) :
                    # n = vector[d] + F * (a[mark][d] - vector[d]) + F * (a[b[0]][d] - a[b[1]][d])
                    n = a[i - size * 5][mark][d] + F * (a[i - size * 5][b[0]][d] - a[i - size * 5][b[1]][d])
                    # n = a[mark][d] + F * (a[b[0]][d] - a[b[1]][d]) + F * (a[b[2]][d] - a[b[3]][d])
                else :
                    n = vector[d]
                v[d] = n
            if(sum(10,vector) > sum(10,v)):
                vector = v
        l = sum(10,vector)
        print(l)
        vec5[i - 50] = l
def DEb3 (size,NP,F,CR,vector,a) :
     for i in range(5 * size,10 * size) :
        # a = np.random.uniform(low = 0,high = 10,size = (i,size))
        for y in range(500):
            b = np.random.choice(np.arange(i, dtype=np.int32), size=(4), replace=False)
            q = np.random.randint(10)
            v = [random.uniform(0,10) for _ in range(10)]
            min = -10000
            mark = 0
            for z in range(1,i):
                if(sum(10,a[i -size * 5][z]) < min):
                    min = sum(10,a[z])
                    mark = z
            for d in range(10):
                m = np.random.rand()
                if (m <= CR or q == z) :
                    # n = vector[d] + F * (a[mark][d] - vector[d]) + F * (a[b[0]][d] - a[b[1]][d])
                    # n = a[mark][d] + F * (a[b[0]][d] - a[b[1]][d])
                    n = a[i - size * 5][mark][d] + F * (a[i - size * 5][b[0]][d] - a[i - size * 5][b[1]][d]) + F * (a[i - size * 5][b[2]][d] - a[i - size * 5][b[3]][d])
                else :
                    n = vector[d]
                v[d] = n
            if(sum(10,vector) > sum(10,v)):
                vector = v
        l = sum(10,vector)
        print(l)
        vec6[i - 50] = l

def jDE (size,NP,F,CR,vector,a) :
     n1 = np.random.normal(0,1,1)[0]
     n2 = np.random.normal(0,1,1)[0]
     F0 = 0.1 + n1 * 0.9
     CR0 = n2
     for i in range(5 * size,10 * size) :
        # a = np.random.uniform(low = 0,high = 10,size = (i,size))
        for y in range(500):
            b = np.random.choice(np.arange(i, dtype=np.int32), size=(3), replace=False)
            q = np.random.randint(10)
            v = [random.uniform(0,10) for _ in range(10)]
            n1 = np.random.normal(0,1,1)[0]
            if(y > 0):
                if(n1 < 0.1):
                    F1 = 0.1 + np.random.normal(0,1,1)[0] * 0.9
                    F0 = 1
                n2 = np.random.normal(0,1,1)[0]
                if(n2 < 0.1):
                    CR1 = np.random.normal(0,1,1)[0]
                    CR0 = CR1
            for z in range(10):
                m = np.random.rand()
                if (m <= CR0 or q == z) :
                    n = a[i - size * 5][b[0]][z] + F0 * (a[i - size * 5][b[1]][z] - a[i - size * 5][b[2]][z])
                    # n = a[b[0]][z] + (F / 2) * (a[b[0]][z] - a[b[1]][z] - a[b[2]][z])
                    # n = a[b[0]][z] + F * (a[b[1]][z] - a[b[2]][z]) + F * (a[b[3]][z] - a[b[4]][z])
                else :
                    n = vector[z]
                v[z] = n
            if(sum(10,vector) > sum(10,v)):
                vector = v
        l = sum(10,vector)
        print(l)
        vec7[i - 50] = l
def DEb3tn (size,NP,F,CR,vector,a) :
     for i in range(5 * size,10 * size) :
        # a = np.random.uniform(low = 0,high = 10,size = (i,size))
        for y in range(500):
            if(y > 0):
                F = 0.9 * F * (1 - F)
            b = np.random.choice(np.arange(i, dtype=np.int32), size=(4), replace=False)
            q = np.random.randint(10)
            v = [random.uniform(0,10) for _ in range(10)]
            min = -10000
            mark = 0
            for z in range(1,i):
                if(sum(10,a[i -size * 5][z]) < min):
                    min = sum(10,a[z])
                    mark = z
            for d in range(10):
                m = np.random.rand()
                if (m <= CR or q == z) :
                    # n = vector[d] + F * (a[mark][d] - vector[d]) + F * (a[b[0]][d] - a[b[1]][d])
                    # n = a[mark][d] + F * (a[b[0]][d] - a[b[1]][d])
                    n = a[i - size * 5][mark][d] + F * (a[i - size * 5][b[0]][d] - a[i - size * 5][b[1]][d]) + F * (a[i - size * 5][b[2]][d] - a[i - size * 5][b[3]][d])
                else :
                    n = vector[d]
                v[d] = n
            if(sum(10,vector) > sum(10,v)):
                vector = v
        l = sum(10,vector)
        print(l)
        vec8[i - 50] = l
# result = A * n + sum(10,vector)
# print(result)
# print(DE(10,1,0.8,0.9,vector))
# print(DEb(10,1,0.8,0.9,vector))
DE(10,1,0.8,0.9,vector,a)
DE1(10,1,0.8,0.9,vector,a)
DE2(10,1,0.8,0.9,vector,a)
DEb(10,1,0.8,0.9,vector,a)
DEb2(10,1,0.8,0.9,vector,a)
DEb3(10,1,0.8,0.9,vector,a)
jDE(10,1,0.8,0.9,vector,a)
DEb3tn(10,1,0.8,0.9,vector,a)
plt.plot([50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99],vec)
plt.xlabel("NP")
plt.ylabel("min")
plt.show()
plt.plot([50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99],vec2)
plt.xlabel("NP")
plt.ylabel("min")
plt.show()
plt.plot([50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99],vec3)
plt.xlabel("NP")
plt.ylabel("min")
plt.show()
plt.plot([50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99],vec4)
plt.xlabel("NP")
plt.ylabel("min")
plt.show()
plt.plot([50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99],vec5)
plt.xlabel("NP")
plt.ylabel("min")
plt.show()
plt.plot([50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99],vec6)
plt.xlabel("NP")
plt.ylabel("min")
plt.show()
plt.plot([50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99],vec7)
plt.xlabel("NP")
plt.ylabel("min")
plt.show()
plt.plot([50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99],vec8)
plt.xlabel("NP")
plt.ylabel("min")
plt.show()

