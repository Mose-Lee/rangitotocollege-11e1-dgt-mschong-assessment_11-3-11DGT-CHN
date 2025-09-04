import tkinter as tk

#name entering function
def enter_name():
    global user_name
    user_name = name_entry.get()
    if user_name == "":
        user_name = "Anonymous"
    name_frame.pack_forget()
    menu_frame.pack(expand=True)


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

brick_game = tk.Button(btn_frame, text="Brick Breaker", font=("Arial", 30),width=15, height=5, fg="white", bg ="red", command=start_brick)

click_game = tk.Button(btn_frame, text="Click Game", font=("Arial", 30),width=15, height=5, fg="white", bg ="green",command=start_click)

ranking = tk.Button(btn_frame, text="Ranking", font=("Arial", 30),width=15, height=5, fg="white", bg ="yellow",command=show_ranking)

maze_game.grid(row=0,column=0,padx=10, pady=10)
brick_game.grid(row=0,column=1,padx=10,pady=10)
click_game.grid(row=1,column=0,padx=10,pady=10)
ranking.grid(row=1, column=1, padx=10, pady=10)

for i in range(2):
    btn_frame.grid_columnconfigure(i, weight=1)
    btn_frame.grid_rowconfigure(i, weight=1)



win.mainloop()
  
