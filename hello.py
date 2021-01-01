a = ['A', 'Z', 1, 5, [100, 200]]
a = a * 20
p1 = 0

def imp(x, p):
    
    for y in range(len(x)):
        if (type(x[y]) in (tuple, list)):
            p = p + 1
            imp(x[y], p)
        else:
            print(str(p) + " -> " + str(x[y]))

imp(a, p1)