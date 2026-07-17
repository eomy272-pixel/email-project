import os

receiver = os.environ.get('RECEIVER_EMAIL')
print(f"DEBUG_START")
if receiver:
    print(f"이메일이 확인되었습니다: {receiver[:2]}****") # 앞 두 글자만 보이게 함
else:
    print("오류: RECEIVER_EMAIL이 비어있습니다!")
print(f"DEBUG_END")
