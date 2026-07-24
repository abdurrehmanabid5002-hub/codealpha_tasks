'''
with open("Task3(Task Automation with Python Scripts)/Extract email addresses/contacts.txt", "w") as file:
    for i in range(1, 1001):
        file.write(f"User {i}\n")
        file.write(f"Email: user{i}@example.com\n")
        file.write(f"Phone: 0300{i:07d}\n")
        file.write("Address: Pakistan\n")
        file.write("--------------------------------\n")

'''
import re
with open("Task3(Task Automation with Python Scripts)/Extract email addresses/contacts.txt", "r") as f :
    text =f.read()

emails=re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",text)

with open("Task3(Task Automation with Python Scripts)/Extract email addresses/emails.txt","w") as f :
    for email in emails:
        f.write(email +"\n")
print (f"{len(emails)} Emails Extracted Successfully ")