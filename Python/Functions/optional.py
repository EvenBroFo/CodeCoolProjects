def send_email(subject, body, to, cc = None):
    if cc is not None:
        print(f"Sending email to {to} with cc: {cc}")
    else:
        print(f"Sending email to {to} without CC")

#send_email("Meetiing  rmeinder", "dont forget about the meeting", "john@company.com", "boss@company.com")
