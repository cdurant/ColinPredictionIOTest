import predictionio
########################################################
# initialize client
client = predictionio.Client(appkey="hkp4eZXspTjIJUhk7RJpEaO1YWO2V4t8QRHG4nZTjHzIJpNvX4K4r5AwanRnoAKv")
########################################################
# recommend five items to each user
user_ids = [str(i) for i in range(1, 6)]
for user_id in user_ids:
	print "Retrieve top 5 recommendations for user " + user_id
	try:
		client.identify(user_id)
		rec = client.get_itemrec_topn("CatalogRecommender", 5)
		print rec
	except predictionio.ItemRecNotFoundError as e:
		print "Caught exception: " + e.strerror()
########################################################