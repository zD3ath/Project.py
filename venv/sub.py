import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


class Stats:

    def first(self):
        countries: object = pd.read_excel(r"C:\Users\Jun Han\Desktop\python\Lab 10\Travellers.xlsx")
        #122-241
        Cunt_List=[19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
        #print(Stats.countries)
        df = countries
        df = df.iloc[:,lambda df:[0,19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]]
        df2 = df.set_index('Unnamed: 0')
        df2 = df2.loc['1978 Jan':'1987 Dec']

        Sums = df2.sum(axis=0)
        print(Sums)
        Sums = Sums.sort_values(ascending=False)
        #print(Sums)

        mos1 = Sums.index[0]
        mos2 = Sums.index[1]
        mos3 = Sums.index[2]
        print("The top 3 countries with the most visitors are", mos1 ,",", mos2,"&", mos3)

        vis1 = Sums[mos1]
        vis2 = Sums[mos2]
        vis3 = Sums[mos3]
        print("The Amount of visitors from the top 3 countries are", vis1 ,",", vis2,"&", vis3, "respectively")

        means = df2.mean(axis=0)
        means = means.sort_values(ascending=False)
        #print (means)
        mean1 = round(means[0],2)
        mean2 = round(means[1],2)
        mean3 = round(means[2],2)
        print("The Average visitors from the top 3 countries are", mean1 ,",", mean2 ,"&", mean3, "respectively")

        medians = df2.median(axis=0)
        medians = medians.sort_values(ascending=False)
        #print (medians)
        med1 = medians[0]
        med2 = medians[1]
        med3 = medians[2]
        print("The Median visitors from the top 3 countries are", med1 ,",", med2 ,"&", med3, "respectively")


        date_sum = df2.sum(axis=1)
        months = np.zeros((12,), dtype=int).tolist()
        month_names = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
        for j in range(0,12):
            for i in np.arange(j,120,12):
                months[j] += date_sum.iat[i]
        topone = [mos1]
        toptwo = [mos2]
        topthree = [mos3]
        topnumber = [vis1,vis2,vis3]
        topcountry = [mos1,mos2,mos3]
        meannumber = [mean1,mean2,mean3]
        #print (months)
        plt.title("Total amount of visitors from Top 3 Countries")
        plt.ticklabel_format(style='plain')
        plt.plot(topcountry,topnumber)
        plt.show()

        #plt.title("Mean amount of visitors from top 3 countries")
        #plt.pie(meannumber, labels=topcountry)
        #plt.show()

        plt.title("Mean amount of visitors from top 3 countries")
        plt.pie(meannumber, labels=topcountry, autopct='%2.f %%')
        plt.show()

        #df = pd.DataFrame(np.random.rand(50, 4), columns=["a", "b", "c", "d"])

        #ax = df.plot.scatter(x="a", y="b", color="DarkBlue", label=topone)
        #xa = df.plot.scatter(x="c", y="d", color="DarkGreen", label=toptwo, ax=ax)
        #df.plot.scatter(x="c", y="d", color="DarkGreen", label=topthree, ax=ax, xa=xa)
        #plt.show()

stats = Stats()

stats.first()
#print("first : " + str(stats.first()))