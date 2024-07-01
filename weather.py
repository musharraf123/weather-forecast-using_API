from tkinter import *
from tkinter import ttk

import requests

def data_get():
    city=city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city +"&appid=44eb86b9c08bf8fa31faa8ca993e19ac").json()
    weater_clim1.config(text=data["weather"][0]["main"])
    weater_dis2.config(text=data["weather"][0]["description"])
    weater_temp3.config(text=str(int(data["main"]["temp"]-273.15)))
    weater_press4.config(text=data["main"]["pressure"])



win = Tk()
win.title("weather app")
win.config(bg="royal blue")
win.geometry("550x550")

name = Label( win, text="weather application" ,font=("Time New Roman",35, "bold") )
name.place(x=50,y=50,height=50,width=450)


# combobox
city_name = StringVar()
list_name=["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
combox = ttk.Combobox(win, values=list_name , text="weather application" ,font=("Time New Roman",20, "bold"),textvariable= city_name )
combox.place(x=75,y=120,height=40,width=400)



# condition 1

weater_clim = Label( win, text="weather climate" ,font=("Time New Roman",10, "bold") , background="royal blue", )
weater_clim.place(x=120,y=250,height=30,width=120)
weater_clim1 = Label( win, text="" ,font=("Time New Roman",10, "bold") )
weater_clim1.place(x=280,y=250,height=30,width=125)

# condition 2
weater_dis = Label( win, text="weather discription" ,font=("Time New Roman",10, "bold") , background="royal blue")
weater_dis.place(x=127,y=300,height=30,width=125)
weater_dis2 = Label( win, text="" ,font=("Time New Roman",10, "bold"))
weater_dis2.place(x=280,y=300,height=30,width=125)

# condition 3
weater_temp = Label( win, text="weather temp." ,font=("Time New Roman",10, "bold") , background="royal blue")
weater_temp.place(x=126,y=350,height=30,width=100)
weater_temp3= Label( win, text="" ,font=("Time New Roman",10, "bold") )
weater_temp3.place(x=280,y=350,height=30,width=125)

# conditino 4
weater_press = Label( win, text="weather press." ,font=("Time New Roman",10, "bold") , background="royal blue")
weater_press.place(x=126,y=400,height=30,width=100)
weater_press4 = Label( win, text="" ,font=("Time New Roman",10, "bold") )
weater_press4.place(x=280,y=400,height=30,width=125)

# button
show_button = Button(win, text="show", font=("Time New Roman",20,"bold"), command=data_get)
show_button.place(x=200,y=180,height=25,width=150)





win.mainloop()