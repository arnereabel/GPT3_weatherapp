import tkinter as tk
import PIL
import requests
from tkinter import font


# from tkinter import messagebox
def format_response(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']
        wind = weather['wind']['speed']
        windk = round(wind * 1.943844, 2)

        weather_answer = 'city: %s \n sky: %s \n temp: %s C°  \n wind: %s knots \n ' % (name, desc, temp, windk)
    except:
        weather_answer = 'problem occurred, please reenter the city name'

    return weather_answer


def Get_Weather(entry):
    weather_key = '61072258eb82dac529fa83c9cf695f40'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': entry, 'units': 'metric', }
    response = requests.get(url, params=params)
    weather = response.json()

    Label['text'] = format_response(weather)

    # print(weather['name'])
    # print(weather['weather'][0]['description'])
    # print(weather['main']['temp'])
    # print(weather['wind']['speed'])
    # print(weather['description'])

    # print(response.json())


# api.openweathermap.org/data/2.5/forecast?q={city name},{state code},{country code}&appid={API key}
# Default 61072258eb82dac529fa83c9cf695f40
# arne 3803b68e81e2c42e897ee17476742c1b


rootscreen = tk.Tk()
# rootscreen.geometry('500x300')

Width = 100
Height = 9
Textcolor = '#857a2c'
Buttoncolor = '#ea8933'
BackgroundC = '#469d8b'
# BGframe2 = '#66ba90'
BGentry = '#e8ae3C'
Labelcolor = '#73bad3'

background_image = tk.PhotoImage(file='C:/Users/arner/PycharmProjects/weatherapp2/landscape.png')
background_label = tk.Label(rootscreen, image=background_image)
background_label.pack()

canvas = tk.Canvas(rootscreen, height=Height, width=Width)
canvas.pack()

frame = tk.Frame(rootscreen, bg=BackgroundC, bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, bg=BGentry, font=('calibri', 40, 'bold'))
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text='Get _weather', fg=Textcolor, bg=Buttoncolor, font=('calibri', 20, 'bold'),
                   command=lambda: Get_Weather(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)

frame2 = tk.Frame(rootscreen, bg=BackgroundC, bd=10)
frame2.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

Label = tk.Label(frame2, text='fill in city name and click the Get_weather button', fg=Textcolor, bg=Labelcolor,
                 font=('calibri', 30, 'bold'))
Label.place(relwidth=1, relheight=1, )

# def hello():
#     messagebox.showinfo('HI', 'how are you')

#print(tk.font.families())

# for r in range(3):
#     for c in range(5):
#         tk.Button(frame, text= 'R%s/C%s'%(r,c),borderwidth= 25).grid(row=r, column=c)


rootscreen.mainloop()
