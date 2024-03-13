import pytest
import polars as pl
import duckdb
from polars.testing import assert_frame_equal

@pytest.fixture
def lf():
    return pl.scan_csv('data/2021_Yellow_Taxi_Trip_Data.csv')

def test_agg(lf):
    polars_df = (
        lf
        .select(
            sum=pl.col('total_amount').sum(),
            avg=pl.col('total_amount').mean(),
            min=pl.col('total_amount').min(),
            max=pl.col('total_amount').max()
        )
        .collect()
    )
    query = f'''
        select 
            sum(total_amount),
            avg(total_amount),
            min(total_amount),
            max(total_amount)
        from lf
        ;
    '''
    duckdb_df = duckdb.sql(query).pl()

    assert_frame_equal(polars_df, duckdb_df)

def test_groupby_agg(lf):
    polars_df = (
        lf
        .group_by('VendorID', 'payment_type')
        .agg(
            sum=pl.col('total_amount').sum(),
            avg=pl.col('total_amount').mean(),
            min=pl.col('total_amount').min(),
            max=pl.col('total_amount').max()
        )
        .collect()
    )
    query = f'''
        select 
            VendorID,
            payment_type,
            sum(total_amount),
            avg(total_amount),
            min(total_amount),
            max(total_amount)
        from lf
        group by
            VendorID,
            payment_type
        ;
    '''
    duckdb_df = duckdb.sql(query).pl()

    assert_frame_equal(polars_df, duckdb_df)


def test_window_func_agg(lf):
    polars_df = (
        lf
        .select(
            avg_fare_per_vendor=pl.col('fare_amount').mean().over('VendorID'),
            ttl_amt_rank_per_pay_type=pl.col('total_amount').rank(method='dense', descending=True).over('payment_type')
        )
        .collect()
    )
    query = f'''
        select 
            avg(fare_amount) over(partition by VendorID),
            dense_rank() over(partition by payment_type order by total_amount desc) 
        from lf
        ;
    '''
    duckdb_df = duckdb.sql(query).pl()

    assert_frame_equal(polars_df, duckdb_df)
