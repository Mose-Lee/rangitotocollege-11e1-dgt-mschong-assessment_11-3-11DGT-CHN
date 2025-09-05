import tkinter as tk

#name entering function
def enter_name():
    global user_name
    user_name = name_entry.get()
    if user_name == "":
        user_name = "Anonymous"
    name_frame.pack_forget()
    menu_frame.pack(expand=True)


#--------------------description games function---------------------------
def desc_maze():
    desc_win = tk.Tk()
    desc_win.title("Maze Game Description")
    desc_win.geometry("700x600")
    desc_win.configure(bg="white")

    desc_title = tk.Label(desc_win, text="How to play Maze Game?", font=("Arial", 28, "bold"), bg="white")
    desc_title.pack(pady=20)

    desc_text = "Enjoy Maze Game!"

    desc_label = tk.Label(desc_win, text=desc_text, font=("Arial",12), fg="black", bg="black")
    desc_label.pack(pady=20,padx=30)

    close_button = tk.Button(desc_win, text="close", font=("Arial", 20), fg="white", bg="grey",command=desc_win.destroy)
    close_button.pack(pady=20)


def desc_brick():
    desc_win = tk.Tk()
    desc_win.title("Brick Breaker Description")
    desc_win.geometry("700x600")
    desc_win.configure(bg="white")

    desc_title = tk.Label(desc_win, text="How to play Brick Breaker?", font=("Arial", 28, "bold"), bg="white")
    desc_title.pack(pady=20)

    desc_text = "Enjoy Brick Breaker!"

    desc_label = tk.Label(desc_win, text=desc_text, font=("Arial",12), fg="black", bg="black")
    desc_label.pack(pady=20,padx=30)

    close_button = tk.Button(desc_win, text="close", font=("Arial", 20), fg="white", bg="grey",command=desc_win.destroy)
    close_button.pack(pady=20)

def desc_click():
    desc_win = tk.Tk()
    desc_win.title("Click Game Description")
    desc_win.geometry("700x600")
    desc_win.configure(bg="white")

    desc_title = tk.Label(desc_win, text="How to play Click Game?", font=("Arial", 28, "bold"), bg="white")
    desc_title.pack(pady=20)

    desc_text = "Enjoy Click Game!"

    desc_label = tk.Label(desc_win, text=desc_text, font=("Arial",12), fg="black", bg="black")
    desc_label.pack(pady=20,padx=30)

    close_button = tk.Button(desc_win, text="close", font=("Arial", 20), fg="white", bg="grey",command=desc_win.destroy)
    close_button.pack(pady=20)


def desc_ranking():
    desc_win = tk.Tk()
    desc_win.title("Show your ranking!")
    desc_win.geometry("700x600")
    desc_win.configure(bg="white")

    desc_title = tk.Label(desc_win, text="Do you want to see your score?", font=("Arial", 28, "bold"), bg="white")
    desc_title.pack(pady=20)

    desc_text = "Your Ranking!"

    desc_label = tk.Label(desc_win, text=desc_text, font=("Arial",12), fg="black", bg="black")
    desc_label.pack(pady=20,padx=30)

    close_button = tk.Button(desc_win, text="close", font=("Arial", 20), fg="white", bg="grey",command=desc_win.destroy)
    close_button.pack(pady=20)


#--------------------------------------game codes--------------------------------------------------
def start_brick():
    print("")
def start_maze():
    print("")
def start_click():
    print("")
def show_ranking():
    print("")






#----------------------------------make the main screen---------------------------------
win = tk.Tk()
win.title("Retro Fun Games")
win.geometry("1000x1000")
win.configure(bg="black")

#------------------------------name frame to get user's nickname---------------------------------
name_frame = tk.Frame(win, bg="black")

#label that showing the text
name_label = tk.Label(name_frame, text="Enter your name:", fg="white", bg="black", font=("Arial", 30))
name_label.pack(pady =10)

#entry to help user input something
name_entry = tk.Entry(name_frame, font=("Arial", 14))
name_entry.pack(pady = 10)

#button to submit their name
submit_button = tk.Button(name_frame, text="Submit",font= ("Arial,20"), command=enter_name)
submit_button.pack(pady = 10)

name_frame.pack(expand=True)


#----------------------------------------the main menu frame------------------------------------------------
menu_frame = tk.Frame(win, bg="black")

#label title on the menu screen
menu_title = tk.Label(menu_frame, text="Retro Fun Games", font=("Arial", 30), fg="white", bg="black")
menu_title.pack(pady=20)

#=======start buttons and button frame========
btn_frame = tk.Frame(menu_frame,bg="black")
btn_frame.pack()

maze_game = tk.Button(btn_frame, text="Maze Game", font=("Arial", 30), width=15, height=5, command=start_maze, fg="white", bg ="blue")
desc_maze_btn = tk.Button(btn_frame,text="How to play Maze Game?", font=("Arial",15), width=15,height=2,fg="white",bg="black",command=desc_maze)

brick_game = tk.Button(btn_frame, text="Brick Breaker", font=("Arial", 30),width=15, height=5, fg="white", bg ="red", command=start_brick)
desc_brick_btn = tk.Button(btn_frame,text="How to play Brick Breaker?", font=("Arial",15), width=15,height=2,fg="white",bg="black",command=desc_brick)


click_game = tk.Button(btn_frame, text="Click Game", font=("Arial", 30),width=15, height=5, fg="white", bg ="green",command=start_click)
desc_click_btn = tk.Button(btn_frame,text="How to play Click Game?", font=("Arial",15), width=15,height=2,fg="white",bg="black",command=desc_click)


ranking = tk.Button(btn_frame, text="Ranking", font=("Arial", 30),width=15, height=5, fg="white", bg ="yellow",command=show_ranking)
desc_rank_btn = tk.Button(btn_frame,text="How ranking system works?", font=("Arial",15), width=15,height=2,fg="white",bg="black",command=desc_ranking)

#grid-----
maze_game.grid(row=0,column=0,padx=10, pady=(10,5))
desc_maze_btn.grid(row=1,column=0,padx=10,pady=(0,10))

brick_game.grid(row=0,column=1,padx=10,pady=(10,5))
desc_brick_btn.grid(row=1,column=1,padx=10,pady= (0,10))

click_game.grid(row=2,column=0,padx=10,pady=(10,5))
desc_click_btn.grid(row=3,column=0,padx=10,pady= (0,10))


ranking.grid(row=2, column=1, padx=10, pady=(10,5))
desc_rank_btn.grid(row=3,column=1,padx=10,pady= (0,10))



for i in range(2):
    btn_frame.grid_columnconfigure(i, weight=1)
for i in range(4):
    btn_frame.grid_rowconfigure(i, weight=1)



win.mainloop()
  
