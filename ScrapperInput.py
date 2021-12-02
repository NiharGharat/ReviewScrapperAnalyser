import logging


class ScrapperInput:

    def __init__(self, name_of_place, all_scrape=True, default_rating="Rated 0.0 out of 5,", default_text="",
                 logging_level=logging.DEBUG, default_no_of_reviews="1 review", count_of_reviews = 50):
        self.name_of_place = name_of_place
        self.all_scrape = all_scrape
        self.logging_level = logging_level
        self.default_rating = default_rating
        self.default_text = default_text
        self.default_no_of_reviews = default_no_of_reviews
        self.count_of_reviews = count_of_reviews

    def __str__(self):
        return str(self.__dict__)
