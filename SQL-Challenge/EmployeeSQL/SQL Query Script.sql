--Lists the following details of each employee: employee number, last name, first name, sex, and salary
select e.emp_no, e.last_name, e.first_name, e.sex, s.salary
from employees e
join salaries s on e.emp_no = s.emp_no
limit 100;

--Lists first name, last name, and hire date for employees who were hired in 1986
select first_name, last_name, hire_date
from employees
where hire_date between '1986-01-01' and '1986-12-31'
order by hire_date, last_name;

--Lists the manager of each department with the following information: department number, department name, the manager's employee number, last name, first name
select dm.dept_no, dep.dept_name, dm.emp_no, e.last_name, e.first_name
from employees e
join dept_manager dm on e.emp_no = dm.emp_no
join departments dep on dep.dept_no = dm.dept_no
order by dept_no, last_name;

--Lists the department of each employee with the following information: employee number, last name, first name, and department name
select e.emp_no, e.last_name, e.first_name, dep.dept_name
from employees e
join dept_emp de on e.emp_no = de.emp_no
join departments dep on dep.dept_no = de.dept_no
order by dept_name, last_name;

--Lists first name, last name, and sex for employees whose first name is "Hercules" and last names begin with "B."
select first_name, last_name, sex
from employees
where first_name = 'Hercules' and last_name like 'B%'
order by last_name;

--Lists all employees in the Sales department, including their employee number, last name, first name, and department name
select e.emp_no, e.last_name, e.first_name, dep.dept_name
from employees e
join dept_emp de on e.emp_no = de.emp_no
join departments dep on dep.dept_no = de.dept_no
where dep.dept_name = 'Sales'
order by e.last_name;

--Lists all employees in the Sales and Development departments, including their employee number, last name, first name, and department name
select e.emp_no, e.last_name, e.first_name, dep.dept_name
from employees e
join dept_emp de on e.emp_no = de.emp_no
join departments dep on dep.dept_no = de.dept_no
where dep.dept_name = 'Sales' or dep.dept_name = 'Development'
order by e.last_name;

--Lists the frequency count of employee last names in descending order
select last_name, count(last_name) as "frequency count"
from employees
group by last_name
order by "frequency count" desc;