import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import preprocessing

#My aim here is to check that the students of which category score good in which subject

df=pd.read_csv('StudentsPerformance.csv')
#print(df.tail())

#Performing EDA
'''
print(df.describe())
'''
#checking for null values if any
'''
print(df.isnull().values)
'''

#converting race/ethnicity columns that has text to numeric groups
df['race/ethnicity']=df['race/ethnicity'].replace(['group A'],1)
df['race/ethnicity']=df['race/ethnicity'].replace(['group B'],2)
df['race/ethnicity']=df['race/ethnicity'].replace(['group C'],3)
df['race/ethnicity']=df['race/ethnicity'].replace(['group D'],4)
df['race/ethnicity']=df['race/ethnicity'].replace(['group E'],5)


#converting parental education columns that has text to numeric groups
df['parental level of education']=df['parental level of education'].replace(['some high school'],1)
df['parental level of education']=df['parental level of education'].replace(['high school'],2)
df['parental level of education']=df['parental level of education'].replace(["associate's degree"],3)
df['parental level of education']=df['parental level of education'].replace(["master's degree"],4)
df['parental level of education']=df['parental level of education'].replace(['some college'],5)
df['parental level of education']=df['parental level of education'].replace(["bachelor's degree"],6)


#dropping unnecessary columns
del df['lunch']

#grouping course
df['test preparation course']=df['test preparation course'].replace(["none"],0)
df['test preparation course']=df['test preparation course'].replace(["completed"],1)

#grouping gender
df['gender']=df['gender'].replace(["female"],0)
df['gender']=df['gender'].replace(["male"],1)

print(df.head())

#Finding corelations
#1.Between race and panrental education
'''
sns.histplot(x=df['race/ethnicity'],y=df['parental level of education'])
plt.show()
'''

#2.Between gender and marks scored in each subject
'''
sns.boxplot(x=df['gender'],y=df['math score'],data=df)
plt.show()

sns.boxplot(x=df['gender'],y=df['reading score'],data=df)
plt.show()

sns.boxplot(x=df['gender'],y=df['writing score'],data=df)
plt.show()
'''


#3. Between parental education and scores
'''
sns.boxplot(x=df['parental level of education'],y=df['math score'],data=df)
plt.show()

sns.boxplot(x=df['parental level of education'],y=df['reading score'],data=df)
plt.show()

sns.boxplot(x=df['parental level of education'],y=df['writing score'],data=df)
plt.show()
'''

#4. Preparation vs scores
sns.boxplot(x=df['test preparation course'],y=df['math score'],data=df)
plt.show()

sns.boxplot(x=df['test preparation course'],y=df['reading score'],data=df)
plt.show()

sns.boxplot(x=df['test preparation course'],y=df['writing score'],data=df)
plt.show()

#Conclusions:

'''
1. It is observed that the female candidates did exceptionally well compared to the male in math
2. Male candidates did exceptionally well in the other two subjects
3. Students whose parents have a master degree have done well in all the three courses
4. It was obvious that students who had test preparation course did better than the one's who didnt in all the three subjects
5.Thus all the conclusions were made.
Further conclusions can also be made if you spend some more time
'''









