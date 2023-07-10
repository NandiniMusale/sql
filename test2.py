import pandas as pd
import mysql.connector
import math

# Establish database connection
db = mysql.connector.connect(
    host="", # basically localhost
    user="", # basically root
    password="",#your password
    database="" # your database name
)
cursor = db.cursor()

# Uncomment the line below to create the table if it doesn't exist
# cursor.execute('CREATE TABLE nandini.dres_sale (Dress_ID int, `29/8/2013` int, `31/8/2013` int, ...')

# Read Excel file into DataFrame (df)
df = pd.read_excel(r'') # give your file path here

cursor.execute('CREATE TABLE dress (Dress_ID int,day1 int,day2 int,day3 int,day4 int,day5 int,day6 int,day7 int, day8 int, day9 int, day10 int, day11 int,day12 int,day13 int ,day14 int,day15 int,day16 int,day17 int,day18 int,day19 int,day20 int,day21 int,day22 int,day23 int )')


for index, row in df.iterrows():
    if any(isinstance(value, float) and math.isnan(value) for value in row.values):
        # Skip rows with missing values
        continue
    
    sql = "INSERT INTO nandini.dres_sale (Dress_ID,day1,day2,day3,day4,day5,day6,day7,day8,day9,day10,day11,day12,day13,day14,day15,day16,day17,day18,day19,day20,day21,day22,day23) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = tuple(row)
    
    cursor.execute(sql, values)

# Commit changes
db.commit()

# Fetch and print the inserted data from the table
cursor.execute("SELECT * dres_sale")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close connections
cursor.close()
db.close()
