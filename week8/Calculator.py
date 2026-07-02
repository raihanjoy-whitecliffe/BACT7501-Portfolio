#importing tkinter library
import tkinter as cl
#tkinter basic interface
#defining function
output=""
def calculate():
    num3=int(num1_textbox.get())
    num4=int(num2_textbox.get())
    total=num3+num4
    output="Total="+ str(total)

    result_label.configure(text=output)
cal=cl.Tk()
cal.title("Calculator")
cal.geometry("600x800")
#entry box for numbers
cl.Label(cal, text="Enter First Number" ).pack()
num1_textbox=cl.Entry(cal)
num1_textbox.configure(bg="red",fg="white")
num1_textbox.pack()

cl.Label(cal, text="Enter Second Number" ).pack()
num2_textbox=cl.Entry(cal)
num2_textbox.configure(bg="red",fg="white")
num2_textbox.pack(pady=10)

#button
calc_button= cl.Button(cal, text="Calculate", command=calculate).pack()
#result
result_label = cl.Label(cal, text="Total", bg="red", fg="white",width=10, height=4)
result_label.pack(pady=10)

cal.mainloop()