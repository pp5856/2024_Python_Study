a = 3 # 같다라는 것이 아니라, 담아서 저장한다는 느낌
a = a + 1 #따라서 이거 가능 a를 a + 1이란 값으로 새로 지정해서 a에 저장함
print(a)

#basic 터미널 명령어
# cls -> 정리

# Chapter 1 == 자료형
# 숫자형
# - 정수형
# - 실수형
# - 컴퓨터 지수 표현, 8진수, 16진수 등등 ...

a = 3
b = 4
c = a + b
print(c)
print(a + b)
print("----------------------")

print(type(a))

b = 1.2

print(type(b))
print("----------------------")

#지수 표현
a = 4.24E10
print(a)
a = 4.24e-10

print("----------------------")
#8진수, 16진수
a = 0o177 # 1 * 8^2 + 7*8 + 7 = 127
print(a)
a = 0x8ff # 8*16^2 + 14*16 + 14 =2303
print(a)

print("----------------------------------------------")

#사칙 연산

a = 17
b = 4
c = a + b
print(c)
print(a + b)
print(a/b)
print(a//b) # //는 몫
print(a%b) # %는 나머지
print(a*b)
print(a**b) #지수표현

print("----------------------------------------------")

#문자열
a = "I'm \" hungry" # \는 뒤에 문자열 보존 따라서 오류 수정 가능
b = '''I'm studying now''' # ''' '''도 사용 가능
print(a)
print(b)
multiline = "Life is too short\nYou need python" #이스케이프 코드 \n -> 줄바꿈
multiline='''
... Life is too short
... You need python
... ''' # 큰 따옴표, 작은 따옴표 3개도 줄바꿈 인식
print(multiline)
 
'''
 이스케이프 코드 설명

\n	문자열 안에서 줄을 바꿀 때 사용
\t	문자열 사이에 탭 간격을 줄 때 사용
\\	\를 그대로 표현할 때 사용 #
\'	작은따옴표(')를 그대로 표현할 때 사용
\"	큰따옴표(")를 그대로 표현할 때 사용

\r	캐리지 리턴(줄 바꿈 문자, 커서를 현재 줄의 가장 앞으로 이동)
\f	폼 피드(줄 바꿈 문자, 커서를 현재 줄의 다음 줄로 이동)
\a	벨 소리(출력할 때 PC 스피커에서 '삑' 소리가 난다)
\b	백 스페이스
\000	널 문자
'''
#주석 들여쓰기 잘해야됨
print("----------------------------------------------")
head = "Python"
tail = " is fun!"
print(head + tail)

print(head * 3) #문자열 곱하기 가능/ 숫자랑만 가능

print("="*50)

print(head +'\n'+tail)

print("="*50)

#인덱싱과 슬라이싱
head = "Python"
print(len(head)) #길이
print(head[3])
print(head[-1])

a = "Life is too short, You need Python"
print(a[0:4]) # a[이상:미만:간격]
print(a[:]) # 비어 있으면 처음부터 or 끝까지
print(a[::2]) # 2칸 간격
print(a[::2]) # -1 거꾸로

# 문자열의 요솟값은 변경 불가능한 자료형 immutable이다

'''문자열 포맷팅'''

print(" %10.4f " % 3.41233332) #칸 표시, 소수점 표시
# %s	문자열(String) 만능
# %c	문자 1개(character)
# %d	정수(Integer)
# %f	부동소수(floating-point)
# %o	8진수
# %x	16진수
# %%	Literal % (문자 % 자체)
a = "{0} {1}".format(2,4)
b = "{number} {day}".format(number=3, day=5)
print(a+"\n"+b)

a = "{0:>10}".format("hi")
print(a)
a = "{0:*^10}".format("hi") # 10 = 칸수, > = 오른쪽 정렬, ^가운데 정렬, 앞에 문자는 공백 채우기
print(a)

name = "hi"
a = f"{name:#>10}"
print(a)
"""f 포맷팅 제일 최신**"""
name = "응애"
print(f"{name}")

age = 21
a = f'내년엔 {age + 1}이다'
print(a)

y = 5.3124125
a = f'{y:0.6f}'
print(a)

number = 1234567890
print(f"{number:,}")

'''문자열 관련 메소드'''

a = "hobby"
print(a.count('b'))

print(a.find('b')) #문자열이 처음으로 나온 인덱스의 위치를 반환한다. / 없는거 -1 반환

#print(a.index('x')) find 함수랑 비슷하지만 없는 거 했을 때 에러남

a = ",".join('abcd') #문자열 사이사이에 문자 넣음
print(a)

a = ",".join(['a','b','c'])
print(a)

a ='hi'
print(a.upper()) #대문자

a = a.upper()
print(a)
print(a.lower()) # 소문자 바꾸기

a = "      s dd          "
print(a.rstrip()) #오른쪽 공백 지우기
print(a.lstrip())
print(a.strip())

'''replace(,)문자열 바꾸기'''

a = "Life is too short"
print(a.replace("Life", "Your face"))

print(a.split()) #문자열 쪼개기
#split 아무것도 없을 땐 띄어쓰기 기준으로 나눔
a = "a:b:c:d"
print(a.split(":"))
a = a.split(":")
print(type(a))


print('='*50)


"""리스트 자료형"""

a = [1, 2, 3, 4, 5, 's', 'd']
print(a[0:5:2])
print(a[::3])

a = [1, 2, ['a','b','c']]
print(a[1:4])
