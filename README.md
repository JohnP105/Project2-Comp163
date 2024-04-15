# Project2-Comp163

### Question#1 Description:

- Objective: Create two database tables within a domain of your interest (e.g., healthcare, products, bikes, books, etc.) using ElephantSQL.

#### Requirements:

1. Design and implement two database tables relevant to your chosen domain. Ensure at least one attribute in one of the tables is suitable for storing a large amount of text and encrypt this attribute using PostgreSQL's encryption functions.

2. Populate the tables with a lot of data.

3. Develop a Python script named 'slow.py'. This script should run a SQL query that intentionally runs slowly (taking at least 5 seconds). Consider using operations like 'LIKE' for pattern matching across large text fields and 'JOIN' to combine rows from both tables.

4. Please upload a screenshot of the ElephantSQL Slow Queries tab showing the query took at least 5 seconds.

### Question#2 Description:

- Objective: Optimize the slow query from Part 1 to execute significantly faster, aiming for a runtime of approximately one second or less.

### Strategies for Optimization:

1. Indexing: Evaluate the slow query to identify columns that would benefit from indexing. Implement the necessary indexes on your tables.

2. Query Refinement: Rewrite the query to optimize its performance. This might involve rephrasing JOIN operations, using more efficient WHERE clauses.

3. Consider Distributed Databases: If applicable, demonstrate how distributing the database could improve query performance.

4. Deliverable: Please write a paragraph explaining what your team did to improve the performance to < 1 second
