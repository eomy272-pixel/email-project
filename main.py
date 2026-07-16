import os

# 환경 변수에서 값 가져오기
receiver = os.environ.get('RECEIVER_EMAIL')

print("메일 발송 작업을 시작합니다!")
print(f"목표 주소: {receiver}")
