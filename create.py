import psycopg2
from psycopg2 import sql

# Healthcare Database connection 
DATABASE_URL = "postgres://nbwocdjm:sQ6O3T_Zvmf80C3fS4nR2UGecaCy32S6@bubble.db.elephantsql.com/nbwocdjm"

# SQL commands to create tables
CREATE_PATIENTS_TABLE = sql.SQL("""
CREATE TABLE IF NOT EXISTS Patients (
    patient_id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    gender VARCHAR(10),
    medical_history TEXT  
)
""")

CREATE_APPOINTMENTS_TABLE = sql.SQL("""
CREATE TABLE IF NOT EXISTS Appointments (
    appointment_id SERIAL PRIMARY KEY,
    patient_id INT REFERENCES Patients(patient_id),
    appointment_date TIMESTAMP,
    doctor_name VARCHAR(100),
    reason_for_appointment TEXT
)
""")

# Function to establish a connection to the PostgreSQL database
def get_connection(db_url):
    return psycopg2.connect(db_url)

# Function to create tables in a given database
def create_tables(conn):
    try:
        cursor = conn.cursor()

        # Create database tables
        cursor.execute(CREATE_PATIENTS_TABLE)
        cursor.execute(CREATE_APPOINTMENTS_TABLE)
        
        conn.commit()
        print("Tables 'Patients' and 'Appointments' created successfully.")
    except psycopg2.DatabaseError as e:
        print(f"An error occurred: {e}")
    finally:
        if cursor: cursor.close()

# Main function to create tables in each database
def main():
    try:
        conn = get_connection(DATABASE_URL)
        create_tables(conn)
    except psycopg2.OperationalError as e:
        print(f"Failed to connect to database at {DATABASE_URL}: {e}")
    finally:
        if conn: conn.close()

if __name__ == '__main__':
    main()
