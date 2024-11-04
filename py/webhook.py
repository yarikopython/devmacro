from functions import webhook
while True:
    url = ""
    message = f"<@{}>"
    webhook(url=url, message=message)