import python_weather
import asyncio

async def main(location):

    async with python_weather.Client(unit=python_weather.IMPERIAL) as client:


        weather = await client.get(location)

        return f"{weather.temperature} degrees in {location}"

import tkinter

window = tkinter.Tk()
window.title("Weather app")
window.geometry("600x500")
window.configure(bg="#333333")

frame = tkinter.Frame(window, bg="#333333")

def getWeather():
    
    weather_entry.delete("0","end")
    yourWeather = asyncio.run(main(location_entry.get()))
    weather_entry.insert(0, yourWeather)

def getWeatherOnEnter(e):
    getWeather()
    

app_label = tkinter.Label(frame, text="Weather Application",font=("Arial",30),fg="lightgreen", bg="#333333")

location_label = tkinter.Label(frame, text="Enter Location",font=("Arial",16), bg="#333333",fg="white")
location_entry = tkinter.Entry(frame, font=("Arial",16), bg="#D3C5C2",width=25)
weather_label = tkinter.Label(frame, text="Temperature Output",font=("Arial",16), bg="#333333",fg="white")
weather_entry = tkinter.Entry(frame, font=("Arial",16), bg="#D3C5C2",width=25)
submit_button = tkinter.Button(frame, text="Submit",font=("Arial",16),fg="lightgreen", bg="#333333",command=getWeather)


app_label.grid(row=0,column=0,columnspan=2,pady=50)
location_label.grid(row=1,column=0,padx=20)
location_entry.grid(row=1,column=1)
weather_label.grid(row=2,column=0,pady=25,padx=20)
weather_entry.grid(row=2,column=1)
submit_button.grid(row=3,column=0,columnspan=2)

frame.pack()


window.bind("<Return>",getWeatherOnEnter)


window.mainloop()

"""make an async main function"""

"await the client | python_weather.Client(unit = python_weather.IMPERIAL)"

"""Full forecast > client.get(str -> location)"""

'run async function > asyncio.run(function)'

"Add a keybind so <enter> does the main function"




