'''
    리스트 => 리스트가 생성 된 후 추가, 삭제, 삽입이 가능하다.
'''
# 과일 리스트 생성.
fruits = ['딸기', '사과', '바나나']
print("과일 목록 : ", fruits)

# 수박 추가 => append() 메소드 사용. (마지막에 추가)
fruits.append('수박')
print("과일 목록(수박 추가) : ", fruits)
fruits.append('망고')
print("과일 목록(망고 추가) : ", fruits)

# 포도 추가 => + 연산자 사용.
fruits = fruits + ['포도']  # 포도를 더해서 fruits에 저장  num = num+ 1
print("과일 목록(포도 추가) : ", fruits)

# 망고가 있나?  => in 연산자 사용(포함되는가?)
print("과일 목록에 망고가 있나요? ", '망고' in fruits)

# 과일 목록에 과일의 개수는? 리스트의 길이는?  len()
print("과일의 개수는 ? ", len(fruits))

# 과일 목록 중 첫 번째 과일은?
print("제일 좋아하는 과일은? ", fruits[0])

# 과일 목록 중 가장 마지막 과일은?
print("제일 싫어하는 과일은? ", fruits[-1])

fruits.append('두리안')

print("과일 중 가장 큰 과일은?(사전식 순서) ", max(fruits))
print("과일 중 가장 작은 과일은?(사전식 순서) ", min(fruits))

# 정렬
# 오름차순
fruits.sort()
print("과일 오름차순 : ", fruits)

# 내림차순
fruits.sort(reverse=True)
print("과일 내림차순 : ", fruits)