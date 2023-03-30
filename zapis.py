import tkinter as tk
from tkinter import *
import random
from tkinter import messagebox
import json

root = tk.Tk()
root.geometry("700x600")

###--------Ustawienie ikonki oraz tytułu okna aplikacji--------###
root.title( 'Wisielec' )
root.iconbitmap( r'C:\wisielec\title_icon_bar.ico' )

#################################
###--------OKNO STARTU--------###
frame_start = tk.Frame(root, bg='#008B45' )
frame_start.pack(fill='both', expand=1)

canvas = tk.Canvas(frame_start, bg='#7CCD7C')
canvas.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)

#--Dodanie obrazka--#
image_handman = PhotoImage(file= r'C:\wisielec\HandMan_image_without_backg.png')
canvas.create_image( 300, 250, image=image_handman, anchor='center' )

#--Zdefiniowanie komendy wykonywanej przez przycisk start--#
def move_level_window():
    #Klikniecie przycisku start spowoduje przejscie do okna wyboru poziomu --> frame_choose_level
    frame_choose_level.pack(fill='both', expand=1)
    frame_start.forget()
''''''
#--Zdefiniowanie komendy wykonywanej przez przycisk wczytaj--#
def load_game_window():
    global number_guess; global word_with_spaces; global level; global score; global cat ; global round_number
    global round_from_start; global a; global b ; global last_score

#--Załadowanie danych
    with open('savefile.json', 'r') as file:
        data = json.load(file)
        score = data['score']
        best_score = data['best_score']
        word_with_spaces = data['word_with_spaces']
        number_guess = data['number_guess']
        level = data['level']
        round_number = data['round_number']
        round_from_start = data['round_from_start']
        a = data['a']
        b = data['b']

    frame_main.pack(fill='both', expand=1)



#--Przycisk Wczytaj--#
load_button = tk.Button(canvas, text="WCZYTAJ", height=2, width=20, bg='#006400', fg='white',
                         font=('Helvetica', 10, 'bold'), command=load_game_window)
load_button.pack(side=BOTTOM , pady=20)

#--Przycisk Start--#
start_button = tk.Button(canvas, text="START", height=2, width=20, bg='#006400', fg='white',
                         font=('Helvetica', 10, 'bold'), command=move_level_window)
start_button.pack(side=BOTTOM, pady=0)
############################################################################################


#######################################
###--------OKNO INSTRUCJI GRY-------###
frame_choose_level = tk.Frame(root, bg='#7CCD7C')
label_level = tk.Label(frame_choose_level, bg='#008B45', height=2, text='INSTRUKCJA',
                       font=('Helvetica', 20, 'bold'))
label_level.pack(fill='x', pady='20', side=TOP)
#-Instrukcja Gry-#
instruction="""Witaj w grze WISIELEC.\n\n Twoim zadaniem jest zdobyć jak najwięcej punktów.\n Czeka na ciebie łącznie
            15 rund podzielonych na 3 poziomy trudności ŁATWY, ŚREDNI oraz TRUDNY.\n W każdym możesz zdobyć odpowiednio
            5, 10 lub 15 punktów.\n Za każdym razem z boku ekranu zostanie wyświetlona kategoria hasła, aby ułatwić
            Ci odgadnięcie.\n Występujące kategorie to: zwierzęta, owoce i warzywa, słówko po angielsku, stolice, państwa.
            \n Po każdej próbie odgadnięcia hasła kliknij DALEJ, żeby przejść do kolejnej rundy.\n
            Jeżeli jesteś gotowy kliknij GRAJ, aby rozpocząć.\n\n Powodzenia :)"""

label_indroduction = tk.Label(frame_choose_level, bg='#66CD00', width=60, height=10, text=instruction,
                       font=('Helvetica', 10, 'bold'))
label_indroduction.pack( ipady='60', ipadx='70', side=TOP)
#--Komenda przeniesienia do okna glownego--#
def move_main_window():
    #Klikniecie jednego z trzech przyciskow spowoduje przejscie do glownego 'okna' --> frame_main
    frame_main.pack(fill='both', expand=1)
    frame_choose_level.forget()

#--Przyciski GRAJ--#
move_next_button = tk.Button(frame_choose_level, text="GRAJ", height=2, width=30, bg='#ADFF2F', fg='black',
                         font=('Helvetica', 10, 'bold'), command=move_main_window)
move_next_button.pack(side=BOTTOM, pady=30)
################################################################################################################

####################################
###--------OKNO GLOWNE GRA-------###
frame_main = tk.Frame(root, bg='#7CCD7C' )
frame_end = tk.Frame(root, bg='#7CCD7C' )

#--Zaladowanie obrazkow wisielca-krok po kroku--#
Images = [PhotoImage(file=r'C:\wisielec\w.1.png'), PhotoImage(file=r'C:\wisielec\w.2.png'),
           PhotoImage(file=r'C:\wisielec\w.3.png'), PhotoImage(file=r'C:\wisielec\w.4.png'),
           PhotoImage(file=r'C:\wisielec\w.5.png'), PhotoImage(file=r'C:\wisielec\w.6.png'),
           PhotoImage(file=r'C:\wisielec\w.7.png'), PhotoImage(file=r'C:\wisielec\w.8.png'),
           PhotoImage(file=r'C:\wisielec\w.9.png'), PhotoImage(file=r'C:\wisielec\w.10.png'),
           PhotoImage(file=r'C:\wisielec\w.11.png')]

#--wybranie losowego slowa z pliku tekstowego--#
global score ; global level ; global cat ; global lev_name ; global round_number ; global round_from_start
score = 0 ; level = 1 ; cat = '' ; round_number = 0 ; round_from_start = 0
lev_name = ''
score_show = StringVar()
category_show = StringVar()
round = StringVar()
level_show = StringVar()
hide_word=StringVar()

global last_score ; global best_score
last_score = 0 ; best_score = 0
Last_Score = StringVar()
Best_Score = StringVar()

global a ; global b   #zakres losowania slow: a i b dopasowujace sie do odpowiedniego poziomu i kategorii
a = 0 ; b = 4

def create_word():
    global number_guess ;global word_with_spaces ; global lev_name ;global level ;global score ;global cat
    global round_number; global round_from_start ; global a ; global b ; global last_score ; global best_score
    number_guess = 0
    round_from_start += 1
    if round_from_start == 16:
        frame_main.forget()
        frame_end.pack(fill='both', expand=1)
        if score >= best_score:
            best_score = score
            Best_Score.set(best_score)
    else:
        if level == 1:
            lev_name = 'ŁATWY'
        elif level == 2:
            lev_name = 'ŚREDNI'
        elif level == 3:
            lev_name = 'TRUDNY'
        level_show.set(lev_name)

        file_with_words = open(r'C:\wisielec\words_guess.txt', encoding="utf-8")
        words = file_with_words.readlines()
        words = [word.upper() for word in words]

        word_place = random.randint(a, b)
        a += 5 ; b += 5
        main_word = words[word_place].strip()
        word_with_spaces = " ".join(main_word)
        hide_word.set(" ".join("_"*len(main_word)))

        round_number += 1

        if round_number == 5:
            level += 1

        if round_number == 1:
            cat = 'ZWIERZĘTA'
        elif round_number == 2:
            cat = 'OWOCE I WARZYWA'
        elif round_number == 3:
            cat = 'ANGIELSKIE SŁÓWKO'
        elif round_number == 4:
            cat = 'STOLICE'
        elif round_number == 5:
            cat = 'PAŃSTWA'
        category_show.set(cat)
        if round_number == 5:
            round_number=0


def guess_letter( letter ):
    global number_guess ; global level ; global cat ; global lev_name ; global score ; global best_score
    txt = list( word_with_spaces )
    guessed = list( hide_word.get() )
    if word_with_spaces.count(letter) > 0:
        for c in range( len(txt) ):
            if txt[c]==letter:
                guessed[c]=letter
            hide_word.set("".join(guessed))
            if hide_word.get()==word_with_spaces:
                score_boost = ''
                if level == 1:
                    score_boost = '+5'
                elif level == 2:
                    score_boost = '+10'
                elif level == 3 or level == 4:
                    score_boost = '+15'
                messagebox.showinfo("Wisielec", "Gratulacje! Zdobywasz " + score_boost + " punktów" )
                if level == 1:
                    score += 5
                elif level == 2:
                    score += 10
                elif level == 3 or level == 4:
                    score += 15
                break
    else:
        number_guess+=1
        label_hangman_steps.config(image=Images[number_guess])
        if number_guess==10:
            messagebox.showinfo("Wisielec", "Niestety nie udało się.\nSłowo to:  " + word_with_spaces)

    score_show.set(score)


##--Fukcja przycisk DALEJ--#
def next_level():
    create_word()


#--Przyciski-litery do wyboru--##
label_letters_button = tk.Label(frame_main, bg='black')
label_letters_button.pack(side=BOTTOM, fill='x')
alphabet = ['A', 'Ą', 'B', 'C', 'Ć', 'D', 'E', 'Ę', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'Ł', 'M', 'N', 'Ń', 'O', 'Ó', 'P', 'R',
           'S', 'Ś', 'T', 'U', 'W', 'Y', 'Z', 'Ź', 'Ż']

#def guess_letter():

##--Umiejscowienie przyciskow-literek do wyboru--##
x=0
y=0
number_of_button=0
for letter in alphabet:
    Letter_Button = tk.Button(label_letters_button, text=letter, bg='#9ACD32', width=11, activebackground='green',
                              command=lambda letter=letter: guess_letter(letter), font=("Times", "10", "bold"))
    Letter_Button.grid(row=y, column=x+1, ipady=5)
    x+=1
    if( x == 8 ):
        x=0
        y+=1


##--Miejsce na slowo do zgadniecia--##

label_word_guess = tk.Label(frame_main, bg='#7CCD7C', textvariable=hide_word, fg='black',
                            font=("Helvetica", "20", "bold"))
label_word_guess.pack(side=BOTTOM, fill='x', ipady=50)

##--Miejsce na bledy wisielca oraz inne informacje dotyczace gry--##

label_game_SCORE = tk.Label(frame_main, bg='#7CCD7C')
label_game_SCORE.pack(ipadx=80, ipady=160, side=LEFT )

label_game_ANSWER = tk.Label(frame_main, bg='#7CCD7C')
label_game_ANSWER.pack(ipadx=80, side=LEFT, ipady=160)

label_game_score = tk.Label(label_game_SCORE, height=5, text='WYNIK: ', bg='#66CD00',
                            font=("Helvetica", "10", "bold"))
label_game_score.pack(side=TOP, fill='x')
label_game_level = tk.Label(label_game_SCORE, height=5, text='POZIOM: ', bg='#66CD00',
                            font=("Helvetica", "10", "bold"))
label_game_level.pack(side=TOP,fill='x')
label_game_category = tk.Label(label_game_SCORE, height=5, text='KATEGORIA: ', bg='#66CD00',
                               font=("Helvetica", "10", "bold"))
label_game_category.pack(side=TOP,fill='x')

label_game_1 = tk.Label(label_game_ANSWER, width=20, height=5, textvariable=score_show, bg='#76EE00',
                        font=("Helvetica", "10", "bold"))
label_game_1.place(anchor='nw')
label_game_2 = tk.Label(label_game_ANSWER,  width=20, height=5, textvariable=level_show, bg='#76EE00',
                        font=("Helvetica", "10", "bold"))
label_game_2.place(y=85)
label_game_3 = tk.Label(label_game_ANSWER, width=20, height=5, textvariable=category_show, bg='#76EE00',
                        font=("Helvetica", "10", "bold"))
label_game_3.place(y=170)

######################################################################################################

##--Funkcja zapisu--##
def save_game_window():
    msg_box = tk.messagebox.askquestion('Nadpisz Grę', 'Czy jesteś pewien, że chcesz nadpisać swój poprzedni zapis?',icon='warning')
    if msg_box == 'yes':
        with open('savefile.json', 'w') as file:
           json.dump({
                'score' : score,
                'best_score' : best_score,
                'word_with_spaces' : word_with_spaces,
                'number_guess' : number_guess,
                'level' : level,
                'round_number' : round_number,
                'round_from_start' : round_from_start,
                'cat' : cat,
                'a' : a,
                'b' : b},
                    file)
    else:
        pass

##--Przycisk zapisu--##
save_button = tk.Button(frame_main, text="ZAPISZ", height=3, width=19, bg='#006400', fg='white',
                         font=('Helvetica', 10, 'bold'), command=save_game_window)

#save_button.pack(fill='both', expand=True)
save_button.place(anchor=NW, rely=0.434,relx=0.367)

######################################################################################################


##--Przycisk graj dalej-kolejny poziom--#
button_next_level = tk.Button(label_game_SCORE, bg='#00CD00', text='DALEJ', font=("bold"),
                              command=lambda: next_level())
button_next_level.pack(fill='both', side=TOP, expand=True)

label_hangman_steps = tk.Label(frame_main, bg='#7CCD7C')
label_hangman_steps.pack(ipadx=195, ipady=155, side=RIGHT)

create_word()
##--Okno podsumowanie--##

#-Zgraj jeszcze raz definicja-#
def play_again():
    global number_guess; global word_with_spaces; global level; global score; global cat ; global round_number
    global round_from_start; global a; global b ; global last_score
    last_score = score
    Last_Score.set(last_score)
    score = 0; level = 1; cat = ''; round_number = 0; round_from_start = 0
    a = 0; b = 4
    score_show.set(score)
    frame_main.pack(fill='both', expand=1)
    frame_end.forget()
    create_word()
#-Przycisk zagraj jeszcze raz-#
play_again_button = tk.Button(frame_end, text="ZAGRAJ PONOWNIE", height=2, width=20, bg='#006400', fg='white',
                         font=('Helvetica', 10, 'bold'), command=play_again)
play_again_button.pack(side=BOTTOM, pady=20)

label_end_title = tk.Label(frame_end, bg='#008B45', height=2, text='PODSUMOWANIE',
                       font=('Helvetica', 20, 'bold'))
label_end_title.pack(fill='x', pady='20', side=TOP)
label_end_ = tk.Label(frame_end, bg='#66CD00', width=40, height=14)
label_end_.pack(ipady='20', side=TOP)

end_text="Jeżeli chcesz spróbować jeszcze raz kliknij\n przycisk ZAGRAJ PONOWNIE :)"
label_textin = tk.Label(frame_end, bg='#7CCD7C', width=40, height=1, text=end_text,
                        font=("Helvetica", "10", "bold"))
label_textin.pack(ipady='50', side=TOP)

label_end1 = tk.Label(label_end_, bg='#66CD00', height=15, width=20)
label_end1.place(anchor='nw')
label_end2 = tk.Label(label_end_, bg='#66CD00', height=15, width=20)
label_end2.place(x=140)

label0e1 = tk.Label(label_end1, width=20, height=5, text='AKTUALNY\nWYNIK:', bg='#66CD00',
                    font=('Helvetica', 10, 'bold'))
label0e1.place(anchor='nw')
label0e2 = tk.Label(label_end1,  width=20, height=5, text='POPRZEDNI\nWYNIK:', bg='#66CD00',
                    font=('Helvetica', 10, 'bold'))
label0e2.place(y=85)
label0e3 = tk.Label(label_end1, width=20, height=5, text='NAJLEPSZY\nWYNIK:', bg='#66CD00',
                    font=('Helvetica', 10, 'bold'))
label0e3.place(y=170)

label1e1 = tk.Label(label_end2, width=20, height=5, textvariable=score_show, bg='#66CD00')
label1e1.place(anchor='nw')
label1e2 = tk.Label(label_end2,  width=20, height=5, textvariable=Last_Score, bg='#66CD00')
label1e2.place(y=85)
label1e3 = tk.Label(label_end2, width=20, height=5, textvariable=Best_Score, bg='#66CD00')
label1e3.place(y=170)

root.mainloop()
