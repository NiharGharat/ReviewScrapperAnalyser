class MainReview:

    def __init__(self, avg_rating, list_of_reviews, number_of_reviews, name_of_apt, address):
        self.avg_rating = avg_rating
        self.list_of_reviews = list_of_reviews
        self.number_of_reviews = number_of_reviews
        self.name_of_apt = name_of_apt
        self.address = address

    def __repr__(self):
        return str(self.__dict__)