# stores
Manage stores

In this exercise I would like to create three chain stores, add an inventory control. It will be simple, because the information will be in smartsheets, probably in csv. The main intent of the exercise is not to focus on extraction and modeling, but on analysis and visualization. Work on connecting tables and creating analyses, visyalizations and reports.

1. Create the tables
    - chain.A [date,store_id,product_id,volume] 
        - Accomplished (chain_a.csv)
    - chain.B [date,store_id,product_id,volume] 
        - Accomplished (chain_b.csv)
    - chain.C [date,store_id,product_id,volume] 
        - Accomplished (chain_c.csv)
    - m.product [product_id,price,product_category,product_name]
        - Accomplished (m.product.csv)
    - m.store [store_id,address,tel,zip_code] 
        - Accomplished (m.store.csv)

2. Returns the daily total volume of the three chains by product.
    - Accomplished (volume_tt.ipynb)

3. In Chain A, return daily sales of 5 most expensive products in each product_category

4. Returns 7 days moving average of volume by store by product each Chain.

5. Creates a calendar lookup table that has following information
    - Date(YYYY-MM-DD)
    - Year(YYYY)
    - Month Number(1,2,3...)
    - Month Name(Jan, Fev, Mar...)
    - Quarter (Q1, Q2,Q3...)
    - WeekNumber(1,2,3...)
    - Weekname(Monday,Tuesday...)
    - Date range is between 2001-01-01 and 2022-12-31)

6. Measure (Cumulative Sales for each Store) that return Cumulative Sales of each product for each Chain)

7. Measure (Volume M0M % change) that returns % increase/decrease compared to the previous month in percentage.