# 1 두 수의 차 구하기
# 변수명으로 함수 먼저 정의, 변수값을 입력받으면 함수 실행 후 계산함.

def solution(num1, num2):
    answer = num1 - num2
    return answer


# 2 배열 원소의 길이 구하기 
# 배열의 길이(len(strlist))만큼 for문으로 반복하려면 
# : range()를 사용
# len(): 길이를 int로 반환
# 배열의 각 요소에 접근하려면 []로 인덱스 접근
# 튜플?? : 

# 오답 코드:
#    for i in len(strlist):
#         i = 0      
#         i =+ 1      
#         answer.append(len(i))

# 오답 분석: for문의 i값이 배열의 길이, 요소의 개수를 계산-> i값이 요소 갯수만큼 반복되면서 자기자신 문자열의 길이를 계산한다고 생각함
##         answer.append(len(i)) ==> len(i)는 말하자면 len(1),len(2)와 다름 없다. 안에 길이값만 들어간다.


def solution(strlist):
    answer = []
    for i in range(len(strlist)):
        answer.append(len(strlist[i]))
    return answer



# 3 편지지의 최소 가로 길이 계산하기
# 조건: 내용은 영소문자, 공백, 특수문자로 구성되고 각각은 하나의 문자 취급
# 문자당 가로 2cm로 작성할 것. 전체 문자수는 1이상 50이하.

def solution(message):
    answer = 2 * len(message)
    return answer