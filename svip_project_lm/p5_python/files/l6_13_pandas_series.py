import pandas as pd

countries = ['Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda',
             'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan',
             'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus',
             'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia']

life_expectancy_values = [74.7,  75. ,  83.4,  57.6,  74.6,  75.4,  72.3,  81.5,  80.2,
                          70.3,  72.1,  76.4,  68.1,  75.2,  69.8,  79.4,  70.8,  62.7,
                          67.3,  70.6]

gdp_values = [ 1681.61390973,   2155.48523109,  21495.80508273,    562.98768478,
              13495.1274663 ,   9388.68852258,   1424.19056199,  24765.54890176,
              27036.48733192,   1945.63754911,  21721.61840978,  13373.21993972,
                483.97086804,   9783.98417323,   2253.46411147,  25034.66692293,
               3680.91642923,    366.04496652,   1175.92638695,   1132.21387981]

# Life expectancy and gdp data in 2007 for 20 countries
life_expectancy = pd.Series(life_expectancy_values)
gdp = pd.Series(gdp_values)

# Change False to True for each block of code to see what it does

# Accessing elements and slicing
if False:
    print (life_expectancy[0])
    # print (gdp[3:6])

# Looping
if False:
    for country_life_expectancy in life_expectancy:
        print ('Examining life expectancy {}'.format(country_life_expectancy))

# Pandas functions
if False:
    print (life_expectancy.mean())
    print (life_expectancy.std())
    print (gdp.max())
    print (gdp.sum())

# Vectorized operations and index arrays
if False:
    a = pd.Series([1, 2, 3, 4])
    b = pd.Series([1, 2, 1, 2])

    print (a + b)
    print (a * 2)
    print (a >= 3)
    print (a[a >= 3])

def variable_correlation(variable1, variable2):
    '''
    Fill in this function to calculate the number of data points for which
    the directions of variable1 and variable2 relative to the mean are the
    same, and the number of data points for which they are different.
    Direction here means whether each value is above or below its mean.

    You can classify cases where the value is equal to the mean for one or
    both variables however you like.

    Each argument will be a Pandas series.

    For example, if the inputs were pd.Series([1, 2, 3, 4]) and
    pd.Series([4, 5, 6, 7]), then the output would be (4, 0).
    This is because 1 and 4 are both below their means, 2 and 5 are both
    below, 3 and 6 are both above, and 4 and 7 are both above.

    On the other hand, if the inputs were pd.Series([1, 2, 3, 4]) and
    pd.Series([7, 6, 5, 4]), then the output would be (0, 4).
    This is because 1 is below its mean but 7 is above its mean, and
    so on.
    '''
    both_above = (variable1 > variable1.mean()) & \
        (variable2 > variable2.mean())
    both_below = (variable1 < variable1.mean()) & \
        (variable2 < variable2.mean())
    #life_expectancy_b = (life_expectancy >= life_expectancy.mean())
    #gdp_b = (gdp >= gdp.mean())
    #both_b = life_expectancy_b & gdp_b
    #both_b1 = not (life_expectancy_b | gdp_b)
    #print(life_expectancy_b)
    #print(gdp_b)
    #print(both_b.any())
    #print(both_b.bool())

    #print (life_expectancy_b, gdp_b, life_expectancy_b | gdp_b)

    is_same_direction = both_above | both_below
    num_same_direction = is_same_direction.sum()
    print(is_same_direction, num_same_direction)
    # .sum()就是求和，因为ture是1所以所有true的加起来就是17了
    num_different_direction = len(variable1) - num_same_direction

    return (num_same_direction, num_different_direction)

print(variable_correlation(life_expectancy, gdp))

# https://stackoverflow.com/questions/36921951/truth-value-of-a-series-is-ambiguous-use-a-empty-a-bool-a-item-a-any-o
# 如何使用布尔判断符将0转化为1？除了循环还有别的方式么。没有意义，但不知道怎么简单翻转
