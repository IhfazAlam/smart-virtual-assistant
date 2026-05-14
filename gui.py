from tkinter import *
from PIL import Image, ImageTk
import action
import spech_to_text

# ---------------- ASSISTANT OBJECT ---------------- #
assistant = action.VirtualAssistant()


# ---------------- MAIN WINDOW ---------------- #
root = Tk()
root.title("AI Assistant")
root.geometry("650x750")
root.config(bg="#0f172a")
root.resizable(False, False)


# ---------------- HEADER ---------------- #
header = Frame(root, bg="#111827", height=80)
header.pack(fill=X)

title = Label(
    header, text="AI ASSISTANT", font=("Arial", 20, "bold"), fg="white", bg="#111827"
)
title.pack(pady=20)


# ---------------- IMAGE ---------------- #
img = Image.open("image/assitant.png")
img = img.resize((140, 140))

Display_Image = ImageTk.PhotoImage(img)

img_label = Label(root, image=Display_Image, bg="#0f172a")
img_label.pack(pady=10)


# ---------------- CHAT FRAME ---------------- #
chat_frame = Frame(root, bg="#0f172a")
chat_frame.pack(pady=10)

scrollbar = Scrollbar(chat_frame)
scrollbar.pack(side=RIGHT, fill=Y)

text = Text(
    chat_frame,
    height=18,
    width=65,
    font=("Consolas", 11),
    bg="#1e293b",
    fg="white",
    wrap=WORD,
    yscrollcommand=scrollbar.set,
    bd=0,
    padx=15,
    pady=15,
    insertbackground="white",
)

text.pack()

scrollbar.config(command=text.yview)


# ---------------- INPUT FRAME ---------------- #
input_frame = Frame(root, bg="#0f172a")
input_frame.pack(pady=20)


entry1 = Entry(input_frame, font=("Arial", 13), width=38, bd=0, relief=FLAT)

entry1.grid(row=0, column=0, ipady=10, padx=10)


# ---------------- FUNCTIONS ---------------- #
def User_send():

    send = entry1.get()

    if send.strip() == "":
        return

    text.insert(END, "You ➜ " + send + "\n")

    bot = assistant.Action(send)

    text.insert(END, "Bot ➜ " + str(bot) + "\n\n")

    text.see(END)

    entry1.delete(0, END)

    if bot == "Okay sir":
        root.destroy()


def ask():

    text.insert(END, "Listening...\n")
    text.see(END)

    root.update()

    ask_val = spech_to_text.spech_to_text()

    if ask_val is None:
        return

    text.insert(END, "You (Voice) ➜ " + ask_val + "\n")

    bot_val = assistant.Action(ask_val)

    text.insert(END, "Bot ➜ " + str(bot_val) + "\n\n")

    text.see(END)

    if bot_val == "Okay sir":
        root.destroy()

def delete_text():

    text.delete("1.0", END)
# ---------------- BUTTON STYLE ---------------- #
def create_btn(master, text, command, color):

    return Button(
        master,
        text=text,
        command=command,
        font=("Arial", 10, "bold"),
        bg=color,
        fg="white",
        activebackground="#334155",
        activeforeground="white",
        bd=0,
        padx=18,
        pady=12,
        cursor="hand2",
    )


# ---------------- BUTTON FRAME ---------------- #
btn_frame = Frame(root, bg="#0f172a")
btn_frame.pack()


btn_voice = create_btn(btn_frame, "🎤 Speak", ask, "#2563eb")

btn_voice.grid(row=0, column=0, padx=10)


btn_send = create_btn(btn_frame, "📩 Send", User_send, "#16a34a")

btn_send.grid(row=0, column=1, padx=10)


btn_clear = create_btn(btn_frame, "🗑 Clear", delete_text, "#dc2626")

btn_clear.grid(row=0, column=2, padx=10)


# ---------------- ENTER KEY SUPPORT ---------------- #
root.bind("<Return>", lambda event: User_send())


# ---------------- RUN ---------------- #
root.mainloop()
