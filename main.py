import os

receiver = os.environ.get('RECEIVER_EMAIL')
print(f"DEBUG: 환경 변수에서 가져온 값은 '{receiver}' 입니다.")

if not receiver:
    print("오류: RECEIVER_EMAIL 환경 변수를 찾을 수 없습니다!")
else:
    print(f"메일 발송 작업을 시작합니다! 목표 주소: {receiver}")
