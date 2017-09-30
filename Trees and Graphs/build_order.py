from collections import deque


def check_build_order(arr):
    graph, visited = {}, set()
    # make the graph
    for tup in arr:
        if tup[1] in graph:
            graph[tup[1]].append(tup[0])
        else:
            graph[tup[1]] = [tup[0]]
    print(graph)
    # start bfs
    q = deque()
    # do as many bfs as we need to go through entire graph
    for node in graph:
        # if we've visited the node before, bfs would've iterated all paths of that node
        cycle_visited = set()
        if node not in visited:
            q.append(node)
        while q:
            curr = q.popleft()
            visited.add(curr)
            if curr in graph:
                for adjacent in graph[curr]:
                    # error if there's a loop in the graph and we returned to a node we've iterated this cycle
                    if adjacent in cycle_visited:
                        return "Error!"
                    cycle_visited.add(adjacent)
                    q.append(adjacent)
        visited.update(cycle_visited)
    return "Can be built!"


def get_graph(arr):
    graph, incoming = {}, {}
    # build graph and frequency of dependencies
    for tup in arr:
        if tup[0] in incoming:
            incoming[tup[0]] += 1
        else:
            incoming[tup[0]] = 1
        if tup[1] in graph:
            graph[tup[1]].append(tup[0])
        else:
            graph[tup[1]] = [tup[0]]
    print(graph, incoming)
    return graph, incoming


# think sub-graph problem
def build_order_dfs(projects, arr):
    graph, paths = get_graph(arr)[0], deque()
    visited, stack = set(), []
    # multiple depth first searches
    for node in projects:
        stack.append(node)
        temp_path, not_visited = deque(), True
        # don't re-iterate already visited nodes
        while stack and node not in visited:
            vertex = stack.pop()
            visited.add(vertex)
            temp_path.append(vertex)
            # handle vertices with no outgoing edges
            if vertex in graph:
                for node in graph[vertex]:
                    if node not in visited:
                        stack.append(node)
                    else:
                        not_visited = False
        # each temp_path is the solution for a sub-graph
        if not_visited:
            paths.extend(temp_path)
        else:
            paths.extendleft(temp_path)

    if len(paths) != len(projects):
        print(paths)
        raise Exception("No possible build error!")
    return paths


def build_order_topological(projects, arr):
    tup = get_graph(arr)
    graph, incoming = tup[0], tup[1]
    q, paths = deque(), []
    # find initial vertices with no incoming edges; expensive call
    for node in (set(projects) - set(incoming.keys())):
        q.append(node)
        paths.append(node)

    while q:  # topological sort
        curr = q.popleft()
        # handle vertices with no outgoing edges
        if curr in graph:
            for node in graph[curr]:
                # if it's in the graph, it'll have incoming edges
                incoming[node] -= 1
                if incoming[node] == 0:
                    q.append(node)
                    paths.append(node)
    if len(paths) != len(projects):
        raise Exception("No possible build order!")
    return paths


projects = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
# (dependant, incoming)
arr = [('d', 'a'), ('b', 'f'), ('d', 'b'), ('a', 'f'), ('d', 'c')]
# get_graph(arr)
# arr = [('b', 'c'), ('b', 'a'), ('f', 'b'), ('a', 'f')]
# arr = [('a', 'b'), ('b', 'a')]
# print(build_order_dfs(projects, arr))
print(build_order_topological(projects, arr))

