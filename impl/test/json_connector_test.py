import unittest

from impl.scrapper_input import ScrapperInput


class JsonConnectorTest(unittest.TestCase):

    def test_push_data(self):
        scrapper_input = ScrapperInput(name_of_place=self.name_of_place_the_deans, all_scrape=True)


