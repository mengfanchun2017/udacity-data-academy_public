import sys
# import library
import pandas as pd
import numpy as np
import matplotlib as plt
import re
import pickle
from sqlalchemy import create_engine

import pprint as pp

# import ml library
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score,f1_score,recall_score
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer


def load_data(database_filepath):
    '''
    function: load data
    input: sql datafile
    output: X,y data to train model
    env: sqlalchemy, pandas
    '''
    engine_name = 'sqlite:///' + database_filepath
    engine = create_engine(engine_name)
    df = pd.read_sql_table('YourTableName',con=engine)
    X = df['message']
    y = df[df.columns[5:]]
    
    return X,y

def tokenize(text):
    '''
    function: get text to tokens, includes
        - tokenize
        - lemmatize
    input: text
    output: tokens
    env: WordNetLemmatizer, word_tokenize
    '''
    tokens = word_tokenize(text)
    lemmatizer = WordNetLemmatizer()
    
    clean_tokens = []
    for tok in tokens:
        clean_tok = lemmatizer.lemmatize(tok).lower().strip()
        clean_tokens.append(clean_tok)
    
    return clean_tokens


def build_model():
    '''
    function: build model
        - set pipeline
        - set parameters
        - set cv
    input: none
    output: cv
    env: sklearn
    '''
    pipeline = Pipeline([
        ('vect', CountVectorizer(tokenizer=tokenize)),
        ('tfidf', TfidfTransformer()),
        ('clf', RandomForestClassifier())
    ])

    # specify parameters for grid search
    parameters = {
        'vect__max_df': (0.75, 1.0),
        'vect__max_features': (None, 5000),
        'tfidf__use_idf': (True, False),
        'clf__n_estimators': [50, 100],
        'clf__min_samples_split': [3, 4],
    }

    # create grid search object
    cv = GridSearchCV(pipeline, param_grid=parameters)
    
    #return pipeline
    return cv

def evaluate_model(model, X_test, Y_test, category_names):
    '''
    function: evaluate model
    input: model, X_test, Y_test, category_names
    output: reports
    env: sklearn
    '''
    y_pred = model.predict(X_test)
    #target_names = df.columns[5:]
    #reports = classification_report(Y_test,y_pred,target_names=target_names)
    reports = classification_report(Y_test,y_pred)
    return reports


def save_model(model, model_filepath):
    '''
    function: save model
    input: model, model_filepath
    output: pickle file
    env: pickle
    '''
    pickle.dump(model, open(model_filepath, 'wb'))


def main():
    '''
    function: main function
    '''
    if len(sys.argv) == 3:
        database_filepath, model_filepath = sys.argv[1:]
        print('Loading data...\n    DATABASE: {}'.format(database_filepath))
        X, Y, category_names = load_data(database_filepath)
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
        
        print('Building model...')
        model = build_model()
        
        print('Training model...')
        model.fit(X_train, Y_train)
        
        print('Evaluating model...')
        evaluate_model(model, X_test, Y_test, category_names)

        print('Saving model...\n    MODEL: {}'.format(model_filepath))
        save_model(model, model_filepath)

        print('Trained model saved!')

    else:
        print('Please provide the filepath of the disaster messages database '\
              'as the first argument and the filepath of the pickle file to '\
              'save the model to as the second argument. \n\nExample: python '\
              'train_classifier.py ../data/DisasterResponse.db classifier.pkl')


if __name__ == '__main__':
    main()