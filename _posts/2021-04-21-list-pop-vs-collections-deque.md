---
layout: post
title: Queue 구현? list.pop(0) vs. deque.popleft()
subtitle: 둘 중에 뭘 써야하지? 효율성을 따져보자!
tags: [CodingTest, Efficiency]
categories: CodingTest
---

[BFS 알고리즘][3]을 작성할 때 queue(큐)를 구현하기 위해서 list 자료형을 즐겨 사용하셨나요? 

하지만 큐에서 데이터를 제거할 때 queue.pop(0)을 사용하면 코딩테스트에서 효율성 점수😅가 낮게 나올 수 있어요! (아래 예시에서 확인할 수 있습니다.) 

효율성을 높이기 위해 큐를 구현하는 다른 방법을 공부하고 두 방법의 효율성을 비교했습니다.



## Queue를 만드는 방법들

### List 사용

```python
queue = [] 
node = queue.pop(0)	# 가장 왼쪽 node 제거 
queue.append(new_node)	# 가장 오른쪽에 node 추가
```

#### 단점: 삽입&삭제 효율성 낮다.

* Contiguous list 자료형은 linear list(선형 리스트)에 속하기 때문에 **빈 공간 없이 차례대로 데이터를 저장**하는 특징이 있습니다. 따라서 list에 데이터를 추가/제거하면 추가/제거하려는 위치 뒷부분의 **데이터를 이동**합니다.

* 즉, list로 구현한 큐에 데이터를 추가/제거할 때, 시간 복잡도는 **O(n)**이므로 데이터 개수가 많아지면 시간이 오래 걸리는 단점이 있습니다.

#### 장점: 쉬운 데이터 접근 



### Deque(데크) 사용

🌟새로운 방법 

collections 모듈이 제공하는 Deque(데크)를 사용합니다.

Deque(double-ended queue)는 데이터를 양방향에서 추가하고 제거할 수 있는 자료 구조입니다.

따라서 데크 자료 구조의 왼쪽에서 데이터를 제거하고 오른쪽으로 새로운 데이터를 삽입하면 큐와 같은 기능을 하게 됩니다.

```python
from collections import deque
queue = deque()
node = queue.popleft()	# 가장 왼쪽 node 제거 
queue.append(new_node)	# 가장 오른쪽에 node 추가
```

#### 장점: 삽입&삭제 효율성이 높다.

* deque는 [linked list 자료형][4]을 사용한다고 합니다. 따라서 데이터를 추가/제거할 때, 시간 복잡도는 **O(1)**이므로 데이터 개수가 많을수록 list로 구현한 queue보다 월등하게 효율적이게 됩니다.

* 시간 복잡도에 대한 내용은 [이 블로그][1] 와 [이 글][5]을 참고해서 만들었습니다.

#### 단점: 어려운 데이터 접근



## 예시

프로그래머스 스택/큐 카테고리의 [주식가격][2] 문제에 두 가지 방법을 적용해보았습니다.

### list.pop(0)

```python
def solution1(prices):
    answer = []
    q = prices # list로 만든 queue
    q_idx = list(range(0,len(prices)))	# list로 만든 queue
    max_idx = len(prices)-1
    while q:
        time = 0
        node = q.pop(0)
        node_idx = q_idx.pop(0)
        for i in range(len(q)):
            if node>q[i]:
                time = (i+node_idx+1)-node_idx
                break
        if time == 0:
            time = max_idx-node_idx
        answer.append(time)
    return answer
```

#### 성능

solution1을 프로그래머스에서 채점하면 시간 초과로 인해 실패합니다.❌

```python
정확성: 66.7
효율성: 0.0 (시간 초과)
```

```python
정확도 테스트
테스트 1 〉 	 통과 (0.01ms, 10.2MB)
테스트 2 〉    통과 (0.09ms, 10.1MB)
테스트 3 〉    통과 (0.97ms, 10.3MB)
테스트 4 〉    통과 (1.17ms, 10.2MB)
테스트 5 〉    통과 (1.37ms, 10.3MB)
테스트 6 〉    통과 (0.04ms, 10.3MB)
테스트 7 〉    통과 (0.68ms, 10.2MB)
테스트 8 〉    통과 (0.86ms, 10.3MB)
테스트 9 〉    통과 (0.05ms, 10.2MB)
테스트 10 〉   통과 (1.30ms, 10.3MB)
```

### deque.popleft()

solution1과 동일하지만 deque로 바꾼 솔루션입니다.

```python
from collections import deque
def solution2(prices):
    answer = []
    q = deque(prices)	# deque로 만든 queue
    q_idx = deque(list(range(0,len(prices))))	# deque로 만든 queue
    max_idx = len(prices)-1
    while q:
        time = 0
        node = q.popleft()
        node_idx = q_idx.popleft()
        for i in range(len(q)):
            if node>q[i]:
                time = (i+node_idx+1)-node_idx
                break
        if time == 0:
            time = max_idx-node_idx
        answer.append(time)
    return answer
```

#### 성능

효율성이 높아졌습니다! ⭕️

```python
dequeue 사용
정확성: 66.7
효율성: 26.7
합계: 93.3 / 100.0
```

```python
정확도 테스트
테스트 1 〉    통과 (0.01ms, 10.2MB)
테스트 2 〉    통과 (0.08ms, 10.3MB)
테스트 3 〉    통과 (0.92ms, 10.2MB)
테스트 4 〉    통과 (1.07ms, 10.3MB)
테스트 5 〉    통과 (1.09ms, 10.2MB)
테스트 6 〉    통과 (0.04ms, 10.2MB)
테스트 7 〉    통과 (0.40ms, 10.2MB)
테스트 8 〉    통과 (0.70ms, 10.3MB)
테스트 9 〉    통과 (0.05ms, 10.2MB)
테스트 10 〉   통과 (1.79ms, 10.3MB)
효율성 테스트
테스트 1 〉    통과 (247.57ms, 21.2MB)
테스트 2 〉    통과 (149.96ms, 19MB)
테스트 3 〉    실패 (시간 초과)
테스트 4 〉    통과 (193.79ms, 19.7MB)
테스트 5 〉    통과 (97.84ms, 18.3MB)
```



[1]: https://www.daleseo.com/python-queue/

[2]: https://programmers.co.kr/learn/courses/30/parts/12081
[3]: https://dasolu.github.io/algorithm/2021/04/20/BFS.html
[4]: https://dasolu.github.io/basic/2021/04/14/data-structure-array-linked-list.html

[5]: https://docs.python.org/3/library/collections.html#collections.deque

