import pathlib
from typing import List

from impl.main_review import MainReview


class JsonConnector:

    def __init__(self, directory_path: str = None):
        if directory_path is None:
            raise Exception("Directory path supplied was None")
        self.directory_path = directory_path

    def __create_directory_if_not_exists(self):
        pathlib.Path(self.directory_path).mkdir(parents=True, exist_ok=True)

    def __write_to_json(self, each_review: MainReview, complete_file_path: str):
        with open(r'complete_file_path', 'w') as fp:
            for item in each_review.list_of_reviews:
                # write each item on a new line
                fp.write("%s\n" % item)
            print('Done')

    def push_to_json(self, list_of_reviews: List[MainReview], directory_path: str):
        '''
        1. Create directory if not exists
        2. Push all the reviews to raw json files
        3. Done
        :param main_review:
        :param directoy_path:
        :return:
        '''
        # Create the directory path
        self.__create_directory_if_not_exists(directory_path)
        # Write all files
        for each_review in list_of_reviews:
            complete_file_path = each_review.name_of_apt + ".json"
            self.__write_to_json(each_review, complete_file_path)
            print("Writing apartment " + each_review.name_of_apt + " done")
        print("Writing all apartment done")