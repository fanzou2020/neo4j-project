import json


def process_business(newFile, line):
    item = json.loads(line)

    newItem = dict()
    newItem["business_id"] = item["business_id"]
    newItem["name"] = item["name"]
    newItem["address"] = item["address"]
    newItem["city"] = item["city"]
    newItem["state"] = item["state"]
    newItem["postal_code"] = item["postal_code"]
    newItem["latitude"] = item["latitude"]
    newItem["longitude"] = item["longitude"]
    newItem["stars"] = item["stars"]
    newItem["categories"] = item["categories"]

    newLine = json.dumps(newItem)
    newFile.write(newLine)
    newFile.write("\n")
    return


def process_user(newFile, line):
    item = json.loads(line)

    newItem = dict()
    newItem["user_id"] = item["user_id"]
    newItem["name"] = item["name"]
    newItem["review_count"] = item["review_count"]
    newItem["average_stars"] = item["average_stars"]
    newItem["friends"] = item["friends"]

    newLine = json.dumps(newItem)
    newFile.write(newLine)
    newFile.write("\n")
    return


def process_review(newFile, line):
    item = json.loads(line)

    newItem = dict()
    newItem["review_id"] = item["review_id"]
    newItem["user_id"] = item["user_id"]
    newItem["business_id"] = item["business_id"]
    newItem["stars"] = item["stars"]
    newItem["date"] = item["date"]

    newLine = json.dumps(newItem)
    newFile.write(newLine)
    newFile.write("\n")
    return

# process business data
filename_business = "../original_data/yelp_academic_dataset_business.json"
newFile = open("data/business.json", "a")

with open(filename_business, 'r') as f:
    line = f.readline()
    while line:
        process_business(newFile, line)
        line = f.readline()


# process user data
filename_user = "../original_data/yelp_academic_dataset_user.json"
newUserFile = open("data/user.json", "a")

with open(filename_user, 'r') as f:
    line = f.readline()
    while line:
        process_user(newUserFile, line)
        line = f.readline()


# process review data
filename_review = "../../../../../Downloads/archive/yelp_academic_dataset_review.json"
newReviewFile = open("data/review.json", "a")

with open(filename_review, 'r') as f:
    line = f.readline()
    while line:
        process_review(newReviewFile, line)
        line = f.readline()

