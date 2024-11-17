
import csv
import hashlib
import math


# Function to calculate the Bloom Filter size (m) and the number of hash functions (k)
def calculate_bloom_filter_parameters(n, p):
    m = -(n * math.log(p)) / (math.log(2) ** 2)
    k = (m / n) * math.log(2)
    return int(m), round(k)


# Hash function that returns an integer value based on the email and concatenate (i)
def hash_function(email, i):
    hash_object = hashlib.sha256((email + str(i)).encode())
    return int(hash_object.hexdigest(), 16)


# Create the Bloom Filter
def create_bloom_filter(emails_in_db, m, k):
    bloom_filter = [0] * m
    for email in emails_in_db:
        for i in range(k):
            index = hash_function(email, i) % m
            bloom_filter[index] = 1
    return bloom_filter


# Function to check if an email is probably in the database
def verify_email(email, bloom_filter, m, k):
    for i in range(k):
        index = hash_function(email, i) % m
        if bloom_filter[index] == 0:
            return "Not in the DB"
    return "Probably in the DB"


# Function to process the two CSV files, create the Bloom filter and check the emails
def process_files(initial_file, verify_file, false_positive_rate):
    with open(initial_file, mode='r', newline='', encoding='utf-8') as data_base, \
         open(verify_file, mode='r', newline='', encoding='utf-8') as verify_data:

        db_reader = csv.reader(data_base)
        verify_reader = csv.reader(verify_data)

        # Skip the header rows of the CSV files
        next(db_reader)
        next(verify_reader)

        # Store the emails in lists
        emails_in_db = [row[0] for row in db_reader]
        emails_to_verify = [row[0] for row in verify_reader]

        # Calculate the size of the Bloom filter and the number of hash functions
        m, k = calculate_bloom_filter_parameters(len(emails_in_db), false_positive_rate)

        # Create the Bloom filter using the emails from the database
        bloom_filter = create_bloom_filter(emails_in_db, m, k)

        results = []
        for email in emails_to_verify:
            result = verify_email(email, bloom_filter, m, k)
            if result == "Not in the DB":
                results.append((email, result, "red"))
            else:
                results.append((email, result, "green"))

        return results

