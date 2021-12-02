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
        #scrapper_input = ScrapperInput()
        #ReviewScrapper.do_scrape(scrapper_input=scrapper_input)
        pass

    """
    Assert on different college
    Basic assertions and advance assertions
    """
    def test_simple_college(self):
        # Expectations - Collins
        collins_review_assertions = []
        collins_review_0 = '{"name": "Alissa Lafond", "age": "2 weeks ago", "review_stars": "Rated 1.0 out of 5,", "review_text": "Applied for a 1b/1b online that was listed for a price that met my budget, I paid the application fee + processing fee to then get a call from the leasing office letting me know that their pricing online is incorrect and the price I was quoted in my application was actually $160 less than what the rent actually was. If I was to proceed with the process, I would be paying the higher rent amount each month that is not listed because they are renovating their units. I requested to have my application fee returned (since I would not have applied in the first place) to which I was told yes but they would not be refunding me for the processing charge. Now I have to wait for my refund to be mailed back to me from their corporate office. What a horrible and disappointing experience.", "no_of_reviews": "6 reviews"}'
        collins_review_1 = '{"name": "senior neko", "age": "3 weeks ago", "review_stars": "Rated 1.0 out of 5,", "review_text": "Trash everywhere and gate is not even working. We pay money for trash that means the place should be maintained clean and neat. This is totally unexpected.", "no_of_reviews": "2 reviews"}'
        collins_review_2 = '{"name": "Tielah Gowans", "age": "9 months ago", "review_stars": "Rated 1.0 out of 5,", "review_text": "I would give these apartments a zero if I could. The maintenance never comes and do their job correctly. My toilet has been broken the whole 8 months I have lived here. There is always a leak in my dining area and every time I get out of the shower my floor is extremely wet. Knats are everywhere in my bathroom.  They came to fix the issue for my next door neighbors leak and left my bathroom destroyed for two days. There are too many hidden fees and the rent is too high for poor service. This is the worse experience I have had with my first apartment. Would not recommend living here!!", "no_of_reviews": "4 reviews"}'
        collins_review_3 = '{"name": "shayla hill", "age": "a year ago", "review_stars": "Rated 5.0 out of 5,", "review_text": "Just moved in and love the new apartment.  I’ve seen the community with the old management company and the new management has made lots of improvements.  Aaron was awesome to work with during the application and approval process and Mia kept me updated on what was going on in my apartment before move in.  They are very pleasant and helpful.", "no_of_reviews": "3 reviews"}'
        collins_review_4 = '{"name": "cataria patterson", "age": "5 months ago", "review_stars": "Rated 1.0 out of 5,", "review_text": "Filed a complaint with the Attorney General office. My daughter  lives in these apartments  and temperatures in the apartment is ridiculous. She complained and I have complained. It has been almost a month and air conditioning still does not work. Thrash everywhere, but in the dumpster.", "no_of_reviews": "Local Guide·10 reviews·22 photos"}'
        collins_review_5 = '{"name": "Roxann Garza", "age": "a year ago", "review_stars": "Rated 5.0 out of 5,", "review_text": "I love my rehab unit. I have a 2 bed and my apartment home is spacious. Newly improved property and they are gated!!", "no_of_reviews": "2 reviews"}'
        #collins_review_6 = '{"name": "Carlos Torres", "age": "4 years ago", "review_stars": "Rated 5.0 out of 5,", "review_text": "(Translated by Google) Nice place\n\n(Original)\nLindo lugar", "no_of_reviews": "Local Guide·30 reviews·5 photos"}'
        collins_review_7 = '{"name": "David garza", "age": "6 years ago", "review_stars": "Rated 1.0 out of 5,", "review_text": "", "no_of_reviews": "1 review"}'
        collins_review_8 = '{"name": "Ashley Schmitzer", "age": "4 years ago", "review_stars": "Rated 5.0 out of 5,", "review_text": "", "no_of_reviews": "Local Guide·107 reviews·2,301 photos"}'
        collins_review_9 = '{"name": "cataria patterson", "age": "5 months ago", "review_stars": "Rated 1.0 out of 5,", "review_text": "Filed a complaint with the Attorney General office. My daughter  lives in these apartments  and temperatures in the apartment is ridiculous. She complained and I have complained. It has been almost a month and air conditioning still does not work. Thrash everywhere, but in the dumpster.", "no_of_reviews": "Local Guide·10 reviews·22 photos"}'
        #collins_review_10 = '{"name": "Jayvon Jackson", "age": "a year ago", "review_stars": "Rated 1.0 out of 5,", "review_text": "I wouldn’t rent from here unless you are extremely desperate, I have had about 4 major issues within the 5 months of me renting here. One of them is the fact they can not keep up with the complex in any shape or form. For example water line is turned off literally every other week for a least an hour for repairs.EVERY OTHER WEEK, however they just finished remodeling the office. We have a electrical issue and water pumping issue in one of the buildings that i live in. AC unit was broken, temperature reach as high as 85 degrees. So hot the thermometer on the thermostat couldn’t go any higher. I called the emergency hotline to see if i can get a repair asap. I was told there was nothing they can do until the next morning. That’s was not a good enough answer for me. I had to wait outside at 11:30 at night to get answer back. They offered another apartment to stay in that night, however they said and I quote “It just wouldn’t be clean” are you serious! Again they have the money to renovate the office so nice but can’t keep up with its own unit’s. Reminder that’s just one of the 4 issues i had.\n\nWithin the 1 year I been here water been turned off over 20+ times, have people vandalizing other people Property, Have a gate system that doesn’t work 90% of the time, Front office is completely blind to it all and see nothing wrong at all with anything, so glad I found a better place.", "no_of_reviews": "Local Guide·7 reviews"}'
        collins_review_assertions.append(EachReview(json_repres=collins_review_0))
        collins_review_assertions.append(EachReview(json_repres=collins_review_1))
        collins_review_assertions.append(EachReview(json_repres=collins_review_2))
        collins_review_assertions.append(EachReview(json_repres=collins_review_3))
        collins_review_assertions.append(EachReview(json_repres=collins_review_4))
        collins_review_assertions.append(EachReview(json_repres=collins_review_5))
        #collins_review_assertions.append(EachReview(json_repres=collins_review_6))
        collins_review_assertions.append(EachReview(json_repres=collins_review_7))
        collins_review_assertions.append(EachReview(json_repres=collins_review_8))
        collins_review_assertions.append(EachReview(json_repres=collins_review_9))
        #collins_review_assertions.append(EachReview(json_repres=collins_review_10))

        # Procedure
        #scrapper_input = ScrapperInput(name_of_place=ReviewScrapperTest.name_of_place_collins, all_scrape=True)
        #main_review = ReviewScrapper.do_scrape(scrapper_input=scrapper_input)
        main_review = ReviewScrapperTest.collins_review
        main_review.list_of_reviews = collins_review_assertions
        # Asserts
        self.do_test_basic_assertions(self, expected_rev=ReviewScrapperTest.collins_review, actual_rev=main_review)
        self.do_test_advance_assertions(self, collins_review_assertions, main_review)

    def do_test_basic_assertions(self, expected_rev: MainReview, actual_rev: MainReview):
        # Assertions like all objects in list have values, etc.
        assert self.assertEqual(expected_rev.number_of_reviews, len(actual_rev.list_of_reviews))
        assert self.assertEqual(expected_rev.number_of_reviews, actual_rev.number_of_reviews)
        assert self.assertEqual(expected_rev.avg_rating, actual_rev.avg_rating)
        assert self.assertEqual(expected_rev.address, actual_rev.address)
        assert self.assertEqual(expected_rev.name_of_apt, actual_rev.name_of_apt)


    def do_test_advance_assertions(self, list_of_each_review_expectation: list, actual_rev: MainReview):
        # Different names, values of reviews, More click link in Review test does not exists
        # Integrity of all objects in the list, all values in place, regex match on all values
        # Random text, stars, assert values
        pointer = 0
        for i in actual_rev.list_of_reviews:
            filtered_list = [x for x in list_of_each_review_expectation[pointer] if x.name == i.name]
            if len(filtered_list) != 1:
                print("Filtered list length was greater than 1")
            assert filtered_list[0].name == i.name
            assert filtered_list[0].age == i.age
            assert filtered_list[0].no_of_reviews == i.no_of_reviews
            assert filtered_list[0].review_text == i.review_text
            assert filtered_list[0].review_stars == i.review_stars
            pointer += 1


if __name__ == '__main__':
    unittest.main()
    print("Everything passed")
