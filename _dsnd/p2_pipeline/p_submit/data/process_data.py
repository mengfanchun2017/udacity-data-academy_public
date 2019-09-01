import sys
import pandas as pd
import numpy as np
import matplotlib as plt
import re

def load_data(messages_filepath, categories_filepath):
    messages = pd.read_csv(messages_filepath)
    categories = pd.read_csv(categories_filepath)
    df = categories.merge(messages, on='id')
    return df


def clean_data(df):

    # Split categories into separate category columns.
    categories = df.categories.str.split(';',expand=True)
    row = categories.iloc[0]
    pat = '(.*)[-/d]'
    row.apply(lambda x: ''.join(re.findall(pat,x)))[:5]

    # set category names
    category_colnames = []
    for i in row:
        listname = ''.join(str(ii) for ii in re.findall(pat,i))
        category_colnames.append(listname)
    categories.columns = category_colnames

    # Convert category values to just numbers 0 or 1
    for column in categories:
        categories[column] = categories[column].str[-1]
        categories[column] = categories[column].astype(str)

    # Replace categories column in df with new category columns.
    df.drop('categories', axis =1, inplace=True)
    df = pd.concat([df,categories], axis=1, join_axes=[df.index], sort=False)

    # drop duplicates
    df.drop_duplicates(inplace=True)

    return df


def save_data(df, database_filename, table_name='YourTableName'):
    engine_name = 'sqlite:///' + database_filename
    from sqlalchemy import create_engine
    engine = create_engine(engine_name)
    table_name = table_name
    df.to_sql(table_name, engine, index=False,  if_exists='replace')


def main():
    if len(sys.argv) == 4:

        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messages_filepath, categories_filepath))
        df = load_data(messages_filepath, categories_filepath)

        print('Cleaning data...')
        df = clean_data(df)
        
        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        save_data(df, database_filepath)
        
        print('Cleaned data saved to database!')
    
    else:
        print('Please provide the filepaths of the messages and categories '\
              'datasets as the first and second argument respectively, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the third argument. \n\nExample: python process_data.py '\
              'disaster_messages.csv disaster_categories.csv '\
              'DisasterResponse.db')


if __name__ == '__main__':
    main()