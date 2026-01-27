# Modul 9: Decorators & Context Managers (Advanced) 🎨

## 📚 Pendahuluan

Modul ini membahas **decorators** dan **context managers** secara mendalam - dua fitur powerful Python yang membuat kode lebih clean, reusable, dan maintainable. Decorators mengubah behavior fungsi/class, sementara context managers mengelola resources secara otomatis.

## 🎯 Tujuan Pembelajaran

Setelah mempelajari modul ini, Anda akan mampu:
1. Memahami decorator pattern secara mendalam
2. Membuat function decorators dengan dan tanpa arguments
3. Membuat class decorators
4. Menggunakan functools untuk preserving metadata
5. Implementasi context managers dengan class dan generator
6. Membuat nested dan reusable decorators
7. Menggunakan built-in decorators (@property, @staticmethod, @classmethod)
8. Membuat decorator untuk caching, timing, logging, validation

## 📖 Materi

### 1. Function Decorators Dasar

```python
def my_decorator(func):
    """Basic decorator"""
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

# Equivalent to:
# say_hello = my_decorator(say_hello)

say_hello()
# Output:
# Before function call
# Hello!
# After function call
```

### 2. Decorators dengan Arguments

```python
def decorator_with_args(func):
    """Decorator yang menangani function arguments"""
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@decorator_with_args
def add(a, b):
    return a + b

@decorator_with_args
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

result = add(5, 3)
message = greet("Budi", greeting="Hi")
```

### 3. Decorators dengan Parameters

```python
def repeat(times):
    """Decorator factory - decorator dengan parameter"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            results = []
            for _ in range(times):
                result = func(*args, **kwargs)
                results.append(result)
            return results
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    return f"Hello, {name}!"

messages = greet("Budi")
print(messages)
# Output: ['Hello, Budi!', 'Hello, Budi!', 'Hello, Budi!']

# Variable repetitions
def repeat_n_times(n=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat_n_times(5)
def print_message(msg):
    print(msg)
    return msg
```

### 4. Preserving Metadata dengan functools

```python
from functools import wraps

def my_decorator(func):
    @wraps(func)  # Preserves original function metadata
    def wrapper(*args, **kwargs):
        """Wrapper docstring"""
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def example_function():
    """Example function docstring"""
    pass

print(example_function.__name__)  # example_function (not wrapper)
print(example_function.__doc__)   # Example function docstring
```

### 5. Class-based Decorators

```python
class CountCalls:
    """Decorator that counts function calls"""
    
    def __init__(self, func):
        self.func = func
        self.num_calls = 0
    
    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"Call {self.num_calls} of {self.func.__name__}")
        return self.func(*args, **kwargs)

@CountCalls
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Budi")
say_hello("Ani")
say_hello("Citra")
print(f"Total calls: {say_hello.num_calls}")

# Class decorator with arguments
class Retry:
    """Decorator for retrying failed operations"""
    
    def __init__(self, max_retries=3, delay=1):
        self.max_retries = max_retries
        self.delay = delay
    
    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            import time
            
            for attempt in range(self.max_retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == self.max_retries - 1:
                        raise
                    print(f"Attempt {attempt + 1} failed: {e}")
                    time.sleep(self.delay)
        
        return wrapper

@Retry(max_retries=3, delay=2)
def unreliable_function():
    import random
    if random.random() < 0.7:
        raise Exception("Random failure")
    return "Success!"
```

### 6. Practical Decorators

```python
import time
import functools
from datetime import datetime

# Timer decorator
def timer(func):
    """Measure execution time"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

# Memoization decorator
def memoize(func):
    """Cache function results"""
    cache = {}
    
    @wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    
    return wrapper

@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Debug decorator
def debug(func):
    """Print function signature and return value"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        
        print(f"Calling {func.__name__}({signature})")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result!r}")
        
        return result
    
    return wrapper

@debug
def add(a, b):
    return a + b

# Rate limiting decorator
def rate_limit(max_calls, time_window):
    """Limit function calls within time window"""
    calls = []
    
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            now = time.time()
            
            # Remove old calls outside time window
            calls[:] = [call_time for call_time in calls 
                       if now - call_time < time_window]
            
            if len(calls) >= max_calls:
                raise Exception(
                    f"Rate limit exceeded: {max_calls} calls per {time_window}s"
                )
            
            calls.append(now)
            return func(*args, **kwargs)
        
        return wrapper
    return decorator

@rate_limit(max_calls=3, time_window=10)
def api_call():
    print("API call executed")
    return "Data"

# Validation decorator
def validate_types(**type_checks):
    """Validate function argument types"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Get function signature
            import inspect
            sig = inspect.signature(func)
            bound_args = sig.bind(*args, **kwargs)
            
            # Validate types
            for arg_name, expected_type in type_checks.items():
                if arg_name in bound_args.arguments:
                    value = bound_args.arguments[arg_name]
                    if not isinstance(value, expected_type):
                        raise TypeError(
                            f"{arg_name} must be {expected_type.__name__}, "
                            f"got {type(value).__name__}"
                        )
            
            return func(*args, **kwargs)
        
        return wrapper
    return decorator

@validate_types(name=str, age=int)
def create_user(name, age):
    return {"name": name, "age": age}

# Authentication decorator
def require_auth(func):
    """Require authentication"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Check authentication (simplified)
        if not hasattr(wrapper, 'authenticated') or not wrapper.authenticated:
            raise PermissionError("Authentication required")
        return func(*args, **kwargs)
    
    wrapper.authenticated = False
    return wrapper

@require_auth
def delete_user(user_id):
    return f"User {user_id} deleted"

# Usage
# delete_user(123)  # Raises PermissionError
delete_user.authenticated = True
delete_user(123)  # Works
```

### 7. Stacking Decorators

```python
@timer
@memoize
@debug
def complex_calculation(n):
    """Complex calculation with caching, debugging, and timing"""
    time.sleep(0.1)  # Simulate complex operation
    return n ** 2

# Order matters!
# Equivalent to:
# complex_calculation = timer(memoize(debug(complex_calculation)))

result = complex_calculation(5)
result = complex_calculation(5)  # Should use cache
```

### 8. Class Decorators

```python
def singleton(cls):
    """Decorator to make a class a singleton"""
    instances = {}
    
    @wraps(cls)
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    
    return get_instance

@singleton
class Database:
    def __init__(self):
        print("Creating database connection")
        self.connection = "Connected"

# Test singleton
db1 = Database()
db2 = Database()
print(db1 is db2)  # True

# Add methods to class
def add_logging(cls):
    """Add logging to all methods"""
    class NewClass(cls):
        def __getattribute__(self, name):
            attr = object.__getattribute__(self, name)
            if callable(attr) and not name.startswith('_'):
                def logged_method(*args, **kwargs):
                    print(f"Calling {name}")
                    result = attr(*args, **kwargs)
                    print(f"{name} completed")
                    return result
                return logged_method
            return attr
    
    return NewClass

@add_logging
class Calculator:
    def add(self, a, b):
        return a + b
    
    def multiply(self, a, b):
        return a * b
```

### 9. Context Managers dengan Class

```python
class FileManager:
    """Custom file manager context manager"""
    
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        """Called when entering 'with' block"""
        print(f"Opening {self.filename}")
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Called when exiting 'with' block"""
        print(f"Closing {self.filename}")
        if self.file:
            self.file.close()
        
        # Handle exceptions
        if exc_type is not None:
            print(f"Exception occurred: {exc_type.__name__}: {exc_val}")
        
        # Return False to propagate exception
        # Return True to suppress exception
        return False

# Usage
with FileManager('test.txt', 'w') as f:
    f.write("Hello, World!")

# Database transaction context manager
class Transaction:
    """Database transaction context manager"""
    
    def __init__(self, connection):
        self.connection = connection
    
    def __enter__(self):
        self.connection.begin()
        return self.connection
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            # Success - commit
            self.connection.commit()
        else:
            # Error - rollback
            self.connection.rollback()
        
        return False

# Timer context manager
class Timer:
    """Measure execution time"""
    
    def __enter__(self):
        self.start = time.time()
        return self
    
    def __exit__(self, *args):
        self.end = time.time()
        self.elapsed = self.end - self.start
        print(f"Elapsed time: {self.elapsed:.4f} seconds")

# Usage
with Timer():
    # Code to time
    time.sleep(1)
```

### 10. Context Managers dengan contextlib

```python
from contextlib import contextmanager

@contextmanager
def file_manager(filename, mode):
    """Function-based context manager"""
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
with file_manager('test.txt', 'w') as f:
    f.write("Hello!")

# Temporary directory
import tempfile
import shutil
from pathlib import Path

@contextmanager
def temporary_directory():
    """Create temporary directory"""
    temp_dir = tempfile.mkdtemp()
    try:
        yield Path(temp_dir)
    finally:
        shutil.rmtree(temp_dir)

# Usage
with temporary_directory() as temp_dir:
    # Work with temporary directory
    (temp_dir / 'file.txt').write_text('data')
    print(f"Created temp dir: {temp_dir}")

# Changing directory
@contextmanager
def change_directory(path):
    """Temporarily change working directory"""
    import os
    original_dir = os.getcwd()
    try:
        os.chdir(path)
        yield path
    finally:
        os.chdir(original_dir)

# Suppress exceptions
from contextlib import suppress

with suppress(FileNotFoundError):
    # This won't raise error
    os.remove('nonexistent_file.txt')

# Redirect stdout
from contextlib import redirect_stdout
import io

f = io.StringIO()
with redirect_stdout(f):
    print("This goes to StringIO")
    print("Not to console")

output = f.getvalue()
```

### 11. Advanced Decorator Patterns

```python
# Decorator with optional arguments
def optional_decorator(func=None, *, prefix=">>>"):
    """Decorator that can be used with or without arguments"""
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            print(f"{prefix} {f.__name__}")
            return f(*args, **kwargs)
        return wrapper
    
    if func is None:
        # Called with arguments: @optional_decorator(prefix="###")
        return decorator
    else:
        # Called without arguments: @optional_decorator
        return decorator(func)

@optional_decorator
def func1():
    print("Function 1")

@optional_decorator(prefix="###")
def func2():
    print("Function 2")

# Decorator for methods
def log_method(func):
    """Decorator for class methods"""
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        class_name = self.__class__.__name__
        print(f"{class_name}.{func.__name__} called")
        return func(self, *args, **kwargs)
    return wrapper

class MyClass:
    @log_method
    def method(self):
        print("Method executed")

# Parameterized class decorator
def add_repr(include_attrs=None):
    """Add __repr__ to class"""
    def decorator(cls):
        def __repr__(self):
            attrs = include_attrs or []
            attr_str = ", ".join(
                f"{attr}={getattr(self, attr)!r}"
                for attr in attrs
            )
            return f"{cls.__name__}({attr_str})"
        
        cls.__repr__ = __repr__
        return cls
    
    return decorator

@add_repr(include_attrs=['name', 'age'])
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

## 🏋️ Latihan Praktik

### Latihan 1: Caching System

```python
import time
import functools
from collections import OrderedDict

class LRUCache:
    """LRU (Least Recently Used) Cache decorator"""
    
    def __init__(self, maxsize=128):
        self.maxsize = maxsize
    
    def __call__(self, func):
        cache = OrderedDict()
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Create cache key
            key = (args, tuple(kwargs.items()))
            
            if key in cache:
                # Move to end (most recently used)
                cache.move_to_end(key)
                return cache[key]
            
            # Compute result
            result = func(*args, **kwargs)
            
            # Store in cache
            cache[key] = result
            
            # Remove oldest if cache is full
            if len(cache) > self.maxsize:
                cache.popitem(last=False)
            
            return result
        
        # Add cache info method
        wrapper.cache_info = lambda: {
            'size': len(cache),
            'maxsize': self.maxsize,
            'hits': getattr(wrapper, '_hits', 0),
            'misses': getattr(wrapper, '_misses', 0)
        }
        
        wrapper.cache_clear = lambda: cache.clear()
        
        return wrapper

@LRUCache(maxsize=100)
def expensive_operation(n):
    time.sleep(0.1)
    return n ** 2

# Test
for i in range(5):
    result = expensive_operation(i)

print(expensive_operation.cache_info())
```

### Latihan 2: Resource Manager

```python
from contextlib import contextmanager
import threading

class ResourcePool:
    """Manage a pool of resources"""
    
    def __init__(self, create_resource, max_size=10):
        self.create_resource = create_resource
        self.max_size = max_size
        self.pool = []
        self.in_use = set()
        self.lock = threading.Lock()
    
    @contextmanager
    def acquire(self):
        """Acquire resource from pool"""
        resource = None
        
        with self.lock:
            if self.pool:
                resource = self.pool.pop()
            elif len(self.in_use) < self.max_size:
                resource = self.create_resource()
            else:
                raise Exception("No resources available")
            
            self.in_use.add(resource)
        
        try:
            yield resource
        finally:
            with self.lock:
                self.in_use.remove(resource)
                self.pool.append(resource)

# Usage
def create_connection():
    return {"id": id(object()), "status": "connected"}

pool = ResourcePool(create_connection, max_size=5)

with pool.acquire() as conn:
    print(f"Using connection: {conn}")
```

### Latihan 3: Monitoring Decorator

```python
import functools
import time
from collections import defaultdict
from datetime import datetime

class Monitor:
    """Monitor function calls and performance"""
    
    def __init__(self):
        self.stats = defaultdict(lambda: {
            'calls': 0,
            'total_time': 0,
            'errors': 0,
            'last_called': None
        })
    
    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            func_name = func.__name__
            stats = self.stats[func_name]
            
            stats['calls'] += 1
            stats['last_called'] = datetime.now()
            
            start = time.time()
            try:
                result = func(*args, **kwargs)
                return result
            except Exception as e:
                stats['errors'] += 1
                raise
            finally:
                elapsed = time.time() - start
                stats['total_time'] += elapsed
        
        return wrapper
    
    def report(self):
        """Generate monitoring report"""
        print("=== Function Monitoring Report ===")
        for func_name, stats in self.stats.items():
            avg_time = stats['total_time'] / stats['calls'] if stats['calls'] else 0
            print(f"\n{func_name}:")
            print(f"  Calls: {stats['calls']}")
            print(f"  Errors: {stats['errors']}")
            print(f"  Total Time: {stats['total_time']:.4f}s")
            print(f"  Avg Time: {avg_time:.4f}s")
            print(f"  Last Called: {stats['last_called']}")

# Usage
monitor = Monitor()

@monitor
def process_data(data):
    time.sleep(0.1)
    return len(data)

@monitor
def validate_data(data):
    if not data:
        raise ValueError("Empty data")
    return True

# Test
for i in range(10):
    process_data(f"data_{i}")

try:
    validate_data([])
except ValueError:
    pass

monitor.report()
```

## 💡 Best Practices

1. **Always use @wraps**: Preserve original function metadata
2. **Keep decorators simple**: One responsibility per decorator
3. **Make decorators reusable**: Design for multiple use cases
4. **Document decorators well**: Clear docstrings about behavior
5. **Use context managers for resources**: Automatic cleanup
6. **Chain decorators thoughtfully**: Order matters

## 🎓 Latihan Mandiri

1. **Access Control Decorator**: Implementasi role-based access control
2. **Retry with Backoff**: Exponential backoff untuk retries
3. **Circuit Breaker**: Prevent cascading failures
4. **Request Rate Limiter**: Advanced rate limiting dengan sliding window
5. **Transaction Manager**: Database transaction dengan savepoints

## 📚 Referensi Tambahan

- [PEP 318 - Decorators](https://www.python.org/dev/peps/pep-0318/)
- [Python Decorator Library](https://wiki.python.org/moin/PythonDecoratorLibrary)
- [contextlib Documentation](https://docs.python.org/3/library/contextlib.html)

---

**💪 Tip Expert:** Decorators dan context managers adalah tentang separation of concerns. Extract cross-cutting concerns ke reusable components!
