import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import mysql.connector

db=mysql.connector.connect(host="localhost",
username="root",
password="RS01Ritul@123",
database="ecommerce")

cur=db.cursor()

# 1. List all unique cities where customers are located.
# query="""select distinct customer_city from customers"""
# cur.execute(query)
# cities=cur.fetchall()
# print(cities)

# 2. Count the number of orders placed in 2017.
# query="""select count(order_id) from orders where year(order_purchase_timestamp)=2017"""
# cur.execute(query)
# data=cur.fetchall()
# print(data[0][0])

# 3. Find the total sales per category.
# query="""select products.product_category category,
# round(sum(payments.payment_value),2) sales from products join orderitems
# on products.product_id=orderitems.product_id join payments
# on payments.order_id=orderitems.order_id
# group by category"""
# cur.execute(query)
# data=cur.fetchall()
# df=pd.DataFrame(data,columns=["Category","Sales"])
# print(df)

# 4. Calculate the percentage of orders that were paid in installments.
# query="""select sum(case when payment_installments>=1 then 1 else 0 end)/count(*)*100
# from payments"""
# cur.execute(query)
# data=cur.fetchall()
# print(data)

# 5. Count the number of customers from each state. 
query="""select customer_state, count(customer_id) from customers group by customer_state
"""
cur.execute(query)
data=cur.fetchall()
df=pd.DataFrame(data,columns=["state","customer_count"])
df=df.sort_values(by="customer_count",ascending=False)
plt.figure(figsize=(9,4))
plt.bar(df["state"],df["customer_count"])
plt.xticks(rotation=90)
plt.show()
# print(df)