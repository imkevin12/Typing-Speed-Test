words = ['resource', 'meeting', 'growth', 'wonder', 'trade', 'lawyer', 'crime', 'dark', 'claim', 'kevin', 'industry',
         'practice', 'describe', 'patient', 'certain', 'attention', 'cause', 'evidence', 'culture', 'congress',
         'material', 'author', 'foreign', 'agency', 'reduce', 'common', 'article', 'stock', 'beyond', 'exactly',
         'against', 'company', 'government', 'million', 'different', 'though', 'business', 'since', 'however',
         'community', 'perhaps', 'field', 'former', 'themselves', 'leader', 'decision', 'military', 'federal',
         'receive', 'season', 'president', 'several', 'whether', 'parent', 'research', 'education', 'although',
         'probably', 'interest', 'experience']


def labelSlider():
    global count, sliderWords
    text = 'Welcome to TYPING SPEED TEST'
    if (count >= len(text)):
        count = 0
        sliderWords = ''
    sliderWords += text[count]
    count += 1
    title.configure(text=sliderWords)
    title.after(200, labelSlider)


def time():
    global timeleft, score, miss
    if (timeleft > 0):
        timeleft -= 1
        time_count.configure(text=timeleft)
        time_count.after(1000, time)
    else:
        score_count.configure(text=(score - miss))
        dashboard.configure(text='Hit = {} | Miss = {} | Total Score (Hit - Miss) = {}'.format(score, miss, (score-miss)))
        ask = messagebox.askretrycancel('Replay', 'Wanna play again?')
        if ask > 0:
            score = 0
            timeleft = 60
            miss = 0
            time_count.configure(text=timeleft)
            words_label.configure(text=words[0])


def startGame(event):
    global score, miss
    if (timeleft == 60):
        time()
    dashboard.configure(text='')

    if (words_entry.get() == words_label['text']):
        score += 1
    else:
        miss += 1

    random.shuffle(words)
    words_label.configure(text=words[0])
    words_entry.delete(0, END)
    score_count.configure(text=score)

from tkinter import *
import random
from tkinter import messagebox

root = Tk()
root.geometry('522x200+400+100')
root.title('Typing Speed Test')
root.iconbitmap('tst.ico')
root.resizable(0, 0)

# *************** Variables *************** #
score = 0
timeleft = 60
count = 0
sliderWords = ''
miss = 0

# *************** Label *************** #
title = Label(root, text='', font=('open sans', 16, 'bold'), width=39, bg='#D98880')
title.place(x=5, y=5)
labelSlider()

score_lable = Label(root, text='Your Score', font=('verdana', 15, 'bold'), bg='#2980B9', fg='white')
score_lable.place(x=10, y=45)
score_count = Label(root, text=score, font=('verdana', 12, 'bold'), fg='#1D8348')
score_count.place(x=60, y=80)

timer_label = Label(root, text='Time Left', font=('verdana', 15, 'bold'), bg='#2980B9', fg='white')
timer_label.place(x=400, y=45)
time_count = Label(root, text=timeleft, font=('verdana', 12, 'bold'), fg='red')
time_count.place(x=445, y=80)

random.shuffle(words)
words_label = Label(root, text=words[0], font=('sans serif', 18, 'bold'), width=20, bg='#A3E4D7')
words_label.place(x=105, y=100)

dashboard = Label(root, text='Type above word and hit enter button !', font=('verdana', 10, 'italic'))
dashboard.place(x=115, y=172)

# *************** Entry *************** #
words_entry = Entry(root, font=('calibri', 16), relief=FLAT, justify='center', width=35, bg='#ABEBC6')
words_entry.place(x=60, y=140)
words_entry.focus_set()

root.bind('<Return>', startGame)
root.mainloop()
