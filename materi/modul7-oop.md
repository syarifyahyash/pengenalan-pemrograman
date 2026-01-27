# Modul 7: Object-Oriented Programming (OOP) 🎯

## 📚 Pendahuluan

**Object-Oriented Programming (OOP)** adalah paradigma pemrograman yang mengorganisir kode dalam bentuk objek yang memiliki atribut (data) dan method (behavior). OOP adalah konsep fundamental dalam Python dan banyak bahasa pemrograman modern.

## 🎯 Tujuan Pembelajaran

Setelah mempelajari modul ini, Anda akan mampu:
1. Memahami konsep dasar OOP: Class, Object, Encapsulation, Inheritance, Polymorphism
2. Membuat dan menggunakan class dan object
3. Mengimplementasikan inheritance (single dan multiple)
4. Memahami dan menggunakan special methods (magic methods)
5. Mengimplementasikan encapsulation dan property
6. Menggunakan class methods dan static methods
7. Memahami abstraction dan interface
8. Menerapkan prinsip SOLID dalam design

## 📖 Materi

### 1. Class dan Object Dasar

```python
# Definisi Class
class Mahasiswa:
    """Class untuk merepresentasikan mahasiswa"""
    
    # Class variable (shared oleh semua instance)
    universitas = "Universitas Indonesia"
    jumlah_mahasiswa = 0
    
    # Constructor
    def __init__(self, nama, npm, jurusan):
        # Instance variables
        self.nama = nama
        self.npm = npm
        self.jurusan = jurusan
        self.nilai = []
        Mahasiswa.jumlah_mahasiswa += 1
    
    # Instance method
    def tambah_nilai(self, nilai):
        self.nilai.append(nilai)
    
    def rata_rata(self):
        if not self.nilai:
            return 0
        return sum(self.nilai) / len(self.nilai)
    
    def info(self):
        return f"{self.nama} ({self.npm}) - {self.jurusan}"
    
    # String representation
    def __str__(self):
        return self.info()
    
    def __repr__(self):
        return f"Mahasiswa('{self.nama}', '{self.npm}', '{self.jurusan}')"

# Membuat object (instance)
mhs1 = Mahasiswa("Budi Santoso", "2106001", "Informatika")
mhs2 = Mahasiswa("Ani Wijaya", "2106002", "Sistem Informasi")

# Menggunakan method
mhs1.tambah_nilai(85)
mhs1.tambah_nilai(90)
mhs1.tambah_nilai(78)

print(mhs1.info())
print(f"Rata-rata: {mhs1.rata_rata()}")
print(f"Total mahasiswa: {Mahasiswa.jumlah_mahasiswa}")
```

### 2. Encapsulation (Information Hiding)

```python
class BankAccount:
    """Class dengan encapsulation"""
    
    def __init__(self, account_number, owner, initial_balance=0):
        self.account_number = account_number
        self.owner = owner
        self.__balance = initial_balance  # Private attribute
        self.__transaction_history = []   # Private attribute
    
    # Getter method
    def get_balance(self):
        return self.__balance
    
    # Setter method dengan validation
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Jumlah deposit harus positif")
        
        self.__balance += amount
        self.__transaction_history.append({
            "type": "deposit",
            "amount": amount,
            "balance": self.__balance
        })
        return self.__balance
    
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Jumlah withdraw harus positif")
        
        if amount > self.__balance:
            raise ValueError("Saldo tidak mencukupi")
        
        self.__balance -= amount
        self.__transaction_history.append({
            "type": "withdraw",
            "amount": amount,
            "balance": self.__balance
        })
        return self.__balance
    
    def get_transaction_history(self):
        # Return copy, bukan reference
        return self.__transaction_history.copy()
    
    def __str__(self):
        return f"Account {self.account_number} - {self.owner}: Rp{self.__balance:,.0f}"

# Usage
account = BankAccount("1234567890", "Budi Santoso", 1000000)
account.deposit(500000)
account.withdraw(200000)
print(account)
print(f"History: {account.get_transaction_history()}")
```

### 3. Property Decorators

```python
class Person:
    """Class menggunakan property decorators"""
    
    def __init__(self, first_name, last_name, age):
        self._first_name = first_name
        self._last_name = last_name
        self._age = age
    
    # Property getter
    @property
    def full_name(self):
        return f"{self._first_name} {self._last_name}"
    
    # Property setter
    @full_name.setter
    def full_name(self, name):
        first, last = name.split(" ", 1)
        self._first_name = first
        self._last_name = last
    
    # Property dengan validation
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Usia tidak boleh negatif")
        if value > 150:
            raise ValueError("Usia tidak valid")
        self._age = value
    
    # Read-only property
    @property
    def birth_year(self):
        from datetime import datetime
        current_year = datetime.now().year
        return current_year - self._age

# Usage
person = Person("Budi", "Santoso", 25)
print(person.full_name)  # Getter
person.full_name = "Ani Wijaya"  # Setter
print(person.full_name)
print(person.birth_year)  # Read-only
```

### 4. Inheritance (Pewarisan)

```python
# Parent class (Base class)
class Employee:
    """Base class untuk employee"""
    
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary
    
    def get_annual_salary(self):
        return self.salary * 12
    
    def give_raise(self, amount):
        self.salary += amount
    
    def __str__(self):
        return f"{self.name} (ID: {self.employee_id})"

# Child class (Derived class)
class Manager(Employee):
    """Manager adalah Employee dengan tambahan fitur"""
    
    def __init__(self, name, employee_id, salary, department):
        # Call parent constructor
        super().__init__(name, employee_id, salary)
        self.department = department
        self.team_members = []
    
    def add_team_member(self, employee):
        self.team_members.append(employee)
    
    def get_team_size(self):
        return len(self.team_members)
    
    # Override parent method
    def get_annual_salary(self):
        # Manager bonus 20%
        base_salary = super().get_annual_salary()
        return base_salary * 1.2
    
    def __str__(self):
        return f"Manager {self.name} - {self.department}"

class Developer(Employee):
    """Developer adalah Employee dengan programming skills"""
    
    def __init__(self, name, employee_id, salary, programming_languages):
        super().__init__(name, employee_id, salary)
        self.programming_languages = programming_languages
        self.projects = []
    
    def add_project(self, project):
        self.projects.append(project)
    
    def get_skills(self):
        return ", ".join(self.programming_languages)
    
    # Override
    def __str__(self):
        return f"Developer {self.name} - Skills: {self.get_skills()}"

# Usage
manager = Manager("Budi", "MGR001", 15000000, "IT")
dev1 = Developer("Ani", "DEV001", 10000000, ["Python", "JavaScript"])
dev2 = Developer("Citra", "DEV002", 10000000, ["Java", "Go"])

manager.add_team_member(dev1)
manager.add_team_member(dev2)

print(manager)
print(f"Team size: {manager.get_team_size()}")
print(f"Annual salary: Rp{manager.get_annual_salary():,.0f}")
```

### 5. Multiple Inheritance

```python
class Flyable:
    """Mixin class untuk objek yang bisa terbang"""
    
    def fly(self):
        return f"{self.name} is flying"

class Swimmable:
    """Mixin class untuk objek yang bisa berenang"""
    
    def swim(self):
        return f"{self.name} is swimming"

class Animal:
    """Base class untuk animal"""
    
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def eat(self):
        return f"{self.name} is eating"

class Duck(Animal, Flyable, Swimmable):
    """Duck bisa fly dan swim"""
    
    def __init__(self, name):
        super().__init__(name, "Duck")
    
    def quack(self):
        return f"{self.name} says: Quack!"

class Fish(Animal, Swimmable):
    """Fish hanya bisa swim"""
    
    def __init__(self, name):
        super().__init__(name, "Fish")

# Usage
donald = Duck("Donald")
print(donald.fly())
print(donald.swim())
print(donald.quack())
print(donald.eat())

nemo = Fish("Nemo")
print(nemo.swim())
print(nemo.eat())
# nemo.fly()  # Error: Fish tidak punya method fly
```

### 6. Polymorphism

```python
# Interface-like base class
class Shape:
    """Base class untuk semua shapes"""
    
    def area(self):
        raise NotImplementedError("Subclass must implement area()")
    
    def perimeter(self):
        raise NotImplementedError("Subclass must implement perimeter()")

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        import math
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        import math
        return 2 * math.pi * self.radius

class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    
    def area(self):
        # Heron's formula
        s = self.perimeter() / 2
        import math
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))
    
    def perimeter(self):
        return self.side1 + self.side2 + self.side3

# Polymorphism in action
def print_shape_info(shape):
    """Function yang bekerja dengan semua Shape"""
    print(f"{shape.__class__.__name__}:")
    print(f"  Area: {shape.area():.2f}")
    print(f"  Perimeter: {shape.perimeter():.2f}")

# Usage
shapes = [
    Rectangle(5, 10),
    Circle(7),
    Triangle(3, 4, 5)
]

for shape in shapes:
    print_shape_info(shape)
    print()
```

### 7. Special Methods (Magic Methods)

```python
class Vector:
    """Class untuk vector matematika dengan operator overloading"""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    # String representation
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
    
    # Arithmetic operators
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
    # Comparison operators
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __lt__(self, other):
        return self.magnitude() < other.magnitude()
    
    # Length
    def __len__(self):
        return 2
    
    # Indexing
    def __getitem__(self, index):
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError("Vector index out of range")
    
    # Boolean conversion
    def __bool__(self):
        return self.x != 0 or self.y != 0
    
    # Helper method
    def magnitude(self):
        import math
        return math.sqrt(self.x ** 2 + self.y ** 2)

# Usage
v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(v1 + v2)  # Vector(4, 6)
print(v1 - v2)  # Vector(2, 2)
print(v1 * 2)   # Vector(6, 8)
print(v1 == v2) # False
print(v1 > v2)  # True (magnitude)
print(v1[0])    # 3
print(len(v1))  # 2
print(bool(v1)) # True
```

### 8. Class Methods dan Static Methods

```python
class DateTime:
    """Class untuk menangani date dan time"""
    
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    
    # Instance method
    def format(self):
        return f"{self.year}-{self.month:02d}-{self.day:02d}"
    
    # Class method - alternative constructor
    @classmethod
    def from_string(cls, date_string):
        """Create DateTime from string format YYYY-MM-DD"""
        year, month, day = map(int, date_string.split("-"))
        return cls(year, month, day)
    
    @classmethod
    def today(cls):
        """Create DateTime untuk hari ini"""
        from datetime import datetime
        now = datetime.now()
        return cls(now.year, now.month, now.day)
    
    # Static method - utility function
    @staticmethod
    def is_leap_year(year):
        """Check if year is leap year"""
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    
    @staticmethod
    def days_in_month(year, month):
        """Get number of days in month"""
        if month in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif month in [4, 6, 9, 11]:
            return 30
        else:  # February
            return 29 if DateTime.is_leap_year(year) else 28
    
    def __str__(self):
        return self.format()

# Usage
# Normal constructor
date1 = DateTime(2024, 1, 15)

# Class method as alternative constructor
date2 = DateTime.from_string("2024-01-15")
date3 = DateTime.today()

# Static method
print(f"Is 2024 leap year? {DateTime.is_leap_year(2024)}")
print(f"Days in Feb 2024: {DateTime.days_in_month(2024, 2)}")
```

### 9. Abstract Base Classes

```python
from abc import ABC, abstractmethod

class Database(ABC):
    """Abstract base class untuk database connection"""
    
    @abstractmethod
    def connect(self):
        """Connect to database"""
        pass
    
    @abstractmethod
    def disconnect(self):
        """Disconnect from database"""
        pass
    
    @abstractmethod
    def execute_query(self, query):
        """Execute SQL query"""
        pass
    
    # Concrete method (implementation provided)
    def get_status(self):
        return "Database connection active"

class MySQLDatabase(Database):
    """MySQL implementation"""
    
    def __init__(self, host, port, username, password):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.connected = False
    
    def connect(self):
        print(f"Connecting to MySQL at {self.host}:{self.port}")
        self.connected = True
    
    def disconnect(self):
        print("Disconnecting from MySQL")
        self.connected = False
    
    def execute_query(self, query):
        if not self.connected:
            raise Exception("Not connected to database")
        print(f"Executing MySQL query: {query}")
        return []

class PostgreSQLDatabase(Database):
    """PostgreSQL implementation"""
    
    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.connected = False
    
    def connect(self):
        print(f"Connecting to PostgreSQL: {self.connection_string}")
        self.connected = True
    
    def disconnect(self):
        print("Disconnecting from PostgreSQL")
        self.connected = False
    
    def execute_query(self, query):
        if not self.connected:
            raise Exception("Not connected to database")
        print(f"Executing PostgreSQL query: {query}")
        return []

# Usage
# db = Database()  # Error: Cannot instantiate abstract class

mysql_db = MySQLDatabase("localhost", 3306, "user", "pass")
mysql_db.connect()
mysql_db.execute_query("SELECT * FROM users")
mysql_db.disconnect()
```

## 🏋️ Latihan Praktik

### Latihan 1: Library Management System

```python
class Book:
    """Class untuk merepresentasikan buku"""
    
    def __init__(self, isbn, title, author, year):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year
        self.is_borrowed = False
    
    def __str__(self):
        status = "Dipinjam" if self.is_borrowed else "Tersedia"
        return f"{self.title} by {self.author} ({self.year}) - {status}"

class Member:
    """Class untuk member perpustakaan"""
    
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []
    
    def borrow_book(self, book):
        if book.is_borrowed:
            return False
        book.is_borrowed = True
        self.borrowed_books.append(book)
        return True
    
    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_borrowed = False
            self.borrowed_books.remove(book)
            return True
        return False
    
    def __str__(self):
        return f"Member: {self.name} (ID: {self.member_id})"

class Library:
    """Class untuk perpustakaan"""
    
    def __init__(self, name):
        self.name = name
        self.books = []
        self.members = []
    
    def add_book(self, book):
        self.books.append(book)
    
    def register_member(self, member):
        self.members.append(member)
    
    def find_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None
    
    def available_books(self):
        return [book for book in self.books if not book.is_borrowed]

# Usage
library = Library("Perpustakaan UI")

# Add books
library.add_book(Book("001", "Python Programming", "John Doe", 2020))
library.add_book(Book("002", "Data Science Basics", "Jane Smith", 2021))

# Register member
member = Member("M001", "Budi")
library.register_member(member)

# Borrow book
book = library.find_book("001")
if member.borrow_book(book):
    print(f"{member.name} meminjam {book.title}")
```

### Latihan 2: E-Commerce Product System

```python
class Product:
    """Base class untuk produk"""
    
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self._price = price
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value
    
    def get_total_price(self, quantity):
        return self._price * quantity
    
    def __str__(self):
        return f"{self.name} - Rp{self._price:,.0f}"

class DigitalProduct(Product):
    """Produk digital (software, ebook, etc)"""
    
    def __init__(self, product_id, name, price, file_size, download_link):
        super().__init__(product_id, name, price)
        self.file_size = file_size
        self.download_link = download_link
    
    def deliver(self):
        return f"Download link: {self.download_link}"

class PhysicalProduct(Product):
    """Produk fisik"""
    
    def __init__(self, product_id, name, price, weight, stock):
        super().__init__(product_id, name, price)
        self.weight = weight
        self.stock = stock
    
    def get_total_price(self, quantity):
        # Physical product has shipping cost
        base_price = super().get_total_price(quantity)
        shipping_cost = self.weight * quantity * 1000  # Rp 1000 per kg
        return base_price + shipping_cost
    
    def check_stock(self, quantity):
        return self.stock >= quantity
    
    def reduce_stock(self, quantity):
        if self.check_stock(quantity):
            self.stock -= quantity
            return True
        return False

# Usage
laptop = PhysicalProduct("P001", "Laptop ASUS", 10000000, 2.5, 10)
ebook = DigitalProduct("D001", "Python Guide", 100000, 5, "https://download.link")

print(f"Laptop price for 2 units: Rp{laptop.get_total_price(2):,.0f}")
print(f"Ebook price for 1 unit: Rp{ebook.get_total_price(1):,.0f}")
```

### Latihan 3: Vehicle Hierarchy

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    """Abstract base class untuk kendaraan"""
    
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = 0
    
    @abstractmethod
    def start_engine(self):
        pass
    
    @abstractmethod
    def stop_engine(self):
        pass
    
    def accelerate(self, increment):
        self.speed += increment
        print(f"Speed: {self.speed} km/h")
    
    def brake(self, decrement):
        self.speed = max(0, self.speed - decrement)
        print(f"Speed: {self.speed} km/h")

class Car(Vehicle):
    def __init__(self, brand, model, year, num_doors):
        super().__init__(brand, model, year)
        self.num_doors = num_doors
    
    def start_engine(self):
        print(f"{self.brand} {self.model} engine started")
    
    def stop_engine(self):
        print(f"{self.brand} {self.model} engine stopped")

class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, engine_cc):
        super().__init__(brand, model, year)
        self.engine_cc = engine_cc
    
    def start_engine(self):
        print(f"{self.brand} {self.model} ({self.engine_cc}cc) engine started")
    
    def stop_engine(self):
        print(f"{self.brand} {self.model} engine stopped")
    
    def wheelie(self):
        if self.speed > 30:
            print("Performing wheelie!")
        else:
            print("Speed too low for wheelie")

# Usage
car = Car("Toyota", "Camry", 2024, 4)
bike = Motorcycle("Honda", "CBR", 2024, 1000)

car.start_engine()
car.accelerate(50)
car.brake(20)
car.stop_engine()

bike.start_engine()
bike.accelerate(50)
bike.wheelie()
```

## 💡 Design Patterns

### 1. Singleton Pattern

```python
class Database:
    """Singleton pattern - hanya satu instance"""
    
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.connection = None
        return cls._instance
    
    def connect(self):
        if self.connection is None:
            self.connection = "Connected to database"
            print("New connection established")
        else:
            print("Using existing connection")

# Usage
db1 = Database()
db2 = Database()
print(db1 is db2)  # True - same instance
```

### 2. Factory Pattern

```python
class ShapeFactory:
    """Factory untuk membuat shape objects"""
    
    @staticmethod
    def create_shape(shape_type, *args):
        if shape_type == "circle":
            return Circle(*args)
        elif shape_type == "rectangle":
            return Rectangle(*args)
        elif shape_type == "triangle":
            return Triangle(*args)
        else:
            raise ValueError(f"Unknown shape type: {shape_type}")

# Usage
circle = ShapeFactory.create_shape("circle", 5)
rectangle = ShapeFactory.create_shape("rectangle", 4, 6)
```

### 3. Observer Pattern

```python
class Subject:
    """Subject yang diamati"""
    
    def __init__(self):
        self._observers = []
        self._state = None
    
    def attach(self, observer):
        self._observers.append(observer)
    
    def detach(self, observer):
        self._observers.remove(observer)
    
    def notify(self):
        for observer in self._observers:
            observer.update(self._state)
    
    def set_state(self, state):
        self._state = state
        self.notify()

class Observer:
    """Observer interface"""
    
    def update(self, state):
        raise NotImplementedError

class ConcreteObserver(Observer):
    def __init__(self, name):
        self.name = name
    
    def update(self, state):
        print(f"{self.name} received update: {state}")

# Usage
subject = Subject()
observer1 = ConcreteObserver("Observer 1")
observer2 = ConcreteObserver("Observer 2")

subject.attach(observer1)
subject.attach(observer2)

subject.set_state("New State!")
```

## 🎓 SOLID Principles

### S - Single Responsibility Principle
```python
# BAD
class User:
    def __init__(self, name):
        self.name = name
    
    def save_to_database(self):
        # Database logic
        pass
    
    def send_email(self):
        # Email logic
        pass

# GOOD
class User:
    def __init__(self, name):
        self.name = name

class UserRepository:
    def save(self, user):
        # Database logic
        pass

class EmailService:
    def send(self, user, message):
        # Email logic
        pass
```

### O - Open/Closed Principle
```python
# Open for extension, closed for modification
class Discount(ABC):
    @abstractmethod
    def calculate(self, price):
        pass

class PercentageDiscount(Discount):
    def __init__(self, percentage):
        self.percentage = percentage
    
    def calculate(self, price):
        return price * (1 - self.percentage / 100)

class FixedDiscount(Discount):
    def __init__(self, amount):
        self.amount = amount
    
    def calculate(self, price):
        return max(0, price - self.amount)
```

## 🎓 Latihan Mandiri

1. **Student Management System**: Buat sistem dengan:
   - Multiple inheritance untuk Student, Teacher, Staff
   - Property decorators untuk validation
   - Abstract base class untuk Person
   - Special methods untuk comparison

2. **Payment Gateway**: Implementasi:
   - Abstract payment processor
   - Multiple payment methods (Credit Card, PayPal, Bank Transfer)
   - Decorator pattern untuk transaction logging
   - Factory pattern untuk creating payment processors

3. **Game Characters**: Buat game system dengan:
   - Base Character class
   - Different character types (Warrior, Mage, Archer)
   - Skills and abilities dengan polymorphism
   - Inventory system

## 📚 Referensi Tambahan

- [Python OOP Documentation](https://docs.python.org/3/tutorial/classes.html)
- [Real Python - OOP](https://realpython.com/python3-object-oriented-programming/)
- [Design Patterns in Python](https://refactoring.guru/design-patterns/python)
- [SOLID Principles](https://realpython.com/solid-principles-python/)

## 🚀 Next Steps

Setelah menguasai OOP, lanjutkan ke:
- **Modul 8**: File I/O & Exception Handling
- **Modul 9**: Decorators & Context Managers
- **Modul 10**: Generators & Iterators

---

**💪 Tip Expert:** OOP adalah tentang modeling the real world. Pikirkan tentang entitas dan relationships mereka sebelum menulis kode!
