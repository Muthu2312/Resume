import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

# Environment variables
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT', '5432')

try:
    # Connect to the PostgreSQL database
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    print("Connected to the database successfully!")

    # Create a cursor object
    cur = conn.cursor()

    # Define the email to search for
    email_to_search = 'dhinesh8361@gmail.com'

    # Execute a query to fetch all records from the Contact table
    # Use the exact table name from the database
    cur.execute('SELECT * FROM "App_contact";')  # Use double quotes for case-sensitive table names
    cur.execute('SELECT * FROM "App_contact" WHERE email = %s;', (email_to_search,))


    # Fetch and print the results
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Close the cursor and connection
    cur.close()
    conn.close()
    print("Connection closed.")

except Exception as e:
    print(f"An error occurred: {e}")
