-- Show all customers
SELECT * FROM customers;

-- Show all products
SELECT * FROM products;

-- Show all orders
SELECT * FROM orders;

----join(who bought what?)------
SELECT customers.name, products.product_name, orders.quantity
FROM orders
JOIN customers ON orders.customer_id = customers.customer_id
JOIN products ON orders.product_id = products.product_id;

----Total spending per customer ---
SELECT customers.name, SUM(products.price * orders.quantity) AS total_spent
FROM orders
JOIN customers ON orders.customer_id = customers.customer_id
JOIN products ON orders.product_id = products.product_id
GROUP BY customers.name;

---MOST EXPERIENCE PRODUCT ----
SELECT * FROM products
ORDER BY price DESC
LIMIT 1;

---TOTAL ORDERS PER CUSTOMER ----
SELECT customer_id, COUNT(*) AS total_orders
FROM orders
GROUP BY customer_id;

----FILTER(CITY BASED)-----
SELECT * FROM customers
WHERE city = 'Delhi';

----ABOVE AVERAGE SPENDING ----
SELECT customers.name, SUM(products.price * orders.quantity) AS total_spent
FROM orders
JOIN customers ON orders.customer_id = customers.customer_id
JOIN products ON orders.product_id = products.product_id
GROUP BY customers.name
HAVING total_spent > (
    SELECT AVG(products.price * orders.quantity)
    FROM orders
    JOIN products ON orders.product_id = products.product_id
);

