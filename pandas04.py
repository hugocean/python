#通过自定义函数 执行你需要的操作

import pandas
import numpy

titanic_survival = pandas.read_csv("titanic_train.csv")
#定义一个函数 查找第100行数据
def hundredth_row(column):
    hundredth_item = column.loc[99]
    return hundredth_item

hundredth_row = titanic_survival.apply(hundredth_row)
print(hundredth_row)

print("__________________________________")
#定义一个函数查找每一列缺失值的个数
def not_null_count(column):
    column_null = pandas.isnull(column)
    null = column[column_null]
    return len(null)

colum_null_count = titanic_survival.apply(not_null_count)
print(colum_null_count)
print("__________________________________")
#对船舱等级进行分析
def which_class(row):
    pclass = row['Pclass']
    if pandas.isnull(pclass):
        return "Unknown"
    elif pclass == 1:
        return "First Class"
    elif pclass == 2:
        return "Second Class"
    elif pclass == 3:
        return "Third Class"

classes = titanic_survival.apply(which_class, axis=1)
print (classes)
print("__________________________________")
#对乘客年龄进行分析 小于18岁的
def is_minor(row):
    if row["Age"] < 18:
        return True
    else:
        return False

minors = titanic_survival.apply(is_minor, axis=1)
print (minors)

print("__________________________________")

#年龄阶层
def generate_age_label(row):
    age = row["Age"]
    if pandas.isnull(age):
        return "unknown"
    elif age < 18:
        return "minor"
    else:
        return "adult"

age_labels = titanic_survival.apply(generate_age_label, axis=1)
print (age_labels)

print("__________________________________")
#没个年龄层的获救几率
titanic_survival['age_labels'] = age_labels
age_group_survival = titanic_survival.pivot_table(index="age_labels", values="Survived")
print (age_group_survival)