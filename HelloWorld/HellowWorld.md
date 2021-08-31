# 父与子的编程之旅：与小卡特一起学 Python（第 3 版）

## 十二、列表与字典

### 12.7 向列表增加元素

append()、extend()、insert()

- append() 向列表末尾增加一个元素
- extend() 向列表末尾增加多个元素
- insert() 在列表的某个位置增加一个元素

```python
list.append('n')
list.extend(['p', 'q', 'r'])
list.insert(2, 'z')
```

### 12.8 从列表删除元素

remove()、del()、pop()

- remove() 从列表删除选择的元素
- del 利用索引从列表中删除元素
- pop() 从列表中取出最后一个元素

```python
list.remove('c')
del list[3]
lastItem = list.pop()
second = list.pop(1)
```

### 12.9 搜索列表

in、index()

- in 查找元素是否在列表中
- index() 查找元素在列表的哪个位置（元素的索引）

```python
'a' in list
list.index('d')
```

### 12.11 列表排序

sort()

- sort() 会自动按字母/数字顺序对字符串/数字从小到大排序

```python
list.sort()
print(list)
```

#### 12.11.1 按逆序排序

reverse()

- reverse() 把列表中元素的顺序倒过来

```python
# 先正常排序再逆置
list.sort()
list.reverse()
# 直接降序排序
list.sort(reverse=True)
```

#### 12.11.2 另一种排序方法————sorted()

- sorted() 提供了原列表的一个有序副本

```python
# 之前的排序会在原来的列表上做改动，操作之前一般需要创建副本
newList = list[:]
# sorted() 可以得到一个列表的有序副本而不会影响原列表的顺序
newlist = sorted(list)
```

### 12.12 元组

不可改变的列表

```python
tuple = ('red', 'green', 'blue')
```

### 12.14 字典

创建一个空的字典：

```python
phoneNumbers = {}
```

向字典中添加元素：

```python
phoneNumbers["John"] = "555-1234"       # 1
phoneNumbers = {"John": "555-1234"}     # 2
```

`keys()` 会列出字典中所有元素的键：

```python
phoneNumbers.keys()
# dict_keys{['john', 'Mary', 'Bob', 'Jenny']}
```

`values()` 则会列出字典中所有元素的值：

```python
phoneNumber.values()
# dict_values{['555-1234', '555-6789', '444-4321', '867-5309']}
```

字典排序：

```python
# 按键排序
for key in sorted(phoneNumbers.keys()):
    print(key, phoneNumbers[key])
print()

# 按值排序
for value in sorted(phoneNumbers.values()):
    for key in phoneNumbers.keys():
        if phoneNumbers[key] == value:
            print(key, phoneNumbers[key])
```

可以用字典实现的一些操作：

- 使用 `del` 删除某个元素。

  ```python
  del phoneNumbers["John"]
  ```

- 使用 `clear()` 删除所有元素（清空字典）。

  ```python
  phoneNumbers.clear()
  ```

- 使用 `in` 关键字 判断字典中是否存在某个键。

  ```python
  "Bob" in phoneNumbers
  ```

## 十四、对象

### 14.2 对象 = 属性 + 方法

属性就是包含在对象中的变量
方法就是包含在对象中的函数

### 14.8 多态和继承

#### 多态————同一个方法，不同的行为

多态是指对于不同的类，可以有同名的两个（或多个）方法。

#### 继承————向父母学习

在面向对象编程时，类可以从其他类继承属性和方法。

## 二十一、打印格式化与字符串

### 21.5 新的格式化方法

#### 21.5.1 以 f 为首的格式化字符串

```python
printf(f"I got {math:.lf} in math, {science:.lf} in science")
distance = 149597870700
myString = f"The sun is {distance:.4e} meters from the earth"
print(f"I got {math:.lf}% in math")
print(f"The sun is {distance} meters from the earth")
```

#### 21.5.2 format() 方法格式化字符串

```python
print("I got (0:.lf) in math, (1:.lf) in science".format(math, science))
```

### 21.6 更多的字符串处理方法

#### 21.6.1 分离字符串

split()

```python
name_string = "Sam,Brad,Alex,Cameron,Toby,Gwen,Jenn,Connor"
name_string.split(',')
# ['Sam', 'Brand', 'Alex', 'Cameron', 'Toby', 'Gwen', 'Jenn', 'Connor']
```

#### 21.6.2 拼接字符串

join()

```python
word_list = ['My', 'name', 'is', 'Warren']
' '.join(word_list)
# 'My name is Warren'
```

#### 21.6.3 搜索字符串

startswith()

```python
name = "Frankenstein"
name.startswith('F')      # True
name.startswith('Flop')   # False
```

endswith()

```python
name = "Frankenstein"
name.endswith('n')        # True
name.endswith('stone')    # False
```

in、index()

```python
add1 = '657 Maple Lane'
if 'Maple' in addr1:
  position = addr1.index('Maple')
  print(f"found 'Maple' at index {position}")
# found 'Maple' at index 4
```

find()

find() 方法检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内，如果指定范围内如果包含指定索引值，返回的是索引值在字符串中的起始位置。如果不包含索引值，返回-1。

```pyhotn
str.find(str, beg=0, end=len(string))
```

- str -- 指定检索的字符串
- beg -- 开始索引，默认为 0。
- end -- 结束索引，默认为字符串的长度。

#### 21.6.5 删除字符串的一部分

strip() 移除头尾指定的字符（默认为空格）或字符序列

```python
name = 'deWarren Sande'
name.strip('de')
# 'Warren San'
```

#### 21.6.6 改变大小写

lower() 全小写
upper() 全大写

## 22 文件的输入和输出

### 22.5 读文件

open() 打开文件
close() 关闭文件

```python
my_file = open('notes.txt', 'r')
lines = my_file.readlines()
print(lines)
my_file.close()
# ['Wash the car\n', 'Make my bed\n', 'Collect allowance\n']
```

rendlines() 读取全部文本
readline() 读取一行文本

```python
my_file = open('notes.txt', 'r')
first_line = my_file.readline()
second_line = my_file.readline()
print(f"first line = {first_line}")
print(f"second line = {second_line}")
my_file.close()
# first line = Wash the car
#
# second line = Make my bed
#
```

seek() 指定 Python 在文件中的位置（参数表示从文件起始位置开始计算的字节数）

```python
first_line = my_file.readline()
second_line = my_file.readline()
my_file.seek(0)

first_line_again = my_file.readline()
```

### 22.7 写文件

write()

- 在读文件时，文件模式使用 'r'

  ```python
  my_file = open('new_notes.txt', 'r')
  ```

- 在写文件时，文件模式使用 'w'

  ```python
  my_file = open('new_notes.txt', 'w')
  my_file.write("Spend allowance\n")
  my_file.close()
  ```

- 在追加文件内容时，文件模式使用 'a'

  ```python
  my_file = open('new_notes.txt', 'a')
  my_file.write("Spend allowance\n")
  my_file.close()
  ```

#### 22.7.3 使用 print()方法写文件

```python
my_file = open("new_file.txt", 'w')
print("Hello there, neighbor!", file=my_file)
my_file.close()
```

### 22.8 在文件中保存内容：pickle 模块

#### 22.8.1 使用 pickle 模块

dump() 把数据“倒入”文件中

```python
import pickle
my_list = ['Fred', 73, 'Hello there', 81.9876e-13]
pickle_file = open('my_pickled_list.pkl', 'wb')
pickle.dump(my_list, picke_file)
pickle_file.close()
```

#### 22.8.2 还原

load() 返回相应的原始数据结构

```python
import pickle
pickle_file = open('my_pickled_list.pkl', 'rb')
recovered_list = pickle.load(pickle_file)
pickle_file.close()
print(recovered_list)
# ['Fred', 73, 'Hello there', 8.19876e-12]
```

## 24 计算机仿真

### 24.4 时间对象

datetime 模块

datetime 类

> datetime 对象分为日期类和时间类。如果只关心日期，可以使用 date 类， 如果只关心时间，可以使用 time 类。

```python
import datetime
when = datetime.datetime(2021, 8, 21, 13, 48, 00)
print(when)
# 2021-08-21 13:48:00
print(when.year)    # 2021
print(when.day)     # 21
print(when.ctime()) # Sat Aug 21 13:48:00 2021
```

combine() 方法：把 date 对象和 time 对象结合起来，构成 datetime 对象

```python
today = datetime.date(month=8, day=21, year=2021)
some_time = datetime.time(second=00, hour=10, minute=45)
when = datetime.datetime.combine(today, some_time)
```

difference 类 得出两个日期或时间之差

```python
import datetime
yesterday = datetime.datetime(2021, 8, 20)
tomorrow = datetime.datetime(2021, 8, 22)
difference = tomorrow - yesterday
print(difference)
# 2 days, 0:00:00
print(type(difference))
# <class 'datetime.timedelta'>
```

now() 方法：给出计算机时钟的当前时间

> 尽管秒部分看起来像是浮点数，但它实际上是按秒和微秒存储的，这两者都是整数。要把他们转换为浮点数还需要一个简单的公式。

```python
print(datetime.datetime.now())
# 2021-08-21 13:57:42.525607
seconds_float = some_time.second + some_time.microsecond / 1000000
# 简单的公式
```

## 26 使用套接字建立连接

### 26.1 　文本与字节

encode() 方法：将字符串转换成字节

```python
hello_str = "Hello!"
hello_bytes = hello_str.encode('utf-8')
print(list(hello_bytes))
# [72, 101, 108, 108, 111, 33]
```

decode() 方法 ： 将字节转换成字符串

```python
secret_word = bytes([112, 105, 122, 122, 97])
print(secret_word.decode('utf-8'))
# pizza
```

如果字符串只包含 ASCII 字符，那么可以在字符串前面加上一个字母 b，把该字符串转换为 byte 对象

```python
some_bytes = b"pepperoni"
```
