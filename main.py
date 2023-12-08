import sqlite3 as sl
import json

con = sl.connect('Airports.db')
cur = con.cursor()

# with open('airport-codes_json.json') as file:
#     data = json.load(file)
#
# column_names = list(data[0].keys())
#
# with con:
#     con.execute("""
#         CREATE TABLE IF NOT EXISTS Airports (
#             id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#             continent TEXT,
#             first_coordinate REAL,
#             second_coordinate REAL,
#             elevation_ft REAL,
#             gps_code TEXT NULL,
#             iata_code TEXT NULL,
#             ident TEXT,
#             iso_country TEXT,
#             iso_region TEXT,
#             local_code TEXT NULL,
#             municipality TEXT,
#             name TEXT,
#             type TEXT
#         );
#     """)
#

# for item in data:
#     coordinates = item["coordinates"].split(", ")
#     first_coordinate = float(coordinates[0])
#     second_coordinate = float(coordinates[1])
#
#     del item["coordinates"]
#     item["first_coordinate"] = first_coordinate
#     item["second_coordinate"] = second_coordinate
# #
#
#
# insert_query = "INSERT INTO Airports (continent, first_coordinate, second_coordinate, elevation_ft, gps_code, iata_code, ident, iso_country, iso_region, local_code, municipality, name, type) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)"
# values = [(item['continent'], item['first_coordinate'], item['second_coordinate'], item['elevation_ft'], item['gps_code'], item['iata_code'], item['ident'], item['iso_country'], item['iso_region'], item['local_code'], item['municipality'], item['name'], item['type']) for item in data]


# with con:
#     con.executemany(insert_query, values)



# задание № 1 Выведите принтом все вертолетные аэропорты
# cur.execute("SELECT * FROM airports WHERE airports.type = 'heliport'")
#
# result = cur.fetchall()
# for i in result:
#     print(i)
#



# задание № 2
# Напишите функцию принимающую диапазон координат (x1,y1,x2,y2, type = None)
# если type не введен - выводящую все виды аэропортов если type введен выодящие только аэропорты такого же типа
#
# def get_airports(x1,y1,x2,y2, type = None):
#     with sl.connect('Airports.db') as con:
#         cur = con.cursor()
#
#         if type is None:
#             query = """SELECT * FROM airports
#             WHERE first_coordinate BETWEEN ? AND ? AND second_coordinate BETWEEN ? AND ?
#             """
#             cur.execute(query,(x1, x2, y1, y2))
#
#         else:
#             query = """SELECT * FROM airports
#                         WHERE first_coordinate BETWEEN ? AND ? AND second_coordinate BETWEEN ? AND ? AND type = ?
#                         """
#             cur.execute(query, (x1, x2, y1, y2, type))
#
#     result = cur.fetchall()
#
#     for i in result:
#         print(i)
#
# get_airports(130.260, 30.777, 130.285, 30.977)
# get_airports(130.260, 30.777, 130.285, 30.977, 'small_airport')





# задание № 3
# Напишите функцию позволяющую принять словарь или список словарей  и дозаписать новые аэропорты
# в том случае если отстутсвует name, type, iso_country, iso_region, coordinates запись отменяется
# def insert_new_data(airports):
#     with sl.connect('Airports.db') as con:
#         cur = con.cursor()
#         important_keys = ['name', 'type', 'iso_country', 'iso_region', 'coordinates']
#
#         for airport in airports:
#             try:
#                 missing_keys = []
#                 for key in important_keys:
#                     if key not in airport:
#                         missing_keys.append(key)
#
#                 if missing_keys:
#                     raise KeyError(f"В Добавляемом в БД списке отсутствует(ют) следующий(е) ключ(и): {', '.join(missing_keys)}")
#
#                 coordinates = airport["coordinates"].split(", ")
#                 first_coordinate = float(coordinates[0])
#                 second_coordinate = float(coordinates[1])
#
#                 del airport["coordinates"]
#                 airport["first_coordinate"] = first_coordinate
#                 airport["second_coordinate"] = second_coordinate
#
#                 insert_query = "INSERT INTO Airports (continent, first_coordinate, second_coordinate, elevation_ft, gps_code, iata_code, ident, iso_country, iso_region, local_code, municipality, name, type) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)"
#                 values = (airport.get('continent'), airport.get('first_coordinate'), airport.get('second_coordinate'), airport.get('elevation_ft'), airport.get('gps_code'), airport.get('iata_code'), airport.get('ident'), airport.get('iso_country'), airport.get('iso_region'), airport.get('local_code'), airport.get('municipality'), airport.get('name'), airport.get('type'))
#
#                 cur.execute(insert_query, values)
#             except KeyError as ke:
#                 print(ke)
#             except Exception as e:
#                 print("The error is:", e)
#
# airports = [
#     {
#         "name": "Moscow Sheremetyevo",
#         "type": "large_airport",
#         "iso_country": "RU",
#         "iso_region": "RU-MOW",
#         "coordinates": "37.4166, 55.9726"
#     },
#     {
#         "name": "New York JFK",
#         "type": "large_airport",
#         "iso_country": "US",
#         "iso_region": "US-NY",
#         "coordinates": "-73.7781, 40.6398"
#     },
#     {
#         "name": "Dubai International",
#         "type": "large_airport",
#         "iso_country": "AE",
#         "iso_region": "AE-DU",
#         "coordinates": "55.364444, 25.253175"
#     },
#     {
#         "name": "London Heathrow",
#         "type": "large_airport",
#         "iso_country": "GB",
#         "iso_region": "GB-ENG",
#         "coordinates": "-0.461941, 51.4706"
#     }
# ]
# insert_new_data(airports)



# задание 4 Напишите функцию делающую тоже самое но требующую напечать эти данные в консоль
# def insert_new_data(airports):
#     with sl.connect('Airports.db') as con:
#         cur = con.cursor()
#         important_keys = ['name', 'type', 'iso_country', 'iso_region', 'coordinates']
#
#         for airport in airports:
#             try:
#                 missing_keys = []
#                 for key in important_keys:
#                     if key not in airport:
#                         missing_keys.append(key)
#
#                 if missing_keys:
#                     raise KeyError(f"В Добавляемом в БД списке отсутствует(ют) следующий(е) ключ(и): {', '.join(missing_keys)}")
#
#                 coordinates = airport["coordinates"].split(", ")
#                 first_coordinate = float(coordinates[0])
#                 second_coordinate = float(coordinates[1])
#
#                 del airport["coordinates"]
#                 airport["first_coordinate"] = first_coordinate
#                 airport["second_coordinate"] = second_coordinate
#
#                 insert_query = "INSERT INTO Airports (continent, first_coordinate, second_coordinate, elevation_ft, gps_code, iata_code, ident, iso_country, iso_region, local_code, municipality, name, type) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)"
#                 values = (airport.get('continent'), airport.get('first_coordinate'), airport.get('second_coordinate'), airport.get('elevation_ft'), airport.get('gps_code'), airport.get('iata_code'), airport.get('ident'), airport.get('iso_country'), airport.get('iso_region'), airport.get('local_code'), airport.get('municipality'), airport.get('name'), airport.get('type'))
#
#                 cur.execute(insert_query, values)
#                 print(f"Вы только что добавили в Базу данных: {airport['name']} - {airport['type']}")
#             except KeyError as ke:
#                 print(ke)
#             except Exception as e:
#                 print("The error is:", e)

# airports = [
#     {
#         "name": "Frankfurt am Main",
#         "type": "large_airport",
#         "iso_country": "DE",
#         "iso_region": "DE-HE",
#         "coordinates": "8.683333, 50.11022"
#     },
#     {
#         "name": "Dubai International",
#         "type": "large_airport",
#         "iso_country": "AE",
#         "iso_region": "AE-DU",
#         "coordinates": "55.364444, 25.253175"
#     },
#     {
#         "name": "Singapore Changi",
#         "type": "large_airport",
#         "iso_country": "SG",
#         "iso_region": "SG-01",
#         "coordinates": "103.994434, 1.364420"
#     }
# ]
# insert_new_data(airports)

# задание 5
# напишите функцию принимающую словарь параметров и выводящую все аэропорты удовлетворяющие параметрам,
# координаты в отличии от всех остальных работают аналогично функции 2

# def get_airports(parameters):
#     with sl.connect('Airports.db') as con:
#         cur = con.cursor()
#         query = "SELECT * FROM airports WHERE "
#         params = []
#         val = []
#
#         for key in parameters.keys():
#             if 'x1' in parameters and 'y1' in parameters and 'x2' in parameters and 'y2' in parameters:
#                 params.append('first_coordinate BETWEEN ? AND ? AND second_coordinate BETWEEN ? AND ?')
#                 val.extend([parameters['x1'], parameters['x2'], parameters['y1'], parameters['y2']])
#             else:
#                 params.append(f"{key}=?")
#                 val.append(parameters[key])
#
#         query += " AND ".join(params)
#
#         cur.execute(query, val)
#
#     result = cur.fetchall()
#
#     for i in result:
#         print(i)


# get_airports({'x1': 103.900, 'y1': 1.357, 'x2': 104.005, 'y2': 1.577})
# get_airports({'continent': 'NA', 'iso_country': 'US', 'local_code': '00CA'})
# get_airports({'id': 2})
