

import os
import requests
import json
import smtplib
from email.mime.text import MIMEText

# 1. 설정 정보
receiver_email = "um0241@naver.com"
sender_email = "um0241@naver.com"
sender_pw = os.environ.get('NAVER_CLIENT_SECRET') # 메일 발송용 앱 비밀번호
client_id = os.environ.get('NAVER_CLIENT_ID')
client_secret = os.environ.get('NAVER_CLIENT_SECRET_API') # API용 Secret

# 2. 네이버 데이터랩 API 호출
def get_naver_keywords():
    url = "https://openapi.naver.com/v1/datalab/search/rank"
    headers = {
        "X-Naver-Client-Id": client_id,
        "X-Naver-Client-Secret": client_secret,
        "Content-Type": "application/json"
    }
    data = {"category": "50000000", "device": "pc"} 
    response = requests.post(url, headers=headers, json=data)
    return response.text

# 3. 메일 발송
try:
    content = get_naver_keywords()
    msg = MIMEText(content)
    msg['Subject'] = "오늘의 네이버 인기 키워드 데이터"
    msg['To'] = receiver_email
    msg['From'] = sender_email

    s = smtplib.SMTP_SSL('smtp.naver.com', 465)
    s.login(sender_email, sender_pw)
    s.sendmail(sender_email, receiver_email, msg.as_string())
    s.quit()
    print("메일 발송 성공!")
except Exception as e:
    print(f"오류 발생: {e}")
