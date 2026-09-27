import tkinter

#buttons
button_values = [
    ["AC","+/-" ,"%" ,"÷"],
    ["7","8" ,"9" ,"+"],
    ["6", "5" ,"4" ,"-"],
    ["3","2" ,"1" ,"×"],
    ["0","." ,"√" ,"="]
]
#top operators
top_symbols = ["AC", "+/-", "%"]
#right operators
right_symbols = ["÷", "+", "-", "×", "="]

row_count = len(button_values)
column_count = len(button_values[0])

#the colors used
background_color = "#1C1C1C"
buttons_color = "#505050"
numbers_color = "#D4D4D2"
modifiers_color = "#FF9500"
black_color = "black"
white_color = "white"

window = tkinter.Tk()
window.title("First Calculator")
window.resizable(False, False)

#create frame, where the calculator is inside the window
frame = tkinter.Frame(window)

#labels, where the numbers are displayted
label = tkinter.Label(frame, text="0", font=("Arial", 60), background=black_color, foreground=white_color ,anchor="e")

#label at row and column 0
label.grid(row=0, column=0, columnspan=column_count, sticky="we")

#buttons
for row in range(row_count):
    for column in range(column_count):
        value = button_values[row][column]
        button = tkinter.Button(frame, text=value, font=("Arial", 24), width=column_count-1, height=1, command=lambda value=value: button_clicked(value))
        #row + 1 to shift row down by one because label is at row 0
        button.grid(row=row+1, column=column)
        
frame.pack()

def button_clicked(value):
    pass


window.mainloop()

