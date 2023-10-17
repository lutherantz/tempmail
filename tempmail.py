import time
from requests import Session

class Tempmail:
    def __init__(self) -> None:
        self.sess = Session()
        self.useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"

        self.sess.headers = {
                "user-agent": self.useragent
        }

    def createMail(self):
        res = self.sess.post("https://api.internal.temp-mail.io/api/v3/email/new")
        email = res.json()["email"]
        token = res.json()["token"]
        return email, token

    def getMail(self, email: str):
        res = self.sess.get(f"https://api.internal.temp-mail.io/api/v3/email/{email}/messages")

        return res.json()
    
if __name__ == "__main__":
    temp = Tempmail()
    email = temp.createMail()[0]
    print(f"Email: {email}")

    while True:
        try:
            re_json = temp.getMail(email)
            for email_data in re_json:
                print("-"*20)
                print(f"Author: {email_data['from']}")
                print(f"To: {email_data['to']}")
                print(f"Object: {email_data['subject']}")
                print(f"Content: {email_data['body_text']}")
                print("-"*20)
            time.sleep(2)
        except:
            continue