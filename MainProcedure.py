import Constants
import LoadCredentials
import MongoDbConnector
import ReviewScrapper
from MongoDbConnector import MongoConnector
from ScrapperInput import ScrapperInput
import re
import logging

_DEFAULT_LOGGER_NAME = "MainProcedure"
DUMP_DATABASE_NAME = "dump_data_review_scrapper"


class Procedures:

    def __init__(self):
        logging.basicConfig(level=logging.INFO)
        self.log = logging.getLogger(_DEFAULT_LOGGER_NAME)

    def pull_all_data_and_push_to_mongo(self):
        self.log.info(">> pull_all_data_and_push_to_mongo")
        name_of_place_collins = "101 center apartments arlington tx"
        name_of_place_404_border = "404 border apartments arlington tx"
        name_of_place_round_rock = "round rock townhomes arlington tx"
        name_of_place_vintage_pads = "vintage pads arlington tx"
        name_of_place_fielder_crossing_condominiums = "fielder crossing condominiums arlington tx"
        name_of_place_pinewoods_apartments = "pinewoods apartments arlington tx"
        name_of_place_liv_plus_arlington_apartments = "liv+ arlington apartments arlington tx"
        name_of_place_the_paddock_apartments = "the paddock apartments arlington tx"
        name_of_place_sam_maverick_apartments = "sam maverick apartments arlington tx"
        name_of_place_the_deans = "the deans apartments arlington tx"
        name_of_place_848_mitchell = "848 mitchell apartments arlington tx"
        name_of_place_centennial_court = "centennial court apartments arlington tx"
        name_of_place_roosevelt_arlington = "the roosevelt at arlington commons arlington tx"
        name_of_place_collins_arlington = "the district on collins apartments arlington tx"
        name_of_place_kace_arlington = "the kace apartments arlington tx"
        name_of_place_louise_townhomes = "the louise townhomes arlington tx"
        name_of_place_viridian_arlington = "the jackson at viridian apartments arlington tx"
        name_of_place_jefferson_collins = "jefferson north collins apartments arlington tx"
        list_of_apartment_names = [name_of_place_jefferson_collins, name_of_place_collins_arlington,
                                   name_of_place_viridian_arlington, name_of_place_kace_arlington,
                                   name_of_place_roosevelt_arlington, name_of_place_louise_townhomes,
                                   name_of_place_centennial_court, name_of_place_collins,
                                   name_of_place_848_mitchell, name_of_place_the_deans,
                                   name_of_place_404_border, name_of_place_round_rock,
                                   name_of_place_vintage_pads, name_of_place_fielder_crossing_condominiums,
                                   name_of_place_pinewoods_apartments, name_of_place_liv_plus_arlington_apartments,
                                   name_of_place_the_paddock_apartments, name_of_place_sam_maverick_apartments]
        # 18 places scrapper
        self.log.info("Going to scrape")
        scrapper_input = ScrapperInput(list_of_names=list_of_apartment_names, all_scrape=True, count_of_reviews=100)
        main_review = ReviewScrapper.do_scrape(scrapper_input=scrapper_input)
        self.log.info("Size of reviews were " + str(len(main_review)))

        # Mongo cred
        self.log.info("Will be pushing data to mongoDb")
        loaded_credentials = LoadCredentials.loadCredentials(
            path_to_config_file=Constants.CREDENTIAL_FILE_KEY_MONGO_CREDENTIAL_FILE_NAME)
        user_name = loaded_credentials.get(Constants.CREDENTIAL_FILE_KEY_MONGO_USER_NAME)
        password = loaded_credentials.get(Constants.CREDENTIAL_FILE_KEY_MONGO_PASSWORD)
        database = DUMP_DATABASE_NAME
        host = loaded_credentials.get(Constants.CREDENTIAL_FILE_KEY_MONGO_HOST)
        port = int(loaded_credentials.get(Constants.CREDENTIAL_FILE_KEY_MONGO_PORT))
        # dump all the data to mongo this db
        mongo_db_connector = MongoConnector()
        mongo_client = MongoDbConnector.create_mongo_client(host=host, port=port, user=user_name, pwd=password)
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
        self.log.info("All done")
        self.log.info("<< pull_all_data_and_push_to_mongo")


if __name__ == '__main__':
    proc = Procedures()
    proc.pull_all_data_and_push_to_mongo()
    print("All done")
