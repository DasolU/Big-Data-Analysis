---
layout: post
title: BAEKJOON 백준 시작 방법 초보자 길라잡이
subtitle: 프로그래머스랑 다르게 입력을 받아서 처리해야하네? 어떻게 하는거지
tags: [CodingTest, BAEKJOON]
categories: CodingTest
---

프로그래머스만 사용하다가 백준을 시작하면 테스트 값 입력 방식이 달라서 당황스러울 수 있습니다.

백준은 프로그래머스와 다르게 입력 값을 직접 받아서 처리해줘야하기 때문입니다.

백준 [ABCDE 문제 13023번][1]을 예로 들며 백준 문제 풀기 방법에 대해 익혔습니다.

## 입력 예시

프로그래머스에서는 함수를 만들고 제출하면 함수에 입력 값이 자동으로 입력되었었죠?

**하지만 백준에서는 답안을 제출할 때 입력을 받아서 처리한뒤 사용하는 코드를 추가해줘야합니다.**

예를 들어, 백준에서는 아래와 같이 배열도 리스트도 아닌 숫자 모음이 입력 예시로 주어집니다.

```python
5 4
0 1
1 2
2 3
3 4
```

## 입력 값 받아오기

백준에서 공식적으로 추천하는 방법은 **input()** 사용입니다.

```python
a, b = map(int, input().split())
print(a,b)
```



그런데 문제 풀이를 구글에 검색해보면 **sys.stdin.readline()**을 사용합니다. (stdin은 standard input을 의미합니다.)

📌**input()대신 sys.stding.readline을 사용하면 input이 여러 줄인 경우 시간 초과를 막을 수 있습니다.** 

📌**sys.stdin.readline()**은 입력 값을 **한 줄 단위로 읽고 str 자료형으로 저장**합니다.

* 따라서 input이 여러 줄이라면 for loop에서 **sys.stdin.readline()**를 사용하여 한 줄씩 읽어주면 됩니다.

* 따라서 str 자료형을 int로 바꿔줘야합니다.

```python
# 입력 받기
import sy
input = sys.stdin.readline	# 한 줄 단위로 입력되고 str으로 저장된다.
```

### 한 줄 읽기

```python
# 한 줄씩 읽기
n, m = map(int, input().split())	# 입력의 첫 번째 줄의 str을 모두 int로 바꾼다.
a, b = map(int, input().split())
c, d = map(int, input().split())
print(n,m)  #->5 4
print(a,b)  #->0 1
print(c,d)  #->1 2
```

### 여러 줄 읽기: 반복문 사용

```python
# 여러 줄 반복문으로 읽기
n, m = map(int, input().split())
for _ in range(m):
    a, b= map(int, input().split())
```

[1]: https://www.acmicpc.net/problem/13023

