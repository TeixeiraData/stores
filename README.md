# stores
Manage stores

In this exercise I would like to create three chain stores, add an inventory control. It will be simple, because the information will be in smartsheets, probably in csv. The main intent of the exercise is not to focus on extraction and modeling, but on analysis and visualization. Work on connecting tables and creating analyses, visyalizations and reports.

1 - Create the tables
    a - chain.A [date,store_id,product_id,volume]
    b - chain.B [date,store_id,product_id,volume]
    c - chain.C [date,store_id,product_id,volume]
    d - m.product [product_id,price,product_category,product_name]
    e - m.store [store_id,address,tel,zip_code]

2 - Returns the daily total volume of the three chains by product.

3 - In Chain A, return daily sales of 5 most expensive products in each product_category

4 - Returns 7 days moving average of volume by store by product each Chain.

5 - Creates a calendar lookup table that has following information
    a - Date(YYYY-MM-DD)
    b - Year(YYYY)
    c - Month Number(1,2,3...)
    d - Month Name(Jan, Fev, Mar...)
    e - Quarter (Q1, Q2,Q3...)
    f - WeekNumber(1,2,3...)
    g - Weekname(Monday,Tuesday...)
    h - Date range is between 2001-01-01 and 2022-12-31)

6 - Measure (Cumulative Sales for each Store) that return Cumulative Sales of each product for each Chain)

7 - Measure (Volume M0M % change) that returns % increase/decrease compared to the previous month in percentage.