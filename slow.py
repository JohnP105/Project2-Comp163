import psycopg2
from psycopg2 import sql
import time
from insert import DATABASE_URL, get_connection

# Function to run a slow SQL query
def run_slow_query(conn):
    try:
        cursor = conn.cursor()

        # Define the slow query
        slow_query = sql.SQL("""
            SELECT Patients.name, Appointments.appointment_date, COUNT(*) AS total_appointments
            FROM Patients
            JOIN Appointments ON Patients.patient_id = Appointments.patient_id
            WHERE Patients.medical_history LIKE %s
            AND EXTRACT(MONTH FROM Appointments.appointment_date) = EXTRACT(MONTH FROM CURRENT_DATE)
            GROUP BY Patients.name, Appointments.appointment_date
            ORDER BY total_appointments DESC
        """)
        
        # Parameter for LIKE query
        search_pattern = '%checkup%'

        start_time = time.time()
        
        # Execute the slow query with parameters
        cursor.execute(slow_query, (search_pattern,))
        
        end_time = time.time()

        # Display the execution time
        print(f"Slow query executed in {end_time - start_time:.2f} seconds.")

        # Fetch the results
        results = cursor.fetchall()

        # Print the results
        for row in results:
            print(row)

    except psycopg2.DatabaseError as e:
        print(f"An error occurred while executing the slow query: {e}")
    finally:
        if cursor: cursor.close()

# Main function
def main():
    conn = None  # Initialize conn to None
    try:
        conn = get_connection(DATABASE_URL)
        run_slow_query(conn)
    except psycopg2.OperationalError as e:
        print(f"Failed to connect to the database at {DATABASE_URL}: {e}")
    finally:
        if conn: conn.close()

if __name__ == '__main__':
    main()
