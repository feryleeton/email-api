import uvicorn

from fastapi import FastAPI
from schemas import GetEmail, SendEmail, Proxy

from mailer import Mailer
from database.mysql import Database

app = FastAPI()
mailer = Mailer()
db = Database()


@app.post("/send_email/")
def read_root(email: SendEmail):
    mailer.send_email(email.sender, email.recipient, email.subject, email.body, email.login, email.password)
    return {"email": email}


@app.get("/get_email_text_by_filter/")
def read_root(email: GetEmail):
    response = {
        'result': [],
        'status': 0
    }

    search_result = mailer.get_emails(email.filter_from, email.filter_to, email.login, email.password)

    if not search_result:
        # if nothing found
        return response
    else:
        response['status'] = 1

    for mail in search_result:
        response['result'].append(
            {
                'received': mail.date_str,
                'from': mail.from_,
                'subject': mail.subject,
                'body': mail.text
            }
        )
    return {"result": response}


@app.get("/get_random_proxy/")
def get_random_proxy(proxy: Proxy):
    if proxy.ip:
        proxy = db.get_proxy_by_ip(proxy.ip)
        if not proxy:
            proxy = db.get_random_proxy()
    else:
        proxy = db.get_random_proxy()

    return {"proxy: ": proxy}


if __name__ == '__main__':
    uvicorn.run("main:app", port=8000, host="0.0.0.0", reload=True)
