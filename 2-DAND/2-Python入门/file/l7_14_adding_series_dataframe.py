import pandas as pd

# Change False to True for each block of code to see what it does

# Adding a Series to a square DataFrame
if 0:
    s = pd.Series([1, 2, 3, 4])
    df = pd.DataFrame({
        0: [10, 20, 30, 40],
        1: [50, 60, 70, 80],
        2: [90, 100, 110, 120],
        3: [130, 140, 150, 160]
    })

    print (df)
    print ('') # Create a blank line between outputs
    print (df + s)

# Adding a Series to a one-row DataFrame
if 0:
    s = pd.Series([1, 2, 3, 4])
    df = pd.DataFrame({0: [10], 1: [20], 2: [30], 3: [40]})

    print (df)
    print ('') # Create a blank line between outputs
    print (df + s)

# Adding a Series to a one-column DataFrame
if 0:
    s = pd.Series([1, 2, 3, 4])
    df = pd.DataFrame({0: [10, 20, 30, 40]})

    print (df)
    print ('') # Create a blank line between outputs
    print (df + s)



# Adding when DataFrame column names match Series index
if 0:
    s = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
    df = pd.DataFrame({
        'a': [10, 20, 30, 40],
        'b': [50, 60, 70, 80],
        'c': [90, 100, 110, 120],
        'd': [130, 140, 150, 160]
    })

    print (df)
    print ('') # Create a blank line between outputs
    print (df + s)

# Adding when DataFrame column names don't match Series index
if 1:
    s = pd.Series([1, 2, 3, 4])
    df = pd.DataFrame({
        'a': [10, 20, 30, 40],
        'b': [50, 60, 70, 80],
        'c': [90, 100, 110, 120],
        'd': [130, 140, 150, 160]
    })

    print (df)
    print ('') # Create a blank line between outputs
    print (df + s)
