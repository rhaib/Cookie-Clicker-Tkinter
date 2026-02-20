import tkinter as tk
import tkinter.messagebox
cookies = 0
increment = 1
passiveincrement = 1

# Create a tutorial window

tutorial = tk.Tk()
tutorial.title("Tutorial")

# Welcome text for the tutorial
tutorialtext = tk.Label(tutorial, text="Welcome to Cookie Clicker! Click the button labelled 'Click' to earn cookies.", font=("Helvetica", 12))
tutorialtext.pack(pady=10)

# Explanation of the rebirth upgrade
tutorialtext2 = tk.Label(tutorial, text="A rebirth upgrade will double your cookies per click, however it will reset your cookies to 0, use it wisely.", font=("Helvetica", 12))
tutorialtext2.pack(pady=10)

# Explanation of the passive upgrade
tutorialtext3 = tk.Label(tutorial, text="A passive upgrade will double your passive cookie generation (cookies also generate when you aren't clicking), it costs 10 cookies, but it is a good investment.", font=("Helvetica", 12))
tutorialtext3.pack(pady=10)

# Wish the player good luck
tutorialtext4 = tk.Label(tutorial, text="Good luck!", font=("Helvetica", 12))
tutorialtext4.pack(pady=10)

# Create the game window
game = tk.Tk()
game.title("Cookie Clicker")

# Create a label for the cookie counter
label = tk.Label(game, text=f"Cookies: {cookies}", font=("Helvetica", 16))
label.pack(pady=10)

# Create a label for the increment counter
label2 = tk.Label(game, text=f"Cookies per click: {increment}", font=("Helvetica", 16))
label2.pack(pady=10)

# Create a label for the passive increment counter
label3 = tk.Label(game, text=f"Passive increment: {passiveincrement}", font=("Helvetica", 16))
label3.pack(pady=10)

# Define the passive clicking function (same as on button click)
def passive():
  global cookies
  global increment
  global passiveincrement
  cookies=cookies+passiveincrement
  label.config(text=f"Cookies: {cookies}")

# Define what happens when button 1 is clicked
def on_button_click():
  global cookies
  global increment
  cookies=cookies+increment
  label.config(text=f"Cookies: {cookies}")

# Define what happens when button 2 is clicked
def on_button2_click():
  global cookies
  global increment
  if cookies==0:
    tk.messagebox.showwarning(title="Not enough clicks", message="You do not have enough clicks.")
  else:
    cookies=0
    label.config(text=f"Cookies: {cookies}")
    increment=increment*2
    label2.config(text=f"Cookies per click: {increment}")
# Define what happens when button 3 is clicked
def on_button3_click():
  global cookies
  global passiveincrement
  if cookies<10:
    tk.messagebox.showwarning(title="Not enough clicks", message="You do not have enough clicks.")
  else:
    cookies=cookies-10
    label.config(text=f"Cookies: {cookies}")
    passiveincrement=passiveincrement*2
    label3.config(text=f"Passive increment: {passiveincrement}")

# Create the main click button
button = tk.Button(game, text="Click", command=on_button_click)
button.pack(pady=10)

# Create the rebirth upgrade button
button2 = tk.Button(game, text="Rebirth Upgrade: Click*2", command=on_button2_click)
button2.pack(pady=5)

# Create the passive upgrade button
button3 = tk.Button(game, text="Passive Upgrade: Passive*2", command=on_button3_click)
button3.pack(pady=5)

# Passively increase the click counter
def schedule():
  passive()  # Call the button click function
  game.after(1000, schedule)

# Run the schedule loop
schedule()

# Run the event loop
game.mainloop()