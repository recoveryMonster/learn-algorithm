from collections import deque
graph = {
  'you': ['alice', 'bob', 'claire'],
  'bob': ['anuj', 'peggy'],
  'alice': ['peggy'],
  'claire': ['jonny', 'thom'],
  'anuj': [],
  'peggy': [],
  'jonny': [],
  'thom': []
}

def person_is_seller(name):
  return name[-1] == 'm'

def search(name):
  search_queue = deque() # 创建一个队列
  search_queue += graph[name] # 将name的邻居加入到这个队列
  checked = [] # 已检查队列
  while search_queue: # 只要队列不为空
    person = search_queue.popleft() #取出其中的第一个人
    if person not in checked: #这个人没有被检查过
      if (person_is_seller(person)): #检查这个人是否为芒果销售商
        print(person + ' is a mango seller')
        return True
      else:
        checked.append(person) # 不是芒果销售商，将其添加到已检查数组中
        search_queue += graph[person] # 将这个人的邻居加入到搜索队列
  return False

search('you') # thom is a mango seller
      