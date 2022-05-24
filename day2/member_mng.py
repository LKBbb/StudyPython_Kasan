# 회원관리 프로그램 탬플릿

num = 0

while True:
    print('메뉴번호를 입력하세요.')
    print('1. 회원정보입력')
    print('2. 회원정보검색')
    print('3. 회원정보수정')
    print('4. 회원정보삭제')
    print('5. 종료')
    
    num = input('숫자 입력 : ')
    if (num == '1') : #괄호 없어도 됨
        print('회원정보 입력화면으로 전환')
    elif (num == '2') :
        print('회원정보 검색화면으로 전환')
    elif (num == '3') :
        print('회원정보 수정화면으로 전환')
    elif (num == '4') :
        print('회원정보 삭제화면으로 전환')
    elif (num == '5') :
        break
    else :
        continue