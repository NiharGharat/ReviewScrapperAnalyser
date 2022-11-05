from impl import apartment_constants


class ScrapperInput:

    def __init__(self, single_name_of_place_to_scrape=None, should_scrape_all_reviews=False,
                 default_rating_of_place=apartment_constants.default_rating_of_place,
                 default_review_text_of_place=apartment_constants.default_review_text_of_place,
                 default_no_of_reviews_of_reviewer=apartment_constants.default_number_of_reviews_of_reviewer,
                 count_of_reviews_to_scrape=apartment_constants.count_of_reviews_to_scrape,
                 list_of_names_of_places=None):
        self.single_name_of_place_to_scrape = single_name_of_place_to_scrape
        self.should_scrape_all_reviews = should_scrape_all_reviews
        self.default_rating_of_place = default_rating_of_place
        self.default_review_text_of_place = default_review_text_of_place
        self.default_no_of_reviews_of_reviewer = default_no_of_reviews_of_reviewer
        self.count_of_reviews_to_scrape = count_of_reviews_to_scrape
        self.list_of_names_of_places = list_of_names_of_places

    def __str__(self):
        return str(self.__dict__)
