# Modul 10: Generators & Iterators ⚡

## 📚 Pendahuluan

**Generators** dan **Iterators** adalah fitur Python yang powerful untuk bekerja dengan sequence data secara efisien. Mereka memungkinkan lazy evaluation, menghemat memory, dan membuat kode lebih elegant.

## 🎯 Tujuan Pembelajaran

Setelah mempelajari modul ini, Anda akan mampu:
1. Memahami konsep iteration protocol
2. Membuat custom iterators
3. Menggunakan generator functions dengan yield
4. Memahami generator expressions
5. Bekerja dengan itertools module
6. Implementasi infinite sequences
7. Chain dan compose generators
8. Menggunakan generators untuk pipeline data

## 📖 Materi

### 1. Iteration Protocol

```python
# Iterable vs Iterator
# Iterable: object yang bisa di-loop (has __iter__)
# Iterator: object yang tracks iteration state (has __next__)

# List adalah iterable
numbers = [1, 2, 3, 4, 5]

# Get iterator from iterable
iterator = iter(numbers)

# Manually iterate
print(next(iterator))  # 1
print(next(iterator))  # 2
print(next(iterator))  # 3

# For loop menggunakan iteration protocol
for num in numbers:
    print(num)

# Equivalent to:
iterator = iter(numbers)
while True:
    try:
        num = next(iterator)
        print(num)
    except StopIteration:
        break
```

### 2. Custom Iterators

```python
class CountDown:
    """Iterator that counts down from start to 0"""
    
    def __init__(self, start):
        self.current = start
    
    def __iter__(self):
        # Return iterator object (self)
        return self
    
    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        
        self.current -= 1
        return self.current + 1

# Usage
countdown = CountDown(5)
for num in countdown:
    print(num)  # 5, 4, 3, 2, 1

# Range-like iterator
class MyRange:
    """Custom range implementation"""
    
    def __init__(self, start, stop=None, step=1):
        if stop is None:
            self.start = 0
            self.stop = start
        else:
            self.start = start
            self.stop = stop
        
        self.step = step
        self.current = self.start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if (self.step > 0 and self.current >= self.stop) or \
           (self.step < 0 and self.current <= self.stop):
            raise StopIteration
        
        value = self.current
        self.current += self.step
        return value

# Usage
for i in MyRange(5):
    print(i)  # 0, 1, 2, 3, 4

for i in MyRange(1, 10, 2):
    print(i)  # 1, 3, 5, 7, 9
```

### 3. Generator Functions

```python
# Generator function dengan yield
def simple_generator():
    """Simple generator example"""
    yield 1
    yield 2
    yield 3

# Usage
gen = simple_generator()
print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3
# next(gen)  # Raises StopIteration

# Generator yang lebih complex
def countdown(n):
    """Generator that counts down"""
    while n > 0:
        yield n
        n -= 1

for i in countdown(5):
    print(i)

# Generator dengan state
def fibonacci():
    """Infinite Fibonacci sequence generator"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Get first 10 Fibonacci numbers
fib = fibonacci()
for _ in range(10):
    print(next(fib))

# Generator dengan input
def echo_generator():
    """Generator that echoes sent values"""
    while True:
        value = yield
        if value is not None:
            print(f"Received: {value}")

gen = echo_generator()
next(gen)  # Prime the generator
gen.send("Hello")
gen.send("World")

# Generator dengan return value
def generator_with_return():
    yield 1
    yield 2
    return "Done"

gen = generator_with_return()
print(next(gen))  # 1
print(next(gen))  # 2
try:
    next(gen)
except StopIteration as e:
    print(e.value)  # "Done"
```

### 4. Generator Expressions

```python
# List comprehension vs Generator expression
# List comprehension (eager - creates list immediately)
squares_list = [x**2 for x in range(1000000)]

# Generator expression (lazy - creates values on demand)
squares_gen = (x**2 for x in range(1000000))

# Memory efficient
import sys
print(sys.getsizeof(squares_list))  # ~8MB
print(sys.getsizeof(squares_gen))   # ~200 bytes

# Using generator expression
for square in (x**2 for x in range(10)):
    print(square)

# Generator expression in function calls
total = sum(x**2 for x in range(100))

# Chain generator expressions
numbers = range(100)
evens = (x for x in numbers if x % 2 == 0)
squared_evens = (x**2 for x in evens)
print(list(squared_evens))
```

### 5. Advanced Generator Patterns

```python
# Reading large files
def read_large_file(file_path):
    """Generator for reading large files line by line"""
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()

# Processing in chunks
def chunk_iterator(iterable, chunk_size):
    """Split iterable into chunks"""
    chunk = []
    for item in iterable:
        chunk.append(item)
        if len(chunk) == chunk_size:
            yield chunk
            chunk = []
    
    if chunk:  # Yield remaining items
        yield chunk

# Usage
for chunk in chunk_iterator(range(10), 3):
    print(chunk)
# Output: [0, 1, 2], [3, 4, 5], [6, 7, 8], [9]

# Pipeline pattern
def read_file(filename):
    with open(filename) as f:
        for line in f:
            yield line

def filter_lines(lines, keyword):
    for line in lines:
        if keyword in line:
            yield line

def process_line(lines):
    for line in lines:
        yield line.upper().strip()

# Compose pipeline
lines = read_file('data.txt')
filtered = filter_lines(lines, 'ERROR')
processed = process_line(filtered)

for line in processed:
    print(line)

# Tree traversal
def traverse_tree(node):
    """Generator for tree traversal"""
    yield node
    if hasattr(node, 'children'):
        for child in node.children:
            yield from traverse_tree(child)

# Flatten nested structure
def flatten(nested_list):
    """Flatten nested lists"""
    for item in nested_list:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item

# Usage
nested = [1, [2, 3, [4, 5]], 6, [7, [8, 9]]]
flat = list(flatten(nested))
print(flat)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### 6. itertools Module

```python
import itertools

# Infinite iterators
# count(start, step) - infinite counter
counter = itertools.count(10, 2)
print(list(itertools.islice(counter, 5)))  # [10, 12, 14, 16, 18]

# cycle(iterable) - cycle through iterable infinitely
colors = itertools.cycle(['red', 'green', 'blue'])
print(list(itertools.islice(colors, 7)))

# repeat(value, times) - repeat value
repeated = itertools.repeat('A', 5)
print(list(repeated))  # ['A', 'A', 'A', 'A', 'A']

# Combinatoric iterators
# product - Cartesian product
for item in itertools.product([1, 2], ['a', 'b']):
    print(item)
# (1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')

# permutations - All permutations
for perm in itertools.permutations([1, 2, 3], 2):
    print(perm)
# (1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)

# combinations - Combinations without replacement
for comb in itertools.combinations([1, 2, 3, 4], 2):
    print(comb)
# (1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)

# combinations_with_replacement
for comb in itertools.combinations_with_replacement([1, 2, 3], 2):
    print(comb)

# Terminating iterators
# chain - Chain multiple iterables
chained = itertools.chain([1, 2], [3, 4], [5, 6])
print(list(chained))  # [1, 2, 3, 4, 5, 6]

# compress - Filter based on selectors
data = ['A', 'B', 'C', 'D', 'E']
selectors = [1, 0, 1, 0, 1]
result = itertools.compress(data, selectors)
print(list(result))  # ['A', 'C', 'E']

# dropwhile - Drop while predicate is true
numbers = [1, 3, 5, 2, 4, 6, 8]
result = itertools.dropwhile(lambda x: x < 5, numbers)
print(list(result))  # [5, 2, 4, 6, 8]

# takewhile - Take while predicate is true
result = itertools.takewhile(lambda x: x < 5, numbers)
print(list(result))  # [1, 3]

# groupby - Group consecutive items
data = [('A', 1), ('A', 2), ('B', 3), ('B', 4), ('C', 5)]
for key, group in itertools.groupby(data, lambda x: x[0]):
    print(f"{key}: {list(group)}")

# accumulate - Running totals
numbers = [1, 2, 3, 4, 5]
running_sum = itertools.accumulate(numbers)
print(list(running_sum))  # [1, 3, 6, 10, 15]

# accumulate with custom function
running_product = itertools.accumulate(numbers, lambda x, y: x * y)
print(list(running_product))  # [1, 2, 6, 24, 120]

# zip_longest - Zip iterables of different lengths
a = [1, 2, 3]
b = ['a', 'b']
result = itertools.zip_longest(a, b, fillvalue='?')
print(list(result))  # [(1, 'a'), (2, 'b'), (3, '?')]
```

### 7. Practical Generator Examples

```python
# CSV Reader Generator
def csv_reader(filename):
    """Generator for reading CSV files"""
    with open(filename, 'r') as file:
        # Skip header
        header = next(file).strip().split(',')
        
        for line in file:
            values = line.strip().split(',')
            yield dict(zip(header, values))

# Log Parser
def parse_logs(log_file, log_level='ERROR'):
    """Parse log file for specific level"""
    with open(log_file, 'r') as file:
        for line in file:
            if log_level in line:
                yield {
                    'timestamp': line.split()[0],
                    'level': log_level,
                    'message': line.split(log_level, 1)[1].strip()
                }

# Moving Average
def moving_average(data, window_size):
    """Calculate moving average"""
    window = []
    for value in data:
        window.append(value)
        if len(window) > window_size:
            window.pop(0)
        yield sum(window) / len(window)

# Usage
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for avg in moving_average(data, 3):
    print(f"{avg:.2f}")

# Pagination Generator
def paginate(items, page_size):
    """Paginate items"""
    for i in range(0, len(items), page_size):
        yield items[i:i + page_size]

# Usage
items = list(range(100))
for page_num, page in enumerate(paginate(items, 10), 1):
    print(f"Page {page_num}: {page}")

# Event Stream Processor
def process_events(events):
    """Process stream of events"""
    for event in events:
        # Transform event
        processed = {
            'type': event['type'],
            'timestamp': event['timestamp'],
            'processed': True
        }
        yield processed

# Infinite Sequence Generators
def fibonacci_generator():
    """Infinite Fibonacci sequence"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def prime_generator():
    """Infinite prime number generator"""
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1

# Get first 20 primes
primes = prime_generator()
print(list(itertools.islice(primes, 20)))
```

### 8. Generator Performance

```python
import time
import sys

# Memory comparison
def list_approach(n):
    """List-based approach"""
    return [i**2 for i in range(n)]

def generator_approach(n):
    """Generator-based approach"""
    return (i**2 for i in range(n))

# Compare memory usage
n = 1000000
list_result = list_approach(n)
gen_result = generator_approach(n)

print(f"List size: {sys.getsizeof(list_result)} bytes")
print(f"Generator size: {sys.getsizeof(gen_result)} bytes")

# Performance for large datasets
def process_large_file_list(filename):
    """Process file - list approach"""
    with open(filename, 'r') as f:
        lines = f.readlines()  # Load all into memory
    
    results = []
    for line in lines:
        if 'ERROR' in line:
            results.append(line.strip())
    return results

def process_large_file_generator(filename):
    """Process file - generator approach"""
    with open(filename, 'r') as f:
        for line in f:  # Process one line at a time
            if 'ERROR' in line:
                yield line.strip()

# Lazy evaluation example
def expensive_operation(x):
    print(f"Processing {x}")
    time.sleep(0.1)
    return x ** 2

# Generator - only computes when needed
gen = (expensive_operation(x) for x in range(10))
print("Generator created (nothing computed yet)")
print(next(gen))  # Only computes first value
print(next(gen))  # Only computes second value
```

## 🏋️ Latihan Praktik

### Latihan 1: Data Pipeline

```python
def read_csv(filename):
    """Read CSV file"""
    with open(filename, 'r') as f:
        header = next(f).strip().split(',')
        for line in f:
            values = line.strip().split(',')
            yield dict(zip(header, values))

def filter_records(records, condition):
    """Filter records based on condition"""
    for record in records:
        if condition(record):
            yield record

def transform_record(records, transformer):
    """Transform each record"""
    for record in records:
        yield transformer(record)

def aggregate(records, key, aggregator):
    """Aggregate records by key"""
    groups = {}
    for record in records:
        group_key = key(record)
        if group_key not in groups:
            groups[group_key] = []
        groups[group_key].append(record)
    
    for group_key, group_records in groups.items():
        yield group_key, aggregator(group_records)

# Build pipeline
pipeline = read_csv('sales.csv')
pipeline = filter_records(pipeline, lambda r: int(r['amount']) > 1000)
pipeline = transform_record(pipeline, lambda r: {**r, 'tax': int(r['amount']) * 0.1})
results = aggregate(
    pipeline,
    key=lambda r: r['category'],
    aggregator=lambda records: sum(int(r['amount']) for r in records)
)

for category, total in results:
    print(f"{category}: {total}")
```

### Latihan 2: Infinite Sequence

```python
def collatz_sequence(n):
    """Generate Collatz sequence"""
    while n != 1:
        yield n
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    yield 1

# Print Collatz sequence for 10
for num in collatz_sequence(10):
    print(num)

def geometric_sequence(start, ratio):
    """Infinite geometric sequence"""
    value = start
    while True:
        yield value
        value *= ratio

# Get first 10 terms
geo = geometric_sequence(2, 3)
print(list(itertools.islice(geo, 10)))
```

### Latihan 3: Custom Iterator

```python
class DateRange:
    """Iterator for date ranges"""
    
    def __init__(self, start_date, end_date):
        from datetime import datetime, timedelta
        self.start = datetime.strptime(start_date, '%Y-%m-%d')
        self.end = datetime.strptime(end_date, '%Y-%m-%d')
        self.current = self.start
        self.delta = timedelta(days=1)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        
        result = self.current
        self.current += self.delta
        return result.strftime('%Y-%m-%d')

# Usage
for date in DateRange('2024-01-01', '2024-01-10'):
    print(date)
```

## 💡 Best Practices

1. **Use generators for large datasets**: Save memory
2. **Generator expressions for simple cases**: More readable
3. **Generators for pipelines**: Compose operations
4. **itertools for common patterns**: Don't reinvent the wheel
5. **Document generator behavior**: Infinite? One-time use?
6. **Handle StopIteration properly**: In custom iterators

## 🎓 Latihan Mandiri

1. **Stream Processor**: Process infinite event stream
2. **Graph Traversal**: DFS/BFS with generators
3. **Text Search**: Search in large files efficiently
4. **Data Sampling**: Random sampling from large datasets
5. **Time Series**: Generate time-based sequences

## 📚 Referensi Tambahan

- [PEP 255 - Simple Generators](https://www.python.org/dev/peps/pep-0255/)
- [Itertools Documentation](https://docs.python.org/3/library/itertools.html)
- [Generator Tricks for Systems Programmers](http://www.dabeaz.com/generators/)

---

**💪 Tip Expert:** Think lazy! Generators let you work with infinite sequences and huge datasets without running out of memory!
