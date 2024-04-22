def calculate_profit(*sales_data):
    cost_price, sell_price, inventory = sales_data
    return round((sell_price - cost_price) * inventory)

todays_sales = [32.67, 45.00, 1200]
calculate_profit(*todays_sales)