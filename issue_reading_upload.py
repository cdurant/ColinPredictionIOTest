import csv
import predictionio
########################################################

# initialize client
client = predictionio.Client(appkey="hkp4eZXspTjIJUhk7RJpEaO1YWO2V4t8QRHG4nZTjHzIJpNvX4K4r5AwanRnoAKv")

########################################################
# open user_ids csv and add each id to predictionio
f = open("user_ids.csv", 'rU')

user_id_reader = csv.reader(f, dialect=csv.excel_tab)

for user_id in user_id_reader:
	print "Add user " + user_id[0]
	client.create_user(user_id[0])
########################################################
g = open("issue_ids.csv", 'rU')

issue_id_reader = csv.reader(g, dialect=csv.excel_tab)

for issue_id in issue_id_reader:
	print "Adding issue " + issue_id[0]
	client.create_item(issue_id[0], "1, ")
########################################################
h = open("catalog_reads.csv", 'rU')

catalog_read_reader = csv.reader(h, dialect=csv.excel_tab)

for row in catalog_read_reader:
	print "User " + row[0] + " views item " + row[1]
	client.identify(row[0])
	client.record_action_on_item("view", row[1])
########################################################
client.close()

