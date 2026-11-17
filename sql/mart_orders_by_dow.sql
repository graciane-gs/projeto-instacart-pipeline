-- Camada Marts (Gold): Volume de pedidos por dia da semana
SELECT 
    order_dow,
    COUNT(order_id) AS total_orders
FROM refined_orders
GROUP BY order_dow
ORDER BY order_dow;