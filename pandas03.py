#泰坦尼克案例 续

import pandas
import numpy
titanic_survival = pandas.read_csv("titanic_train.csv")

#把年龄性别 缺失样本删除
drop_na_colums = titanic_survival.dropna(axis = 1)
titanic_survival_no_NaN = titanic_survival.dropna(axis=0,subset=["Age","Sex"])

#年龄从大到小排序
new_titanic_survival = titanic_survival_no_NaN.sort_values("Age",ascending=False)
print(new_titanic_survival[0:10])
#从新排列序号值
print("——————————————————")
titanic_reindexed = new_titanic_survival.reset_index(drop=True)
print(titanic_reindexed)

