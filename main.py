import math
from time import perf_counter
from scipy import spatial


def load_file(file_name):
    try:
        f = open(file_name, "r")
    except:
        print("File doesnt exist")
        exit()

    lines = f.readlines()
    array = []
    for line in lines:
        array.append(line)
    return array


def get_dictionary(array):
    dict = {}
    visited = {}
    for line in array:
        if line == "":
            continue

        a = line.split()

        a[0] = str(a[0]).replace('[', '').replace(']', '').replace('\'',
                                                                   '').replace(
            '\"', '')
        a[1] = str(a[1]).replace('[', '').replace(']', '').replace('\'',
                                                                   '').replace(
            '\"', '')
        sur1 = a[0].split(",")
        sur2 = a[1].split(",")
        x1, y1, x2, y2 = int(sur1[0]), int(sur1[1]), int(sur2[0]), int(sur2[1])

        k = (x1, y1)
        v = (x2, y2)

        if not k in dict:
            dict[k] = []
        dict[k].append(v)
        if not v in dict:
            dict[v] = []
        dict[v].append(k)

        if not k in visited:
            visited[k] = False
        if not v in visited:
            visited[v] = False
    return dict, visited


def dfsutil(temp, sur, visited, ind, comp, dic):
    visited[sur] = True
    temp.append(list(sur))
    comp[ind].append(list(sur))
    if sur in dic:
        for i in dic[sur]:
            if not visited[i]:
                temp = dfsutil(temp, i, visited, ind, comp, dic)

    return temp


def createGraph(dic, visited):
    pol = []
    i = 0
    comp = {}
    indexes = []
    for key, value in dic.items():
        if not visited[key]:
            comp[i] = []
            temp = []
            pol.append(dfsutil(temp, key, visited, i, comp, dic))
            indexes.append(i)
        i += 1
    return pol, comp, indexes


def savetoFile(dic, file):
    f = open(file, 'w')
    for key, value in dic.items():
        f.write(f"{list(value[0])} {list(value[1])}\n")


def print_distance(dist):
    distance = 0
    for key, value in dist.items():
        distance += value
    print(f"Distance: {distance}")


def getsur(arr, new):
    for i in arr:
        new.append(i)
    return new


def find(cc):
    new = []
    new += cc.pop(0)
    n = 1
    low = {}
    distance = {}
    while cc:
        min_val = math.inf
        first = None
        secod = None
        tree = spatial.KDTree(new)
        for j in range(len(cc)):
            for l in cc[j]:
                idxs = tree.query(l,1)
                # dist = idxs[0][0]
                if idxs[0] < min_val:
                    min_val = idxs[0]
                    first = new[idxs[1]]
                    secod = l
                    idx = j

        new += cc.pop(idx)
        distance[n] = min_val
        low[n] = []
        low[n].append(first)
        low[n].append(secod)
        n += 1
    return low, distance


def get_suradnice(arr, sur):
    pol = []
    ind = None
    out = None
    for idx, i in enumerate(arr):
        if sur in i:
            ind = idx
            continue
        pol += i
    if ind != None:
        out = arr.pop(ind)
    return pol, out


def find2(cc):
    new = []
    new += cc.pop(0)
    n = 0
    low = {}
    distance = {}
    while cc:
        if n == 0:
            pol, out = get_suradnice(cc, None)
        min_val = math.inf
        first = None
        secod = None
        tree = spatial.KDTree(pol)

        for k in new:
            idxs = tree.query(k, 1)
            if idxs[0] < min_val:
                min_val = idxs[0]
                first = k
                secod = pol[idxs[1]]

        pol, out = get_suradnice(cc, secod)
        new += out
        distance[n] = min_val

        low[n] = []
        low[n].append(first)
        low[n].append(secod)
        n += 1

    return low, distance


def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0]) *
                     (p1[0] - p2[0]) +
                     (p1[1] - p2[1]) *
                     (p1[1] - p2[1]))


def bruteforce(cc):
    new = []
    new = getsur(cc.pop(0), new)
    n = 0
    low = {}
    distance = {}
    while cc:
        min_val = math.inf
        first = None
        secod = None
        idx = 0
        for k in range(len(new)):
            for j in range(len(cc)):
                for l in cc[j]:
                    if dist(new[k], l) < min_val:
                        min_val = dist(new[k], l)
                        first = new[k]
                        secod = l
                        idx = j

        new = getsur(cc.pop(idx), new)
        distance[n] = min_val
        low[n] = []
        low[n].append(first)
        low[n].append(secod)
        n += 1
    return low, distance


def main():
    file_name = input("\nPlease write name of file: ")
    out_name = input("Please write name of output file: ")
    t_start = perf_counter()
    arr = load_file(file_name)

    dic, visited = get_dictionary(arr)
    cc, comp, indexes = createGraph(dic, visited)

    low, distance = find(cc)
    t_end = perf_counter()
    print_distance(distance)

    savetoFile(low, out_name)
    print(f'Total time: {t_end - t_start:.2f} s')


while True:
    main()
