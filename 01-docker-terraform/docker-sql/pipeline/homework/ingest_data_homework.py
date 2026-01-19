#!/usr/bin/env python
# coding: utf-8

import click
import pandas as pd
from sqlalchemy import create_engine
from tqdm.auto import tqdm

@click.command()
@click.option('--pg-user', default='root', help='PostgreSQL user')
@click.option('--pg-pass', default='root', help='PostgreSQL password')
@click.option('--pg-host', default='pgdatabase', help='PostgreSQL host')
@click.option('--pg-port', default=5432, type=int, help='PostgreSQL port')
@click.option('--pg-db', default='ny_taxi', help='PostgreSQL database name')
@click.option('--target-table', default='yellow_taxi_data', help='Target table name')
@click.option('--chunksize', default=100000, type=int, help='Chunk size for writing to DB')
@click.option('--url', default=None, help='URL of the data file (CSV or Parquet)')
def run(pg_user, pg_pass, pg_host, pg_port, pg_db, target_table, chunksize, url):
    """Ingest NYC taxi data into PostgreSQL database."""

    engine = create_engine(f'postgresql://{pg_user}:{pg_pass}@{pg_host}:{pg_port}/{pg_db}')

    if url.endswith('.parquet'):
        df = pd.read_parquet(url)
        for i in tqdm(range(0, len(df), chunksize)):
            df_chunk = df.iloc[i:i + chunksize]
            df_chunk.to_sql(
                name=target_table,
                con=engine,
                if_exists='replace' if i == 0 else 'append'
            )
    else:
        df_iter = pd.read_csv(url, iterator=True, chunksize=chunksize)
        first = True
        for df_chunk in tqdm(df_iter):
            if first:
                df_chunk.head(0).to_sql(name=target_table, con=engine, if_exists='replace')
                first = False
            df_chunk.to_sql(name=target_table, con=engine, if_exists='append')

if __name__ == '__main__':
    run()