import smtplib
from email.mime.text import MIMEText
import os

# 1. GitHub Secrets에서 정보 가져오기
receiver = os.environ.get('RECEIVER_EMAIL')
sender_email = "본인아이디@naver.com"  # 여기에 본인의 네이버 이메일을 입력하세요
sender_pw = os.environ.get('NAVER_CLIENT_SECRET')

# 2. 메일 내용 만들기
msg = MIMEText("테스트 메일이 성공적으로 발송되었습니다!")
msg['Subject'] = "GitHub Actions 메일 발송 테스트"
msg['To'] = receiver

# 3. 네이버 SMTP를 이용한 메일 발송
try:
    s = smtplib.SMTP_SSL('smtp.naver.com', 465)
    s.login(sender_email, sender_pw)
    s.sendmail(sender_email, receiver, msg.as_string())
    s.quit()
    print("메일 발송 성공!")
except Exception as e:
    print(f"오류 발생: {e}")


