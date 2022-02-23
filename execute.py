"""
This file will read the data from input json data, evaluates BMI,
and store back the output back in one json file

USAGE: execute.py [Options]

Options:
    --input_file    Input File Name with absolute path
    --output_file   Output File Name with absolute path
"""

import click
import pandas as pd
from pandas.core.frame import DataFrame
import os


def _get_input_file(input_file: str) -> DataFrame:
    with open(input_file, 'r') as f:
        return pd.read_json(f, orient='records')


def _write_csv(df: DataFrame, output_file: str) -> str:
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    return df.to_csv(output_file, index=False)


def compute_bmi(weight: int, height: int) -> float:
    if weight is None or height is None:
        return None
    return round(weight / ((height/100)**2), 1)


def generate_category(bmi: float) -> str:
    category = None
    if bmi is None:
        return category
    if bmi <= 18.4:
        category = 'Underweight'
    if (bmi >= 18.5) and (bmi <= 24.9):
        category = 'Normal weight'
    if (bmi >= 25) and (bmi <= 29.9):
        category = 'Overweight'
    if (bmi >= 30) and (bmi <= 34.9):
        category = 'Moderately obese'
    if (bmi >= 35) and (bmi <= 39.9):
        category = 'Severely obese'
    if bmi >= 40:
        category = 'Very severely obese'
    return category


def generate_risk(category: str) -> str:
    category_risk_map: dict = {
        'Underweight': 'Malnutrition risk',
        'Normal weight': 'Low risk',
        'Overweight': 'Enhanced risk',
        'Moderately obese': 'Medium risk',
        'Severely obese': 'High risk',
        'Very severely obese': 'Very high risk'
    }
    if category is None and category not in category_risk_map.keys():
        return None
    return category_risk_map[category]


def apply(df: DataFrame) -> DataFrame:
    df['bmi'] = df.apply(lambda row: compute_bmi(row['WeightKg'], row['HeightCm']), axis=1)
    df['category'] = df.apply(lambda row: generate_category(row['bmi']), axis=1)
    df['risk'] = df.apply(lambda row: generate_risk(row['category']), axis=1)
    return df


@click.command()
@click.option('--input_file', type=str, help='Input File Name', default='resources/sampledata.json', required=True)
@click.option('--output_file', type=str, help='Output File Name', default='resources/sampleoutput.csv', required=True)
def main(input_file: str, output_file: str):
    df = apply(_get_input_file(input_file))
    _write_csv(df, output_file)


if __name__ == '__main__':
    main()
