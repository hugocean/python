#泰坦尼克案例

import pandas
import numpy
titanic_survival = pandas.read_csv("titanic_train.csv")
#处理缺失值 NaN  如果数据中有缺失值 在处理数据是会输出错误NaN
age = titanic_survival["Age"]
age_is_null = pandas.isnull(age) #是否是缺失值 输出True or False
age_null_true = age[age_is_null] #会帮我们把True都保留下来 把False 过滤
age_null_count = len(age_null_true) #python自带的函数 输出确实值的个数
#处理缺失值的一种方法 把缺失值去掉 算平均年龄(两种方法)
good_age = titanic_survival["Age"][age_is_null == False]
# correct_mean_age = sum(good_age) / len(good_age)
# print(correct_mean_age)
correct_mean_age = titanic_survival["Age"].mean()
print(correct_mean_age)

#每个船舱等级价格的平均值
passenger_classes = [1,2,3]
fares_by_class = {}
for this_class in passenger_classes:
    pclass_rows = titanic_survival[titanic_survival["Pclass"] == this_class]  #存储等级相等船舱的数据
    pclass_fares = pclass_rows["Fare"] #将等级相等船舱的价格这一列 输入到一个数组中
    fares_for_class = pclass_fares.mean() #求平均
    fares_by_class[this_class] = fares_for_class #输出到字典中
print(fares_by_class)

#pivot_table函数:统计一个量和其他量关系之间的一个函数
passenger_survival = titanic_survival.pivot_table(index="Pclass",values="Survived",aggfunc=numpy.mean)
print(passenger_survival)

passenger_age = titanic_survival.pivot_table(index="Pclass",values="Age") #如果不写aggfunc 默认求均值
print(passenger_age)

passenger_fare = titanic_survival.pivot_table(index="Pclass",values="Fare")
print(passenger_fare)

passenger_stats = titanic_survival.pivot_table(index="Embarked",values=["Fare","Survived"],aggfunc=numpy.sum)
print(passenger_stats)

#把缺失值删除
drop_na_colums = titanic_survival.dropna(axis = 1)
new_titanic_survival = titanic_survival.dropna(axis=0,subset=["Age","Sex"])

#定位到一个具体值 第83号样本的年纪
row_index_83_age = titanic_survival.loc[83,"Age"]
print(row_index_83_age)

