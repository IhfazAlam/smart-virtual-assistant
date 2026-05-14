from tkinter import *
from PIL import Image, ImageTk
import action
import spech_to_text

# ---------------- ASSISTANT ---------------- #
assistant = action.VirtualAssistant()

# ---------------- MAIN WINDOW ---------------- #
root = Tk()
root.title("AI Assistant")
root.geometry("420x600")   # ✅ fixed size
root.config(bg="#0f172a")
root.resizable(False, False)

# ---------------- TOP SECTION ---------------- #
top_frame = Frame(root, bg="#0f172a")
top_frame.pack()

header = Frame(top_frame, bg="#111827", height=45)
header.pack(fill=X)

Label(
    header,
    text="AI ASSISTANT",
    font=("Arial", 14, "bold"),
    fg="white",
    bg="#111827"
).pack(pady=8)

img = Image.open("image/assitant.png")
img = img.resize((70, 70))
Display_Image = ImageTk.PhotoImage(img)

Label(top_frame, image=Display_Image, bg="#0f172a").pack(pady=5)

# ---------------- CHAT SECTION ---------------- #
chat_frame = Frame(root, bg="#0f172a")
chat_frame.pack(expand=True, fill=BOTH, padx=5)

scrollbar = Scrollbar(chat_frame)
scrollbar.pack(side=RIGHT, fill=Y)

text = Text(
    chat_frame,
    font=("Consolas", 9),
    bg="#1e293b",
    fg="white",
    wrap=WORD,
    yscrollcommand=scrollbar.set,
    bd=0,
    padx=8,
    pady=8,
    insertbackground="white"
)

text.pack(expand=True, fill=BOTH)
scrollbar.config(command=text.yview)

# ---------------- INPUT SECTION ---------------- #
bottom_frame = Frame(root, bg="#0f172a")
bottom_frame.pack(pady=5)

entry1 = Entry(bottom_frame, font=("Arial", 11), width=28)
entry1.grid(row=0, column=0, padx=5, ipady=5)

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

    if not ask_val:
        return

    text.insert(END, "You 🎤 ➜ " + ask_val + "\n")

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
        font=("Arial", 9, "bold"),
        bg=color,
        fg="white",
        activebackground="#334155",
        activeforeground="white",
        bd=0,
        padx=10,
        pady=6,
        cursor="hand2"
    )

# ---------------- BUTTONS ---------------- #
btn_frame = Frame(bottom_frame, bg="#0f172a")
btn_frame.grid(row=1, column=0, pady=5)

btn_voice = create_btn(btn_frame, "🎤", ask, "#2563eb")
btn_voice.grid(row=0, column=0, padx=3)

btn_send = create_btn(btn_frame, "Send", User_send, "#16a34a")
btn_send.grid(row=0, column=1, padx=3)

btn_clear = create_btn(btn_frame, "Clear", delete_text, "#dc2626")
btn_clear.grid(row=0, column=2, padx=3)

# ---------------- ENTER KEY ---------------- #
root.bind("<Return>", lambda event: User_send())

# ---------------- RUN ---------------- #
root.mainloop()