
a = [66.25, 333, 333, 1, 1234.5]
print(a.count(333))
print(len(a))
a.insert(2,-1)
# 把一个元素添加到列表的结尾，相当于 a[len(a):] = [x]。
a.append(333)
# 返回列表中第一个值为 x 的元素的索引。如果没有匹配的元素就会返回一个错误。
print(a.index(333))
# 删除列表中值为 x 的第一个元素。如果没有这样的元素，就会返回一个错误。
a.remove(333)
# 倒排列表中的元素。
a.reverse()
# 对列表中的元素进行排序。
a.sort()
print(a)
# 移除列表中的所有项，等于del a[:]。
a.clear()
# 从列表的指定位置移除元素，并将其返回。如果没有指定索引，a.pop()返回最后一
# 个元素。元素随即从列表中被移除。（方法中 i 两边的方括号表示这个参数是可选的
# ，而不是要求你输入一对方括号，你会经常在 Python 库参考手册中遇到这样的标记。）
a = [66.25, 333, 333, 1, 1234.5]
print(a.pop(1))

print(a)
# 列表方法使得列表可以很方便的作为一个堆栈来使用，堆栈作为特定的数据结构，最先进入的元素最后一
# 个被释放（后进先出）。用 append() 方法可以把一个元素添加到堆栈顶。用不指定索引的 pop() 方
# 法可以把一个元素从堆栈顶释放出来
import this
# 将列表当做堆栈使用
# 列表方法使得列表可以很方便的作为一个堆栈来使用，堆栈作为特定的数据结构，最先进入的元素最后一个被释放（后进先出）
# 。用 append() 方法可以把一个元素添加到堆栈顶。用不指定索引的 pop() 方法可以把一个元素从堆栈顶释放出来
stack = [3,4,5]
stack.append(6)
print(stack)
stack.pop()
print(stack)


# # 将列表当作队列使用
# 也可以把列表当做队列用，只是在队列里第一加入的元素，第一个取出来；但是拿列表用作这样的目的效率不高。
# 在列表的最后添加或者弹出元素速度快，然而在列表里插入或者从头部弹出速度却不快（因为所有其他的元素都得一个一个地移动）
from _collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
queue.popleft()                 # The first to arrive now leaves
queue.popleft()                 # The second to arrive now leaves

# 列表推导式/
# 每个列表推导式都在 for 之后跟一个表达式，然后有零到多个 for 或 if 子句。返回结果是一个根据表达从其后的
#  for 和 if 上下文环境中生成出来的列表。如果希望表达式推导出一个元组，就必须使用括号。
vec = [2, 4, 6]
res = [3*x for x in vec]

res = [[x,x**2] for x in vec]
print(res)

freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
res =[weapon.strip() for weapon in freshfruit] 
print(res)

vec = [2, 4, 6]
res = [3*x for x in vec if x > 3]
print(res)

vec1 = [2, 4, 6]
vec2 = [4, 3, -9]
res = [x*y for x in vec1 for y in vec2]
res = [vec1[i]*vec2[i] for i in range(len(vec1))]
print(res)