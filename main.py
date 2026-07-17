import os
import requests
import json
import smtplib
from email.mime.text import MIMEText

# 1. 환경 변수에서 설정 정보 가져오기
receiver_email = "um0241@naver.com"
sender_email = "um0241@naver.com"
# 메일 발송용 앱비밀번호와 네이버 API Secret이 같은 경우입니다
sender_pw = os.environ.get('NAVER_CLIENT_SECRET') 
client_id = os.environ.get('NAVER_CLIENT_ID')
client_secret = os.environ.get('NAVER_CLIENT_SECRET')

# 2. 네이버 데이터랩 API 호출 함수
def get_naver_keywords():
    url = "https://openapi.naver.com/v1/datalab/search/rank"
    headers = {
        "X-Naver-Client-Id": client_id,
        "X-Naver-Client-Secret": client_secret,
        "Content-Type": "application/json"
    }
    # 카테고리: 전체, 기기: PC
    data = {"category": "50000000", "device": "pc"} 
    response = requests.post(url, headers=headers, json=data)
    return response.text

# 3. 메일 발송 실행
try:
    content = get_naver_keywords()
    
    # 메일 구성
    msg = MIMEText(content)
    msg['Subject'] = "네이버 실시간 인기 키워드 데이터"
    msg['To'] = receiver_email
    msg['From'] = sender_email

    # SMTP 서버 연결 (네이버 메일)
    s = smtplib.SMTP_SSL('smtp.naver.com', 465)
    s.login(sender_email, sender_pw)
    s.sendmail(sender_email, receiver_email, msg.as_string())
    s.quit()
    print("메일 발송 성공!")
except Exception as e:
    print(f"오류 발생: {e}")
