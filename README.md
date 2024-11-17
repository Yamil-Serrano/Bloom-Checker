
# Bloom Checker

## Overview

Bloom Checker is a fast and efficient tool for verifying whether an email or dataset item is present in a database. Using the Bloom Filter algorithm, it provides quick results with low memory usage, perfect for handling large datasets.

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
