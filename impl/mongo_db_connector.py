import pymongo.database
from pymongo import MongoClient
import urllib.parse
import logging
import json

_DEFAULT_LOGGER_NAME = "MongoDbConnector"
"""
Static method to create mongo client
"""


def create_mongo_client(host: str, port: int, user: str, pwd: str) -> MongoClient:
    username = urllib.parse.quote(user)
    password = urllib.parse.quote(pwd)
    mongo_uri = "mongodb://" + username + ":" + password + "@" + host + ":" + str(port) + "/"
    return MongoClient(mongo_uri)


class MongoConnector:

    def __init__(self):
        logging.basicConfig(level=logging.INFO)
        self.log = logging.getLogger(_DEFAULT_LOGGER_NAME)

    def push_reviews_to_mongo(self):
        self.log.info("Will be pushing data to mongoDb")
        loaded_credentials = load_credentials.loadCredentials(
            path_to_config_file=apartment_constants.CREDENTIAL_FILE_KEY_MONGO_CREDENTIAL_FILE_NAME)
        user_name = loaded_credentials.get(apartment_constants.CREDENTIAL_FILE_KEY_MONGO_USER_NAME)
        password = loaded_credentials.get(apartment_constants.CREDENTIAL_FILE_KEY_MONGO_PASSWORD)
        database = DUMP_DATABASE_NAME
        host = loaded_credentials.get(apartment_constants.CREDENTIAL_FILE_KEY_MONGO_HOST)
        port = int(loaded_credentials.get(apartment_constants.CREDENTIAL_FILE_KEY_MONGO_PORT))
        # dump all the data to mongo this db
        mongo_db_connector = MongoConnector()
        mongo_client = mongo_db_connector.create_mongo_client(host=host, port=port, user=user_name, pwd=password)
        ctr = 0
        for each_review in main_review:
            self.log.info("On review " + str(ctr))
            self.log.info("Number of reviews are " + str(len(each_review.list_of_reviews)))
            assert each_review is not None
            collection_name = each_review.name_of_apt
            assert collection_name is not None
            collection_name = collection_name.lower()
            collection_name_cleaned = re.sub('[^A-Za-z0-9]+', "_", collection_name)
            print("Collection name to be used for " + collection_name + " is " + collection_name_cleaned)
            push_results = mongo_db_connector.push(each_review.list_of_reviews, mongo_client=mongo_client,
                                                   database=database,
                                                   collection=collection_name_cleaned)
            assert push_results == len(each_review.list_of_reviews), "The length was not equal"
            self.log.info("Done with apartment " + each_review.name_of_apt)
            ctr += 1

    def push(self, json_list_data: list, mongo_client: MongoClient, database: str, collection: str) -> int:
        self.log.info(">> push")
        database_to_use: pymongo.database.Database = mongo_client.get_database(name=database)
        collection_to_use: pymongo.collection.Collection = database_to_use.get_collection(name=collection)
        if len(json_list_data) == 0:
            self.log.warning("Data size was zero, skipping ops")
            return 0
        try:
            self.log.debug("Trying to insert %d records", len(json_list_data))
            ctr = 0
            for each_rec in json_list_data:
                c = json.dumps(each_rec.__dict__)
                json_list_data[ctr] = json.loads(c)
                ctr += 1
            # json_list_data = [json.dumps(x.__dict__) for x in json_list_data]
            insert_many_result = collection_to_use.insert_many(json_list_data)
            self.log.info("Records inserted, number of record ids inserted were %d",
                          len(insert_many_result.inserted_ids))
        except Exception as e:
            self.log.exception(e, exc_info=True)
            raise e
        self.log.info("<< push")
        return len(insert_many_result.inserted_ids) if insert_many_result is not None else 0

    def pull(self, mongo_client: MongoClient, database: str, collection: str):
        collection_documents = mongo_client.get_database(name=database).get_collection(name=collection).find()
        documents_as_list = list(collection_documents)
        return documents_as_list
        # str_docs = dumps(documents_as_list)
        # loaded_json = json.loads(str_docs)
        # for i in loaded_json:
        #     pprint(i)
