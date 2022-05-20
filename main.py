"""
Authors: Bc. Simon Youssef
Coppyright 2022 All Rights Reserved.
Resources:
https://edutechlearners.com/download/Introduction_to_algorithms-3rd%20Edition.pdf
https://www.geeksforgeeks.org/optimal-binary-search-tree-dp-24/
"""


import numpy as np
from sortedcontainers import SortedDict


def load_file(file_name):
    d = {}
    with open(file_name) as f:
        for line in f:
           val, key = line.split()
           d[key] = int(val)
    s = SortedDict(d)
    return s


def sum_freq(d):
    sum = 0
    for i in d.items():
        sum += i[1]
    return sum


def get_probability(d, f):
    dic = {}
    p = []
    q = []
    sum_freg = 0
    p.append(0.0)
    for i in d.items():
        if i[1] <= 50000:
            sum_freg += i[1]
        else:
            dic[i[1]/f] = i[0]
            p.append(i[1]/f)
            q.append((sum_freg/f))
            sum_freg = 0
    q.append((sum_freg / f))
    return dic, p, q


def find(p, q):
    n = len(p) - 1
    e = [[0] * (n + 1) for _ in range(n + 1 + 1)]
    w = [[0] * (n + 1) for _ in range(n + 1 + 1)]
    root = [[0] * (n + 1) for _ in range(n + 1 + 1)]

    for i in range(0, n + 1):
        e[i + 1][i] = q[i]
        w[i + 1][i] = q[i]

    for l in range(1, n + 1):
        for i in range(1, n - l + 2):
            j = i + l - 1
            e[i][j] = np.inf
            w[i][j] = w[i][j - 1] + p[j] + q[j]
            for r in range(i, j + 1):
                t = e[i][r - 1] + e[r + 1][j] + w[i][j]
                if t < e[i][j]:
                    e[i][j] = t
                    root[i][j] = r
    return root


def load_tree(root, dic, i, j, l, arr):
    if j < 0 or i > j or i > (len(root[0]) - 1):
        return
    node = root[i][j]
    j1 = node - 1
    i1 = node + 1
    if (len(arr)-1) >= l:
        arr[l].append(list(dic.values())[node-1])
    else:
        nl = []
        nl.append(list(dic.values())[node-1])
        arr.append(nl)
    load_tree(root, dic, i, j1, l+1, arr)
    load_tree(root, dic, i1, j, l+1, arr)


def number_comparisons(mat, word):
    for i, v in enumerate(mat):
        if word in v:
            print(f"Počet porovaní: {i}."
                  f"\nPočet porovaní vrátane koreňa: {i+1}."
                  f"\nSlovo sa nachádza v strome.")
            return



def main():
    dictionary = load_file("dictionary.txt")
    freq = sum_freq(dictionary)
    dic, p, q = get_probability(dictionary, freq)

    root = find(p, q)
    j = len(root[0])-1
    tree = []
    load_tree(root, dic, 1, j, 0, tree)
    for i, o in enumerate(tree):
        print(f"-----------level {i}-----------")
        print(o)

    while True:
        word = input("\nZadajte slovo: ")
        number_comparisons(tree, word)


main()
