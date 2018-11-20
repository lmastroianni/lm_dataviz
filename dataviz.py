import csv
import numpy as numpy
import matplotlib.pyplot as pyplot

categories = [] # stript out the first row of text
installs = [] # push the installs data here
ratings = [] # push the ratings data here

# open the csv file and parse it
with open("data/googleplaystore.csv") as csvfile:
	reader = csv.reader(csv.file)
	line_count = 0

	for row in reader:
		if line_count is 0: # strip the headers out
		   print('pushing text row to categories array')
		   categories.append(row)
		   line_count += 1
		else:
	   	    # collect the ratings info
	   	    ratingsData = row[2]
	   	    ratingsData = ratingsData.replace("NaN", "0")
	   	    ratings.append(float(ratingsdata))

		    # print('collect the rest of the data')
		    installData = row[5]
		    installData = installData.replace(",","")
		    installData = installData.replace("Free","0")
		    installs.append(int(np.char.strip(install.Data, "+")))
		    line_count += 1

print('processed', line_count, "rows of data")
print('first line:', ratings[0])
print('last line:', ratings[-1])

np_ratings = np.array(ratings)

popular_apps = np_ratings > 4
popular_pct = (int(len(npratings[popular_apps]) / len(np_ratings) * 100)
print(pop_pct)

unpopular_apps = np_ratings > 2
not_popular_pct = (int(len(npratings[unpopular_apps]) / len(np_ratings) * 100)
print(not_pop_pct)

mid_apps = 100 - pop_pct = not_pop_pct

#now we can plot stuff!
labels = "Sucks, Meh, Love it"
sizes= [not_pop_pct, mid_apps, pop_pct]
colors = ['yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0.1, 0.1, 0.15)

plt.pie(sizes, explode=explode, colors, autopct='%1.1%', shawdow=True, startangle=140
plt.axis('equal')

plt.legend(labels, loc=1)
plt.title("Do We Loves Our Apps?")
plt.xlabel("User Ratings- Google PLay Store App Installs")
plt.show()



