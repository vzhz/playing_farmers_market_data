import csv
f = open('farmers-markets.csv')
csv_f = csv.reader(f)

### instructions from https://newcircle.com/s/post/1572/python_for_beginners_reading_and_manipulating_csv_files#opening-a-csv-file ###
#test that csv file has been read in
#for row in csv_f:
#	print row
#for col in csv_f:
#	print col #why doesn't this work?

#########################################
#seperate elements in CSV file into rows and columns
#########################################
matrix = []

for line in csv_f:
	matrix.append(line)

header = matrix[0][:]
data = matrix[1:][:]
#########################################
#Since all questions ask us to exclude markets located within a city > one word in name,
#copy only entries with one-word city names to a new file and pull information from that file.
#########################################

#created farmers-markets-one-word-cities.csv in the terminal with subl farmers-markets-one-word-cities.csv
#when this didn't work (still not sure why), I created the file by hand (I decided to save my googling energy for learning things I didn't have another solution for)
#at this point, I realized how long I had been working just to read the file so I decided to answer the questions using excel, which I am more familiar with, but the idea of manipulating thousands of entries by hand made me swallow my pride and ask some questions to get myself on-track again.

#new plan: use matrixes instead of populating a new CSV, which was my original instinct

#for this next step, a friend told me about the "in" function. On my own, would have tried looking for white space (but wasn't yet sure how) or split the city strings with two or more words into seperate strings and counted the number of strings
#we also sat down and drew a matrix together since I was having a lot of trouble imagining how to interact with a list of lists (could identify which col within a list needed to be accessed but couldn't loop through the lists (rows))
#I knew how to append a matrix.
one_word_matrix = []

for row in data[:]:
	if " " in row[4]:
		one_word_matrix.append(row)
#test with "print one_word_matrix"
#it worked! oh, thank god. I'm on my way again!
#now all the markets in one-word cities are in one matrix. I will use this matrix to answer the questions.

#########################################
#Question One
#1. How many markets sell vegetables, but not anything sweet?
#########################################
one_word_matrix_veggies = []

for row in one_word_matrix[:]:
	if "Y" in row[32]: #the veggie col.
		one_word_matrix_veggies.append(row)
#test with "print one_word_matrix_veggies" it works, hallleluha!

#define what foods are sweet: Bakedgoods (row=24), Honey (row=33), Jams (row=34), "row" is counted starting at 0 (0, 1, 2...)
#use booleon to find all markets that have any of the sweet items
one_word_matrix_veggies_sweets = []

for row in one_word_matrix_veggies[:]:
	if "Y" in row[24] or row[33] or row[34]:
		one_word_matrix_veggies_sweets.append(row)
print one_word_matrix_veggies_sweets

#to see how many markets have both veggies and sweets, we count the number of rows in one_word_matrix_veggies_sweets
#len gives number of lists in the matrix
number_of_rows = len(one_word_matrix_veggies_sweets)
print number_of_rows

#########################################
#Question Two
#2. What state has the highest density of famers market per capita? What state has the lowest?
#########################################
#I will make a matrix for every state and make a counter to count the number of farmers markets in that state
#then I will search for the population of each state online and calculate the per capita

#both lists are alphabetized so the state name in position 0 matches the state population in position 0, etc.
#state names came from http://www.50states.com/abbreviations.htm#.Vahwb3g-B8c and all spelled-out names were deleted by hand *grumble* I want to find a better way to do that
#state_names = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
state_names = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas",\
"Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico",\
"New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia",\
"Washington", "West Virginia", "Wisconsin", "Wyoming"]
#I tried looking up how to convert each state to it's own string within the state_names list (I know it can be done), but I didn't find anything
#state_names = str(state_names) <-- I tried this, but my code stopped at line 79 because AL (and all the state names) are currently undefined variables
#I decided to make each state a string by hand
#I expect that even if state_names = str(state_names), it would give me one long string "AL, AK, AZ,...[and so on]" when what I want is "AL", "AK",...


#state populations came from http://state.1keydata.com/state-population.php and I grumpily erased all the state names.
#I realized the commas within a population would be a problem and removed all of them using find>replace in the menu bar before adding them to the list
state_populations = [4779736, 710231, 6392017, 2915918, 37253956, 5029196, 3574097, 897934, 18801310, 9687653, 1360301, 1567582, \
12830632, 6483802, 3046355, 2853118, 4339367, 4533372, 1328361, 5773552, 6547629, 9883640, 5303925, 2967297, 5988927, 989415, 1826341, \
2700551, 1316470, 8791894, 2059179, 19378102, 9535483, 672591, 11536504, 3751351, 3831074, 12702379, 1052567, 4625364, 814180, \
6346105, 25145561, 2763885, 625741, 8001024, 6724540, 1852994, 5686986, 563626]

#I had a lot of trouble with this next step, so I stopped and tried thinking about what each line was doing and printed often. I commented out the code I wrote first and continued with the revised code below
#I sometimes get confused about types and when they are important. oh well, #goals.
# state_number_markets = []
# for i in state_names:
# 	i = []
# 	i_count = 0
# 	for row in one_word_matrix[:]:
# 		if "i" in row[6]: #this is the row that contains the state if counting begins at 0
# 			i.append(row) #FREAKS OUT RIGHT HERE
# 			i_count = i_count + 1
# 			state_number_markets.append(i_count)

all_state_number_markets = []
for name in state_names:
	list_markets_in_state = []
	count = 0
	for row in one_word_matrix[:]:
		if name in row[6]: #this is the row that contains the state if counting begins at 0 #[several hours later]: OH MY GOODNESS the CSV spelled out the state names
			list_markets_in_state.append(row)
			count = count + 1
			all_state_number_markets.append(count)
#			print all_state_number_markets
			print len(all_state_number_markets)


#next I divide the number of markets by the population of each state

per_capita_by_state = []
# #print "hello I am am about to start a for loop and WANT TO SEE IF PEOPLE CAN HEAR ME"
# print all_state_number_markets
# for markets in all_state_number_markets[:]:
# #	print "hello I am in a for loop and WANT TO SEE IF PEOPLE CAN HEAR ME"
# 	number_markets = markets
# #	print number_markets
# 	for population in state_populations[:]:
# #		print population
# 		per_cap = (float(number_markets)/population) #noticed I was always getting whole numbers but wasn't sure why until reminded that dividing to ints will get you an int
# #		print per_cap
# 		per_capita_by_state.append(per_cap)
# #print per_capita_by_state
# print len(per_capita_by_state) #this is not 50 (the number of states), so I'm sad. what is happening?
# #oh my goodness, I just divided and saved the number of markets in, say, Alabama by the population of Alabama and then the population of the next state and so on.  Wow.
# #I will comment out this section and try again.
population = state_populations
number_markets = all_state_number_markets
print len(population)
print len(number_markets)#this length is really big (should be 50), so I'll go back and see what it's so gosh darned large

for index in range(len(all_state_number_markets)):
	per_capita_by_state.append(float(number_markets[index])/population[index])

#find lowest and highest per capita
highest_percap = max(per_capita_by_state)
lowest_percap = min(per_capita_by_state)

#now that I know what numbers are the lowest and highest percapita, I will search through the list and find what index those numbers are at and hence with state they are associated with
#I am assuming that there are no repeats in the percapita


#########################################
#Question Three
#3. How many US farmers markets are between the Rocky Mountains and the Mississippi river?
#########################################
#Define the location of the Rocky Mountains and the Mississippi river
#haha, I started to abbreviate them "RM" and "MR" LETS NOT DO THAT mistake waiting to happen
#Rocky Mountains location is 43.7400 N, 110.8000 W (according to google)
#Mississippi location is 29.1536 N, 89.2508 W (according to google)
#I confirmed this is the same form used in the CSV file with http://www.earthpoint.us/Convert.aspx

#look for all markets between these two lats and between these two longs

RockyMountains_lat = 43.7400
RockyMountains_long = 110.8000
Mississippi_lat = 29.1536
Mississippi_long = 89.2508

markets_lat_between = []
markets_long_between = []

#first find markets between the lats
for row in one_word_matrix[:]:
	if Mississippi_lat<=row[17] and row[17]<=RockyMountains_lat:
		markets_lat_between.append(row)

#then find markets between the longs
for row in one_word_matrix[:]:
	if Mississippi_long<=row[16] and row[16]<=RockyMountains_long:
		markets_long_between.append(row)

#find markets both in our lat range and long range
markets_target_latlong = []

#for row in markets_lat_between[:]:
#	if #how to compare rows?

#########################################
#Question Four
#4. What is one fact or pattern about farmers markets in the United States that you can recognize using the raw data?
#########################################
#It's quite difficult to see any trends by looking at the raw data in the CSV, which is why being able to manipulate the data using some tool (a spreadsheet, python, a thousand notecards (incrediably time-consuming), etc.)
