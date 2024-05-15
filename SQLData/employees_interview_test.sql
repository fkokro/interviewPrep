-- Create employees Table
CREATE TABLE employees(
	emp_no INT PRIMARY KEY NOT NULL,
	birth_date VARCHAR(255) NOT NULL,
	first_name VARCHAR(255) NOT NULL,
	last_name VARCHAR(255) NOT NULL,
	gender VARCHAR(1) NOT NULL,
	hire_date VARCHAR NOT NULL
);

-- Create table departments
CREATE TABLE departments(
	dept_no VARCHAR(255) PRIMARY KEY NOT NULL,
	dept_name VARCHAR(255) NOT NULL
);

--Create Table salaries
CREATE TABLE salaries (
	emp_no INT NOT NULL,
	salary INT NOT NULL,
	from_date TIMESTAMP NOT NULL,
	to_date TIMESTAMP NOT NULL,
		FOREIGN KEY (emp_no) REFERENCES employees(emp_no)
);

--CREATE TABLE dept_emp
CREATE TABLE dept_emp(
	emp_no INT NOT NULL,
	dept_no VARCHAR(255) NOT NULL,
	from_date TIMESTAMP NOT NULL,
	to_date TIMESTAMP NOT NULL,
		FOREIGN KEY (emp_no) REFERENCES employees(emp_no),
		FOREIGN KEY (dept_no) REFERENCES departments(dept_no)
);

--Create Table titles
CREATE TABLE titles(
	emp_no INT NOT NULL,
	title VARCHAR(255) NOT NULL,
	from_date TIMESTAMP NOT NULL,
	to_date TIMESTAMP NOT NULL,
		FOREIGN KEY (emp_no) REFERENCES employees(emp_no)
);

--Create Table dept_manager
CREATE TABLE dept_manager(
	dept_no VARCHAR(255) NOT NULL,
	emp_no INT NOT NULL,
	from_date TIMESTAMP NOT NULL,
	to_date TIMESTAMP NOT NULL,
		FOREIGN KEY (emp_no) REFERENCES employees(emp_no),
		FOREIGN KEY (dept_no) REFERENCES departments(dept_no)
)

-------------------Check Data Loads
Select * from departments
limit 100;

Select * from dept_emp
limit 100;

Select * from dept_manager
limit 100;

Select * from employees
limit 100;

Select * from salaries
limit 100;

Select * from titles
limit 100;

------Interview Review
--1.List the following details of each employee: employee number, last name, first name, gender, and salary.
SELECT e.emp_no, e.last_name, e.first_name, e.gender, s.salary 
FROM employees e
LEFT JOIN salaries s
ON (e.emp_no=s.emp_no)
--2.List employees who were hired in 1986.
SELECT * FROM employees
WHERE HIRE_DATE LIKE '1986%'
--3.List the manager of each department with the following information: department number, department name, the manager's employee number, last name, first name, and start and end employment dates.
WITH manager_info_cte AS
(SELECT dm.dept_no, d.dept_name, dm.emp_no 
FROM dept_manager dm
LEFT JOIN departments d
ON dm.dept_no = d.dept_no)

SELECT mi.dept_no, mi.dept_name, mi.emp_no, e.last_name, e.first_name, de.from_date, de.to_date  FROM manager_info_cte mi
LEFT JOIN employees e
on mi.emp_no = e.emp_no
LEFT JOIN dept_emp de
on e.emp_no = de.emp_no
--4.List the of each employee with the following information: employee number, last name, first name, and department name
select l.emp_no, l.last_name, l.first_name, r.dept_name from employees l
inner join 
(select r.*, l.dept_name from departments l
inner join
(select dn.emp_no, dn.dept_no from dept_emp dn
inner join
(select 
 		emp_no,
 		dept_no,
		row_number() over(partition by emp_no order by from_date desc) as t
from dept_emp) r
on dn.emp_no = r.emp_no and dn.dept_no = r.dept_no
where r.t = 1) r
on r.dept_no = l.dept_no) r
on l.emp_no = r.emp_no
--5.List all employees whose first name is "Hercules" and last names begin with "B."
select first_name, last_name from employees
where first_name = 'Hercules'
and
last_name LIKE 'B%'
--6.List all employees in the Sales department, including their employee number, last name, first name, and department name.
with curr_dept_cte as (
select *,
	   row_number() over(partition by emp_no order by from_date desc) transfer
from dept_emp)

select l.emp_no, e.last_name, e.first_name, r.dept_name from curr_dept_cte l
left join departments r
on l.dept_no = r.dept_no
left join employees e
on l.emp_no = e.emp_no
where transfer = 1
and
dept_name = 'Sales'
order by emp_no asc
--7.List all employees in the Sales and Development departments, including their employee number, last name, first name, and department name.
with curr_dept_cte as
(select *,
       row_number() over (partition by emp_no order by from_date) transfer
from dept_emp)

select e.emp_no, e.last_name, e.first_name, r.dept_name from curr_dept_cte l
left join departments r
on r.dept_no = l.dept_no
left join employees e
on l.emp_no = e.emp_no
where transfer = 1
and r.dept_name = 'Sales'
or r.dept_name = 'Development'
        
--8.In descending order, list the frequency count of employee last names, i.e., how many employees share each last name.
select last_name, count(last_name) as frequeny from employees
group by last_name
order by frequeny desc
--9. Calculate the year over year salary
WITH sales_product_year AS (  SELECT    product,    year(ship_date) as year,    SUM(price) as total_amt  FROM    item_sales  GROUP BY    product, year )