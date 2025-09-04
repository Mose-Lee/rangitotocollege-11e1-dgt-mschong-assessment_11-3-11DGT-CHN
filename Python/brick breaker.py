import tkinter as tk
Width = 800
Height = 600
paddle_width= 100
paddle_height=10
ball_radius = 10

#create the main game window for brick breaker
window = tk.Tk()
window.title("Brick Breaker")
canvas = tk.Canvas(window,width=Width, height=Height,bg="black")
canvas.pack()


#make paddle 
paddle_x= Width/2 - paddle_width/2
paddle_y = Width/2-paddle_width/2
paddle = canvas.create_rectangle(paddle_x, Height-paddle_height, paddle_y+paddle_width, Height, fill = "white")


#make ball 
ball_x = Width/2
ball_y = Height-paddle_height-ball_radius
ball = canvas.create_oval(ball_x - ball_radius, 
                          ball_y - ball_radius, 
                          ball_x + ball_radius, 
                          ball_y + ball_radius, fill="white")




window.mainloop()
