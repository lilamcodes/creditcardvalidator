# More SQL!!


### Advanced Topics

#### Aggregate Functions


##### count()
```
SELECT count(*) FROM students_table;
```
- Counts the number of records returned by the query.

##### max()
```
SELECT max(age) FROM students_table;
```
- Maximum of a given column in records returned.

##### min()
```
SELECT min(age) FROM students_table;
```
- Minimum of a given column in records returned.

##### sum()
```
SELECT sum(salary) FROM employee_table;
```
- Sum together a given column in records returned.

##### avg()
```
SELECT avg(salary) FROM employee_table;
```
- Average ofna given column in records returned.

#### Group By and Order By

##### Order By

- Order By is used when there is a specific order you would like the records returned.
- For example, you may want your records returned alphabetically, from largest to smallest numerically, and etc.

```
SELECT * FROM employee_table ORDER BY salary;

```
- The following will return all records ordered from highest to lowest based on salary.


##### Group By

- Group By is used for decipering something aggregate about a handful of records that are connected.
- For example, lets say if you had a population table of people from United States from all different states. You may want to find out how many people live in each state, or what is the average salary per state. Essentially, a rule of thumb is that there will be an aggregate function involved.

```
SELECT max(salary) FROM employee_table GROUP BY department_id;
```


#### Joins

- Joins are used in SQL to strategically merge multiple tables based on certain criteria. The usage of joins is what allows programmers to take advantage of the relational nature of relational databases.

##### Inner Join

- Inner Join is used for when you are looking for an exact match between two tables and want records that do not match to be ignored.

```
SELECT * FROM salary_table 
INNER JOIN employee_table 
ON salary_table.employee_id = employee_table.id;

```
- The following command states that you would like all records from both tables where the id record in the employee_table matches the salary_table employee_id.
- NOTE: You can additionally provide a WHERE statement after to specify a condition after the join.



##### Outer Join

- Outer Join is similar to an inner join however the records that do not match from the first table mentioned will return in the final query regardless if there is a match on the condition you are joining on.

```
SELECT * FROM student_table 
OUTER JOIN physics_table 
ON student_table.id = physics_table.stud_id;
```
- The following query will return all the students followed by their record in the physics_table if there is a connection or not.
- This would be useful if you wanted to see how many people were not in physics class for example.





