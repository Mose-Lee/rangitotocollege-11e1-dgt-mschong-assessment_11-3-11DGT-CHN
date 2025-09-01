import tkinter as tk

#name entering function
def enter_name():
    global user_name
    user_name = entry.get()
    if user_name == "":
        user_name = "Anonymous"
    name_frame.pack_forget()
    menu_frame.pack(expand=True)

#the screen
win = tk.Tk()
win.title("Retro Fun Games")
win.geometry("1000x1000")
win.configure(bg="black")

#name frame
name_frame = tk.Frame(win, bg="black")

#label
label = tk.Label(name_frame, text="Enter your name:", fg="white", bg="black", font=("Arial", 40))
label.pack(pady =40)

#entry
entry = tk.Entry(name_frame, width=30,font=("Arial", 14))
entry.pack(pady = 20)

#button
submit_button = tk.Button(name_frame, text="Submit", command=enter_name)
submit_button.pack(pady = 20)

name_frame.pack(expand=True)


#menu frame
menu_frame = tk.Frame(win, bg="black")
#label
menu_title = tk.Label(menu_frame, text="Retro Fun Games", font=("Arial", 30), fg="white", bg="white")
menu_title.grid(row = 0, column = 0)


#start buttons
btn_frame = tk.Frame(menu_title)
maze_game = tk.Button(btn_frame, text="Maze Game", font=("Arial", 30), fg="white", bg ="blue")
maze_game.grid(row = 1, column = 0 , sticky="nsew" , padx=10, pady=10)

brick_game = tk.Button(btn_frame, text="Brick Breaker", font=("Arial", 30), fg="white", bg ="red")
brick_game.grid(row = 0, column = 0, sticky="nsew", padx=10, pady=10)

click_game = tk.Button(btn_frame, text="Click Game", font=("Arial", 30), fg="white", bg ="green")
click_game.grid(row = 0, column = 1, sticky="nsew", padx=10, pady=10)

ranking = tk.Button(btn_frame, text="Ranking", font=("Arial", 30), fg="white", bg ="yellow")
ranking.grid(row = 1, column = 1, sticky="nsew", padx=10, pady=10)


for i in range(2):
    btn_frame.grid_rowconfigure(i, weight=1)
    btn_frame.grid_columnconfigure(i, weight=1)

btn_frame.grid(row = 2, column = 0, sticky="nsew")
menu_frame.pack(expand=True)

win.mainloop()
  

