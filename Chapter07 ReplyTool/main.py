from openai import OpenAI
import win32com.client
import tkinter as tk
import config

client = OpenAI(
  api_key=config.API_KEY,
)

def last_10_emails():
    outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
    inbox = outlook.GetDefaultFolder(6)
    messages = inbox.Items
    emails = [messages.GetLast().Subject]
    email_number = 10
    for i in range(email_number):
        emails.append(messages.GetPrevious().Subject)
    return emails


root = tk.Tk()
root.title("Outlook Emails")
root.geometry("300x300")

email_subjects = last_10_emails()
selected_subject = tk.StringVar()

dropdown = tk.OptionMenu(root, selected_subject, *email_subjects)
dropdown.pack()

label = tk.Label(root, text="")
label.pack()

def reply():
    email = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI").\
        GetDefaultFolder(6).Items.Item(selected_subject.get())
    response = client.chat.completions.create(
        model="gpt-4",
        max_tokens=1024,
        n=1,
        messages=[
            {"role": "user", "content": "You are a professional email writer"},
            {"role": "assistant", "content": "Ok"},
            {"role": "user", "content": f"Create a reply to this email:\n {email.Body}"}
        ]
    )

    reply = email.Reply()
    reply.Body = response.choices[0].message.content

    reply.Display()
    return


button = tk.Button(root, text="Generate Reply",
                   command=reply)
button.pack()

root.mainloop()

