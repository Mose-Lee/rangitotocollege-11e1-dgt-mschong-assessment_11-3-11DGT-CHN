import tkinter as tk

#name entering function
def enter_name():
    user_name = entry.get()
    if user_name == "":
        user_name = "Anonymous"
    name_frame.pack_forget()
    menu()

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

name_frame.pack()

def menu():
    #menu frame
    menu_frame = tk.Frame(win, bg="white")
    menu_title.grid(row = 0, column = 0, columnspan = 2, pady = 20)
    #label
    menu_title = tk.Label(menu_frame, text="Retro Fun Games", font=("Arial", 30), fg="white", bg="white")
    menu_title.grid(row = 0, column = 0, columnspan = 2, pady = 20)

    #start buttons
    maze_game = tk.Button(menu_title, text="Maze Game", font=("Arial", 30), fg="white", bg ="blue")
    maze_game.grid(row = 1, column = 0, padx=0,pady = 20)

    brick_game = tk.Button(menu_title, text="Brick Breaker", font=("Arial", 30), fg="white", bg ="red")
    brick_game.grid(row = 1, column = 0, padx=0,pady = 20)


    click_game = tk.Button(menu_title, text="Click Game", font=("Arial", 30), fg="white", bg ="green")
    click_game.grid(row = 1, column = 0, padx=0, pady = 20)


    ranking = tk.Button(menu_title, text="Ranking", font=("Arial", 30), fg="white", bg ="yellow")
    ranking.grid(row = 1, column = 0, padx=0, pady = 20)

    menu_frame.pack()

win.mainloop()
  

