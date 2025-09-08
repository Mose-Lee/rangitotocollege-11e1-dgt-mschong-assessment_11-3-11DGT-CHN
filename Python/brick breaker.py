import tkinter as tk

#contants
Width = 800
Height = 600
paddle_width= 100
paddle_height=10
ball_radius = 10
brick_width = 100
brick_height = 20
brick_rows = 5
brick_cols = 10
brick_gap = 10
brick_colours = ["red", "orange", "yellow", "green", "blue"]
bricks = []


#create the main game window for brick breaker
window = tk.Tk()
window.title("Brick Breaker")
canvas = tk.Canvas(window,width=Width, height=Height,bg="black")
canvas.pack()


#make paddle used to hit the ball
paddle_x= Width/2 - paddle_width/2
paddle_y = Width/2-paddle_width/2
paddle = canvas.create_rectangle(paddle_x, Height-paddle_height, paddle_y+paddle_width, Height, fill = "white")


#make ball that breaks the bricks
ball_x = Width/2
ball_y = Height-paddle_height-ball_radius
ball = canvas.create_oval(ball_x - ball_radius, 
                          ball_y - ball_radius, 
                          ball_x + ball_radius, 
                          ball_y + ball_radius, fill="white")

#create bricks
for row in range(brick_rows):
    for col in range(brick_cols):
        x = col * (brick_width + brick_gap)
        y = row * (brick_height + brick_gap)
        brick_colour = brick_colours[row]
        brick = canvas.create_rectangle(x, y, x + brick_width, y + brick_height, fill="white")




window.mainloop()
