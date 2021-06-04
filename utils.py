import yagmail

import json


def send_results(sender: str, sender_pass: str, receiver: str, results: dict):
    mail = yagmail.SMTP(user=sender, password=sender_pass)

    mail.send(
        to=receiver,
        subject="Content Aggregator",
        contents=json.dumps(results, indent=2)
    )
