import unittest
import ReviewScrapper
from ScrapperInput import ScrapperInput
from MainReview import MainReview
from EachReview import EachReview
import json


class ReviewScrapperTest(unittest.TestCase):
    name_of_place_collins = "the district on collins apartments arlington"
    name_of_place_848_mitchell = "848 mitchell apartments arlington tx"
    collins_review = MainReview(avg_rating="2.4", list_of_reviews=[], number_of_reviews=88,
                                name_of_apt="The District on Collins Apartments",
                                address="2910 S Collins St, Arlington, TX, United States")
    mitchell_review = MainReview(avg_rating="2.9", list_of_reviews=[], number_of_reviews=235,
                                 name_of_apt="848 Mitchell",
                                 address="848 W Mitchell St, Arlington, TX, United States")

    def test_different_place(self):
        # Assert on different college
        # Basic assertions and advance assertions
        list_of_names_of_places = []
        list_of_names_of_places.append(ReviewScrapperTest.name_of_place_collins)
        list_of_names_of_places.append(ReviewScrapperTest.name_of_place_848_mitchell)
        scrapper_input = ScrapperInput(all_scrape=True, list_of_names=list_of_names_of_places, count_of_reviews=50)
        main_review = ReviewScrapper.do_scrape(scrapper_input=scrapper_input)

        # assert on 2 as size
        assert self.assertEqual(len(list_of_names_of_places), len(main_review))
        self.do_test_basic_assertions(self, expected_rev=ReviewScrapperTest.collins_review, actual_rev=main_review[0])
        self.do_test_basic_assertions(self, expected_rev=ReviewScrapperTest.mitchell_review, actual_rev=main_review[1])
        pass

    """
    Assert on different college
    Basic assertions and advance assertions
    """

    def atest_simple_college(self):
        # Procedure
        scrapper_input = ScrapperInput(name_of_place=ReviewScrapperTest.name_of_place_collins, all_scrape=True)
        main_review = ReviewScrapper.do_scrape(scrapper_input=scrapper_input)

        # Asserts
        self.do_test_basic_assertions(self, expected_rev=ReviewScrapperTest.collins_review, actual_rev=main_review[0])
        # self.do_test_advance_assertions(self, collins_review_assertions, main_review[0])

    def do_test_basic_assertions(self, expected_rev: MainReview, actual_rev: MainReview):
        # Assertions like all objects in list have values, etc.
        assert self.assertTrue(len(actual_rev.list_of_reviews))
        assert self.assertTrue(actual_rev.number_of_reviews)
        # assert self.assertEqual(expected_rev.avg_rating, actual_rev.avg_rating)
        assert self.assertEqual(expected_rev.address, actual_rev.address)
        assert self.assertEqual(expected_rev.name_of_apt, actual_rev.name_of_apt)


if __name__ == '__main__':
    unittest.main()
    print("Everything passed")
