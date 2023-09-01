import smtplib
import os
from email.message import EmailMessage
from datetime import date

date_td = date.today()
date_td = date_td.strftime("%a %d %b %Y")
print(date_td)

def send_news(content):
    # Secret values need to be added to perm environment variables
    USERNAME = os.getenv("PY_USERNAME")
    PASSWORD = os.getenv("PY_PASSWORD")
    # RECIVER added for re-usability
    RECIEVER = os.getenv("PY_USERNAME")

    msg = EmailMessage()
    msg['Subject'] = f"🚴🏻🗞️ Todays News: {date_td}"
    msg['From'] = USERNAME
    msg['To'] = RECIEVER

    
    html = f"""
    <html>
        <body>
    """
    for item in content:
        # embedded_email = f"<a href={item['URL']}>{item['Source']}</a>" # - US configuration
        embedded_email = f"<a href={item['URL']}>{item['Author']}</a>"
        html = html + "<br>" + "<b>" + item["Title"] + "</b>" +"<br>" + embedded_email + "<br>"
    html = html + """
        </body>
    </html>
    """

    msg.set_content(html, subtype='html')

    s = smtplib.SMTP_SSL('smtp.gmail.com')
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com') as s:
            # uncomment == DEBUG
            # s.set_debuglevel(1)
            s.login(USERNAME, PASSWORD)
            s.send_message(msg)
            print("🚴🏻 News sent successfully! ")
    except:
        print("Email sending failed, set debug via 's.set_debuglevel(1)'")
        print('REMINDER: Export secrets locally')

if __name__ == "__main__":
    attempts = 0
    while attempts < 3:
        try:
            dummy_data = [{'Title': 'Burger King Faces Whopper Lawsuit As More Customers Challenge Fast Food Giants Over Portion Sizes—Including McDonald’s, Wendy’s', 'Source': 'Forbes', 'URL': 'https://www.forbes.com/sites/roberthart/2023/08/30/burger-king-faces-whopper-lawsuit-as-more-customers-challenge-fast-food-giants-over-portion-sizes-including-mcdonalds-wendys/'}, {'Title': 'Course Hero Is Graduating—Just In Time', 'Source': 'Forbes', 'URL': 'https://www.forbes.com/sites/emmylucas/2023/08/30/course-hero-is-graduating-just-in-time/'}]
            send_news(dummy_data)
            break
        except:
            attempts += 1
            print("Email sending failed, set debug via 's.set_debuglevel(1)'")
            print('REMINDER: Export secrets locally')