import json


class EachReview:

    def __init__(self, name=None, review_stars=None, age=None, no_of_reviews=None, review_text=None, json_repres=None):
        self.name = name
        self.age = age
        self.review_stars = review_stars
        self.review_text = review_text
        self.no_of_reviews = no_of_reviews
        if json_repres is not None:
            self.__dict__ = json.loads(json_repres)

    def __str__(self):
        return str(self.__dict__)
