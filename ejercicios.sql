'Companies often perform salary analyses to ensure fair compensation practices. One useful analysis is to check if there are any employees earning more than their direct managers.

As a HR Analyst, youre asked to identify all employees who earn more than their direct managers. The result should include the employees ID and name.
''
SELECT 
e.employee_id as employee_id,
e.name as employee_name,
e.salary as salario_empleado,
m.employee_id AS m_id,
m.name as manager,
m.salary as salario_manager
FROM employee AS e 
INNER JOIN employee as m 
ON e.manager_id = m.employee_id
WHERE e.salary > m.salary;'