'''
check_sample(df)
check_detail(df,list)
check_value(df,list)
drop_column(df,list)
'''
import pprint as pp

# build function (base on solution2)
def check_sample(df):
    '''
    input: dataframe which to exam
    
    check:
    a sample of the data,
    for some feature are long and can not be show full length,
    so use this function to see all in detail.
    
    output: str
    full info from a sample with every featrue noted.
    '''
    sample = df.sample(1)
    print('----checking sample index: {}'.format(sample.index[0]))
    ### sometimes pp is uncaptible with .format
    i = 1
    for (colname, coldata) in sample.iteritems():
        print('\n- columns #{} : {:-<8}'.format(i,colname))
        print(coldata.values)
        i += 1
    pp.pprint('----checking complete----')

### original from wrangle_test_full    

# build function
def check_detail(df,list):
    '''
    input: 
    1\ dataframe which to exam
    2\ list which feature to exam
    
    check:
    s specified feature(column) 's detail data,
    for if a data in a column (e.g for comment) is so long,
    the data will not show entirely.
    
    output: str
    full data for a specific feature to show.
    '''
    sampe = df.sample(1)
    c = 1
    for i in list:
        print(('\n- columns #{} : {:-<8}'.format(c,i)))
        pp.pprint(df[i].iloc[0])
        c += 1
        ## 使用 pprint 优化 dict 显示

## build fuction
def drop_column(df,list):
    '''
    input: 
    1\ dataframe which to exam
    2\ list which feature to exam
    
    check:
    to drop a list of fearures that do not need,
    and get some extra infor for indicating which column is droped,
    for drop data is always sensitive, logs is needed.
    
    output: str
    full information for deleting featrues.
    '''
    ## proceed
    dflen = len(df.columns)
    df.drop(list,axis=1,inplace=True)
    ### 在函数中要用 inplace=True 而不是赋值来作用于df
    ## check
    print('---- proceding ----')
    print('- drop {} columns: {} '.format(len(list), list))
    print('- remain {} columns'.format(len(df.columns)))
    print('- success : {}'.format(len(list) + len(df.columns) == dflen))


# build function
def check_value(df,list):
    for i in list:
        print(('\n- columns: {:-<8}'.format(i)))
        print((df[i].value_counts()))


# build function
def check_value1(df,show_list):
    '''
    input: 
    1\ dataframe which to exam
    2\ list which feature to exam
    
    check:
    and if features are many, columns will be hide,
    checks specified feature(column) for values,
    for category feature,
    then we can see the featrue's value distribution.
    a sample of the data,
    
    output: str
    full info from a specific feature value distribution.
    '''
    
    c = 1
    for i in show_list:
        print(('\n- columns #{} : {:-<8}'.format(c,i)))
        print((df[i].value_counts().nlargest(5)))
        ### nlargest 非常好用
        c += 1
    pp.pprint('----checking complete----')