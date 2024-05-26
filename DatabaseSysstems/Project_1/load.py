import csv
import mysql.connector

import mysql.connector
from mysql.connector import cursor, IntegrityError, DatabaseError

conn = mysql.connector.connect(
    host='academicmysql.mysql.database.azure.com',
    user='lxm6009',
    password='Lathi2525@',
    database='lxm6009'
)


def load_data(table_name, data_file):
  with open(data_file, "r") as f:
    reader = csv.reader(f)
    headers = next(reader)

    # Create a list of column names
    columns = []
    for header in headers:
      columns.append(header)
    columns = [ele.replace("-", "_") for ele in columns]
    columns = [ele.replace(" ", "") for ele in columns]
    print(columns)

    # Insert the data into the table
    with conn.cursor() as cursor:
      for row in reader:
            print(row)
            #print(columns)

            try:
                cursor.execute(
                    f"INSERT INTO {table_name} ({','.join(columns)}) VALUES ({','.join(['%s' for _ in columns])})", row)
            except IntegrityError as e:
                print(e)
            conn.commit();

# Load the data into the WORLD_CUPS table
load_data("WORLD_CUPS", "Project1_datasets/WorldCups.csv")
print("WORLD_CUPS")

# Load the data into the WORLD_CUP_MATCHES table
load_data("WORLD_CUP_MATCHES", "Project1_datasets/WorldCupMatches.csv")
print("WORLD_CUP_MATCHES")
# Load the data into the WORLD_CUP_PLAYERS table
load_data("WORLD_CUP_PLAYERS", "Project1_datasets/WorldCupPlayers.csv")
print("WORLD_CUP_PLAYERS")
# Close the connection
conn.close()