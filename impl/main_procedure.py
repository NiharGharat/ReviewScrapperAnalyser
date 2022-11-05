from typing import List

from impl import apartment_constants, json_connector

from impl.main_review import MainReview
from scrapper_input import ScrapperInput
import logging
from review_scrapper import ReviewScrapper

DUMP_DATABASE_NAME = "dump_data_review_scrapper"


class Scrapper:
    logger_name = "ClassScrapper"

    def __init__(self, destination_type=apartment_constants.JOB_DESTINATION_FILE_JSON, destination_path=""):
        logging.basicConfig(level=logging.INFO)
        self.destination_type = destination_type
        self.log = logging.getLogger(Scrapper.logger_name)
        self.destination_path = destination_path

    def push_to_destination(self, list_of_reviews: List[MainReview]):
        self.log.info(">> push_to_destination")
        if self.destination_type == apartment_constants.JOB_DESTINATION_FILE_JSON:
            self.log.info("Pushing to raw json")
            json_connector.push_to_json(list_of_reviews, self.destination_path)
            self.log.info("Successfully pushed to json local")
        elif self.destination_type == apartment_constants.JOB_DESTINATION_NOSQL_MONGO:
            self.log.info("Pushing to mongodb")
            #mongo_db_connector.push_to_mongo(list_of_reviews)
            self.log.info("Successfully pushed to mongo")
        else:
            self.log("Unknown/Unimplemented destination ", self.destination_type)
        self.log.info("<< push_to_destination")

    def execute_job(self, scrapper_input: ScrapperInput):
        self.log.info(">> execute_job")
        self.log.info("Number of apartment reviews to fetch was %s", str(len(scrapper_input.list_of_names_of_places)))
        review_scrapper = ReviewScrapper()
        list_of_reviews = review_scrapper.do_scrape(scrapper_input=scrapper_input)
        self.log.info("Done with scrapping")
        self.log.info("Number of scrapped apartment reviews were " + str(len(list_of_reviews)))
        if len(scrapper_input.list_of_names_of_places) == len(list_of_reviews):
            self.log.info("Number of apartment reviews was equal to expected apartments")
        else:
            self.log.warning("Number of given apartment reviews was not equal to expected apartments")
        self.push_to_destination(list_of_reviews)
        self.log.info("All done")
        self.log.info("<< execute_job")


def apartment_review_18():
    default_rating_of_each_review = "Rated 0.0 out of 5,"
    default_text_of_review = "",
    default_no_of_reviews_of_reviewer = "1 review"
    dump_directory = "dump/dumpDirectory"
    list_of_apartment_names = \
        [apartment_constants.name_of_place_jefferson_collins,
         apartment_constants.name_of_place_collins_arlington,
         apartment_constants.name_of_place_viridian_arlington,
         apartment_constants.name_of_place_kace_arlington,
         apartment_constants.name_of_place_roosevelt_arlington,
         apartment_constants.name_of_place_louise_townhomes,
         apartment_constants.name_of_place_centennial_court,
         apartment_constants.name_of_place_collins,
         apartment_constants.name_of_place_848_mitchell,
         apartment_constants.name_of_place_the_deans,
         apartment_constants.name_of_place_404_border,
         apartment_constants.name_of_place_round_rock,
         apartment_constants.name_of_place_vintage_pads,
         apartment_constants.name_of_place_fielder_crossing_condominiums,
         apartment_constants.name_of_place_pinewoods_apartments,
         apartment_constants.name_of_place_liv_plus_arlington_apartments,
         apartment_constants.name_of_place_the_paddock_apartments,
         apartment_constants.name_of_place_sam_maverick_apartments]
    all_scrape = True
    count_of_reviews_to_scrape = 100
    destination_type = apartment_constants.JOB_DESTINATION_FILE_JSON
    main_scrapper = Scrapper(destination_type = destination_type, destination_path = dump_directory)
    scrapper_input = ScrapperInput(should_scrape_all_reviews=all_scrape,
                 default_rating_of_place=apartment_constants.default_rating_of_place,
                 default_review_text_of_place=apartment_constants.default_review_text_of_place,
                 default_no_of_reviews_of_reviewer=apartment_constants.default_number_of_reviews_of_reviewer,
                 count_of_reviews_to_scrape=count_of_reviews_to_scrape,
                 list_of_names_of_places=list_of_apartment_names)
    main_scrapper.execute_job(scrapper_input)
    print("Job execution done")


if __name__ == '__main__':
    apartment_review_18()
    print("All done")


