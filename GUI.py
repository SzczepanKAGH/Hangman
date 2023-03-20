import tkinter as tk
from tkinter import *

root = tk.Tk()
root.geometry("700x600")

###--------Ustawienie ikonki oraz tytułu okna aplikacji--------###
root.title( 'Wisielec' )
root.iconbitmap( r'C:\Users\HP\Desktop\wisielec\title_icon_bar.ico' )

#################################
###--------OKNO STARTU--------###
frame_start = tk.Frame(root, bg='#008B45' )
frame_start.pack(fill='both', expand=1)

canvas = tk.Canvas(frame_start, bg='#7CCD7C')
canvas.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)

#--Dodanie obrazka--#
image_handman = PhotoImage(file= r'C:\Users\HP\Desktop\wisielec\HandMan_image_without_backg.png')
canvas.create_image( 300, 250, image=image_handman, anchor='center' )

#--Zdefiniowanie komendy wykonywanej przez przycisk start--#
def move_level_window():
    #Klikniecie przycisku start spowoduje przejscie do okna wyboru poziomu --> frame_choose_level
    frame_choose_level.pack(fill='both', expand=1)
    frame_start.forget()

#--Przycisk Start--#
start_button = tk.Button(canvas, text="START", height=2, width=20, bg='#006400', fg='white',
                         font=('Helvetica', 10, 'bold'), command=move_level_window)
start_button.pack(side=BOTTOM, pady=80)
############################################################################################


#######################################
###--------OKNO WYBOR POZIOMU-------###
frame_choose_level = tk.Frame(root, bg='#7CCD7C')
label_level = tk.Label(frame_choose_level, bg='#008B45', height=2, text='WYBIERZ POZIOM TRUDNOSCI',
                       font=('Helvetica', 25, 'bold'))
label_level.pack(fill='x', pady='40')

#--Komenda przeniesienia do okna glownego z wyboru poziomu--#
def move_main_window():
    #Klikniecie jednego z trzech przyciskow spowoduje przejscie do glownego 'okna' --> frame_main
    frame_main.pack(fill='both', expand=1)
    frame_choose_level.forget()

#--Przyciski wyboru poziomu--#
easy_level_button = tk.Button(frame_choose_level, text="LATWY", height=2, width=30, bg='#006400', fg='white',
                         font=('Helvetica', 10, 'bold'), command=move_main_window)
easy_level_button.pack(side=TOP, pady=30)
medium_level_button = tk.Button(frame_choose_level, text="SREDNI", height=2, width=30, bg='#006400', fg='white',
                         font=('Helvetica', 10, 'bold'), command=move_main_window)
medium_level_button.pack(side=TOP, pady=30)
hard_level_button = tk.Button(frame_choose_level, text="TRUDNY", height=2, width=30, bg='#006400', fg='white',
                         font=('Helvetica', 10, 'bold'), command=move_main_window)
hard_level_button.pack(side=TOP, pady=30)
################################################################################################################


####################################
###--------OKNO GLOWNE GRA-------###
frame_main = tk.Frame(root, bg='#7CCD7C' )

#--Zaladowanie obrazkow wisielca-krok po kroku--#
Images = [PhotoImage(file=r'C:\Users\HP\Desktop\wisielec\w.1.png'), PhotoImage(file=r'C:\Users\HP\Desktop\wisielec\w.2.png'),
           PhotoImage(file=r'C:\Users\HP\Desktop\wisielec\w.3.png'), PhotoImage(file=r'C:\Users\HP\Desktop\wisielec\w.4.png'),
           PhotoImage(file=r'C:\Users\HP\Desktop\wisielec\w.5.png'), PhotoImage(file=r'C:\Users\HP\Desktop\wisielec\w.6.png'),
           PhotoImage(file=r'C:\Users\HP\Desktop\wisielec\w.7.png'), PhotoImage(file=r'C:\Users\HP\Desktop\wisielec\w.8.png'),
           PhotoImage(file=r'C:\Users\HP\Desktop\wisielec\w.9.png'), PhotoImage(file=r'C:\Users\HP\Desktop\wisielec\w.10.png'),
           PhotoImage(file=r'C:\Users\HP\Desktop\wisielec\w.11.png')]

#--Przyciski-litery do wyboru--##
label_letters_button = tk.Label(frame_main, bg='#006400')
label_letters_button.pack(side=BOTTOM, fill='x')
alphabet = ['A', 'Ą', 'B', 'C', 'Ć', 'D', 'E', 'Ę', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'Ł', 'M', 'N', 'Ń', 'O', 'Ó', 'P', 'R',
           'S', 'Ś', 'T', 'U', 'W', 'Y', 'Z', 'Ź', 'Ż']

#def guess_letter():

##--Umiejscowienie przyciskow-literek do wyboru--##
x=0
y=0
number_of_button=0
for letter in alphabet:
    Letter_Button = tk.Button(label_letters_button, text=letter, bg='green', width=11, font=("Times", "10", "bold"))
    Letter_Button.grid(row=y, column=x+1, ipady=5)
    x+=1
    if( x == 8 ):
        x=0
        y+=1

##--Miejsce na slowo do zgadniecia--##
label_word_guess = tk.Label(frame_main, bg='black')
label_word_guess.pack(side=BOTTOM, fill='x', ipady=50)

##--Miejsce na bledy wisielca oraz inne informacje dotyczace gry--##
label_game_info = tk.Label(frame_main, bg='white')
label_game_info.pack(ipadx=150, ipady=155, side=LEFT)
label_hangman_steps = tk.Label(frame_main, bg='orange')
label_hangman_steps.pack(ipadx=195, ipady=155, side=LEFT)








root.mainloop()
