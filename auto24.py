import sqlite3
import tkinter as tk
# Import Module
from tkinter import *

is_on_switch_price = True
is_on_switch_year = True

def search_cars():
    brand = brand_entry.get().strip()
    model = model_entry.get().strip()
    year = year_entry.get().strip()
    price = price_entry.get().strip()

    if not (brand or model or year or price):
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Please fill in at least one search criteria.")
        return

    criteria = {}
    if brand:
        criteria['brand'] = brand
    if model:
        criteria['model'] = model
    if year:
        try:
            criteria['year'] = int(year)
        except ValueError:
            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, "Invalid input for year. Please enter a valid integer.")
            return
    if price:
        try:
            criteria['price'] = int(price)
        except ValueError:
            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, "Invalid input for price. Please enter a valid integer.")
            return
    conn = sqlite3.connect('auto_database.db')
    cursor = conn.cursor()

    query = "SELECT * FROM auto_table WHERE "
    conditions = []
    values = []
    for key, value in criteria.items():
        if key == 'price':
            conditions.append(f"{key} < ?")
        else:
            conditions.append(f"{key} = ?")
        values.append(value)
    query += " AND ".join(conditions)
    if is_on_switch_price or is_on_switch_year:
        query += "ORDER BY "
        if is_on_switch_price:
            query += "price, "
        else:
            query += "-price, "
        if is_on_switch_year:
            query += "year"
        else:
            query += "-year"
        query += ";"
    
    cursor.execute(query, tuple(values))
    cars = cursor.fetchall()

    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, "Found cars:\n")
    for car in cars:
        result_text.insert(tk.END, f"{car}\n")
    result_text.insert(tk.END, f"Total number of cars found: {len(cars)}")

    conn.close()

# Create the main window
root = tk.Tk()
root.title("Car Search")
root.configure(bg="black")

def switch_by_price():
    global is_on_switch_price
     
    # Determine is on or off
    if is_on_switch_price:
        on_button_price.config(image = off)
        is_on_switch_price = False
    else:
        on_button_price.config(image = on)
        is_on_switch_price = True

def switch_by_year():
    global is_on_switch_year
     
    # Determine is on or off
    if is_on_switch_year:
        on_button_year.config(image = off)
        is_on_switch_year = False
    else:
        on_button_year.config(image = on)
        is_on_switch_year = True

# Create labels and entry widgets for input
title_label = tk.Label(root, text="Auto Program", bg="black", fg="white", font=("Arial", 16))  # Set background to black, text to white, and font size
title_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
# brand_entry = tk.Entry(root, font=("Arial", 14))  # Set font size
# brand_entry.grid(row=0, column=1, padx=10, pady=10)

brand_label = tk.Label(root, text="Brand:", bg="black", fg="white", font=("Arial", 12))  # Set background to black, text to white, and font size
brand_label.grid(row=1, column=0, padx=10, pady=10)
brand_entry = tk.Entry(root, font=("Arial", 14))  # Set font size
brand_entry.grid(row=1, column=1, padx=10, pady=10)

model_label = tk.Label(root, text="Model:", bg="black", fg="white", font=("Arial", 12))  # Set background to black, text to white, and font size
model_label.grid(row=2, column=0, padx=10, pady=10)
model_entry = tk.Entry(root, font=("Arial", 14))  # Set font size
model_entry.grid(row=2, column=1, padx=10, pady=10)

year_label = tk.Label(root, text="Year:", bg="black", fg="white", font=("Arial", 12))  # Set background to black, text to white, and font size
year_label.grid(row=3, column=0, padx=10, pady=10)
year_entry = tk.Entry(root, font=("Arial", 14))  # Set font size
year_entry.grid(row=3, column=1, padx=10, pady=10)

price_label = tk.Label(root, text="Max Price:", bg="black", fg="white", font=("Arial", 12))  # Set background to black, text to white, and font size
price_label.grid(row=4, column=0, padx=10, pady=10)
price_entry = tk.Entry(root, font=("Arial", 14))  # Set font size
price_entry.grid(row=4, column=1, padx=10, pady=10)

on = PhotoImage(file = "on.png")
off = PhotoImage(file = "off.png")

price_label_low = tk.Label(root, text="Sort by price(from low to high):", bg="black", fg="white", font=("Arial", 12))  # Set background to black, text to white, and font size
price_label_low.grid(row=6, column=0, padx=10, pady=10)
on_button_price = Button(root, image = on, bd =0, bg="black",
                   command = switch_by_price)
on_button_price.grid(row=6, column=1)

price_label_low = tk.Label(root, text="Sort by year(from laster to newer):", bg="black", fg="white", font=("Arial", 12))  # Set background to black, text to white, and font size
price_label_low.grid(row=7, column=0, padx=10, pady=10)
on_button_year = Button(root, image = on, bd =0, bg="black",
                   command = switch_by_year)
on_button_year.grid(row=7, column=1)

search_button = tk.Button(root, text="Search", command=search_cars, bg="black", fg="white")
search_button.grid(row=8, column=0, columnspan=2, padx=5, pady=5)

result_text = tk.Text(root, height=30, width=150)
result_text.grid(row=9, column=0, columnspan=2, padx=5, pady=5)

# Run the main event loop
root.mainloop()