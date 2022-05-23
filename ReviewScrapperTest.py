import unittest
import ReviewScrapper
from ScrapperInput import ScrapperInput
from MainReview import MainReview


class ReviewScrapperTest(unittest.TestCase):
    name_of_place_collins = "the district on collins apartments arlington"
    name_of_place_848_mitchell = "848 mitchell apartments arlington tx"
    name_of_place_the_deans = "the deans apartments arlington tx"
    name_of_place_centennial_court = "centennial court apartments arlington tx"
    name_of_place_roosevelt_arlington = "the roosevelt at arlington commons arlington tx"
    name_of_place_collins_arlington = "the district on collins apartments arlington tx"
    name_of_place_kace_arlington = "the kace apartments arlington tx"
    name_of_place_louise_townhomes = "the louise townhomes arlington tx"
    name_of_place_viridian_arlington = "the jackson at viridian apartments arlington tx"
    name_of_place_jefferson_collins = "jefferson north collins apartments arlington tx"
    collins_review = MainReview(avg_rating="2.4", list_of_reviews=[], number_of_reviews=88,
                                name_of_apt="The District on Collins Apartments",
                                address="2910 S Collins St, Arlington, TX")
    mitchell_review = MainReview(avg_rating="2.9", list_of_reviews=[], number_of_reviews=235,
                                 name_of_apt="848 Mitchell",
                                 address="848 W Mitchell St, Arlington, TX")

    def tearDown(self) -> None:
        print("Test done")

    def setUp(self) -> None:
        print("Setup ")

    """
    Load all reviews for single apartment to check the all load condition
    """
    def test_load_all_reviews_for_single_apartment(self):
        # Number of reviews dont matter, all scrape means take all reviews
        count_of_reviews = 50
        scrapper_input = ScrapperInput(name_of_place=self.name_of_place_collins, all_scrape=True, count_of_reviews=count_of_reviews)
        main_review = ReviewScrapper.do_scrape(scrapper_input=scrapper_input)

        # Asserts
        self.do_test_basic_assertions(expected_rev=self.collins_review, actual_rev=main_review[0])
        self.do_overall_assertions(main_review[0])
        for i in main_review:
            self.assertTrue(len(i.list_of_reviews) != count_of_reviews)
            self.do_overall_assertions(i)


    """
    Load all reviews for 3 apartments
    """
    def test_load_all_reviews_for_multiple_apartment(self):
        # Assert on different college
        # Basic assertions and advance assertions
        list_of_names_of_places = [ReviewScrapperTest.name_of_place_collins,
                                   ReviewScrapperTest.name_of_place_the_deans]
        count_of_reviews = 50
        scrapper_input = ScrapperInput(all_scrape=True, list_of_names=list_of_names_of_places,
                                       count_of_reviews=count_of_reviews)
        main_review = ReviewScrapper.do_scrape(scrapper_input=scrapper_input)

        # assert on 2 as size
        self.assertEqual(len(list_of_names_of_places), len(main_review))
        self.do_test_basic_assertions(expected_rev=self.collins_review, actual_rev=main_review[0])
        for i in main_review:
            self.assertTrue(len(i.list_of_reviews) != count_of_reviews)
            self.do_overall_assertions(i)

    def test_apartment_has_no_reviews(self):
        count_of_reviews = 5
        scrapper_input = ScrapperInput(all_scrape=False, name_of_place=ReviewScrapperTest.name_of_place_louise_townhomes,
                                       count_of_reviews=count_of_reviews)
        main_review = ReviewScrapper.do_scrape(scrapper_input=scrapper_input)
        self.assertEqual(1, len(main_review))
        self.assertEqual(0, main_review[0].avg_rating)
        self.assertEqual(0, len(main_review[0].list_of_reviews))
        self.assertEqual(0, main_review[0].number_of_reviews)
        self.assertEqual('', main_review[0].address)
        self.assertEqual('', main_review[0].name_of_apt)

    def test_multiple_locations(self):
        # Assert on 10 locations
        list_of_names_of_places = [ReviewScrapperTest.name_of_place_collins,
                                   ReviewScrapperTest.name_of_place_848_mitchell,
                                   ReviewScrapperTest.name_of_place_the_deans,
                                   ReviewScrapperTest.name_of_place_centennial_court,
                                   ReviewScrapperTest.name_of_place_roosevelt_arlington,
                                   ReviewScrapperTest.name_of_place_collins_arlington,
                                   ReviewScrapperTest.name_of_place_kace_arlington,
                                   ReviewScrapperTest.name_of_place_louise_townhomes,
                                   ReviewScrapperTest.name_of_place_viridian_arlington,
                                   ReviewScrapperTest.name_of_place_jefferson_collins]
        count_of_reviews = 5
        scrapper_input = ScrapperInput(all_scrape=False, list_of_names=list_of_names_of_places, count_of_reviews=count_of_reviews)
        main_review = ReviewScrapper.do_scrape(scrapper_input=scrapper_input)
        self.assertEqual(len(list_of_names_of_places), len(main_review))
        self.do_test_basic_assertions(expected_rev=self.collins_review, actual_rev=main_review[0])
        self.do_test_basic_assertions(expected_rev=self.mitchell_review, actual_rev=main_review[1])
        for i in main_review:
            self.do_number_of_assertions(i, count_of_reviews)
            self.do_overall_assertions(i)

    def test_different_place(self):
        # Assert on different college
        # Basic assertions and advance assertions
        list_of_names_of_places = [ReviewScrapperTest.name_of_place_collins,
                                   ReviewScrapperTest.name_of_place_848_mitchell]
        count_of_reviews = 50
        scrapper_input = ScrapperInput(all_scrape=False, list_of_names=list_of_names_of_places, count_of_reviews=count_of_reviews)
        main_review = ReviewScrapper.do_scrape(scrapper_input=scrapper_input)

        # assert on 2 as size
        self.assertEqual(len(list_of_names_of_places), len(main_review))
        self.do_test_basic_assertions(expected_rev=self.collins_review, actual_rev=main_review[0])
        self.do_test_basic_assertions(expected_rev=self.mitchell_review, actual_rev=main_review[1])
        for i in main_review:
            self.do_number_of_assertions(i, count_of_reviews)
            self.do_overall_assertions(i)

    """
    Assert on different college
    Basic assertions and advance assertions
    """

    def test_simple_college(self):
        # Procedure
        scrapper_input = ScrapperInput(name_of_place=self.name_of_place_collins, all_scrape=False)
        main_review = ReviewScrapper.do_scrape(scrapper_input=scrapper_input)

        # Asserts
        self.do_test_basic_assertions(expected_rev=self.collins_review, actual_rev=main_review[0])
        self.do_number_of_assertions(main_review[0], 10)
        self.do_overall_assertions(main_review[0])
        # self.do_test_advance_assertions(self, collins_review_assertions, main_review[0])

    def do_test_basic_assertions(self, expected_rev: MainReview, actual_rev: MainReview):
        # Assertions like all objects in list have values, etc.
        self.do_overall_assertions(actual_rev)
        # This keeps changing
        # assert self.assertEqual(expected_rev.avg_rating, actual_rev.avg_rating)
        self.assertEqual(expected_rev.address, actual_rev.address)
        self.assertEqual(expected_rev.name_of_apt, actual_rev.name_of_apt)

    def do_overall_assertions(self, the_review: MainReview):
        self.assertTrue(the_review.list_of_reviews is not None)
        self.assertTrue(the_review.number_of_reviews is not None)

    def do_number_of_assertions(self, main_review: MainReview, expected_number_of_reviews: int):
        if len(main_review.list_of_reviews) != expected_number_of_reviews:
            self.assertEqual(0, len(main_review.list_of_reviews))
        else:
            self.assertEqual(len(main_review.list_of_reviews), expected_number_of_reviews)


if __name__ == '__main__':
    unittest.main()
    print("Everything passed")
