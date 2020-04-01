from collections import deque
graph = {
    'you': ['alice', 'bob', 'claire'],
    'bob': ['anuj', 'peggy'],
    'alice': ['peggy'],
    'claire': ['thom', 'jonny'],
    'peggy': [],
    'anuj': [],
    'thom': [],
    'jonny': []
}


def findSeller(name):
    return name[-1] == 'm'  # 判断姓名是否以m结尾，如果是，那么就为售卖者


def search(name):
    searchDeque = deque()
    searchDeque += graph[name]
    searched = []
    while searchDeque:
        person = searchDeque.popleft()
        if person not in searched:
            if findSeller(person):
                print('the seller is ' + person)
                return True
            else:
                searchDeque += graph[person]
                searched.append(person)
    return False


search('you')
