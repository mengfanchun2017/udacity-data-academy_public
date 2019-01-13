# Import, read, and split data
import pandas as pd
data = pd.read_csv('data.csv')
import numpy as np
from sklearn.model_selection import learning_curve
X = np.array(data[['x1', 'x2']])
y = np.array(data['y'])

# Fix random seed
np.random.seed(55)

### Imports
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.svm import SVC

# TODO: Uncomment one of the three classifiers, and hit "Test Run"
# to see the learning curve. Use these to answer the quiz below.

### Logistic Regression
#estimator = LogisticRegression()

### Decision Tree
estimator = GradientBoostingClassifier()

### Support Vector Machine
#estimator = SVC(kernel='rbf', gamma=1000)

#num_trainings = 10
#train_sizes, train_scores, test_scores = learning_curve(
#    estimator, X, y, cv=None, n_jobs=1, train_sizes=np.linspace(.1, 1.0, num_trainings))
#

# Plotting

#from utils import randomize
from utils import draw_learning_curves

#randomize(X, y)

# 阶数要比数据点少（100个，60个训练，20个交叉验证，20个测试）
draw_learning_curves(X, y, estimator, 60)
# draw_learning_curves(X, y, estimator,num_trainings)
# 按照官网的说明实际上是默认调用5 train_sizes=np.linspace(.1, 1.0, 5)
# 但是例子执行说少一个参数，可能和函数有关系，再研究