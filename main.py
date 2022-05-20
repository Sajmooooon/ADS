from collections import defaultdict


def load_file(file_name):
    a, b, n, m = [], [], 0, 0
    try:
        f = open(file_name, "r")
    except:
        print("File doesnt exist")
        exit()

    lines = f.readlines()
    for idx, line in enumerate(lines):
        x = line.split()
        if idx == 0:
            n = int(x[0])
            m = int(x[1])
        else:
            if len(x) == 3:
                a.append(int(x[0]))
                b.append(int(x[1]))
                valid(int(x[2]))
            elif len(x) == 2:
                a.append(int(x[0]))
                b.append(a[idx - 1])
                valid(int(x[1]))
            else:
                print("Wrong format.")
                exit()
    return n, m, a, b


def valid(inp):
    if inp != 0:
        print("Wrong format.")
        exit()


def transpose(edges):
    transpose_edges = defaultdict(list)
    for i in edges:
        for j in edges[i]:
            add_edge(transpose_edges, j, i)
    return transpose_edges


def add_edge(edges, src, edg):
    if edg not in edges[src]:
        edges[src].append(edg)


def create_graph(a, b, n, m):
    edges = defaultdict(list)
    for i in range(n * 2):
        edges[i + 1] = []

    for i in range(m):
        if a[i] > 0:
            a_edge = a[i]
            a_neg_edge = n + a[i]
        else:
            a_edge = n - a[i]
            a_neg_edge = -a[i]

        if b[i] > 0:
            b_edge = b[i]
            b_neg_edge = n + b[i]
        else:
            b_edge = n - b[i]
            b_neg_edge = -b[i]

        add_edge(edges, a_neg_edge, b_edge)
        add_edge(edges, b_neg_edge, a_edge)
    return edges


def dfs1(graph, u, visited, stack):
    if visited[u]:
        return
    visited[u] = True
    for i in graph[u]:
        dfs1(graph, i, visited, stack)
    stack.append(u)


def dfs2(reverse_graph, comp, u, c):
    comp[u] = c
    for destination in reverse_graph[u]:
        if comp[destination] == -1:
            dfs2(reverse_graph, comp, destination, c)


def check_2sat(edges, n):
    visited = dict([(k, False) for k in sorted(edges.keys())])
    vertices_stack = []
    for i in visited.keys():
        if not visited[i]:
            dfs1(edges, i, visited, vertices_stack)

    j = 0
    comp = dict([(k, -1) for k in sorted(edges.keys())])
    for i in range(len(vertices_stack)):
        v = vertices_stack.pop()
        if comp[v] == -1:
            dfs2(transpose(edges), comp, v, j)
            j += 1

    assignment = [False] * n
    for i in range(1, n + 1):
        if comp[i] == comp[i + n]:
            return False, []
        assignment[i - 1] = comp[i] > comp[i + n]

    return True, assignment


def add_prv(assignment):
    for i in assignment:
        if i:
            print("PRAVDA")
        else:
            print("NEPRAVDA")


def main():
    filename = input("\nPlease write name of file: ")
    n, m, a, b = load_file(filename)
    edges = create_graph(a, b, n, m)

    is_2sat, assignment = check_2sat(edges, n)
    if not is_2sat:
        print("NESPLNITEĽNÁ")
    else:
        print("SPLNITEĽNÁ")
        add_prv(assignment)


while True:
    main()
