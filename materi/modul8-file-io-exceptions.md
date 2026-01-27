# Modul 8: File I/O & Exception Handling 📁

## 📚 Pendahuluan

Modul ini membahas dua konsep penting dalam pemrograman: **File I/O** (Input/Output) untuk bekerja dengan file, dan **Exception Handling** untuk menangani error secara elegan. Kedua skill ini essential untuk membuat aplikasi yang robust dan production-ready.

## 🎯 Tujuan Pembelajaran

Setelah mempelajari modul ini, Anda akan mampu:
1. Membaca dan menulis file dengan berbagai mode
2. Bekerja dengan berbagai format file (text, CSV, JSON, binary)
3. Menggunakan context managers untuk file handling
4. Memahami exception hierarchy di Python
5. Menangani error dengan try-except-else-finally
6. Membuat custom exceptions
7. Menggunakan best practices untuk error handling
8. Bekerja dengan file paths dan directories

## 📖 Materi

### 1. File Operations Dasar

```python
# Mode file:
# 'r'  - Read (default)
# 'w'  - Write (overwrite)
# 'a'  - Append
# 'x'  - Exclusive creation
# 'b'  - Binary mode
# 't'  - Text mode (default)
# '+'  - Read and write

# Cara 1: Manual open/close
file = open('example.txt', 'r')
content = file.read()
print(content)
file.close()

# Cara 2: Context manager (RECOMMENDED)
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
# File otomatis tertutup setelah keluar dari with block

# Menulis file
with open('output.txt', 'w') as file:
    file.write("Hello, World!\n")
    file.write("Python File I/O\n")

# Append ke file
with open('output.txt', 'a') as file:
    file.write("New line appended\n")
```

### 2. Membaca File

```python
# Read entire file
with open('data.txt', 'r') as file:
    content = file.read()

# Read line by line
with open('data.txt', 'r') as file:
    for line in file:
        print(line.strip())  # strip() menghilangkan whitespace

# Read specific number of characters
with open('data.txt', 'r') as file:
    chunk = file.read(100)  # Read 100 characters

# Read all lines into list
with open('data.txt', 'r') as file:
    lines = file.readlines()
    print(lines)

# Read one line at a time
with open('data.txt', 'r') as file:
    line1 = file.readline()
    line2 = file.readline()

# Best practice: Iterate directly (memory efficient)
with open('large_file.txt', 'r') as file:
    for line in file:
        process_line(line)
```

### 3. Menulis File

```python
# Write (overwrite)
with open('output.txt', 'w') as file:
    file.write("First line\n")
    file.write("Second line\n")

# Write multiple lines
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open('output.txt', 'w') as file:
    file.writelines(lines)

# Append
with open('log.txt', 'a') as file:
    file.write(f"Log entry: {datetime.now()}\n")

# Write with print
with open('output.txt', 'w') as file:
    print("Hello", file=file)
    print("World", file=file)
```

### 4. Working with CSV Files

```python
import csv

# Write CSV
students = [
    ['Name', 'NPM', 'Score'],
    ['Budi', '2106001', 85],
    ['Ani', '2106002', 92],
    ['Citra', '2106003', 78]
]

with open('students.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(students)

# Write CSV with dict
students_dict = [
    {'name': 'Budi', 'npm': '2106001', 'score': 85},
    {'name': 'Ani', 'npm': '2106002', 'score': 92}
]

with open('students.csv', 'w', newline='') as file:
    fieldnames = ['name', 'npm', 'score']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(students_dict)

# Read CSV
with open('students.csv', 'r') as file:
    reader = csv.reader(file)
    header = next(reader)  # Skip header
    for row in reader:
        print(row)

# Read CSV as dict
with open('students.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"{row['name']}: {row['score']}")
```

### 5. Working with JSON Files

```python
import json

# Python object to JSON file
data = {
    'name': 'Budi Santoso',
    'age': 20,
    'courses': ['Python', 'JavaScript', 'Java'],
    'grades': {
        'Python': 90,
        'JavaScript': 85
    }
}

# Write JSON
with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)

# Read JSON
with open('data.json', 'r') as file:
    loaded_data = json.load(file)
    print(loaded_data)

# JSON string conversion
json_string = json.dumps(data, indent=2)
print(json_string)

loaded_from_string = json.loads(json_string)
print(loaded_from_string)

# Pretty print JSON
print(json.dumps(data, indent=2, sort_keys=True))

# Custom JSON encoder
from datetime import datetime

class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)

data_with_date = {
    'name': 'Budi',
    'timestamp': datetime.now()
}

json_str = json.dumps(data_with_date, cls=DateTimeEncoder)
```

### 6. Binary Files

```python
# Write binary
data = bytes([0, 1, 2, 3, 4, 5])
with open('data.bin', 'wb') as file:
    file.write(data)

# Read binary
with open('data.bin', 'rb') as file:
    binary_data = file.read()
    print(binary_data)

# Copy file (binary mode)
def copy_file(source, destination):
    with open(source, 'rb') as src:
        with open(destination, 'wb') as dst:
            dst.write(src.read())

# Copy large file in chunks
def copy_large_file(source, destination, chunk_size=8192):
    with open(source, 'rb') as src:
        with open(destination, 'wb') as dst:
            while True:
                chunk = src.read(chunk_size)
                if not chunk:
                    break
                dst.write(chunk)
```

### 7. File Path Operations

```python
import os
from pathlib import Path

# os.path module
file_path = '/home/user/documents/file.txt'

# Get directory
print(os.path.dirname(file_path))  # /home/user/documents

# Get filename
print(os.path.basename(file_path))  # file.txt

# Join paths
path = os.path.join('folder', 'subfolder', 'file.txt')

# Check existence
if os.path.exists('file.txt'):
    print("File exists")

# Get file size
size = os.path.getsize('file.txt')

# Get absolute path
abs_path = os.path.abspath('file.txt')

# pathlib (Modern approach - RECOMMENDED)
path = Path('folder/subfolder/file.txt')

# Create directory
path.parent.mkdir(parents=True, exist_ok=True)

# Check if file/directory
print(path.is_file())
print(path.is_dir())

# Get parts
print(path.name)        # file.txt
print(path.stem)        # file
print(path.suffix)      # .txt
print(path.parent)      # folder/subfolder

# List directory
for item in Path('.').iterdir():
    print(item)

# Find all Python files
for py_file in Path('.').rglob('*.py'):
    print(py_file)

# Read/Write with pathlib
path = Path('output.txt')
path.write_text('Hello, World!')
content = path.read_text()
```

### 8. Exception Handling Dasar

```python
# Try-except
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Multiple exceptions
try:
    number = int(input("Enter number: "))
    result = 10 / number
except ValueError:
    print("Invalid input!")
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Catch multiple exceptions in one block
try:
    # some code
    pass
except (ValueError, TypeError) as e:
    print(f"Error: {e}")

# Catch any exception
try:
    # some code
    pass
except Exception as e:
    print(f"An error occurred: {e}")

# Get exception details
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error type: {type(e).__name__}")
    print(f"Error message: {e}")
```

### 9. Try-Except-Else-Finally

```python
def read_file(filename):
    try:
        file = open(filename, 'r')
        content = file.read()
    except FileNotFoundError:
        print(f"File {filename} not found")
        return None
    except PermissionError:
        print(f"No permission to read {filename}")
        return None
    else:
        # Executed if no exception occurred
        print("File read successfully")
        return content
    finally:
        # Always executed, regardless of exceptions
        try:
            file.close()
            print("File closed")
        except:
            pass

# Better approach with context manager
def read_file_safe(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"File {filename} not found")
        return None
    else:
        print("File read successfully")
        return content
```

### 10. Raising Exceptions

```python
def validate_age(age):
    """Validate age input"""
    if not isinstance(age, int):
        raise TypeError("Age must be an integer")
    
    if age < 0:
        raise ValueError("Age cannot be negative")
    
    if age > 150:
        raise ValueError("Invalid age")
    
    return True

# Usage
try:
    validate_age(-5)
except ValueError as e:
    print(f"Validation error: {e}")

# Re-raising exceptions
def process_data(data):
    try:
        # Process data
        result = risky_operation(data)
    except Exception as e:
        # Log error
        print(f"Error processing data: {e}")
        # Re-raise the same exception
        raise

# Raise with traceback
def function_a():
    function_b()

def function_b():
    try:
        risky_operation()
    except Exception as e:
        raise RuntimeError("Error in function_b") from e
```

### 11. Custom Exceptions

```python
# Simple custom exception
class InvalidCredentialsError(Exception):
    """Raised when login credentials are invalid"""
    pass

# Exception with additional data
class InsufficientFundsError(Exception):
    """Raised when account has insufficient funds"""
    
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        message = f"Insufficient funds: balance={balance}, required={amount}"
        super().__init__(message)

# Exception hierarchy
class DatabaseError(Exception):
    """Base class for database errors"""
    pass

class ConnectionError(DatabaseError):
    """Raised when database connection fails"""
    pass

class QueryError(DatabaseError):
    """Raised when query execution fails"""
    pass

# Usage
def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount

try:
    new_balance = withdraw(1000, 1500)
except InsufficientFundsError as e:
    print(f"Error: {e}")
    print(f"Current balance: {e.balance}")
    print(f"Requested amount: {e.amount}")
```

### 12. Context Managers

```python
# Built-in context manager
with open('file.txt', 'r') as file:
    content = file.read()

# Custom context manager - Class-based
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        print(f"Opening {self.filename}")
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Closing {self.filename}")
        if self.file:
            self.file.close()
        # Return False to propagate exception
        # Return True to suppress exception
        return False

# Usage
with FileManager('test.txt', 'w') as file:
    file.write("Hello, World!")

# Custom context manager - Function-based
from contextlib import contextmanager

@contextmanager
def file_manager(filename, mode):
    file = None
    try:
        print(f"Opening {filename}")
        file = open(filename, mode)
        yield file
    finally:
        print(f"Closing {filename}")
        if file:
            file.close()

# Usage
with file_manager('test.txt', 'w') as file:
    file.write("Hello, World!")

# Multiple context managers
with open('input.txt', 'r') as infile, open('output.txt', 'w') as outfile:
    for line in infile:
        outfile.write(line.upper())
```

## 🏋️ Latihan Praktik

### Latihan 1: Log File Analyzer

```python
import re
from datetime import datetime
from collections import defaultdict

class LogAnalyzer:
    """Analyze log files"""
    
    def __init__(self, log_file):
        self.log_file = log_file
        self.errors = []
        self.warnings = []
        self.stats = defaultdict(int)
    
    def analyze(self):
        """Analyze log file"""
        try:
            with open(self.log_file, 'r') as file:
                for line_num, line in enumerate(file, 1):
                    try:
                        self._process_line(line, line_num)
                    except Exception as e:
                        print(f"Error processing line {line_num}: {e}")
        
        except FileNotFoundError:
            raise FileNotFoundError(f"Log file not found: {self.log_file}")
        except PermissionError:
            raise PermissionError(f"No permission to read: {self.log_file}")
    
    def _process_line(self, line, line_num):
        """Process single log line"""
        if 'ERROR' in line:
            self.errors.append((line_num, line.strip()))
            self.stats['errors'] += 1
        elif 'WARNING' in line:
            self.warnings.append((line_num, line.strip()))
            self.stats['warnings'] += 1
        else:
            self.stats['info'] += 1
    
    def generate_report(self, output_file):
        """Generate analysis report"""
        with open(output_file, 'w') as file:
            file.write("=== Log Analysis Report ===\n\n")
            file.write(f"Total Errors: {self.stats['errors']}\n")
            file.write(f"Total Warnings: {self.stats['warnings']}\n")
            file.write(f"Total Info: {self.stats['info']}\n\n")
            
            if self.errors:
                file.write("=== Errors ===\n")
                for line_num, error in self.errors:
                    file.write(f"Line {line_num}: {error}\n")

# Usage
analyzer = LogAnalyzer('application.log')
try:
    analyzer.analyze()
    analyzer.generate_report('analysis_report.txt')
except Exception as e:
    print(f"Analysis failed: {e}")
```

### Latihan 2: Configuration File Manager

```python
import json
from pathlib import Path

class ConfigError(Exception):
    """Base exception for configuration errors"""
    pass

class ConfigNotFoundError(ConfigError):
    """Raised when config file not found"""
    pass

class ConfigValidationError(ConfigError):
    """Raised when config validation fails"""
    pass

class ConfigManager:
    """Manage application configuration"""
    
    DEFAULT_CONFIG = {
        'app_name': 'MyApp',
        'version': '1.0.0',
        'debug': False,
        'database': {
            'host': 'localhost',
            'port': 5432
        }
    }
    
    def __init__(self, config_file='config.json'):
        self.config_file = Path(config_file)
        self.config = {}
    
    def load(self):
        """Load configuration from file"""
        try:
            if not self.config_file.exists():
                raise ConfigNotFoundError(
                    f"Config file not found: {self.config_file}"
                )
            
            with open(self.config_file, 'r') as file:
                self.config = json.load(file)
            
            self._validate()
            
        except json.JSONDecodeError as e:
            raise ConfigError(f"Invalid JSON in config file: {e}")
    
    def _validate(self):
        """Validate configuration"""
        required_keys = ['app_name', 'version']
        
        for key in required_keys:
            if key not in self.config:
                raise ConfigValidationError(
                    f"Missing required config key: {key}"
                )
    
    def save(self):
        """Save configuration to file"""
        try:
            with open(self.config_file, 'w') as file:
                json.dump(self.config, file, indent=4)
        except PermissionError:
            raise ConfigError(
                f"No permission to write config file: {self.config_file}"
            )
    
    def get(self, key, default=None):
        """Get configuration value"""
        keys = key.split('.')
        value = self.config
        
        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default
        
        return value
    
    def set(self, key, value):
        """Set configuration value"""
        keys = key.split('.')
        config = self.config
        
        for k in keys[:-1]:
            if k not in config:
                config[k] = {}
            config = config[k]
        
        config[keys[-1]] = value
    
    def create_default(self):
        """Create default configuration file"""
        self.config = self.DEFAULT_CONFIG.copy()
        self.save()

# Usage
config = ConfigManager('app_config.json')

try:
    config.load()
except ConfigNotFoundError:
    print("Config not found, creating default...")
    config.create_default()
except ConfigError as e:
    print(f"Configuration error: {e}")
else:
    print(f"App: {config.get('app_name')}")
    print(f"DB Host: {config.get('database.host')}")
```

### Latihan 3: CSV Data Processor

```python
import csv
from pathlib import Path
from typing import List, Dict

class CSVProcessor:
    """Process CSV data files"""
    
    def __init__(self, input_file, output_file=None):
        self.input_file = Path(input_file)
        self.output_file = Path(output_file) if output_file else None
        self.data = []
        self.errors = []
    
    def read(self, skip_errors=True):
        """Read CSV file"""
        if not self.input_file.exists():
            raise FileNotFoundError(f"File not found: {self.input_file}")
        
        with open(self.input_file, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            
            for line_num, row in enumerate(reader, start=2):
                try:
                    validated_row = self._validate_row(row)
                    self.data.append(validated_row)
                except ValueError as e:
                    error_msg = f"Line {line_num}: {e}"
                    self.errors.append(error_msg)
                    
                    if not skip_errors:
                        raise ValueError(error_msg)
        
        return self.data
    
    def _validate_row(self, row):
        """Validate and transform row data"""
        # Example: validate and convert types
        validated = {}
        
        if 'age' in row:
            try:
                validated['age'] = int(row['age'])
                if validated['age'] < 0 or validated['age'] > 150:
                    raise ValueError("Invalid age")
            except ValueError:
                raise ValueError(f"Invalid age: {row['age']}")
        
        # Copy other fields
        for key, value in row.items():
            if key not in validated:
                validated[key] = value
        
        return validated
    
    def filter(self, condition):
        """Filter data based on condition"""
        self.data = [row for row in self.data if condition(row)]
        return self
    
    def transform(self, transformer):
        """Transform data"""
        self.data = [transformer(row) for row in self.data]
        return self
    
    def write(self, output_file=None):
        """Write data to CSV"""
        output = Path(output_file) if output_file else self.output_file
        
        if not output:
            raise ValueError("No output file specified")
        
        if not self.data:
            raise ValueError("No data to write")
        
        with open(output, 'w', newline='', encoding='utf-8') as file:
            fieldnames = self.data[0].keys()
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.data)
    
    def get_errors(self):
        """Get list of errors"""
        return self.errors

# Usage
processor = CSVProcessor('students.csv', 'processed_students.csv')

try:
    # Read data
    data = processor.read(skip_errors=True)
    
    # Filter students with score >= 80
    processor.filter(lambda row: int(row.get('score', 0)) >= 80)
    
    # Add grade column
    def add_grade(row):
        score = int(row['score'])
        if score >= 90:
            row['grade'] = 'A'
        elif score >= 80:
            row['grade'] = 'B'
        else:
            row['grade'] = 'C'
        return row
    
    processor.transform(add_grade)
    
    # Write result
    processor.write()
    
    # Report errors
    if processor.get_errors():
        print("Errors encountered:")
        for error in processor.get_errors():
            print(f"  {error}")

except Exception as e:
    print(f"Processing failed: {e}")
```

## 💡 Best Practices

### 1. Always Use Context Managers for Files
```python
# BAD
file = open('file.txt', 'r')
content = file.read()
file.close()  # Might not execute if exception occurs

# GOOD
with open('file.txt', 'r') as file:
    content = file.read()
# File automatically closed
```

### 2. Specific Exception Handling
```python
# BAD
try:
    # code
    pass
except:  # Too broad!
    pass

# GOOD
try:
    # code
    pass
except (ValueError, TypeError) as e:
    # Handle specific exceptions
    logging.error(f"Validation error: {e}")
except Exception as e:
    # Catch unexpected errors
    logging.error(f"Unexpected error: {e}")
    raise
```

### 3. Use pathlib for Path Operations
```python
# OLD way
import os
path = os.path.join('folder', 'file.txt')

# MODERN way
from pathlib import Path
path = Path('folder') / 'file.txt'
```

### 4. Validate Before Processing
```python
def process_file(filename):
    path = Path(filename)
    
    # Validate first
    if not path.exists():
        raise FileNotFoundError(f"File not found: {filename}")
    
    if not path.is_file():
        raise ValueError(f"Not a file: {filename}")
    
    if path.stat().st_size == 0:
        raise ValueError(f"File is empty: {filename}")
    
    # Then process
    with open(path, 'r') as file:
        return file.read()
```

## 🎓 Latihan Mandiri

1. **File Backup System**: Buat sistem backup file dengan:
   - Copy files dengan progress tracking
   - Handle large files efficiently
   - Verify copied files (checksum)
   - Exception handling untuk disk space, permissions

2. **Data Migration Tool**: Buat tool untuk:
   - Read dari CSV/JSON/XML
   - Transform data
   - Write ke different format
   - Error logging dan recovery

3. **Configuration Merger**: Tool untuk:
   - Read multiple config files
   - Merge configurations dengan priority
   - Validate merged config
   - Write back dengan backup

4. **Log Rotation**: Implementasi:
   - Automatic log file rotation
   - Compression of old logs
   - Cleanup of very old logs
   - Thread-safe logging

## 📚 Referensi Tambahan

- [Python File I/O](https://docs.python.org/3/tutorial/inputoutput.html)
- [Python Exceptions](https://docs.python.org/3/tutorial/errors.html)
- [pathlib Documentation](https://docs.python.org/3/library/pathlib.html)
- [Context Managers](https://docs.python.org/3/reference/datamodel.html#context-managers)

## 🚀 Next Steps

Setelah menguasai File I/O dan Exception Handling, lanjutkan ke:
- **Modul 9**: Decorators & Context Managers (Advanced)
- **Modul 10**: Generators & Iterators
- **Modul 11**: Asynchronous Programming

---

**💪 Tip Expert:** Always assume files can fail. Good error handling is what separates hobbyist code from production code!
