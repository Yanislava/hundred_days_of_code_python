from tkinter import *
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
reps = 0
timer = None
marks = ''

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global marks, reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')
    label_timer.config(fg=GREEN, text='Timer')
    marks = ''
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1
    print(reps)
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        label_timer.config(fg=RED, text='Break')
    elif reps % 2 == 0:
        count_down(short_break_sec)
        label_timer.config(fg=PINK, text='Break')
    else:
        count_down(work_sec)
        label_timer.config(fg=GREEN, text='Work')

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer, marks
    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = f'0{seconds}'


    canvas.itemconfig(timer_text, text=f'{minutes}:{seconds}')
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        work_sessions = math.floor(reps/2)
        for i in range(work_sessions):
            marks += '✔'
        label_checkbox.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)



canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)


label_timer = Label(text='Timer', background=YELLOW, fg=GREEN, font=(FONT_NAME, 50))
label_timer.grid(column=1, row=0)

label_checkbox = Label(background=YELLOW, fg=GREEN, font=(FONT_NAME, 20, 'bold'))
label_checkbox.grid(column=1, row=3)

button_start = Button(text='Start', highlightbackground=YELLOW, command=start_timer)
button_start.grid(column=0, row=2)

button_reset = Button(text='Reset', highlightbackground=YELLOW, command=reset_timer)
button_reset.grid(column=2, row=2)

window.mainloop()
