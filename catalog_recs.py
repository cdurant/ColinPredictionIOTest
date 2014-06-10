import predictionio
import random
import csv
########################################################

# initialize client
client = predictionio.Client(appkey="hkp4eZXspTjIJUhk7RJpEaO1YWO2V4t8QRHG4nZTjHzIJpNvX4K4r5AwanRnoAKv")

########################################################
# open user_ids csv and put users into a list. Then generate a list of 100 users to get recs for.
# f = open("user_ids.csv", 'rU')

# user_id_reader = csv.reader(f, dialect=csv.excel_tab)

# users = []

# for user_id in user_id_reader:
# 	users.append(user_id)

# users_for_recs = []

# counter = 0
# while counter < 100:
# 	i = random.randrange(0, len(users)-1)
# 	users_for_recs.append(str(users[i]))
# 	print users[i]
# 	counter += 1
########################################################
# get five recommendations for each user

users_for_recs = [16574, 270589, 362485]

for user_id in users_for_recs:
	print "Retrieve top 5 recommendations for user " + str(user_id)
	try:
		client.identify(str(user_id))
		rec = client.get_itemrec_topn("CatalogRecommender", 5)
		print rec
	except predictionio.ItemRecNotFoundError as e:
		print "Caught exception: " + e.strerror()