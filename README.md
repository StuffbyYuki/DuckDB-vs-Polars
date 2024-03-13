# DuckDB vs Polars
Unofficial Benchmarking on Performance Difference Between DuckDB and Polars.

## Data
[2021 Yellow Taxi Trip](https://data.cityofnewyork.us/Transportation/2021-Yellow-Taxi-Trip-Data/m6nq-qud6/about_data) that contains 30M rows with 18 columns. It's about 3GB in size on disk. 

## Method
Using the following operations for the benchmark:
- Reading a csv file
- Simple aggregations (sum, mean, min, max)
- Groupby aggregations
- Window functions
- Joins
- Writing to a file
