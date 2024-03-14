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
I did the benchmark on an `Apple M1 MAX MacBook Pro 2021` with `64GB RAM`, `1TB SSD`, and `10‑Core CPU`.
\
\
![output](./output.png)

## How to Run This Benchmark on Your Own
1. Download the csv file at: [2021 Yellow Taxi Trip](https://data.cityofnewyork.us/Transportation/2021-Yellow-Taxi-Trip-Data/m6nq-qud6/about_data).
2. Create `data` folder at the top level in the repo and place the csv file in the folder. The path the the file should be: `data/2021_Yellow_Taxi_Trip_Data.csv`. If you name it differently then you'll need to adjust the file path in the Python script(s).
3. Make sure you're in the virtual environment. 
```bash
python -m venv env
source env/bin/activate
```
4. Install dependencies.
```bash
pip install -r requirements.txt
```
Or
```bash
pip install duckdb polars pyarrow pytest
```
5. Run the benchmark.
```bash
python duckdb_vs_polars
```
6. Optional: Run the following command in terminal to run unit tests. 
```bash
pytest
```

