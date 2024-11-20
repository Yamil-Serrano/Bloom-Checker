
# Bloom Checker

## Overview

Bloom Checker is a fast and efficient tool for verifying whether an email or dataset item is present in a database. Using the Bloom Filter algorithm, it provides quick results with low memory usage, perfect for handling large datasets.

## Background & Problem Context

### The Cache Penetration Problem

Imagine an email verification service that needs to check if millions of email addresses exist in a database. A common implementation might look like this:

```python
def check_email(email):
    # First, check cache
    if cache.get(email):
        return True
    
    # If not in cache, check database
    if database.exists(email):
        cache.set(email, True)
        return True
        
    return False
```

This approach faces two significant challenges:

1. **Cache Miss**: When a valid email isn't in the cache but exists in the database:
   ```
   Client → Cache (Miss) → Database (Found) → Update Cache
   ```
   This creates one extra unnecessary lookup, but it's manageable.

2. **Cache Penetration**: When checking non-existent emails:
   ```
   Client → Cache (Miss) → Database (Not Found) → No Cache Update
   ```
   This becomes problematic when:
   - Attackers deliberately query non-existent emails
   - Each query unnecessarily hits both cache and database
   - System resources are wasted on known-invalid queries

### The Bloom Filter Solution

Bloom Checker solves this by adding a Bloom Filter as a preliminary check:

```
Client → Bloom Filter → Cache → Database
```

When checking an email:
- If Bloom Filter says "No" → Email definitely doesn't exist (stop here)
- If Bloom Filter says "Yes" → Email might exist (proceed to cache/database)

Real-world example:
```python
# Without Bloom Filter:
check_email("attacker@fake.com")  # Cache miss + DB query wasted
check_email("attacker2@fake.com") # Cache miss + DB query wasted
check_email("attacker3@fake.com") # Cache miss + DB query wasted

# With Bloom Checker:
check_email("attacker@fake.com")  # Bloom Filter: No (stops here)
check_email("attacker2@fake.com") # Bloom Filter: No (stops here)
check_email("attacker3@fake.com") # Bloom Filter: No (stops here)
```

Benefits:
- Protects against DoS attacks using non-existent emails
- Reduces unnecessary database load
- Extremely memory efficient (10 million emails ≈ 15MB of memory)
- Quick response times (O(k) where k is number of hash functions)


## Key Features

- **Fast Email Verification**: Quickly checks whether an email is probably in the database or definitely not.
- **Bloom Filter Algorithm**: Implements the space-efficient probabilistic data structure to minimize memory usage.
- **Low False Positive Rate**: Configurable false positive rates to suit different application needs.
- **Customizable Parameters**: Adjust the size of the Bloom Filter and the number of hash functions based on the dataset size.
- **Graphical User Interface (GUI)**: Intuitive and easy-to-use interface built with Tkinter.
- **File Input**: Supports CSV files for email lists and results display.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Yamil-Serrano/Bloom-Checker.git
   ```

2. Navigate to the project directory:
   ```bash
   cd Bloom-Checker
   ```

3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```bash
   python main.py
   ```

2. Use the interface to:
   - Select the **initial database** CSV file.
   - Select the **verification** CSV file.
   - View the verification results in the interface, with color-coded outputs:
     - **Green**: The email is probably in the database.
     - **Red**: The email is definitely not in the database.

3. Adjust the false positive rate directly in the `main.py` script if needed.

## Example CSV Format

### Initial Database File
| Email Address       |
|---------------------|
| example1@gmail.com  |
| example2@yahoo.com  |
| example3@hotmail.com|

### Verification File
| Email Address       |
|---------------------|
| example1@gmail.com  |
| unknown@gmail.com   |

## Screenshot of the Interface

![image](https://github.com/user-attachments/assets/da225619-89de-47f2-977b-a6f9d5e0ec15)


## Icon Attribution

- **[Lotus flower icons](https://www.flaticon.com/free-icons/lotus-flower)** created by [Freepik](https://www.flaticon.com/authors/freepik) - Flaticon
- **[File icons](https://www.flaticon.com/free-icons/file)** created by [Good Ware](https://www.flaticon.com/authors/good-ware) - Flaticon

## License

This project is licensed under the [Creative Commons Attribution-NonCommercial 4.0 International License](LICENSE.md).

## Contact

For questions, suggestions, or contributions, please reach out via:

- GitHub: [Neowizen](https://github.com/Yamil-Serrano)
