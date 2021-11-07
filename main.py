import numpy as np
import matplotlib.pyplot as plt

y = []
x = []

import pandas as pd
import statistics as st


# import mat
# Explain the concept of the project, use code as examples and write website
# showing results, concepts and code.

def calculator(catx, caty, type):
    # df = (catx,caty)
    calculate = 0
    div = 0
    slope = 0
    yInt = 0

    avCx = st.mean(catx)
    avCy = st.mean(caty)

    for i in range(len(catx)):
        calculate += ((catx[i] - avCx) * (caty[i] - avCy))
        div += (pow((catx[i] - avCx), 2))

    slope = calculate / div
    print("slope (b) = ", round(slope, 6))
    yInt = (avCy - (slope * avCx))
    print("Y-int = ", round(yInt, 2))
    print("y =(", round(slope, 6), "* x) + ", round(yInt, 6))
    print()

    # calculator(df[h], df["height"])
    # print(catx," v ",caty)
    # Not sure how to print the names of each column here
    np.random.seed(19680801)
    tickmark = round((catx.max() - catx.min()) / 10)
    N = 178
    plt.xticks(np.arange(round(catx.min()), catx.max(), tickmark))
    plt.yticks(np.arange(0, 165, 5))

    colors = np.random.rand(N)
    line_x = catx
    line_y = (slope * line_x) + yInt
    # https://stackoverflow.com/questions/3777861/setting-y-axis-limit-in-matplotlib
    # For possibly changing axis spacing or limits
    plt.plot(line_x, line_y)
    plt.xlabel(type)
    plt.ylabel("Height")
    plt.scatter(catx, caty, s=10, c=colors, alpha=0.5)
    plt.show()
    seLine = 0
    seYav = 0
    for i in range(len(df)):
        seLine = seLine + (caty[i] - ((slope * catx[i]) + yInt))
    print("SE line = ", round(seLine, 15))

    for i in range(len(df)):
        seYav += (caty[i] - avCy)
    print("SE y average = ", round(seYav, 15))

    rSq = 1 - (seLine / seYav)
    print("R Squared = ", round(rSq, 6))
    print("</\></\></\></\></\></\></\></\></\></\></\></\>")
    print()


df = pd.read_csv(r'Plant_Height_Data.csv')
# df.head()
# y_val = df.height
# x_val = df.temp
# df = df[[h, "height"]]
# headList = ["temp","rain","site","alt"]
# for h in headList:

calculator(df["temp"], df["height"], "Temperature")
calculator(df["rain"], df["height"], "Rain")
calculator(df["site"], df["height"], "Site")
calculator(df["alt"], df["height"], "Altitude")
