graph = {
    'start': {'a': 6, 'b': 2},
    'a': {'fin': 1},
    'b': {'a': 3, 'fin': 5},
    'fin': {}  # 终点没有任何邻居
}

#  无穷大
infinity = float('inf')
# consts 散列表 从开始节点到各节点的时间
costs = {
    'a': 6,
    'b': 2,
    'fin': infinity
}

# parents 散列表
parents = {
    'a': 'start',
    'b': 'start',
    'fin': None
}


processed = []  # 用于记录处理过的节点


def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:  # 遍历所有节点
        cost = costs[node]
        # 如果当前开销更低且未处理过
        if cost < lowest_cost and node not in processed:
            # 将其视为开销最低的节点
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


# 在未处理的节点中找出开销最小的节点
node = find_lowest_cost_node(costs)

while node is not None:  # 在所有的节点被处理过后结束
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():  # 遍历当前节点的所有邻居
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:  # 经过当前节点前往该邻居更近
            costs[n] = new_cost  # 更新该邻居的开销
            parents[n] = node  # 将该邻居的父节点设置为当前节点
    processed.append(node)  # 将当前节点标记为处理过
    node = find_lowest_cost_node(costs)  # 找出接下来要处理的节点，并循环

