# src/dataops/preprocess.py
import numpy as np
import click
# from sklearn. ... # import joblib from sklearn.external

def get_label():
    pass

def get_features():
    pass

def read_raw_data(fname='data/raw/iris.csv'):
    # read the raw data 
#     data = {'X': X, 'y': y}
#     return data
    pass

def preprocess_data(data):
    pass

def read_processed_data(fname='data/processed/processed.pkl'):
    """Note: pathname is relative to the PROJ_ROOT
    because we assume this script will be called in PROJ_ROOT
    """
    pass

@click.command()
@click.argument('input_file', type=click.Path(exists=True, readable=True, dir_okay=False))
@click.argument('output_file', type=click.Path(writable=True, dir_okay=False))
@click.option('--excel', type=click.Path(writable=True, dir_okay=false))
def main(input_file, output_file, excel):
    print('Preprocessing data')
    data = read_raw_data(input_file)
    data = preprocess_data(data)
    
    joblib.dump(data, output_file)
    if excel is not None:
        data.to_excel(excel) #todo: works only if data is a pd.DataFrame object
    
if __name__ = '__main__':
    main()
    