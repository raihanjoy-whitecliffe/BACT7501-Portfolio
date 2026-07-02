#importing tkinter library
import tkinter as tp
#tkinter basic interface
#defining function
cv=""
fv=""
def convert():
    fahrenheit=float(tem_field.get())* 9/5 + 32
    cv="Fahrenheit="+ str(fahrenheit)+"°F"
    result_label.configure(text=cv)
def fahrenheit_to_celsius(fahrenheit):
    celsius=(fahrenheit-32)*5/9
    fv= "Celsius="+ str(celsius)+"°C"
    result_label.configure(text=fv)
def clear():
    tem_field.delete(0, "end")
#main UI
tem=tp.Tk()
tem.title("Temperature Converter")
tem.geometry("600x800")
#input box for temperature
tp.Label(tem,text="Please Enter Temperature(Celsius)").pack()
tem_field=tp.Entry(tem)
tem_field.configure(bg="lime", fg="black", font=("Arial", 18))
tem_field.pack()
#convert to Fahrenheit
temp1_button=tp.Button(tem, text="Convert to Fahrenheit",command=convert)
temp1_button.pack()
#convert to Celsius
temp2_button=tp.Button(tem, text="Convert to Celsius",command=fahrenheit_to_celsius)
temp2_button.pack()
#clear all
clear=tp.Button(tem, text="Clear", command=clear)
clear.pack()
result_label= tp.Label(tem, text="Result", bg="lime", fg="black", font=("Arial", 20), width=20, height=10)
result_label.pack()
tem.mainloop()
result_label.pack()

tem.mainloop()