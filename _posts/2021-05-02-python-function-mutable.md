---
layout: post
title: python 함수 밖 list와 integer를 가져와서 연산하는 방법
subtitle: integer는 불러와야 하는데, list는 안불러와도 그냥 바로 쓸 수 있다!
categories: Basic
tags: [Basic, CodingTest]
---
python 함수 밖에 있는 데이터를 함수 안에 가져와서 연산하고 변화된 데이터를 return해야할 때가 있죠!

python 기초 공부를 마치신 분들은 integer를 함수 안으로 가져오는 방법에 대해서 익숙하실겁니다.

저도 integer에 대해서 공부했기때문에, list를 가져오는 방법도 동일할 것이라고 생각했습니다.

📌 그렇지만 list는 integer와 달리 불러오지 않아도 함수 안에서 바로 사용할 수 있습니다‼️

이유가 뭘까요?

## 함수 밖의 integer를 함수 안으로 가져오는 방법

두 가지 방법이 알려져 있습니다.

1. **매개변수**로 가져오기

   * def function(매개변수)에서 "매개변수" 자리에 integer를 넣어준다.

   * 함수 안에서 연산한다.

   * 변화된 integer 값을 (new_integer) return 으로 내보낸다.

```python
integer = 1
def function(integer):
    integer +=1
    return integer
new_integer = function(integer)
print(new_integer)
#-> 2
```

2. **global**을 사용하기
   * 매개변수를 사용하지 않고 global interger로 가져온다.
   * 함수 안에서 연산한다.
   * return으로 변화된 값을 내보낸다.

```python
integer = 1
def function():
    global integer
    integer +=1
    return integer
new_integer = function()
print(new_integer)
#-> 2
```

## 함수 밖의 list를 함수 안으로 가져오는 방법

📌list는 함수 밖 list를 사용할 때, 그냥 바로 사용하면 됩니다.

​	integer와 달리 매개변수로 데러오지 않아도, global로 선언하지 않아도 됩니다‼️

```python
l = [1,2,3]
def function():
    l[0]+=100
    l.pop()
    
function()
print(l)
#-> [101, 2]
```

## list와 integer 방법 차이 원인

📌 integer는 **immutable**(변화 불가능한) 

* integer가 정의되면 특정 주소에 저장되기 때문에, integer를 복사하고 그 값을 연산해도 원본 값은 변화하지 않는다. 
* 따라서 매개변수 또는 global로 직접 값을 가져와서 연산해줘야 원본에 변화를 줄 수 있다.

📌list는 **mutable**(변화 가능한)

* list.pop()과 같은 연산은 list 원본에 변화를 줄 수 있다.
* 따라서 **함수 내부에서 list의 연산은 함수 밖의 list 원본에 영향을 미친다.** 

출처 : https://stackoverflow.com/questions/23029727/why-do-list-operations-in-python-operate-outside-of-the-function-scope

