import unittest

from impl import review_scrapper, mongo_db_connector, load_credentials, apartment_constants
from ReviewScrapperTest import ReviewScrapperTest
from impl.scrapper_input import ScrapperInput
from impl.mongo_db_connector import MongoConnector


class MongoDbConnectorTest(unittest.TestCase):
    name_of_place_collins = "the district on collins apartments arlington"
    name_of_place_the_deans = "the deans apartments arlington tx"
    USER_NAME = ""
    PASSWORD = ""
    HOST = ""
    PORT = 0

    @classmethod
    def setUpClass(cls) -> None:
        loaded_credentials = load_credentials.loadCredentials(
            path_to_config_file=apartment_constants.CREDENTIAL_FILE_KEY_MONGO_CREDENTIAL_FILE_NAME)
        MongoDbConnectorTest.USER_NAME = loaded_credentials.get(apartment_constants.CREDENTIAL_FILE_KEY_MONGO_USER_NAME)
        MongoDbConnectorTest.PASSWORD = loaded_credentials.get(apartment_constants.CREDENTIAL_FILE_KEY_MONGO_PASSWORD)
        MongoDbConnectorTest.HOST = loaded_credentials.get(apartment_constants.CREDENTIAL_FILE_KEY_MONGO_HOST)
        MongoDbConnectorTest.PORT = int(loaded_credentials.get(apartment_constants.CREDENTIAL_FILE_KEY_MONGO_PORT))

    def test_push_pull_data(self):
        # Pull from collins and push into mongoDb
        scrapper_input = ScrapperInput(name_of_place=self.name_of_place_the_deans, all_scrape=True)
        main_review = review_scrapper.do_scrape(scrapper_input=scrapper_input)

        ReviewScrapperTest().do_overall_assertions(main_review[0])

        # Push data to mongodb
        database_name = "my_first_db"
        collection_name = "deans_collection"
        mongo_db_connector = MongoConnector()
        mongo_client = mongo_db_connector.create_mongo_client(host=MongoDbConnectorTest.HOST, port=MongoDbConnectorTest.PORT, user=MongoDbConnectorTest.USER_NAME, pwd=MongoDbConnectorTest.PASSWORD)
        push_results = mongo_db_connector.push(main_review[0].list_of_reviews, mongo_client=mongo_client,
                                               database=database_name,
                                               collection=collection_name)
        self.assertEqual(push_results, len(main_review[0].list_of_reviews))

        # pull and check
        connector_pull = mongo_db_connector.pull(mongo_client, database_name, collection_name)
        # self.assertEqual(push_results, len(connector_pull))
        self.assertNotEqual(0, len(connector_pull))
        mongo_client.close()


if __name__ == '__main__':
    unittest.main()
    print("Testing done")
