#!/usr/bin/env python3
"""
Script to generate fake customer data for analytical database.
Generates a CSV file at data/customers.csv with fields:
customer_id, name, email, phone, age, sex, join_date, leave_date, churn_flag,
subscription_plan, city, state, zip_code, last_login_date
"""
import csv
import random
import datetime
import os

def random_date(start, end):
    """Generate a random date between start and end."""
    delta = end - start
    int_delta = delta.days
    random_day = random.randrange(int_delta + 1)
    return start + datetime.timedelta(days=random_day)

def random_phone():
    """Generate a random US phone number."""
    return f"+1-{random.randint(200,999)}-{random.randint(200,999)}-{random.randint(1000,9999)}"

def main():
    # Output directory and file
    output_dir = 'data'
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, 'customers.csv')

    # Parameters
    num_customers = 1000
    start_date = datetime.date(2015, 1, 1)
    today = datetime.date.today()

    # Sample data pools
    first_names = ['John', 'Jane', 'Alex', 'Emily', 'Michael', 'Sarah', 'David', 'Laura', 'Robert', 'Linda']
    last_names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Miller', 'Davis', 'Garcia', 'Rodriguez', 'Wilson']
    domains = ['gmail.com', 'yahoo.com', 'hotmail.com', 'example.com']
    sexes = ['Male', 'Female', 'Other']
    plans = ['Free', 'Basic', 'Premium', 'Enterprise']
    # Finnish cities
    cities = ['Helsinki', 'Espoo', 'Tampere', 'Vantaa', 'Oulu', 'Turku', 'Jyväskylä', 'Lahti', 'Kuopio', 'Pori']

    # Write CSV
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        # Header
        writer.writerow([
            'customer_id', 'name', 'email', 'phone', 'age', 'sex',
            'join_date', 'leave_date', 'churn_flag',
            'subscription_plan', 'city', 'zip_code', 'last_login_date'
        ])

        for cid in range(1, num_customers + 1):
            # Basic personal info
            first = random.choice(first_names)
            last = random.choice(last_names)
            name = f"{first} {last}"
            email = f"{first.lower()}.{last.lower()}{random.randint(1,99)}@{random.choice(domains)}"
            phone = random_phone()
            age = random.randint(18, 80)
            sex = random.choice(sexes)

            # Dates and churn
            join_dt = random_date(start_date, today)
            if random.random() < 0.3:
                leave_dt = random_date(join_dt, today)
                churn_flag = 1
            else:
                leave_dt = ''
                churn_flag = 0

            last_login = random_date(join_dt, today)

            # Location and plan (Finnish cities)
            city = random.choice(cities)
            zip_code = f"{random.randint(100, 99999):05d}"
            plan = random.choice(plans)

            # Write row
            writer.writerow([
                cid, name, email, phone, age, sex,
                join_dt, leave_dt, churn_flag,
                plan, city, zip_code, last_login
            ])

    print(f"Generated {num_customers} customers to {output_file}")

if __name__ == '__main__':
    main()