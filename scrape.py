from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

res=requests.get('https://content.codecademy.com/courses/beautifulsoup/cacao/index.html')

soup=BeautifulSoup(res.content,'html.parser')

rating_tags=soup.find_all(attrs={"class":"Rating"})

ratings=[r.get_text() for r in rating_tags][1:]
ratings=[float(r) for r in ratings]

plt.hist(ratings)
plt.show()

#top rated
company_tags=soup.find_all(attrs={"class":"Company"})

companies=list()
for tag in company_tags:
  companies.append(tag.get_text())
companies=companies[1:]

d={"Companies":companies,"Ratings":ratings}
df=pd.DataFrame.from_dict(d)

mean_ratings=df.groupby("Companies").Ratings.mean()
ten_best=mean_ratings.nlargest(10)

#ratings, percent cocoa correlation

coco_tags=soup.find_all(attrs={"class":"CocoaPercent"})
coco_tags=coco_tags[1:]
coco_percents=[float(c.get_text()[:-1]) for c in coco_tags]

df["CocoaPercentage"]=coco_percents

plt.scatter(df.CocoaPercentage,df.Ratings)
plt.show()
