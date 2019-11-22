'''
function list:
1 /check df/
-1.1 checkdf(df) - 基准df信息输出
-1.2 checksample(df,random=42) - 对于列信息很多或者嵌套的,详细输出一个
2 /check column/
-2.1 checknest(df,colname) - 嵌套diclike信息输出
-2.2 checkvalue(df,list='all') - 检查指定列的value分布
3 /alter data/
-3.1 dorpcolumn(df,collist) - 删除列
'''


# prepare env
#需要使用 display 显示和 jupyter output 一样的样式
from IPython.display import display
import pprint as pp


# section1
def checkdf(df):
    '''
    input: dataframe which to exam
    
    check:
    shape, info, head, tail, null
    for some feature are long and can not be show full length,
    so use this function to see all in detail.
    
    output: str
    '''
    print('---checking start---')

    displaystr = "check shape"
    print('\n', displaystr.center(40, '-'))
    print(df.shape)

    displaystr = "check info"
    print('\n', displaystr.center(40, '-'))
    print(df.info())

    displaystr = "check head and tail"
    print('\n', displaystr.center(40, '-'))
    display(df.head(1))
    display(df.tail(1))

    displaystr = "check null"
    print('\n', displaystr.center(40, '-'))
    print(df.isnull().sum())

    print('---checking complete---')


def checkdup(df):
    '''
    input: dataframe which to exam
    
    check:
    duplicated info of the data,
    if there are columns contain interabel, will enconter a error,
    use try/except to warining if so.
    
    output: str
    '''
    displaystr = " check duplicate "
    print('\n', displaystr.center(40, '-'))

    try:
        numdup = df.duplicated().sum()
    except TypeError:
        displaystr = ' Found List like, cant check '
        print('\n', displaystr.center(40, '-'))
    else:
        prestr = ' duplicated No.: ' + str(numdup) + ' '
        print('\n', prestr.center(40, '-'))
        if numdup > 0:
            df[df.duplicated()]
            #further add subset and show paras
    finally:
        pass

    print('---checking complete---')

    #We can deduce from this error that df.duplicated is using set to determine the duplicates, hence all objects in the series must be hashable. Lists are not hashable.
    #https://stackoverflow.com/questions/50020231/pandas-typeerror-unhashable-type-list


def checksample(df,random=42):
    '''
    input: dataframe which to exam
    
    check:
    a sample of the data,
    for some feature are long and can not be show full length,
    so use this function to see all in detail.
    
    output: str
    '''
    sample = df.sample(1,random_state=random)
    print('---checking sample index: {}---'.format(sample.index[0]))
    for (colname, coldata) in sample.iteritems():
        print('\n- columns : {:-<16}'.format(colname))
        print(coldata.values)
    print('---checking complete---')


# section2
def checkvalue(df, list='all'):
    '''
    input: 
    1 dataframe which to exam value distribution
    2 list which feature to exam, if omit will exam all list
    
    check:
    checks specified feature(column) for values,
    for category feature,
    then we can see the featrue's value distribution.
    show 5 largest and 10 smallest.
    
    output: str
    '''
    if list == 'all':
        list = df.columns.tolist()
    for i in list:
        print('\n-check column value: {:-^16}'.format(i))
        print('largest:\n', df[i].value_counts().nlargest(5))
        print('smallest\n:', df[i].value_counts().nsmallest(10))
    print('---checking complete---')


def checknest(df,colname):
    '''
    input: 
    1 dataframe which to exam
    2 column which is nested dict format
    
    check:
    s specified nested feature(column) 's detail data,
    for if a data in a column which is nested it is not easy for a long info to show.
    ! currently only work for 1 nested dict format !
    
    output: str
    '''
    print('\n // checking nested data: {} //'.format(colname))
    sample = df[colname].sample(1)
    pp.pprint(sample.values[0])
    #使用 pprint 优化 dict 显示


# section3
def dropcolumn(df,list):
    '''
    input: 
    1 dataframe which to exam
    2 list which feature to exam
    
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
    print('---proceding---')
    print('- drop {} columns: {} '.format(len(list), list))
    print('- remain {} columns'.format(len(df.columns)))
    print('- success : {}'.format(len(list) + len(df.columns) == dflen))


# section to be
#https://stackoverflow.com/questions/13383244/python-centre-string-using-format-specifier
#居中显示