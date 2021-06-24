# 딕셔너리

person = {}

person['name'] = '홍길동'
person['age'] = 40
print(person)

person['address'] = '전라도'
print(person)

#dic의 value 출력
for value in person:
    print(person[value])

#요소 삭제: dic.pop('address') 와 같
del person['address']
print(person)
