import psycopg2
from faker import Faker
from datetime import datetime, timedelta
import random

# Database connection settings
DATABASE_URL = "postgres://nbwocdjm:sQ6O3T_Zvmf80C3fS4nR2UGecaCy32S6@bubble.db.elephantsql.com/nbwocdjm"

# Function to establish a connection to the PostgreSQL database
def get_connection():
    return psycopg2.connect(DATABASE_URL)

# Function to generate mock patient data
def generate_patient_data(fake):
    patients = []
    for _ in range(1000):  # Insert 1000 patients
        name = fake.name()
        age = random.randint(18, 100)
        gender = random.choice(['Male', 'Female'])
        medical_history = fake.paragraph(nb_sentences=5)  # Generate medical history text
        patients.append((name, age, gender, medical_history))
    return patients

# Function to generate mock appointment data
def generate_appointment_data(fake):
    appointments = []
    for _ in range(2000):  # Insert 2000 appointments
        patient_id = random.randint(1, 1000)  # Random patient ID
        appointment_date = fake.date_time_between(start_date='-1y', end_date='+1y')  # Random appointment date
        doctor_name = fake.name()
        reason_for_appointment = fake.sentence(nb_words=6)  # Generate reason for appointment text
        appointments.append((patient_id, appointment_date, doctor_name, reason_for_appointment))
    return appointments

# Function to insert patient data into the database
def insert_patients(conn, patients):
    cursor = conn.cursor()
    cursor.executemany("""
        INSERT INTO Patients (name, age, gender, medical_history)
        VALUES (%s, %s, %s, %s)
    """, patients)
    conn.commit()
    cursor.close()

# Function to insert appointment data into the database
def insert_appointments(conn, appointments):
    cursor = conn.cursor()
    cursor.executemany("""
        INSERT INTO Appointments (patient_id, appointment_date, doctor_name, reason_for_appointment)
        VALUES (%s, %s, %s, %s)
    """, appointments)
    conn.commit()
    cursor.close()

# Main function to insert data into the tables
def main():
    fake = Faker()
    patients = generate_patient_data(fake)
    appointments = generate_appointment_data(fake)
    conn = get_connection()
    insert_patients(conn, patients)
    insert_appointments(conn, appointments)
    conn.close()
    print("Data insertion completed.")

if __name__ == '__main__':
    main()
