# Modul 6: Functions & Modules (Expert Level) 🚀

## 📚 Pendahuluan

Modul ini membahas konsep **advanced functions** dan **modules** dalam Python. Anda akan mempelajari teknik-teknik expert level seperti lambda functions, higher-order functions, closures, decorators dasar, dan cara mengorganisir kode dalam modules dan packages.

## 🎯 Tujuan Pembelajaran

Setelah mempelajari modul ini, Anda akan mampu:
1. Membuat dan menggunakan lambda functions
2. Memahami dan mengimplementasikan higher-order functions
3. Menggunakan built-in functions seperti map(), filter(), reduce()
4. Memahami konsep closures dan variable scope
5. Membuat decorators sederhana
6. Mengorganisir kode dalam modules dan packages
7. Menggunakan *args dan **kwargs
8. Membuat recursive functions yang efisien

## 📖 Materi

### 1. Lambda Functions (Anonymous Functions)

Lambda adalah fungsi anonim yang ditulis dalam satu baris.

```python
# Syntax: lambda arguments: expression

# Function biasa
def tambah(x, y):
    return x + y

# Lambda equivalent
tambah_lambda = lambda x, y: x + y

print(tambah_lambda(5, 3))  # Output: 8

# Lambda untuk sorting
students = [
    {"name": "Budi", "score": 85},
    {"name": "Ani", "score": 92},
    {"name": "Citra", "score": 78}
]

# Sort berdasarkan score
sorted_students = sorted(students, key=lambda x: x["score"], reverse=True)
print(sorted_students)
```

**Kapan menggunakan Lambda:**
- Untuk fungsi sederhana yang hanya digunakan sekali
- Sebagai argument untuk higher-order functions
- Untuk operasi singkat dan jelas

### 2. Higher-Order Functions

Functions yang menerima fungsi sebagai argument atau mengembalikan fungsi.

```python
# Function sebagai argument
def apply_operation(x, y, operation):
    return operation(x, y)

result = apply_operation(5, 3, lambda x, y: x * y)
print(result)  # Output: 15

# Function yang mengembalikan function
def create_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

times_3 = create_multiplier(3)
times_5 = create_multiplier(5)

print(times_3(10))  # Output: 30
print(times_5(10))  # Output: 50
```

### 3. Built-in Higher-Order Functions

#### a) map() - Menerapkan fungsi ke setiap item

```python
numbers = [1, 2, 3, 4, 5]

# Menggunakan map dengan lambda
squared = list(map(lambda x: x**2, numbers))
print(squared)  # Output: [1, 4, 9, 16, 25]

# Map dengan multiple iterables
list1 = [1, 2, 3]
list2 = [10, 20, 30]
result = list(map(lambda x, y: x + y, list1, list2))
print(result)  # Output: [11, 22, 33]
```

#### b) filter() - Menyaring elemen berdasarkan kondisi

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter bilangan genap
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6, 8, 10]

# Filter dengan kondisi kompleks
students = [
    {"name": "Budi", "score": 85},
    {"name": "Ani", "score": 92},
    {"name": "Citra", "score": 78},
    {"name": "Doni", "score": 65}
]

passed = list(filter(lambda s: s["score"] >= 80, students))
print(passed)
```

#### c) reduce() - Menggabungkan elemen menjadi satu nilai

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Hitung total
total = reduce(lambda x, y: x + y, numbers)
print(total)  # Output: 15

# Cari nilai maksimum
maximum = reduce(lambda x, y: x if x > y else y, numbers)
print(maximum)  # Output: 5

# Kalikan semua elemen
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 120
```

### 4. Closures

Closure adalah fungsi yang mengingat variabel dari outer scope-nya.

```python
def outer_function(message):
    # outer_function's variable
    
    def inner_function():
        # inner function mengakses variable dari outer function
        print(message)
    
    return inner_function

# Create closure
my_func = outer_function("Hello from closure!")
my_func()  # Output: Hello from closure!

# Contoh praktis: Counter
def create_counter():
    count = 0
    
    def increment():
        nonlocal count  # Mengubah variable dari outer scope
        count += 1
        return count
    
    return increment

counter1 = create_counter()
counter2 = create_counter()

print(counter1())  # Output: 1
print(counter1())  # Output: 2
print(counter2())  # Output: 1 (counter terpisah)
```

### 5. Decorators Dasar

Decorator adalah fungsi yang memodifikasi fungsi lain.

```python
# Decorator sederhana
def my_decorator(func):
    def wrapper():
        print("Sebelum fungsi dijalankan")
        func()
        print("Setelah fungsi dijalankan")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# Output:
# Sebelum fungsi dijalankan
# Hello!
# Setelah fungsi dijalankan

# Decorator dengan arguments
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")

greet("Budi")
# Output:
# Hello, Budi!
# Hello, Budi!
# Hello, Budi!

# Decorator untuk timing
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
    return "Done"

slow_function()
```

### 6. *args dan **kwargs

```python
# *args - Variable positional arguments
def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total

print(sum_all(1, 2, 3))  # Output: 6
print(sum_all(1, 2, 3, 4, 5))  # Output: 15

# **kwargs - Variable keyword arguments
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Budi", age=20, city="Jakarta")

# Kombinasi semua
def complex_function(a, b, *args, **kwargs):
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")

complex_function(1, 2, 3, 4, 5, name="Budi", age=20)
```

### 7. Recursive Functions

```python
# Faktorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # Output: 120

# Fibonacci
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Fibonacci dengan memoization (lebih efisien)
def fibonacci_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]

print([fibonacci_memo(i) for i in range(10)])
# Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# Binary Search (recursive)
def binary_search(arr, target, left, right):
    if left > right:
        return -1
    
    mid = (left + right) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, left, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, right)

numbers = [1, 3, 5, 7, 9, 11, 13, 15]
print(binary_search(numbers, 7, 0, len(numbers) - 1))  # Output: 3
```

### 8. Modules dan Packages

#### Membuat Module

```python
# File: math_operations.py
"""
Module untuk operasi matematika
"""

def add(a, b):
    """Menambahkan dua angka"""
    return a + b

def subtract(a, b):
    """Mengurangi dua angka"""
    return a - b

def multiply(a, b):
    """Mengalikan dua angka"""
    return a * b

def divide(a, b):
    """Membagi dua angka"""
    if b == 0:
        raise ValueError("Tidak bisa membagi dengan nol")
    return a / b

PI = 3.14159

class Calculator:
    """Class untuk kalkulator sederhana"""
    
    def __init__(self):
        self.result = 0
    
    def add(self, value):
        self.result += value
        return self.result
```

#### Menggunakan Module

```python
# Import seluruh module
import math_operations

result = math_operations.add(5, 3)
print(result)

# Import specific functions
from math_operations import add, multiply

result = add(5, 3)
print(result)

# Import dengan alias
from math_operations import Calculator as Calc

calc = Calc()
calc.add(10)

# Import semua (not recommended)
from math_operations import *
```

#### Membuat Package

```
my_package/
    __init__.py
    module1.py
    module2.py
    sub_package/
        __init__.py
        module3.py
```

```python
# File: my_package/__init__.py
"""
My Package - Koleksi modules
"""
from .module1 import function1
from .module2 import function2

__all__ = ['function1', 'function2']
__version__ = '1.0.0'
```

## 🏋️ Latihan Praktik

### Latihan 1: Data Processing Pipeline

Buat pipeline untuk memproses data menggunakan map, filter, dan reduce.

```python
from functools import reduce

# Data: list of transactions
transactions = [
    {"id": 1, "amount": 100, "type": "debit"},
    {"id": 2, "amount": 50, "type": "credit"},
    {"id": 3, "amount": 200, "type": "debit"},
    {"id": 4, "amount": 75, "type": "credit"},
    {"id": 5, "amount": 150, "type": "debit"},
]

# TODO:
# 1. Filter hanya transaksi debit
# 2. Ambil hanya amount-nya
# 3. Kalikan setiap amount dengan 1.1 (pajak 10%)
# 4. Hitung total

# Solusi
debit_transactions = list(filter(lambda t: t["type"] == "debit", transactions))
amounts = list(map(lambda t: t["amount"], debit_transactions))
taxed_amounts = list(map(lambda x: x * 1.1, amounts))
total = reduce(lambda x, y: x + y, taxed_amounts)

print(f"Total debit dengan pajak: {total}")
```

### Latihan 2: Decorator untuk Caching

```python
def cache(func):
    """Decorator untuk caching hasil function"""
    cached_results = {}
    
    def wrapper(*args):
        if args in cached_results:
            print(f"Cache hit untuk {args}")
            return cached_results[args]
        
        print(f"Menghitung untuk {args}")
        result = func(*args)
        cached_results[args] = result
        return result
    
    return wrapper

@cache
def expensive_computation(n):
    """Simulasi komputasi yang mahal"""
    result = 0
    for i in range(n):
        result += i ** 2
    return result

# Test
print(expensive_computation(1000))
print(expensive_computation(1000))  # Akan menggunakan cache
print(expensive_computation(2000))
```

### Latihan 3: Function Factory

```python
def create_validator(validation_type):
    """Factory untuk membuat berbagai validator"""
    
    validators = {
        "email": lambda x: "@" in x and "." in x,
        "phone": lambda x: x.isdigit() and len(x) >= 10,
        "positive": lambda x: x > 0,
        "alphabetic": lambda x: x.isalpha()
    }
    
    def validator(value):
        if validation_type not in validators:
            raise ValueError(f"Unknown validation type: {validation_type}")
        return validators[validation_type](value)
    
    return validator

# Buat validators
email_validator = create_validator("email")
phone_validator = create_validator("phone")

print(email_validator("user@example.com"))  # True
print(email_validator("invalid-email"))     # False
print(phone_validator("08123456789"))       # True
```

### Latihan 4: Recursive Directory Tree

```python
def print_tree(directory, prefix="", is_last=True):
    """Print directory tree structure (simulasi)"""
    
    # Simulasi dengan nested dict
    tree = {
        "project": {
            "src": {
                "main.py": None,
                "utils.py": None
            },
            "tests": {
                "test_main.py": None
            },
            "README.md": None
        }
    }
    
    def print_tree_recursive(node, prefix="", is_last=True):
        if isinstance(node, dict):
            items = list(node.items())
            for i, (name, value) in enumerate(items):
                is_last_item = i == len(items) - 1
                connector = "└── " if is_last_item else "├── "
                print(prefix + connector + name)
                
                if value is not None:
                    extension = "    " if is_last_item else "│   "
                    print_tree_recursive(value, prefix + extension, is_last_item)
    
    print_tree_recursive(tree)

print_tree("project")
```

### Latihan 5: Advanced Calculator Module

Buat module `advanced_calculator.py` dengan fitur:
- Basic operations (+, -, *, /)
- Scientific operations (power, sqrt, log)
- History tracking
- Chainable operations

```python
# advanced_calculator.py
import math

class AdvancedCalculator:
    def __init__(self):
        self.history = []
        self.current = 0
    
    def _record(self, operation, value, result):
        self.history.append({
            "operation": operation,
            "value": value,
            "result": result
        })
    
    def add(self, value):
        result = self.current + value
        self._record("add", value, result)
        self.current = result
        return self
    
    def subtract(self, value):
        result = self.current - value
        self._record("subtract", value, result)
        self.current = result
        return self
    
    def multiply(self, value):
        result = self.current * value
        self._record("multiply", value, result)
        self.current = result
        return self
    
    def divide(self, value):
        if value == 0:
            raise ValueError("Cannot divide by zero")
        result = self.current / value
        self._record("divide", value, result)
        self.current = result
        return self
    
    def power(self, value):
        result = self.current ** value
        self._record("power", value, result)
        self.current = result
        return self
    
    def sqrt(self):
        result = math.sqrt(self.current)
        self._record("sqrt", None, result)
        self.current = result
        return self
    
    def get_result(self):
        return self.current
    
    def get_history(self):
        return self.history
    
    def clear(self):
        self.current = 0
        self.history = []
        return self

# Usage
calc = AdvancedCalculator()
result = calc.add(10).multiply(5).subtract(20).power(2).get_result()
print(f"Result: {result}")
print(f"History: {calc.get_history()}")
```

## 💡 Best Practices

### 1. Function Design
```python
# BAD: Function yang melakukan terlalu banyak
def process_user(user_data):
    # validate, save, send email, log, etc.
    pass

# GOOD: Single Responsibility
def validate_user(user_data):
    pass

def save_user(user_data):
    pass

def send_welcome_email(user):
    pass
```

### 2. Documentation
```python
def complex_function(arg1, arg2, optional=None):
    """
    Brief description of function.
    
    Args:
        arg1 (int): Description of arg1
        arg2 (str): Description of arg2
        optional (bool, optional): Description. Defaults to None.
    
    Returns:
        dict: Description of return value
    
    Raises:
        ValueError: When arg1 is negative
    
    Example:
        >>> complex_function(5, "test")
        {'result': 'success'}
    """
    pass
```

### 3. Module Organization
```python
# module.py

# 1. Imports (stdlib, third-party, local)
import os
import sys
from typing import List

import requests

from .utils import helper_function

# 2. Constants
DEFAULT_TIMEOUT = 30
MAX_RETRIES = 3

# 3. Classes
class MyClass:
    pass

# 4. Functions
def my_function():
    pass

# 5. Main execution
if __name__ == "__main__":
    # Code yang dijalankan jika file dijalankan langsung
    pass
```

## 🎓 Latihan Mandiri

1. **Banking System**: Buat module untuk sistem banking dengan:
   - Account class
   - Transaction history dengan decorators
   - Interest calculation menggunakan closures
   - Validation menggunakan higher-order functions

2. **Text Analyzer**: Buat text analyzer dengan:
   - Word frequency menggunakan reduce
   - Filter stop words
   - Sentiment analysis dengan lambda
   - Decorator untuk timing dan caching

3. **Custom Iterator**: Buat iterator dan generator untuk:
   - Fibonacci sequence
   - Prime numbers
   - Custom range dengan step dan filter

4. **Plugin System**: Buat simple plugin system menggunakan:
   - Dynamic imports
   - Decorators untuk registration
   - Higher-order functions untuk plugin execution

## 📚 Referensi Tambahan

- [Python Official Docs - Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [Real Python - Decorators](https://realpython.com/primer-on-python-decorators/)
- [Python Functional Programming](https://docs.python.org/3/howto/functional.html)
- [Python Closures](https://realpython.com/inner-functions-what-are-they-good-for/)

## 🚀 Next Steps

Setelah menguasai modul ini, lanjutkan ke:
- **Modul 7**: Object-Oriented Programming (OOP)
- **Modul 8**: File I/O & Exception Handling
- **Modul 9**: Decorators & Context Managers (Advanced)

---

**💪 Tip Expert:** Pahami kapan menggunakan functional programming vs OOP. Keduanya adalah tools yang powerful, dan expert programmer tahu kapan harus menggunakan masing-masing approach!
