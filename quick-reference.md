# Quick Reference Guide

## 🚀 Panduan Cepat Konsep Pemrograman

### 📋 Cheat Sheet Syntax

#### Python
```python
# Variabel
nama = "Ahmad"
umur = 25
tinggi = 175.5
aktif = True

# List
buah = ["apel", "jeruk", "mangga"]
angka = [1, 2, 3, 4, 5]

# Dictionary
mahasiswa = {"nama": "Alice", "umur": 20}

# Conditional
if umur >= 18:
    print("Dewasa")
elif umur >= 13:
    print("Remaja")
else:
    print("Anak-anak")

# Loop
for i in range(5):
    print(i)

for item in buah:
    print(item)

while umur < 30:
    umur += 1

# Function
def sapa(nama):
    return f"Halo, {nama}!"

# Class
class Person:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
```

#### Java
```java
// Variabel
String nama = "Ahmad";
int umur = 25;
double tinggi = 175.5;
boolean aktif = true;

// Array
String[] buah = {"apel", "jeruk", "mangga"};
int[] angka = {1, 2, 3, 4, 5};

// Conditional
if (umur >= 18) {
    System.out.println("Dewasa");
} else if (umur >= 13) {
    System.out.println("Remaja");
} else {
    System.out.println("Anak-anak");
}

// Loop
for (int i = 0; i < 5; i++) {
    System.out.println(i);
}

for (String item : buah) {
    System.out.println(item);
}

// Function
public static String sapa(String nama) {
    return "Halo, " + nama + "!";
}

// Class
class Person {
    private String nama;
    private int umur;
    
    public Person(String nama, int umur) {
        this.nama = nama;
        this.umur = umur;
    }
}
```

### 🔍 Algoritma Umum

#### Binary Search
```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

#### Bubble Sort
```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
```

#### Quick Sort
```python
def quick_sort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi-1)
        quick_sort(arr, pi+1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1
```

### 📊 Kompleksitas Algoritma

| Algoritma | Best | Average | Worst | Space |
|-----------|------|---------|-------|-------|
| **Searching** |
| Linear Search | O(1) | O(n) | O(n) | O(1) |
| Binary Search | O(1) | O(log n) | O(log n) | O(1) |
| **Sorting** |
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) |

### 🛠️ Debugging Tips

#### Common Errors
```python
# Index Error
lst = [1, 2, 3]
# print(lst[5])  # IndexError

# Type Error
# result = "5" + 5  # TypeError

# Name Error
# print(undefined_variable)  # NameError

# Logic Error
for i in range(10):
    if i == 5:
        break  # vs continue
```

#### Debug Techniques
```python
# Print debugging
def debug_function(x):
    print(f"Input: {x}")
    result = x * 2
    print(f"Result: {result}")
    return result

# Assert statements
def divide(a, b):
    assert b != 0, "Division by zero!"
    return a / b

# Try-except
try:
    result = int(input("Enter number: "))
except ValueError:
    print("Invalid input!")
```

### 🎯 Problem Solving Patterns

#### Two Pointers
```python
def two_sum_sorted(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return (left, right)
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return None
```

#### Sliding Window
```python
def max_sum_subarray(arr, k):
    if len(arr) < k:
        return None
    
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i-k] + arr[i]
        max_sum = max(max_sum, window_sum)
    
    return max_sum
```

#### Recursion Pattern
```python
def recursive_function(n):
    # Base case
    if n <= 1:
        return 1
    
    # Recursive case
    return n * recursive_function(n - 1)
```

### 📚 Data Structures Operations

#### List/Array
```python
# Creation
arr = [1, 2, 3]
arr = list(range(10))

# Access
first = arr[0]
last = arr[-1]

# Modification
arr.append(4)        # Add at end
arr.insert(0, 0)     # Add at index
arr.remove(2)        # Remove by value
arr.pop()           # Remove last
arr.pop(0)          # Remove by index

# Searching
index = arr.index(3)  # Find index
exists = 3 in arr     # Check existence
count = arr.count(1)  # Count occurrences

# Sorting
arr.sort()           # In-place sort
sorted_arr = sorted(arr)  # New sorted list
```

#### Dictionary
```python
# Creation
d = {"key": "value"}
d = dict(a=1, b=2)

# Access
value = d["key"]
value = d.get("key", "default")

# Modification
d["new_key"] = "new_value"
d.update({"k1": "v1", "k2": "v2"})
del d["key"]
d.pop("key")

# Iteration
for key in d:
    print(key, d[key])

for key, value in d.items():
    print(key, value)
```

### 🎨 String Operations

```python
s = "Hello World"

# Case conversion
s.upper()      # HELLO WORLD
s.lower()      # hello world
s.title()      # Hello World
s.capitalize() # Hello world

# Searching
s.find("World")     # 6
s.index("World")    # 6 (raises exception if not found)
s.count("l")        # 3
"World" in s        # True

# Splitting/Joining
words = s.split()         # ["Hello", "World"]
s.split("l")             # ["He", "", "o Wor", "d"]
" ".join(["Hello", "World"])  # "Hello World"

# Formatting
name = "Alice"
age = 25
f"My name is {name} and I'm {age}"  # f-string
"My name is {} and I'm {}".format(name, age)
```

### 💡 Best Practices

#### Code Style
```python
# Good variable names
student_count = 25
user_email = "user@example.com"

# Bad variable names
# x = 25
# e = "user@example.com"

# Good function names
def calculate_average(numbers):
    return sum(numbers) / len(numbers)

# Good class names
class StudentManager:
    def __init__(self):
        self.students = []
```

#### Error Handling
```python
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Cannot divide by zero!")
        return None
    except TypeError:
        print("Both arguments must be numbers!")
        return None
```

### 🚨 Common Pitfalls

```python
# Mutable default arguments
def bad_function(lst=[]):  # BAD!
    lst.append(1)
    return lst

def good_function(lst=None):  # GOOD!
    if lst is None:
        lst = []
    lst.append(1)
    return lst

# Modifying list while iterating
lst = [1, 2, 3, 4, 5]
# for item in lst:  # BAD!
#     if item % 2 == 0:
#         lst.remove(item)

# Good approach
lst = [item for item in lst if item % 2 != 0]
```

### 📖 Quick Formulas

```python
# Math operations
import math

# Common calculations
average = sum(numbers) / len(numbers)
factorial = math.factorial(n)
gcd = math.gcd(a, b)
sqrt = math.sqrt(number)
power = base ** exponent
abs_value = abs(number)

# String/List operations
length = len(collection)
maximum = max(collection)
minimum = min(collection)
reversed_list = list(reversed(collection))
```

---

📌 **Bookmark this page** untuk referensi cepat saat coding!

💡 **Pro tip**: Print halaman ini dan letakkan di dekat workspace Anda untuk referensi cepat.