from openai import OpenAI
import asyncio

import tkinter 


def getResponse(prompt):
    client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="ENTER YOUR API KEY HERE",
    )

    completion = client.chat.completions.create(
    model="deepseek/deepseek-r1:free",
    messages=[
        {
        "role": "user",
        "content": prompt
        }
    ]
    )
    return completion.choices[0].message.content

window = tkinter.Tk()
window.title("Chat Bot")
window.geometry("900x900")
window.configure(bg="#333333")

def submit():
    response_text.delete("1.0","end")
    chat = getResponse(prompt_entry.get())
    response_text.insert("1.0", chat)



frame = tkinter.Frame(bg="#333333")

chatBot_label = tkinter.Label(frame, text="chat app",bg="#333333",fg="#07BF38", font=("Arial", 30))
prompt_label = tkinter.Label(frame, text="Prompt",bg="#333333", fg="#FFFFFF", font=("Arial", 16))
prompt_entry = tkinter.Entry(frame,font=("Arial", 16))
response_label = tkinter.Label(frame, text="response",fg="#FFFFFF",bg="#333333", font=("Arial", 16))
response_text = tkinter.Text(frame,font=("Arial", 16),width=40)
submit_button = tkinter.Button(frame, text="Submit",bg="#07BF38",fg="#FFFFFF",font=("Arial", 16),command=submit)



chatBot_label.grid(row=0,column=0, columnspan=2, sticky="news",pady=40)
prompt_label.grid(row=1,column=0)
prompt_entry.grid(row=1,column=1,pady=20)
response_label.grid(row=2,column=0,sticky="nw")
response_text.grid(row=2,column=1,columnspan=2,rowspan=1)
submit_button.grid(row=3,column=0,columnspan=2, pady=30)


frame.pack()




window.mainloop()

