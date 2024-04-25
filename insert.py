import psycopg2
import random
from create import DATABASE_URL

# Function to establish a connection to the PostgreSQL database
def get_connection(db_url):
    try:
        conn = psycopg2.connect(db_url)
        return conn
    except psycopg2.Error as e:
        print("Error connecting to the database:", e)
        return None

# Function to generate mock patient data
def generate_patient_data():
    patients = []
    for _ in range(100000):  # Insert 100000 patients
        name = f"Patient_{_}"  # Generate a simple patient name
        age = random.randint(18, 100)
        gender = random.choice(['Male', 'Female'])
        medical_history = f"This is medical history for {name}"  # Generate a simple medical history
        patients.append((name, age, gender, medical_history))
    return patients

# Function to generate mock appointment data
def generate_appointment_data():
    appointments = []
    for _ in range(200000):  # Insert 200000 appointments
        patient_id = random.randint(1, 100000)  # Random patient ID
        appointment_date = f"2024-04-{random.randint(1, 30)} {random.randint(0, 23)}:{random.randint(0, 59)}:00"  # Random appointment date
        doctor_name = f"Doctor_{random.randint(1, 10)}"  # Generate a simple doctor name
        reason_for_appointment = f"This is reason for appointment for Patient_{patient_id}"  # Generate a simple reason for appointment
        appointments.append((patient_id, appointment_date, doctor_name, reason_for_appointment))
    return appointments

# Function to insert patient data into the database
def insert_patients(conn, patients):
    cursor = conn.cursor()
    try:
        for patient in patients:
            name, age, gender, medical_history = patient
            
            # Encrypt medical_history using pgp_sym_encrypt function
            cursor.execute("""
                INSERT INTO Patients (name, age, gender, medical_history)
                VALUES (%s, %s, %s, %s)
            """, (name, age, gender, medical_history))

        conn.commit()
        print("Patients insertion completed.")
    except psycopg2.Error as e:
        conn.rollback()
        print("Error inserting patients:", e)
    finally:
        cursor.close()

# Function to insert appointment data into the database
def insert_appointments(conn, appointments):
    cursor = conn.cursor()
    try:
        cursor.executemany("""
            INSERT INTO Appointments (patient_id, appointment_date, doctor_name, reason_for_appointment)
            VALUES (%s, %s, %s, %s)
        """, appointments)
        conn.commit()
        print("Appointments insertion completed.")
    except psycopg2.Error as e:
        conn.rollback()
        print("Error inserting appointments:", e)
    finally:
        cursor.close()

# Main function to insert data into the tables
def main():
    conn = get_connection(DATABASE_URL)
    if conn is None:
        return  # Exit the function if connection is not established
    patients = generate_patient_data()
    appointments = generate_appointment_data()
    insert_patients(conn, patients)
    insert_appointments(conn, appointments)
    conn.close()
    print("Data insertion completed.")

if __name__ == '__main__':
    main()
