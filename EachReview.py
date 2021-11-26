class EachReview:

    def __init__(self, name, review_stars, age, no_of_reviews, review_text):
        self.name = name
        self.age = age
        self.review_stars = review_stars
        self.review_text = review_text
        self.no_of_reviews = no_of_reviews

    def __str__(self):
        return str(self.__dict__)