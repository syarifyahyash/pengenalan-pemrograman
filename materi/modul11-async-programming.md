# Modul 11: Asynchronous Programming (Async/Await) 🚄

## 📚 Pendahuluan

**Asynchronous Programming** memungkinkan program menjalankan multiple tasks secara concurrent tanpa multi-threading. Ini sangat berguna untuk I/O-bound operations seperti network requests, file operations, dan database queries.

## 🎯 Tujuan Pembelajaran

Setelah mempelajari modul ini, Anda akan mampu:
1. Memahami perbedaan sync vs async programming
2. Menggunakan async/await syntax
3. Membuat dan menjalankan coroutines
4. Bekerja dengan asyncio event loop
5. Menangani concurrent tasks
6. Menggunakan async context managers
7. Implementasi async generators
8. Menangani errors dalam async code

## 📖 Materi

### 1. Synchronous vs Asynchronous

```python
import time

# Synchronous approach
def fetch_data_sync(name, delay):
    """Simulate fetching data synchronously"""
    print(f"Fetching {name}...")
    time.sleep(delay)  # Blocking operation
    print(f"{name} completed")
    return f"Data from {name}"

def main_sync():
    start = time.time()
    
    result1 = fetch_data_sync("API 1", 2)
    result2 = fetch_data_sync("API 2", 3)
    result3 = fetch_data_sync("API 3", 1)
    
    end = time.time()
    print(f"Total time: {end - start:.2f}s")  # ~6 seconds

# Asynchronous approach
import asyncio

async def fetch_data_async(name, delay):
    """Simulate fetching data asynchronously"""
    print(f"Fetching {name}...")
    await asyncio.sleep(delay)  # Non-blocking operation
    print(f"{name} completed")
    return f"Data from {name}"

async def main_async():
    start = time.time()
    
    # Run concurrently
    results = await asyncio.gather(
        fetch_data_async("API 1", 2),
        fetch_data_async("API 2", 3),
        fetch_data_async("API 3", 1)
    )
    
    end = time.time()
    print(f"Total time: {end - start:.2f}s")  # ~3 seconds
    return results

# Run async function
# asyncio.run(main_async())
```

### 2. Coroutines Dasar

```python
import asyncio

# Define coroutine dengan async def
async def simple_coroutine():
    """Simple coroutine example"""
    print("Coroutine started")
    await asyncio.sleep(1)
    print("Coroutine finished")
    return "Result"

# Run coroutine
async def main():
    result = await simple_coroutine()
    print(f"Got result: {result}")

# asyncio.run(main())

# Multiple coroutines
async def task1():
    print("Task 1 started")
    await asyncio.sleep(2)
    print("Task 1 completed")
    return "Task 1 result"

async def task2():
    print("Task 2 started")
    await asyncio.sleep(1)
    print("Task 2 completed")
    return "Task 2 result"

async def run_tasks():
    # Sequential execution
    result1 = await task1()
    result2 = await task2()
    # Total time: ~3 seconds
    
    # Concurrent execution
    results = await asyncio.gather(task1(), task2())
    # Total time: ~2 seconds
    
    return results

# Awaitable objects
async def example():
    # await coroutine
    result = await simple_coroutine()
    
    # await Task
    task = asyncio.create_task(simple_coroutine())
    result = await task
    
    # await Future
    loop = asyncio.get_event_loop()
    future = loop.create_future()
    # ... set result later
    # result = await future
```

### 3. Creating and Running Tasks

```python
import asyncio

async def long_task(name, duration):
    """Simulate long-running task"""
    print(f"{name} started")
    await asyncio.sleep(duration)
    print(f"{name} completed")
    return f"{name} result"

async def main():
    # Create tasks
    task1 = asyncio.create_task(long_task("Task 1", 2))
    task2 = asyncio.create_task(long_task("Task 2", 1))
    task3 = asyncio.create_task(long_task("Task 3", 3))
    
    # Tasks start running immediately
    print("All tasks created")
    
    # Wait for all tasks
    results = await asyncio.gather(task1, task2, task3)
    print(f"Results: {results}")

# Run with asyncio.run()
# asyncio.run(main())

# Task with exception handling
async def risky_task():
    await asyncio.sleep(1)
    raise ValueError("Something went wrong")

async def handle_tasks():
    task = asyncio.create_task(risky_task())
    
    try:
        result = await task
    except ValueError as e:
        print(f"Caught error: {e}")

# Cancel tasks
async def cancellable_task():
    try:
        await asyncio.sleep(10)
    except asyncio.CancelledError:
        print("Task was cancelled")
        raise

async def cancel_example():
    task = asyncio.create_task(cancellable_task())
    
    await asyncio.sleep(1)
    task.cancel()
    
    try:
        await task
    except asyncio.CancelledError:
        print("Task cancelled successfully")
```

### 4. Async Context Managers

```python
import asyncio

class AsyncDatabase:
    """Async context manager for database"""
    
    async def __aenter__(self):
        print("Connecting to database...")
        await asyncio.sleep(1)  # Simulate connection
        print("Connected!")
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print("Closing database connection...")
        await asyncio.sleep(0.5)  # Simulate cleanup
        print("Connection closed")
        return False

async def use_database():
    async with AsyncDatabase() as db:
        print("Using database")
        await asyncio.sleep(1)

# asyncio.run(use_database())

# Using contextlib for async context managers
from contextlib import asynccontextmanager

@asynccontextmanager
async def async_file_manager(filename):
    """Async context manager using decorator"""
    print(f"Opening {filename}")
    file = await open_async(filename)  # Hypothetical async file open
    try:
        yield file
    finally:
        print(f"Closing {filename}")
        await close_async(file)  # Hypothetical async file close

# Lock with async context manager
lock = asyncio.Lock()

async def critical_section(worker_id):
    async with lock:
        print(f"Worker {worker_id} acquired lock")
        await asyncio.sleep(1)
        print(f"Worker {worker_id} releasing lock")
```

### 5. Async Iterators and Generators

```python
import asyncio

# Async iterator
class AsyncRange:
    """Async range iterator"""
    
    def __init__(self, start, stop):
        self.current = start
        self.stop = stop
    
    def __aiter__(self):
        return self
    
    async def __anext__(self):
        if self.current >= self.stop:
            raise StopAsyncIteration
        
        await asyncio.sleep(0.1)  # Simulate async operation
        value = self.current
        self.current += 1
        return value

async def use_async_iterator():
    async for i in AsyncRange(0, 5):
        print(i)

# Async generator
async def async_countdown(n):
    """Async generator"""
    while n > 0:
        await asyncio.sleep(0.5)
        yield n
        n -= 1

async def use_async_generator():
    async for num in async_countdown(5):
        print(num)

# Async comprehension
async def async_squares():
    # Async list comprehension
    squares = [i**2 async for i in AsyncRange(0, 10)]
    print(squares)
    
    # Async generator expression
    squares_gen = (i**2 async for i in AsyncRange(0, 10))
    async for square in squares_gen:
        print(square)
```

### 6. Concurrent Operations

```python
import asyncio
import aiohttp  # For async HTTP requests

# asyncio.gather - Run multiple tasks concurrently
async def fetch_user(user_id):
    await asyncio.sleep(1)
    return {"id": user_id, "name": f"User {user_id}"}

async def fetch_all_users():
    # Run concurrently
    users = await asyncio.gather(
        fetch_user(1),
        fetch_user(2),
        fetch_user(3)
    )
    return users

# Handle exceptions with gather
async def might_fail(value):
    await asyncio.sleep(1)
    if value % 2 == 0:
        raise ValueError(f"Value {value} is even")
    return value

async def gather_with_errors():
    try:
        # By default, gather stops on first exception
        results = await asyncio.gather(
            might_fail(1),
            might_fail(2),
            might_fail(3)
        )
    except ValueError as e:
        print(f"Error: {e}")
    
    # Continue on errors
    results = await asyncio.gather(
        might_fail(1),
        might_fail(2),
        might_fail(3),
        return_exceptions=True
    )
    print(results)  # [1, ValueError(...), 3]

# asyncio.wait - More control over completion
async def wait_example():
    tasks = [
        asyncio.create_task(asyncio.sleep(i))
        for i in range(1, 4)
    ]
    
    # Wait for first completion
    done, pending = await asyncio.wait(
        tasks,
        return_when=asyncio.FIRST_COMPLETED
    )
    
    # Cancel pending tasks
    for task in pending:
        task.cancel()

# Timeout
async def with_timeout():
    try:
        result = await asyncio.wait_for(
            long_running_task(),
            timeout=5.0
        )
    except asyncio.TimeoutError:
        print("Operation timed out")

# as_completed - Process results as they complete
async def as_completed_example():
    tasks = [
        fetch_user(i)
        for i in range(1, 6)
    ]
    
    for coro in asyncio.as_completed(tasks):
        user = await coro
        print(f"Got user: {user}")
```

### 7. Async Queue and Synchronization

```python
import asyncio
from asyncio import Queue

# Producer-Consumer pattern
async def producer(queue, n):
    """Produce items"""
    for i in range(n):
        await asyncio.sleep(0.5)
        await queue.put(i)
        print(f"Produced: {i}")
    await queue.put(None)  # Sentinel

async def consumer(queue, name):
    """Consume items"""
    while True:
        item = await queue.get()
        if item is None:
            queue.task_done()
            break
        
        print(f"{name} consuming: {item}")
        await asyncio.sleep(1)
        queue.task_done()

async def producer_consumer():
    queue = Queue()
    
    await asyncio.gather(
        producer(queue, 10),
        consumer(queue, "Consumer 1"),
        consumer(queue, "Consumer 2")
    )

# Semaphore - Limit concurrent operations
async def limited_task(sem, task_id):
    async with sem:
        print(f"Task {task_id} started")
        await asyncio.sleep(1)
        print(f"Task {task_id} completed")

async def semaphore_example():
    # Allow only 3 concurrent tasks
    sem = asyncio.Semaphore(3)
    
    tasks = [
        limited_task(sem, i)
        for i in range(10)
    ]
    
    await asyncio.gather(*tasks)

# Event - Signal between coroutines
async def waiter(event, name):
    print(f"{name} waiting for event")
    await event.wait()
    print(f"{name} received event")

async def setter(event):
    await asyncio.sleep(2)
    print("Setting event")
    event.set()

async def event_example():
    event = asyncio.Event()
    
    await asyncio.gather(
        waiter(event, "Waiter 1"),
        waiter(event, "Waiter 2"),
        setter(event)
    )
```

### 8. Error Handling

```python
import asyncio

async def task_with_error():
    await asyncio.sleep(1)
    raise ValueError("Task failed")

async def error_handling():
    # Try-except
    try:
        await task_with_error()
    except ValueError as e:
        print(f"Caught error: {e}")
    
    # Gather with error handling
    results = await asyncio.gather(
        task1(),
        task_with_error(),
        task2(),
        return_exceptions=True
    )
    
    for i, result in enumerate(results):
        if isinstance(result, Exception):
            print(f"Task {i} failed: {result}")
        else:
            print(f"Task {i} succeeded: {result}")

# Timeout and cancellation
async def robust_operation():
    try:
        async with asyncio.timeout(5):  # Python 3.11+
            result = await slow_operation()
    except asyncio.TimeoutError:
        print("Operation timed out")
    except asyncio.CancelledError:
        print("Operation was cancelled")
        raise  # Re-raise to propagate cancellation
    except Exception as e:
        print(f"Unexpected error: {e}")

# Shield from cancellation
async def critical_task():
    """Task that should not be cancelled"""
    await asyncio.sleep(2)
    return "Critical result"

async def shield_example():
    task = asyncio.create_task(critical_task())
    
    # Shield task from cancellation
    try:
        result = await asyncio.shield(task)
    except asyncio.CancelledError:
        # Task continues running
        result = await task
    
    return result
```

### 9. Real-World Examples

```python
import asyncio
import aiohttp  # pip install aiohttp
from typing import List

# Async HTTP requests
async def fetch_url(session, url):
    """Fetch URL asynchronously"""
    try:
        async with session.get(url, timeout=10) as response:
            return await response.text()
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

async def fetch_multiple_urls(urls: List[str]):
    """Fetch multiple URLs concurrently"""
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
        return results

# Async file operations
async def async_read_file(filename):
    """Read file asynchronously (using executor)"""
    loop = asyncio.get_event_loop()
    with open(filename, 'r') as f:
        return await loop.run_in_executor(None, f.read)

async def async_write_file(filename, content):
    """Write file asynchronously"""
    loop = asyncio.get_event_loop()
    with open(filename, 'w') as f:
        await loop.run_in_executor(None, f.write, content)

# Async database operations (example)
class AsyncDatabase:
    async def connect(self):
        await asyncio.sleep(0.1)
        print("Connected to database")
    
    async def query(self, sql):
        await asyncio.sleep(0.5)
        return [{"id": 1}, {"id": 2}]
    
    async def close(self):
        await asyncio.sleep(0.1)
        print("Database closed")

async def database_operations():
    db = AsyncDatabase()
    await db.connect()
    
    # Run multiple queries concurrently
    results = await asyncio.gather(
        db.query("SELECT * FROM users"),
        db.query("SELECT * FROM posts"),
        db.query("SELECT * FROM comments")
    )
    
    await db.close()
    return results

# Web scraper
async def scrape_website(session, url):
    """Scrape website"""
    html = await fetch_url(session, url)
    if html:
        # Parse HTML (using BeautifulSoup, etc.)
        return f"Data from {url}"
    return None

async def scrape_multiple_sites(urls):
    """Scrape multiple websites concurrently"""
    async with aiohttp.ClientSession() as session:
        # Limit concurrency with semaphore
        sem = asyncio.Semaphore(5)
        
        async def bounded_scrape(url):
            async with sem:
                return await scrape_website(session, url)
        
        tasks = [bounded_scrape(url) for url in urls]
        results = await asyncio.gather(*tasks)
        return results

# Periodic task
async def periodic_task(interval, func, *args):
    """Run function periodically"""
    while True:
        await func(*args)
        await asyncio.sleep(interval)

async def heartbeat():
    print("Heartbeat")

async def run_periodic():
    # Run periodic task in background
    task = asyncio.create_task(periodic_task(5, heartbeat))
    
    # Do other work
    await asyncio.sleep(20)
    
    # Cancel periodic task
    task.cancel()
```

## 🏋️ Latihan Praktik

### Latihan 1: Async Download Manager

```python
import asyncio
import aiohttp

class AsyncDownloadManager:
    """Manage multiple concurrent downloads"""
    
    def __init__(self, max_concurrent=5):
        self.semaphore = asyncio.Semaphore(max_concurrent)
        self.progress = {}
    
    async def download_file(self, url, filename):
        """Download single file"""
        async with self.semaphore:
            async with aiohttp.ClientSession() as session:
                try:
                    async with session.get(url) as response:
                        total = response.content_length
                        downloaded = 0
                        
                        with open(filename, 'wb') as f:
                            async for chunk in response.content.iter_chunked(8192):
                                f.write(chunk)
                                downloaded += len(chunk)
                                self.progress[filename] = (downloaded / total) * 100
                        
                        return filename, True
                
                except Exception as e:
                    print(f"Error downloading {url}: {e}")
                    return filename, False
    
    async def download_multiple(self, downloads):
        """Download multiple files"""
        tasks = [
            self.download_file(url, filename)
            for url, filename in downloads
        ]
        
        results = await asyncio.gather(*tasks)
        return results

# Usage
async def main():
    manager = AsyncDownloadManager(max_concurrent=3)
    
    downloads = [
        ("https://example.com/file1.zip", "file1.zip"),
        ("https://example.com/file2.zip", "file2.zip"),
        ("https://example.com/file3.zip", "file3.zip"),
    ]
    
    results = await manager.download_multiple(downloads)
    print(results)
```

### Latihan 2: Async Task Queue

```python
import asyncio
from asyncio import Queue, PriorityQueue
from dataclasses import dataclass, field
from typing import Any

@dataclass(order=True)
class PrioritizedTask:
    priority: int
    task: Any = field(compare=False)

class AsyncTaskQueue:
    """Async task queue with workers"""
    
    def __init__(self, num_workers=3):
        self.queue = PriorityQueue()
        self.num_workers = num_workers
        self.results = []
    
    async def worker(self, name):
        """Worker that processes tasks"""
        while True:
            try:
                prioritized_task = await self.queue.get()
                task_func, args = prioritized_task.task
                
                print(f"{name} processing task (priority {prioritized_task.priority})")
                result = await task_func(*args)
                self.results.append(result)
                
                self.queue.task_done()
            
            except asyncio.CancelledError:
                break
    
    async def add_task(self, task_func, args=(), priority=0):
        """Add task to queue"""
        await self.queue.put(
            PrioritizedTask(priority, (task_func, args))
        )
    
    async def run(self):
        """Run workers"""
        workers = [
            asyncio.create_task(self.worker(f"Worker-{i}"))
            for i in range(self.num_workers)
        ]
        
        await self.queue.join()
        
        for worker in workers:
            worker.cancel()
        
        await asyncio.gather(*workers, return_exceptions=True)
        return self.results

# Usage
async def example_task(task_id, duration):
    await asyncio.sleep(duration)
    return f"Task {task_id} completed"

async def main():
    queue = AsyncTaskQueue(num_workers=3)
    
    # Add tasks with priorities
    await queue.add_task(example_task, (1, 2), priority=2)
    await queue.add_task(example_task, (2, 1), priority=1)
    await queue.add_task(example_task, (3, 3), priority=3)
    
    results = await queue.run()
    print(results)
```

## 💡 Best Practices

1. **Use asyncio.run() for entry point**: Clean startup/shutdown
2. **Create tasks for concurrent execution**: Don't just await
3. **Handle cancellation properly**: Cleanup resources
4. **Use timeouts**: Prevent hanging operations
5. **Limit concurrency**: Use Semaphore for rate limiting
6. **Don't mix sync and async**: Use run_in_executor for blocking code
7. **Error handling**: Always handle exceptions in tasks

## 🎓 Latihan Mandiri

1. **Async Web Crawler**: Crawl websites concurrently
2. **Chat Server**: Async WebSocket server
3. **API Rate Limiter**: Respect API rate limits
4. **Data Pipeline**: Process data streams asynchronously
5. **Monitoring System**: Periodic health checks

## 📚 Referensi Tambahan

- [asyncio Documentation](https://docs.python.org/3/library/asyncio.html)
- [Real Python - Async IO](https://realpython.com/async-io-python/)
- [aiohttp Documentation](https://docs.aiohttp.org/)

---

**💪 Tip Expert:** Async is perfect for I/O-bound tasks. For CPU-bound tasks, use multiprocessing instead!
