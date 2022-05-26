# 파일 테스트
# f = open('C:/Repository/StudyPython_Kasan/day4/sample2.log', mode = 'w', encoding = 'UTF-8') # 절대 경로
f = open('./day4/sample3.log', mode = 'w', encoding = 'UTF-8') # 상대 경로
f.write('테스트, 테스트 !!!')
f.close()
print('로그파일 생성완료')