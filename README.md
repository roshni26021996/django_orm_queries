In Django, Object-Relational Mapping (ORM) allows you to interact with your database using Python objects instead of SQL queries. Here’s a comprehensive overview of common ORM queries and how to use them in Django:

### 1. **Setting Up Your Model**
Before querying, you need to define your models in `models.py`.

```python
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    published_date = models.DateField()

    def __str__(self):
        return self.title
```

### 2. **Creating Objects**
To create objects, you can use the `create()` method or instantiate a model and call `save()`.

```python
# Using create()
author = Author.objects.create(name="John Doe", email="john@example.com")

# Using save()
book = Book(title="Sample Book", author=author, published_date="2024-01-01")
book.save()
```

### 3. **Retrieving Objects**
You can retrieve objects using various methods:

#### a. **Get Single Object**
```python
# Get a single object by primary key
author = Author.objects.get(pk=1)

# Get a single object with a specific condition
book = Book.objects.get(title="Sample Book")
```

#### b. **Get Multiple Objects**
```python
# Get all objects
authors = Author.objects.all()

# Filter by specific criteria
books = Book.objects.filter(author__name="John Doe")

# Exclude certain objects
books = Book.objects.exclude(title="Sample Book")
```

### 4. **Querying with Conditions**
You can use various lookups for querying:

#### a. **Field Lookups**
```python
# Exact match
authors = Author.objects.filter(name__exact="John Doe")

# Case-insensitive match
authors = Author.objects.filter(name__iexact="john doe")

# Contains (like)
books = Book.objects.filter(title__contains="Sample")

# Starts with
books = Book.objects.filter(title__startswith="Sample")

# Ends with
books = Book.objects.filter(title__endswith="Book")

# Range
books = Book.objects.filter(published_date__range=["2020-01-01", "2024-12-31"])
```
### What are Lookups in Django ORM?

Lookups in Django ORM are used to filter querysets based on conditions applied to model fields. They provide a way to perform complex SQL queries with conditions directly in Python code. Each lookup corresponds to an SQL operation, like `=`, `LIKE`, or `IN`, and Django translates them into the appropriate SQL for the database.

### Why Use Lookups in Django ORM?

Lookups are important because they:
1. **Simplify SQL queries**: Instead of writing raw SQL, you can express conditions using Python code.
2. **Increase readability**: They make the code easier to understand for people who may not be familiar with SQL.
3. **Protect against SQL injection**: Since Django ORM automatically escapes values, lookups are safer to use than writing raw SQL.
4. **Enable complex queries**: You can easily chain multiple lookups to build complex filtering logic.
   
### How to Use Lookups in Django ORM?

Lookups are generally used with Django’s `.filter()`, `.exclude()`, and `.get()` methods to filter querysets.
In Django ORM, the double underscore (`__`) acts as a separator between a field name and a lookup. It is a way to specify that a particular operation (like `gt`, `exact`, `icontains`, etc.) should be applied to a specific field in the model. 

Here’s a breakdown:

- The part before the `__` refers to the **field** name in the model.
- The part after the `__` refers to the **lookup** that you want to apply to the field.

For example:
```python
City.objects.filter(population__gt=1000000)
```

In this case:
- `population` is the field in the `City` model.
- `gt` (greater than) is the lookup operation that filters cities where the population is greater than 1,000,000.

The `__` allows Django to differentiate between the field (`population`) and the lookup (`gt`).

This syntax allows for complex queries by chaining multiple lookups or referencing related models (foreign keys), making the Django ORM powerful and flexible.

### Example of Chaining Lookups with `__`:

You can use `__` to traverse relationships and apply lookups on related models. For example, if the `City` model has a foreign key to a `Country` model:
```python
City.objects.filter(country__name__iexact="usa")
```
This query:
- Traverses the `country` foreign key.
- Applies the `iexact` lookup to the `name` field in the related `Country` model.

Here, `country__name` refers to the `name` field of the related `Country` model, and `iexact` means a case-insensitive exact match.

#### Common Lookups and Examples:

1. **Exact match (`exact`)**:
   Filters rows where the field is exactly equal to the specified value.
   ```python
   City.objects.filter(name__exact="New York")
   # Equivalent SQL: WHERE name = 'New York'
   ```

2. **Case-insensitive exact match (`iexact`)**:
   Filters rows where the field matches the specified value, case-insensitively.
   ```python
   City.objects.filter(name__iexact="new york")
   # Equivalent SQL: WHERE LOWER(name) = LOWER('new york')
   ```

3. **Contains (`contains`)**:
   Filters rows where the field contains the specified substring.
   ```python
   City.objects.filter(name__contains="York")
   # Equivalent SQL: WHERE name LIKE '%York%'
   ```

4. **Case-insensitive contains (`icontains`)**:
   Filters rows where the field contains the specified substring, case-insensitively.
   ```python
   City.objects.filter(name__icontains="york")
   # Equivalent SQL: WHERE LOWER(name) LIKE LOWER('%york%')
   ```

5. **Greater than (`gt`) / Less than (`lt`)**:
   Filters rows where the field is greater than or less than the specified value.
   ```python
   City.objects.filter(population__gt=1000000)
   # Equivalent SQL: WHERE population > 1000000
   ```

6. **Range (`range`)**:
   Filters rows where the field is within the given range of values.
   ```python
   City.objects.filter(population__range=(500000, 1000000))
   # Equivalent SQL: WHERE population BETWEEN 500000 AND 1000000
   ```

7. **In (`in`)**:
   Filters rows where the field's value is in the specified list.
   ```python
   City.objects.filter(name__in=["New York", "Los Angeles", "Chicago"])
   # Equivalent SQL: WHERE name IN ('New York', 'Los Angeles', 'Chicago')
   ```

8. **Starts with / Ends with (`startswith`, `endswith`)**:
   Filters rows where the field starts or ends with the specified string.
   ```python
   City.objects.filter(name__startswith="New")
   # Equivalent SQL: WHERE name LIKE 'New%'
   ```

9. **Is null (`isnull`)**:
   Filters rows where the field is `NULL`.
   ```python
   City.objects.filter(country__isnull=True)
   # Equivalent SQL: WHERE country IS NULL
   ```

10. **Negating lookups**:
    You can negate any lookup using `exclude()`.
    ```python
    City.objects.exclude(name__icontains="york")
    # Equivalent SQL: WHERE name NOT LIKE '%york%'
    ```

#### Combining Lookups:

Lookups can be chained together to form more complex queries.
```python
City.objects.filter(population__gt=1000000, name__icontains="york")
# Equivalent SQL: WHERE population > 1000000 AND LOWER(name) LIKE LOWER('%york%')
```

For more advanced queries, you can also use `Q` objects to construct OR logic:
```python
from django.db.models import Q
City.objects.filter(Q(population__gt=1000000) | Q(name__icontains="york"))
# Equivalent SQL: WHERE population > 1000000 OR LOWER(name) LIKE LOWER('%york%')
```

---

In summary, lookups in Django ORM are a powerful and flexible way to filter querysets by applying conditions on model fields. They make it easier to write readable, safe, and maintainable database queries.




### 5. **Ordering Results**
You can order your query results using the `order_by()` method.

```python
# Order by a field
books = Book.objects.all().order_by('published_date')

# Order by descending
books = Book.objects.all().order_by('-published_date')
```

### 6. **Limiting Querysets**
You can limit the number of results using slicing:

```python
# Get the first 10 books
books = Book.objects.all()[:10]

# Get books from index 5 to 15
books = Book.objects.all()[5:15]
```

### 7. **Aggregating Data**
Django ORM provides aggregation functions such as `Count`, `Sum`, `Avg`, etc.

```python
from django.db.models import Count, Avg

# Count authors
author_count = Author.objects.count()

# Average published date of books
average_published = Book.objects.aggregate(Avg('published_date'))

# Count books by each author
book_count_per_author = Author.objects.annotate(book_count=Count('book'))
```

### 8. **Related Queries**
Django ORM makes it easy to query related models.

```python
# Get all books by a specific author
author_books = author.book_set.all()

# Get authors with their books
authors_with_books = Author.objects.prefetch_related('book_set').all()
```

### 9. **Updating Objects**
You can update objects using the `update()` method or by modifying the object and calling `save()`.

```python
# Update using update()
Book.objects.filter(author=author).update(title="Updated Sample Book")

# Update by getting the object
book = Book.objects.get(pk=1)
book.title = "New Title"
book.save()
```

### 10. **Deleting Objects**
To delete objects, use the `delete()` method.

```python
# Delete a specific object
book = Book.objects.get(pk=1)
book.delete()

# Delete multiple objects
Book.objects.filter(author=author).delete()
```

### 11. **Chaining Queries**
Django allows you to chain methods to build complex queries.

```python
# Chaining filters
books = Book.objects.filter(author__name="John Doe").exclude(title__contains="Sample").order_by('published_date')
```

### 12. **Using Q Objects for Complex Queries**
You can use `Q` objects to perform complex queries with OR conditions.

```python
from django.db.models import Q

# OR query
books = Book.objects.filter(Q(author__name="John Doe") | Q(author__name="Jane Doe"))

# AND query (default behavior)
books = Book.objects.filter(Q(author__name="John Doe") & Q(title__contains="Sample"))
```

### 13. **Transactions**
Django supports database transactions to ensure data integrity.

```python
from django.db import transaction

with transaction.atomic():
    author = Author.objects.create(name="New Author", email="new@example.com")
    Book.objects.create(title="New Book", author=author, published_date="2024-01-01")
```



### Conclusion
Django's ORM provides a powerful and flexible way to interact with databases using Python code. You can perform a wide variety of queries, from simple data retrieval to complex aggregations and transactions. This not only simplifies database operations but also makes your code cleaner and more maintainable.
