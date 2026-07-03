#importing tkinter library
import tkinter as tp
#tkinter basic interface
#defining function
cv=""
def convert():
    fahrenheit=float(tem_field.get())* 9/5 + 32
    cv="Fahrenheit="+ str(fahrenheit)+"°F"
    result_label.configure(text=cv)
#main UI
tem=tp.Tk()
tem.title("Temperature Converter")
tem.geometry("600x800")
#input box for temperature
tp.Label(tem,text="Please Enter Temperature(Celsius)").pack()
tem_field=tp.Entry(tem)
tem_field.configure(bg="lime", fg="black", font=("Arial", 18))
tem_field.pack()

temp_button=tp.Button(tem, text="Convert",command=convert)
temp_button.pack()

result_label= tp.Label(tem, text="Result", bg="lime", fg="black", font=("Arial", 20), width=20, height=10)
result_label.pack()
tem.mainloop()
result_label.pack()

tem.mainloop()