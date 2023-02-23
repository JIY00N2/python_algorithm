# 리스트 / 딕셔너리
## 1. 리스트
✔ 리스트 - 순서대로 저장하는 시퀀스이자 변경 가능한 목록

### 1-1 리스트의 주요 연산 시간 복잡도

|연산|시간 복잡도|설명|
|:---:|:---:|:---:|
|len(a)|O(1)|전체 요소의 개수를 리턴|
|a[i]|O(1)|인덱스 i의 요소를 가져옴|
|a[i:j]|O(k)|인덱스 i부터 j-1까지 슬라이스의 길이만큼의 k개의 요소를 가져온다.<br> 이 경우 객체 k개에 대한 조회가 필요하므로 O(k)이다.|
|elem in a|O(n)|elem 요소가 존재하는지 확인한다. <br>처음부터 순차 탐색하므로 n만큼 시간이 소요된다.|
|a.index(elem)|O(n)|elem 요소의 인덱스를 리턴한다.|
|a.append(elem)|O(1)|리스트 마지막에 elem 요소를 추가한다.|
|a.pop()|O(1)|리스트 마지막 요소를 추출한다. 스택의 연산이다.|
|a.pop(0)|O(n)|리스트 첫번째 요소를 추출한다. 큐의 연산이다.<br>이 경우 전체 복사가 필요하므로 O(n)이다. <br> 큐의 연산을 주로 사용한다면 리스트보다는 O(1)에 가능한 데크(deque) 권장
|del a[i]|O(n)|i에 따라 다르다. 최악의 경우 O(n)|
|a.sort()|O(nlogn)|정렬한다. <br>팀소트(Timsort)를 사용하며, 최선의 경우 O(n)에서도 실행 가능|
|min(a), max(a)|O(n)|최솟값 / 최댓값을 계산하기 위해서는 전체를 선형 탐색함|
|a.reverse|O(n)|뒤집는다. 리스트는 입력 순서가 유지되므로 뒤집으면 입력 순서가 반대|

### 1-2 리스트 활용 방법
1. 선언 - list(), []
```python
>>> a = list() # list()
>>> a= [] # []
```
2. 추가 - append, insert
```python
>>> a = [1,2,3]
>>> a.append(4) # append (문자, 불리언도 가능)
>>> a
1 2 3 4
>>> a.insert(3,5) # insert
>>> a
[1,2,3,5,4]
```
3. 슬라이싱
```python
>>> a = [1,2,3,5,4]
>>> a[1:3] # 슬라이싱
[2,3]
>>> a[1:4:2]
[2,5]
```
4. 삭제 - del, remove, pop
```python
>>> a = [1,2,3,5,4,'안녕',True]
>>> del a[1] # del
>>> a
[1,3,5,4,'안녕',True]
>>> a.remove(3) # remove
>>> a
[1,5,4,'안녕',True]
>>> a.pop(3) # pop
'안녕'
>>> a
[1,5,4,True]
```
## 2. 딕셔너리
✔ 딕셔너리 - 키 / 값 구조로 이뤄진 딕셔너리 <br>
✔ 숫자, 문자, 집합까지 불변 객체릴 모두 키로 사용 가능<br>
✔ 해시 테이블로 구현<br>
✔ 해싱 - 해시 테이블을 이용해 자료를 저장
### 2-1 딕셔너리의 주요 연산 시간 복잡도
|연산|시간 복잡도|설명|
|:---:|:---:|:---:|
|len(a)|O(1)|요소의 개수를 리턴|
|a[key]|O(1)|키를 조회하여 값을 리턴|
|a[key] = value|O(1)|키 / 값을 삽입|
|key in a|O(1)|딕셔너리에 키가 존재하는지 확인|
### 2-2 딕셔너리 활용 방법
1. 선언 - dict(), {}
```python
>>> a = dict() # dict()
>>> a= {} # {}
```
2. 추가
```python
>>> a = {'key1': 'value1','key2': 'value2'}
>>> a['key3'] = 'value3'
>>> a
{'key1': 'value1','key2': 'value2', 'key3': 'value3'}
```
3. 조회 - items()
```python
>>> for k,v in a.itmes(): # items()
        print(k,v)
        
key1 value1
key2 value2
key3 value3
```
4. 삭제 - del
```python
>>> a = {'key1': 'value1','key2': 'value2', 'key3': 'value3'}
>>> del a['key1'] # del
>>> a
{'key2': 'value2', 'key3': 'value3'}
```
### 2-3 딕셔너리  모듈
1. defaultdict 객체<br>
✔ defaultdict 객체 - 존재하지 않는 키를 조회할 경우, 에러 메시지를 출력하는 대신 디폴트 값(0)을 기준으로 해당 키에 대한 딕셔너리 아이템을 생성해줌<br>
✔ 실제로는 collections.defaultdict 클래스를 가짐
```python
>>> a = collections.defaultdict(int)
>>> a['A']=5
>>> a['B']=4
>>> a
defaultdict(<class 'int'>, {'A':5, 'B': 4})

>>> a['C'] += 1
>>> a
defaultdict(<class 'int'>, {'A':5, 'B': 4, 'C': 1})
```
2. Counter 객체<br>
✔ counter 객체 - 아이템에 대한 개수를 계산해 딕셔너리로 리턴<br>
✔ 실제로는 딕셔너리를 한 번 더 래핑한 collections.Counter 클래스를 가짐<br>
✔ most_common() - Counter 객체에서 가장 빈도 수가 높은 요소 추출
```python
>>> a = [1,2,3,4,5,5,5,6,6,]
>>> b = collections.Counter(a)
>>> b
Counter({5: 3, 6: 2, 1: 1, 2: 1, 3: 1, 4: 1})

>>> type(b)
<class 'collections.Counter'>

>>> b.most_common(2)
[(5,3), (6,2)] # 가장 빈도가 높은 2개의 요소 추출
```
3. OrderedDict 객체<br>
✔ 3.6이하에서 입력 순서가 유지되는 OrderedDict 객체 제공<br>
✔ 3.7 부터는 필요 없음
```python
>>> collections.OrderDict({'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2})
OrderedDict([('banana',3), ('apple',4), ('pear',1), ('orange',2)])
```
#### 🎯 타입 선언
```python
# 리스트
>>> type([])
<class 'list'>
# 튜플
>>> type(())
<class 'tuple'>
# 딕셔너리
>>> type({})
<class 'dict'>
# set
>>> type({1})
<class 'set'>
```