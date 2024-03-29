import sqlite3

conn = sqlite3.connect('celeb.dataset')

#create a cursor object
cursor = conn.cursor()

# # Create a dummy celebrity dataset with the following features name, genre, num_albums, age, awards, years_in_industry
# cursor.execute(
#     """ 
#     CREATE TABLE celebrity_dataset(
#      name TEXT,
#      genre TEXT,
#      num_albums INTEGER,
#      age INTEGER,
#      awards INTEGER,
#      years_in_industry INTEGER
#      )
     
#      """
# )

#insert data
celebrity_dataset = [
    ('Micheal Jackson', 'R&B/ Soul', '10', '50', '834', '40'),
    ('wizkid', 'Afropop\ Afrobeats', '4', '32', '85', '21' ),
    ('Beyonce', 'R&B/ Soul', '13', '41', '660','24'),
    ('Davido', 'Afropop\ Afrobeats', '8', '29', '60', '12'),
    ('Whitney Houston', 'R&B/ Soul', '7', '48', '657', '10'),
    ('2face', 'Afropop\ Afrobeats', '9', '46', '51', '23'),
    ('Lady Gaga', 'pop', '8', '36', '450', '21'),
    ('D Banj', 'Afropop\ Afrobeats', '5', '42', '29', '17'),
    ('Taylor Swift', 'pop', '26', '32', '414', '15'),
    ('Burna Boy', 'Afropop\ Afrobeats', '6', '31', '23', '12'),
    ('Eminem', 'Hip-pop/Rap', '13', '49', '392', '20'),
    ('Olamide', 'Afropop\ Afrobeats', '9', '33', '22', '12'),
    ('Rihanna', 'pop', '8', '34', '362', '19'),
    ('Justin Bieber', 'pop', '6', '28', '368', '15'),
    ('Janet Jackson', 'R&B/ Soul', '10', '56', '358', '48'),
    ('Nicki Minaj', 'Hip-pop/Rap', '4', '39', '318', '17'),
    ('Madonna', 'pop', '14', '64', '340', '43'),
    ('Cardi B', 'Hip-pop/Rap','1', '29', '162', '7'),
    ('Mariah Carey', 'pop', '15', '53','339', '34'),
    ('Ed Sheeran', 'pop', '5', '31', '124', '18')
 
]

cursor.executemany(
"""
INSERT INTO celebrity_dataset
VALUES (?, ?, ?, ?, ?, ?)

""",
celebrity_dataset
)


# Query your data to answer the following questions:
cursor.execute(
    """
    SELECT * FROM celebrity_dataset
    """
)

items = cursor.fetchall()

#format outputs to display in a tabular form
# print("name"+ "\t\t genre"+ "\t\t num_albums" + "\t age" + "\t\t awards" + "\t years_in_industry \n" f"{'.' * 90}")

#loop through the items
# for item in items:
#     name, genre, num_albums, age, awards, years_in_industry  = item
#     print(f"{name:18}{genre:10}{num_albums:12}{age:10}{awards:10}\t\t{years_in_industry}")
    
#  Who is the most decorated celebrity?
# query = """
# SELECT * 
# FROM celebrity_dataset 
# """
# cursor.execute(query)

# items = cursor.fetchall()

# print(f"name \t\t genre \t\t num_albums \t age \t awards\t years_in_industry")
# print(f"{'-' * 90}")

#  Who is the most decorated celebrity?
# MAX aggregate
# query =  """
# SELECT MAX(awards)
# FROM celebrity_dataset 
# """
# cursor.execute(query)

# items = cursor.fetchall()

# print(items)

# Who is the oldest celebrity?

query =  """
SELECT MAX(age)
FROM celebrity_dataset 
"""
cursor.execute(query)

items = cursor.fetchall()

print(items)

# Which celebrity has been in the industry the longest?  
query =  """
SELECT MAX(years_in_industry)
FROM celebrity_dataset 
"""
cursor.execute(query)

items = cursor.fetchall()

print(items)


#  - Which celebrity has the least number of albums?

query =  """
SELECT MIN(num_albums)
FROM celebrity_dataset 
"""
cursor.execute(query)

items = cursor.fetchall()

# print(items)

print(items)

#  - What is the most popular genre of music amongst all celebrities in the dataset?

query = """
SELECT COUNT(genre) 
FROM celebrity_dataset 
"""
cursor.execute(query)

items = cursor.fetchall()

print(items)