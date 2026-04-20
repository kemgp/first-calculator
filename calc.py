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
color_button = "#505050"
color_number = "#D4D4D2"
color_modifier = "#FF9500"
color_black = "black"
color_white = "white"

window = tkinter.Tk()
window.title("First Calculator")
window.resizable(False, False)

#create frame, where the calculator is inside the window
frame = tkinter.Frame(window)

#labels, where the numbers are displayted
label = tkinter.Label(frame, text="0", font=("Arial", 60), background=color_black, foreground=color_white ,anchor="e", width=column_count)

#label at row and column 0
label.grid(row=0, column=0, columnspan=column_count, sticky="we")

#buttons
for row in range(row_count):
    for column in range(column_count):
        value = button_values[row][column]
        button = tkinter.Button(frame, text=value, font=("Arial", 24), width=column_count-1, height=1, command=lambda value=value: button_clicked(value))
        
        #give buttons different colors
        if value in top_symbols:
            button.config(foreground=color_modifier, background=color_button)
        elif value in right_symbols:
            button.config(foreground=color_black, background=color_modifier)
        else:
            button.config(foreground=color_black, background=color_number)
            
        #row + 1 to shift row down by one because label is at row 0
        button.grid(row=row+1, column=column)
        
frame.pack()

#operations
A = "0"
operator = None
B = None

def clear_all(): #clear the operations
    global A, B, operator
    A = "0"
    operator = None
    B = None

def button_clicked(value):
    #global because we need to access these values outside of function
    global right_symbols, top_symbols, label, A, B, operator
    
    if value in right_symbols:
        pass
    elif value in top_symbols:
        if value == "AC":
            clear_all() 
            label["text"] = A #back to zero
        elif value == "+/-":
            result = float(label["text"]) * -1 #convert to float and multiply by negative one
            label["text"] = str(result) #after multiplying convert back to string
            
        elif value =="%":
            pass
    else:
        if value == ".":
            if value not in label["text"]: #make sure only one decimal point can be used
                label["text"] += value 
        elif value in "0123456789":
            if label["text"] == "0": 
                label["text"] = value #replace initial zero
            else:
                label["text"] += value #leading zero replaced with value

#open in center
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width/2) - (window_width/2))
window_y = int((screen_height/2) - (window_height/2))

#formatting
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

window.mainloop()

