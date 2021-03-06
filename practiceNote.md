# 练习笔记——Python

## 5.数据结构

### 5.6 循环的技巧

在序列中循环时，用 enumerate() 函数可以同时取出位置索引和对应的值：

```python
>>> for i, v in enumerate(['tic', 'tac', 'toe']):
...     print(i, v)
...
# 0 tic
# 1 tac
# 2 toe
```

同时循环两个或多个序列时，用 zip() 函数可以将其内的元素一一匹配：

```python
>>> questions = ['name', 'quest', 'favorite color']
>>> answers = ['lancelot', 'the holy grail', 'blue']
>>> for q, a in zip(questions, answers):
...     print('What is your {0}?  It is {1}.'.format(q, a))
...
# What is your name?  It is lancelot.
# What is your quest?  It is the holy grail.
# What is your favorite color?  It is blue.
```

逆向循环序列时，先正向定位序列，然后调用 reversed() 函数：

```python
>>> for i in reversed(range(1, 10, 2)):
...     print(i)
...
# 9
# 7
# 5
# 3
# 1
```

按指定顺序循环序列，可以用 sorted() 函数，在不改动原序列的基础上，返回一个重新的序列：

```python
>>> basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
>>> for i in sorted(basket):
...     print(i)
...
# apple
# apple
# banana
# orange
# orange
# pear
```

按指定顺序循环序列，可以用 sorted() 函数，在不改动原序列的基础上，返回一个重新的序列：

```python
>>> basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
>>> for i in sorted(basket):
...     print(i)
...
# apple
# apple
# banana
# orange
# orange
# pear
```

使用 set() 去除序列中的重复元素。使用 sorted() 加 set() 则按排序后的顺序，循环遍历序列中的唯一元素：

```python
>>> basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
>>> for f in sorted(set(basket)):
...     print(f)
...
# apple
# banana
# orange
# pear
```

一般来说，在循环中修改列表的内容时，创建新列表比较简单，且安全：

```python
>>> import math
>>> raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
>>> filtered_data = []
>>> for value in raw_data:
...     if not math.isnan(value):
...         filtered_data.append(value)
...
>>> filtered_data
# [56.2, 51.7, 55.3, 52.5, 47.8]
```

3 个数比较大小：

```python
if i > j:
    i = j
if i > k:
    i = k
# output i(min)
```
