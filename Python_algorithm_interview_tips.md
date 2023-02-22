# 파이썬 알고리즘 인터뷰
## 파이썬 문법
### 1. 인덴트(Indent, 들여쓰기)
✔ 공백 4칸
### 2. 네이밍 컨벤션(Naming Convention)
✔ 스네이크 케이스(Snake Case)를 따름 - 단어를 언더스코어(_)로 구분, 소문자표기<br>
<-> 카멜 케이스(Camel Case)
### 3. 타입 힌트(Type Hint)
```python
a: str = "1"
b: int = 1
```
✔ mypy - 타입 힌트에 오류가 없는지 자동으로 확인 가능
```python
$ pip install mypy
```
### 4. 리스트 컴프리헨션(List Comprehension)
✔ 리스트 컴프리헨션 - 기존 리스트를 기반으로 새로운 리스트를 만들어내는 구문
```python
// 홀수인 경우 2를 곱해 출력하는 리스트 컴프리헨션
[n * 2 for n in range(1,10+1) if n % 2 == 1]
```
✔ 표현식은 2개를 넘지 않는다.
### 5. 제너레이터(Generator)
✔ 제너레이터 - 루프의 반복 동작을 제어할 수 있는 루틴 형태<br>

✔ yield - 제너레이터가 여기까지 실행 중이던 값을 내보낸다는 의미로 중간값을 리턴한 다음 함수는 종료되지 않고 계속해서 맨 끝에 도달할때 까지 실행<br>

✔ next - 다음 값 생성
```python
def get_natural_number():
    n=0
    while True:
        n+=1
        yield n

g = get_natural_number()
for _ in range(0,100):
    print(next(g))
// 100개의 값을 생성 1,2,3,,,100
```
✔ range - 메모리 점유율 적음, 인덱스로 접근시에는 바로 생성하도록 구현(리스트와 거의 동일한 느낌)
### 6. enumerate
✔ enumerate() - 여러 가지 자료형(list, set, tuple등)을 인덱스로 포함한 enumerate 객체로 리턴<br>

✔ 인덱스르 자동으로 부여함
```python
a=['a1','b1','c1']
for i, v in enumerate(a):
    print(i,v)
```
### 7. print
✔ 항상 줄바꿈
1. 콤마 - 한 칸 공백이 디폴트
```python
>>> print('A1','B2')
A1 B2
```
2. sep 파라미터
```python
>>> print('A1','B2', SEP=',')
A1,B2
```
3. end 파라미터
```python
>>> print('aa', end=' ')
>>> print('bb')
aa bb
```
4. join() - 리스트를 출력
```python
>>> a = ['A','B']
>>> print(' '.join(a))
A B
```
5. f-string - 3.6+에서만 지원
```python
>>> idx = 1
>>> fruit = "Apple"
>>> print(f'{idx + 1}: {fruit}')
2: Apple
```
### 8. pass
✔ pass - 널 연산으로 아무것도 하지 않는 기능
### 9. locals
✔ locals() - 로컬 심볼 테이블 딕셔너리를 가져오는 메소드로 업데이트 또한 가능<br>

✔ 로컬에 선언된 모든 변수를 조회할 수 있는 강력한 명력으로 디버깅에 도움
```python
import pprint
pprint.pprint(locals())
```
