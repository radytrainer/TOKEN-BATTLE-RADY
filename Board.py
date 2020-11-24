
ROW_GRID = 6
COL_GRID = 7
database = []

for row in range(ROW_GRID):
    database.append([])

for row in range(len(database)):
    for col in range(COL_GRID):
        database[row].append(0)

    
# print(database)