import pymongo

if __name__ == "__main__":

    myclient = pymongo.MongoClient(
        "mongodb://127.0.0.1:27017/test_db",
        username="user",
        password="pass"
    )

    mydb = myclient["test_db"]
    # use collection named "testers"
    mycol = mydb["testers"]

    # a document
    tester = {"name": "Saranya", "address": "Kochi"}

    # insert a document to the collection
    x = mycol.insert_one(tester)

    print("List of Collections\n--------------------")
    # list the collections
    for coll in mydb.list_collection_names():
        print(coll)
