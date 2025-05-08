#!/usr/bin/env python
import argparse
from pyspark.sql import SparkSession

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_appearances', required=True)
    parser.add_argument('--input_competitions', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()

    spark = SparkSession.builder \
        .appName('test') \
        .config('spark.sql.legacy.allowCreatingManagedTableUsingNonemptyLocation', 'true') \
        .getOrCreate()

    spark.conf.set('temporaryGcsBucket', 'dataproc-temp-asia-southeast1-1026077313769-iixm4lww')

    # Read data
    df_appearances = spark.read.parquet(args.input_appearances)
    df_competitions = spark.read.parquet(args.input_competitions)

    # Explicitly handle column ambiguity
    join_columns = ['competition_id']
    df_data_all = df_appearances.join(
        df_competitions,
        on=join_columns,
        how='left'
    )

    # Write to BigQuery with overwrite
    df_data_all.write.format('bigquery') \
        .option('table', args.output) \
        .mode('overwrite') \
        .save()

if __name__ == '__main__':
    main()