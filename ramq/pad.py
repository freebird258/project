import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("./train.csv")

mean = df['Age'].mean()
df['Age'] = df['Age'].fillna(mean)
df['Age'].count()

#fig = plt.figure()
#ax = fig.add_subplot(1,1,1)
#ax.hist(df['Age'],bins=10)
#plt.title("test")
#plt.xlabel('Age')
#plt.ylabel('Count of people')
#plt.show()

temp1 = df.groupby('Pclass').Survived.count()
temp2 = df.groupby('Pclass').Survived.sum()/df.groupby('Pclass').Survived.count()
#fig = plt.figure(figsize(8,4))
fig = plt.figure()
ax1 =  fig.add_subplot(121)
ax1.set_xlabel('Pclass')
ax1.set_ylabel('Count of Passengers')
ax1.set_title('Passengers by Pclass')
temp1.plot(kind='bar')
plt.show()
