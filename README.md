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

## Result 
![output](./output.png)

## How to run this benchmark on your own
1. Download the csv file at: [2021 Yellow Taxi Trip](https://data.cityofnewyork.us/Transportation/2021-Yellow-Taxi-Trip-Data/m6nq-qud6/about_data).
2. Create `data` folder at the top level in the repo and place the csv file in the folder. The path the the file should be: `data/2021_Yellow_Taxi_Trip_Data.csv`. If you name it differently then you'll need to adjust the file path in the Python script(s).
3. Make sure you're in the virtual environment. 
```bash
python -m venv env
source env/bin/activate
```
4. Run the benchmark.
```bash
python duckdb_vs_polars
```
5. Optional: Run the following command in terminal to run unit tests. 
```bash
pytest
```

