#1 2022년 기준으로 나이로 출생년도 구하기 문제

def solution(age):
    answer = 2022 - age +1
    return answer



#2 모음 list를 만들고, 각 char가 모음인지 확인하기 위해 for문으로 문자열 길이만큼 반복
# char가 모음 list의 요소이면 answer의 문자열에 추가 안 함. else answer에 추가함.
def solution(my_string):
    vowels = ['a','e','i','o','u']
    answer = ''
    
    for i in my_string:
       if i in vowels:
           answer = answer
       else:
           answer = answer+i
        
    return answer


#2-2 문자열 my_string에서 각각의 char를 for문으로 모음인지 비교
# : 각 char가 모음 중 하나인지 확인하기 위해 모음 대조를 or로 연결
def solution(my_string):
    answer = ''
    for w in my_string :
        if w == 'a' or w =='e' or w=='i' or w=='o' or w=='u' :
            answer=answer
        else :
            answer=answer+w
            
    return answer

#2-3 모음 list를 만들고 .replace()로 모음 자리를 공백('')으로 대체
def solution(my_string):
    vowels = ['a','e','i','o','u']
    
    for vowel in vowels:
        my_string = my_string.replace(vowel, '')
        
    return my_string



#3 삼각형의 조건 문제: 가장 긴 변의 길이가 나머지 두 변의 길이의 합보다 같거나 크면 불가(return 2), else return 1.
# max와 sum을 이용해 배열의 최댓값과 배열의 합을 구함. 
# 최댓값: max(sides) / 나머지 두 변의 길이의 합: sum(sides)-max(sides)
# sides는 배열. len(sides)=3, 모든 변의 길이는 0보다 크고, 자연수이다.
def solution(sides):
    answer = 0
    if max(sides) < sum(sides)-max(sides):
        answer = 1
    else:
        answer = 2

    return answer