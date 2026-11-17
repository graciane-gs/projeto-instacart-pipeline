-- Camada Marts (Gold): Top produtos mais pedidos e recomprados
SELECT 
    product_id,
    product_name,
    COUNT(order_id) AS total_orders,
    SUM(reordered) AS total_reorders
FROM refined_orders_products
GROUP BY product_id, product_name
ORDER BY total_orders DESC;