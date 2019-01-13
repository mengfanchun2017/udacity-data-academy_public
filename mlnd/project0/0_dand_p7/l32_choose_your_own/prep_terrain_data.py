#!/usr/bin/python
import random


def makeTerrainData(n_points=1000):
###############################################################################
### make the toy dataset
    #print('\n---testing start---\n')
    random.seed(42)
    # 用ii是习惯，可能是暗示数据是在元祖嵌套2层输出的，无影响
    grade = [random.random() for ii in range(0,n_points)]
    #print('\n---testing---')
    #print(grade)
    bumpy = [random.random() for ii in range(0,n_points)]
    #print('\n---testing---')
    #print(bumpy)
    error = [random.random() for ii in range(0,n_points)]
    #print('\n---testing---')
    #print(error)
    # 下面通过round的方式把grade和bumpy和errro组合，把y定义到0或者1
    y = [round(grade[ii]*bumpy[ii]+0.3+0.1*error[ii]) for ii in range(0,n_points)]
    #print('\n---testing---')
    #print(y)
    #print('\n')
    # 下面是对上面生成的y进行一个修正（数量不少）
    # 因为修正是将y改为1.0浮点型，所以可以在输出中看出（round生成的是1）
    for ii in range(0, len(y)):
        if grade[ii]>0.8 or bumpy[ii]>0.8:
            #为了统一，改为1注释掉的是原代码
            #y[ii] = 1.0
            y[ii] = 1

### split into train/test sets
    # 通过zip建立X的列表，包括x和y坐标（这也是为什么要用X大写暗示的原因，可以参考，小写也ok的
    X = [[gg, ss] for gg, ss in zip(grade, bumpy)]
    #print('\n---testing---')
    #print(X)
    # 简单粗暴的通过list的片选择进行拆分
    # 因为前面是随机的，这里就没有用
    # 也可以用random choice进行拆分
    split = int(0.75*n_points)
    X_train = X[0:split]
    X_test  = X[split:]
    y_train = y[0:split]
    y_test  = y[split:]

    # 此处是将上述的list转化为dict的处理，在输出中并没有调用
    '''
    # 将train数据根据y的0、1信息进行标签化分组，将X的grade和bumpy写入字典
    grade_sig = [X_train[ii][0] for ii in range(0, len(X_train)) if y_train[ii]==0]
    bumpy_sig = [X_train[ii][1] for ii in range(0, len(X_train)) if y_train[ii]==0]
    grade_bkg = [X_train[ii][0] for ii in range(0, len(X_train)) if y_train[ii]==1]
    bumpy_bkg = [X_train[ii][1] for ii in range(0, len(X_train)) if y_train[ii]==1]

    training_data = {"fast":{"grade":grade_sig, "bumpiness":bumpy_sig}
            , "slow":{"grade":grade_bkg, "bumpiness":bumpy_bkg}}

    # 同上处理test数据
    grade_sig = [X_test[ii][0] for ii in range(0, len(X_test)) if y_test[ii]==0]
    bumpy_sig = [X_test[ii][1] for ii in range(0, len(X_test)) if y_test[ii]==0]
    grade_bkg = [X_test[ii][0] for ii in range(0, len(X_test)) if y_test[ii]==1]
    bumpy_bkg = [X_test[ii][1] for ii in range(0, len(X_test)) if y_test[ii]==1]

    test_data = {"fast":{"grade":grade_sig, "bumpiness":bumpy_sig}
            , "slow":{"grade":grade_bkg, "bumpiness":bumpy_bkg}}
    '''
    return X_train, y_train, X_test, y_test

# testing output
# print(type(makeTerrainData()))
# print(makeTerrainData()[3])
# 经过测试，输出是4个元素的元祖


print(makeTerrainData(30))