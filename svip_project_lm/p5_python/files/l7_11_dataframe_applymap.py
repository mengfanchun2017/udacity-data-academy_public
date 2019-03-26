import pandas as pd

# Change False to True for this block of code to see what it does

# DataFrame applymap()
if 0:
    df = pd.DataFrame({
        'a': [1, 2, 3],
        'b': [10, 20, 30],
        'c': [5, 10, 15]
    })

    def add_one(x):
        return x + 1

    print (df.applymap(add_one))
    # 就是把df的每个元素都运行一遍add_one函数

grades_df = pd.DataFrame(
    data={'exam1': [43, 81, 78, 75, 89, 70, 91, 65, 98, 87],
          'exam2': [24, 63, 56, 56, 67, 51, 79, 46, 72, 60]},
    index=['Andre', 'Barry', 'Chris', 'Dan', 'Emilio',
           'Fred', 'Greta', 'Humbert', 'Ivan', 'James']
)

def convert_grades(grades):
    '''
    Fill in this function to convert the given DataFrame of numerical
    grades to letter grades. Return a new DataFrame with the converted
    grade.

    The conversion rule is:
        90-100 -> A
        80-89  -> B
        70-79  -> C
        60-69  -> D
        0-59   -> F
    '''
    if grades >= 90:
        return 'A'
    elif grades >= 80:
        grades = 'B'
        return grades
    #注意if和elif的写法，都是可以的，但第1种直接return的更加简洁
    elif grades >= 70:
        return 'C'
    elif grades >= 60:
        return 'D'
    else:
        return 'F'

print(grades_df.applymap(convert_grades))
# 如果不使用.apply,而直接把df作为输入，就会报错：
# ValueError: The truth value of a DataFrame is ambiguous.
# 因为不知道要怎么处理df中的那么多数据，apply就明确的说每个都要处理
print(grades_df)
# 注意虽然上面做了转换但是没有写入到grades_df，所以打印df还是以前的值
