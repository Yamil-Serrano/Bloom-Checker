import csv
import hashlib
import math
import array


# Function to calculate the Bloom Filter size (m) and the number of hash functions (k)
def calculate_bloom_filter_parameters(n, p):
    m = -(n * math.log(p)) / (math.log(2) ** 2)
    k = (m / n) * math.log(2)
    return int(m), round(k)


# Hash function that returns an integer value based on the email and an index (i)
def hash_function(email, i):
    hash_object = hashlib.sha256((email + str(i)).encode())
    return int(hash_object.hexdigest(), 16)

# Function to create a bit array
def make_bit_array(bit_size, fill=0):
    int_size = bit_size >> 5                # Number of 32-bit integers
    if (bit_size & 31):                     # If bit_size is not a multiple of 32, add an extra integer
        int_size += 1
    if fill == 1:
        fill = 4294967295  # All bits set to 1
    else:
        fill = 0           # All bits set to 0

    bit_array = array.array('I')  # Create an array of unsigned 32-bit integers
    bit_array.extend((fill,) * int_size)
    return bit_array

# Function to set a bit in the array
def set_bit(bit_array, bit_num):
    record = bit_num >> 5       # Determine which integer the bit is in
    offset = bit_num & 31       # Position of the bit within the integer
    mask = 1 << offset          # Create a mask for that bit
    bit_array[record] |= mask   # Set the bit to 1

# Function to get the value of a bit
def get_bit(bit_array, bit_num):
    record = bit_num >> 5       # Determine which integer the bit is in
    offset = bit_num & 31       # Position of the bit within the integer
    mask = 1 << offset          # Create a mask for that bit
    return (bit_array[record] & mask) != 0  # Return True if the bit is 1

# Create the Bloom Filter
def create_bloom_filter(emails_in_db, m, k):
    bloom_filter = make_bit_array(m)  # Create a bit array
    for email in emails_in_db:
        for i in range(k):
            index = hash_function(email, i) % m
            set_bit(bloom_filter, index)  # Use set_bit to set the bit to 1
    return bloom_filter

# Verify if an email is in the database
def verify_email(email, bloom_filter, m, k):
    for i in range(k):
        index = hash_function(email, i) % m
        if not get_bit(bloom_filter, index):  # Use get_bit to check the bit
            return "Not in the DB"
    return "Probably in the DB"


# Function to process the two CSV files, create the Bloom filter, and check the emails
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
