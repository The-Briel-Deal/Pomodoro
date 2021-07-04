import tkinter
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REP = 0
NUM_CHECK = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global checks
    global NUM_CHECK
    global REP
    window.after_cancel(timer)
    label.config(text="TIMER", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 30, "bold"))
    checks.destroy()
    checks = tkinter.Canvas(width=203, height=50, bg=YELLOW, highlightthickness=0)
    canvas.itemconfig(timer_text, text=f"00:00")
    NUM_CHECK = 0
    REP = 0



# ---------------------------- TIMER MECHANISM ------------------------------- #


def check_marks():
    global NUM_CHECK
    checks.create_text(51+25*NUM_CHECK, 33, text="✓", fill=GREEN, font=(FONT_NAME, 20, "bold"))
    NUM_CHECK += 1


def start_timer():
    global REP
    global label
    if REP % 2 == 0:
        label.config(text="WORKING", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 30, "bold"))
        current_rep = WORK_MIN*60
    elif REP % 7 == 0:
        label.config(text="LONG BREAK", bg=YELLOW, fg=RED, font=(FONT_NAME, 30, "bold"))
        current_rep = LONG_BREAK_MIN * 60
    else:
        label.config(text="SHORT BREAK", bg=YELLOW, fg=PINK, font=(FONT_NAME, 30, "bold"))
        current_rep = SHORT_BREAK_MIN*60
    countdown(current_rep)
    REP += 1
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown(count):
    global timer
    count_min = math.floor(count/60)
    if count_min < 10:
        count_min = "0" + str(count_min)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = "0" + str(count_sec)
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, countdown, count - 1)
    else:
        if REP % 2 == 1:
            check_marks()
        start_timer()
# ---------------------------- UI SETUP ------------------------------- #


window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = tkinter.Canvas(width=203, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(101, 112, image=tomato_img)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))

label = tkinter.Label(text="TIMER", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 30, "bold"))

button1 = tkinter.Button(text="Start", command=start_timer)
button2 = tkinter.Button(text="Stop", command=reset_timer)

checks = tkinter.Canvas(width=203, height=50, bg=YELLOW, highlightthickness=0)


label.grid(row=0, column=1)
canvas.grid(row=1, column=1, pady=2, padx=2)
button1.grid(row=2, column=0)
button2.grid(row=2, column=2)
checks.grid(row=2, column=1)


tkinter.mainloop()
