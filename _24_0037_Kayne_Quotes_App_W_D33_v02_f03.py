
import requests
from tkinter import *

data = ""

def get_quote():
    global data
    response = requests.get(url="https://api.kanye.rest")
    # print("If None below, then there are no issues:")
    # print(response.raise_for_status())
    response.raise_for_status()
    data = response.json()["quote"]
    # tuple_quote = (data)
    print(f"The Kanye quote is: {data}")

    canvas.itemconfig(quote_text, text=data)  #to place data quote on our Canvas, as the updated text


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text=data, width=250, font=("Arial", 30, "bold"), fill="black")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)


window.mainloop()