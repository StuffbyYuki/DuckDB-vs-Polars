import duckdb

def window_func_duckdb(file_path):
    query = f'''
        select 
            avg(fare_amount) over(partition by VendorID),
            dense_rank() over(partition by payment_type order by total_amount desc) 
        from "{file_path}"
        ;
    '''
    return duckdb.sql(query).arrow()

if __name__ == '__main__':
    print(window_func_duckdb('data/2021_Yellow_Taxi_Trip_Data.csv'))