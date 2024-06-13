weather = input("What the wheather , Sunny , Rainy and Snow: ")


# if (weather == 'Sunny'):
#     print("Go for a walk")
# elif (weather == 'Rainy'):
#     print("Read a book")
# elif (weather == 'Snow'):
#     print("Build a snow man")

# or 


if (weather == 'Sunny'):
    activity = "Go for Walk"
elif (weather == 'Rainy'):
    activity = "Read a Book"
elif (weather == 'Snow'):
    activity = "Build a snow"

print("Activity:",activity)


# import tkinter as tk
# from tkinter import ttk

# def check_weather():
#     weather = weather_var.get()
#     if weather == 'Sunny':
#         result_label.config(text="Go for a walk")
#     elif weather == 'Rainy':
#         result_label.config(text="Read a book")
#     elif weather == 'Snow':
#         result_label.config(text="Build a snow man")

# # Create the main window
# root = tk.Tk()
# root.title("Weather Activity Suggestion")

# # Create a StringVar to hold the selected weather option
# weather_var = tk.StringVar()

# # Create a label for the dropdown
# label = tk.Label(root, text="Select the weather:")
# label.pack()

# # Create the dropdown (combobox)
# weather_combobox = ttk.Combobox(root, textvariable=weather_var)
# weather_combobox['values'] = ('Sunny', 'Rainy', 'Snow')
# weather_combobox.pack()

# # Create a button to check the weather
# check_button = tk.Button(root, text="Check", command=check_weather)
# check_button.pack()

# # Create a label to display the result
# result_label = tk.Label(root, text="")
# result_label.pack()

# # Run the main event loop
# root.mainloop()
