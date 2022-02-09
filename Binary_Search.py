#이진탐색
#데이터는 정렬이 되어있고 반으로 나눠가며 비교
#여기서는 오름차순으로 정렬된 데이터를 사용함

def b_search(lst, target):      #lst는 탐색할 데이터리스트, target은 찾을 값
    head = 0
    tail = len(lst)-1    
    #head와 tail은 탐색범위의 양끝의 index번호를 나타냄 
    # -> head와 tail의 이동(값의 변화)는 탐색범위의 변화
    
    #반복횟수를 예측하기 힘드므로 while
    while head <= tail: 
        center = (head+tail)//2 
        #center는 현재 head와 tail의 중앙 index를 저장한다.(head와 tail의 평균값)
        #소수점은 필요 없으므로 몫만 구한다. (//)
        #int((head+tail)/2)로 소수점을 날려도된다.
        
        if target == lst[center]:   #찾으려는 값과 lst중앙의 값이 같은지 비교
            result = f'{center}번 index요소와 일치'
            return result           #같으면 여기서 result 반환하고 함수 종료
        
        elif target > lst[center]:  #target이 크다면
            head = center + 1       #head의 값을 조정(탐색범위의 축소)
        else: 
            tail = center - 1       #target이 작다면 tail을 조정(탐색범위의 축소)
            
    result = "찾지 못했습니다."        
    return result   #탐색이 끝나도 값이 존재하지 않다면 여기서 result 반환하고 함수종료



lst = [i for i in range(25,100)]
print(f'{lst[0]}~{lst[-1]}까지의 데이터')
target = int(input('찾을 정수를 입력 >> '))

print(b_search(lst, target))

# 예외처리시
# try:
#     target = int(input('찾을 정수를 입력 >> '))
#     print(b_search(lst, target))
# except ValueError as e:
#     print(e)
#     print('즐거운 오해')