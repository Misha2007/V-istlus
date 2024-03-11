import csv
import sqlite3


# filename to form database
file = "auto_database.db"


try:
    conn = sqlite3.connect(file)
    print("Database Sqlite3.db formed.")
except:
    print("Database Sqlite3.db not formed.")

file_path = 'autod.csv'



connection = sqlite3.connect("auto_database.db")

cursor = connection.cursor()

# cursor.execute("CREATE TABLE auto_table(url str, brand str, engine str, mileage, int, fuel str, model str, model_short str, transmission str, year int, bodytype str, drive str, price float);").fetchall()

with open(file_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    
    # Read the header row
    header = next(reader)
    print("Header:", header)
    
    # Find the indexes of the columns you're interested in
    url_index = -1
    brand_index = -1
    engine_index = -1
    mileage_index = -1
    fuel_index = -1
    model_index = -1
    model_short_index = -1
    transmission_index = -1
    year_index = -1
    bodytype_index = -1
    drive_index = -1
    price_index = -1
    
    for i, column in enumerate(header):
        if column.lower() == 'url':
            url_index = i
        elif column.lower() == 'brand':
            brand_index = i
        elif column.lower() == 'engine':
            engine_index = i
        elif column.lower() == 'mileage':
            mileage_index = i
        elif column.lower() == 'fuel':
            fuel_index = i
        elif column.lower() == 'model':
            model_index = i
        elif column.lower() == 'model_short':
            model_short_index = i
        elif column.lower() == 'transmission':
            transmission_index = i
        elif column.lower() == 'year':
            year_index = i
        elif column.lower() == 'bodytype':
            bodytype_index = i
        elif column.lower() == 'drive':
            drive_index = i
        elif column.lower() == 'price':
            price_index = i
    
    if url_index == -1 or brand_index == -1 or engine_index == -1 \
            or mileage_index == -1 or fuel_index == -1 or model_index == -1 \
            or model_short_index == -1 or transmission_index == -1 or year_index == -1 \
            or bodytype_index == -1 or drive_index == -1 or price_index == -1:
        print("One or more columns not found in CSV file.")
    else:
        # Iterate over remaining rows
        for row in reader:
            # Extract fields from the row using indexes
            url = row[url_index]
            brand = row[brand_index]
            engine = row[engine_index]
            mileage = row[mileage_index]
            fuel = row[fuel_index]
            model = row[model_index]
            model_short = row[model_short_index]
            transmission = row[transmission_index]
            year = row[year_index]
            bodytype = row[bodytype_index]
            drive = row[drive_index]
            price = row[price_index]


            print("URL:", url)
            print("Brand:", brand)
            print("Engine:", engine)
            print("Mileage:", mileage)
            print("Fuel:", fuel)
            print("Model:", model)
            print("Model Short:", model_short)
            print("Transmission:", transmission)
            print("Year:", year)
            print("Bodytype:", bodytype)
            print("Drive:", drive)
            print("Price:", price)
            

            # add auto to database
            # cursor.execute(f"""
            # INSERT INTO auto_table(url, brand, engine, mileage, fuel, model, model_short, transmission, year, bodytype, drive, price)
            # VALUES
            # (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);""", (url, brand, engine, mileage, fuel, model, model_short, transmission, year, bodytype, drive, price))



            connection.commit()


rows = cursor.execute("SELECT * FROM auto_table").fetchall()

print(rows)