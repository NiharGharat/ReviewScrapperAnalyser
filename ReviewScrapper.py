from selenium import webdriver
import time
from EachReview import EachReview
from MainReview import MainReview
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import logging
import random


# Req op
# 1. Website link
# 2. All reviews in a json      D
# 3. Name of apt                D
# 4. Total no of reviews        D
# 5. Total Avg rating           D
# 6. Per review - Age, Name, Stars, Number of reviews of that person, Local Guide status,
# 7. Often mentions

DEFAULT_SLEEP_UPPER_BOUND = 15
DEFAULT_SLEEP_LOWER_BOUND = 7
FLAG_DEFAULT_ALL_SCRAPE = True
DEFAULT_INITIAL_SLEEP_SECONDS = 5
VALUE_SUPPRESS_EXCEPTION = "SUPPRESS_EXCEPTION"
VALUE_RAISE_EXCEPTION = "RAISE_EXCEPTION"
DEFAULT_NO_OF_REVIEWS = "1 review"
DEFAULT_RATING = "Rated 0.0 out of 5,"


# Process those elements
# 1. Get that pointer review block element
# 2. Create the response
# 3. Move pointer
def process_review_block(review_block, pointer, list_of_reviews):
    log.info("Inside processing_review_block")
    log.debug("Processing review block " + str(pointer))
    log.info("List size is " + str(len(list_of_reviews)))
    block = review_block[pointer].find_elements_by_css_selector("div[jscontroller^='fIQYlf']")
    log.info("Block size is " + str(len(block)))
    for each_elem in block:
        # Name of reviewer
        reviewer_name_element = each_elem.find_elements_by_css_selector("div[class='TSUbDb']")
        check_component(reviewer_element=reviewer_name_element, element_name="reviewer_name_element",
                        action="exception")
        reviewer_name = reviewer_name_element[0].text
        # Age of review
        reviewer_age_element = each_elem.find_elements_by_css_selector("span[class='dehysf lTi8oc']")
        review_age = reviewer_age_element[0].text
        check_component(reviewer_element=reviewer_age_element, element_name="reviewer_age_element", action="exception")
        # Rating
        reviewer_rating_element = each_elem.find_elements_by_css_selector("span[class='Fam1ne EBe2gf']")
        check_component(reviewer_element=reviewer_rating_element, element_name="reviewer_rating_element",
                        action="exception")
        try:
            review_rating = reviewer_rating_element[0].get_attribute("aria-label")
        except NoSuchElementException as e:
            log.error("Star rating does not exists for the reviewer " + reviewer_name)
            raise e
            # review_rating = DEFAULT_RATING
        # No of reviews
        no_of_reviews_element = each_elem.find_elements_by_css_selector("span[class='A503be']")
        check_component(reviewer_element=no_of_reviews_element, element_name="no_of_reviews_element",
                        action="exception")
        try:
            reviewer_no_of_reviews = no_of_reviews_element[0].text
        except Exception:
            log.warning("No no of review element, defaulting to 1")
            reviewer_no_of_reviews = DEFAULT_NO_OF_REVIEWS
        review_text = ""
        try:
            # More link in some
            each_elem.find_element_by_css_selector("a[class='review-more-link']").click()
            more_text_block = each_elem.find_elements_by_css_selector("span[class='review-full-text']")
            if more_text_block is None or len(more_text_block) < 1:
                log.warning("No more element but no exception")
                raise NoSuchElementException("No more element but no exception")
            log.info("More exists for this reviewer " + reviewer_name)
            review_text = more_text_block[0].text
        except NoSuchElementException:
            log.warning("More does not exists for this reviewer " + reviewer_name)
            text_block = each_elem.find_elements_by_css_selector("span[jscontroller='MZnM8e']")
            if text_block is None or len(text_block) < 1:
                log.warning("No more element but no exception")
                raise NoSuchElementException("No more element but no exception")
            review_text = text_block[0].text
        except NoSuchElementException:
            log.warning("No text present even for not more element")
        if len(review_text) == 0:
            log.warning("Empty text")
        each_review = EachReview(name=reviewer_name, review_stars=review_rating, age=review_age,
                                 no_of_reviews=reviewer_no_of_reviews,
                                 review_text=review_text)
        list_of_reviews.append(each_review)
    log.info("Block " + str(pointer) + " Done")
    log.info("List size is ", str(len(list_of_reviews)))


def check_component(reviewer_element, element_name, action):
    if len(reviewer_element) < 1:
        if action == VALUE_RAISE_EXCEPTION:
            raise RuntimeError("Element {} was empty".format(element_name))
        elif action == VALUE_SUPPRESS_EXCEPTION:
            log.warning("Element {} was empty".format(element_name))
    elif len(reviewer_element) > 1:
        if action == VALUE_RAISE_EXCEPTION:
            raise RuntimeError("Element {} has more elements".format(element_name))
        elif action == VALUE_SUPPRESS_EXCEPTION:
            log.warning("Element {} has more elements".format(element_name))
    else:
        log.debug("Element {} is correct".format(element_name))


# Setup
log = logging.getLogger("Scrapper")
logging.basicConfig(level=logging.DEBUG)

# Setup done
chrome_path = "/usr/bin/chromedriver"
google_link = "https://www.google.com/search?q="
google_search_term = "the district on collins apartments arlington"
xpath_reviews_to_click = "/html/body/div[7]/div/div[10]/div[2]/div/div/div[2]/div/div[1]/div[2]/div[2]/div/div/span[" \
                         "3]/span/a "

driver = webdriver.Chrome(chrome_path)
log.info("Driver opened")
google_search_term = google_search_term.replace(" ", "+")
complete_link = google_link + google_search_term
log.debug("Complete link created")
driver.get(complete_link)

reviews = driver.find_element(By.XPATH, xpath_reviews_to_click)
reviews.click()
log.info("Clicked on reviews")
time.sleep(DEFAULT_INITIAL_SLEEP_SECONDS)

# Main review, get the name, add, overall score, and number of reviewers later
xpath_of_main_review_parent = "/html/body/span[2]/g-lightbox/div[2]/div[3]/span/div/div/div"
main_review_element = reviews.find_element(By.XPATH, xpath_of_main_review_parent)
name_of_apt = main_review_element.find_element_by_class_name("P5Bobd").text
avg_rating = main_review_element.find_element_by_class_name("Aq14fc").text
number_of_reviews = main_review_element.find_element_by_class_name("z5jxId").text
address_of_apt = main_review_element.find_element_by_class_name("T6pBCe").text

# Basics done, now onto main review part
css_path_of_review_parent = "gws-localreviews__general-reviews-block"
_number_of_reviews = int(number_of_reviews.split(" ")[0])
log.debug("Number of reviews is " + str(_number_of_reviews))

_reviews_block_pointer = 0
all_scrape = FLAG_DEFAULT_ALL_SCRAPE
list_of_reviews = []
review_block = main_review_element.find_elements_by_class_name(css_path_of_review_parent)
refresh_element = main_review_element.find_element_by_class_name("loris")
while all_scrape:
    if len(review_block) != _reviews_block_pointer + 1:
        # Need newer elements
        # Call the refresh, and then populate the review_block
        # Refresh - Need to scroll it into view, then trigger a window switch
        driver.execute_script("arguments[0].scrollIntoView(true);", refresh_element)
        driver.switch_to.window(driver.current_window_handle)
        random_stop = random.randint(DEFAULT_SLEEP_LOWER_BOUND, DEFAULT_SLEEP_UPPER_BOUND)
        time.sleep(random_stop)
        review_block = main_review_element.find_elements_by_class_name(css_path_of_review_parent)
    # Else Already has those elements process them

    process_review_block(review_block, _reviews_block_pointer, list_of_reviews)
    _reviews_block_pointer += 1
    # Are reviews still left?
    all_scrape = (len(list_of_reviews) < _number_of_reviews) & all_scrape

log.info("List size is " + str(len(list_of_reviews)))
MainReview = MainReview(avg_rating=avg_rating, list_of_reviews=list_of_reviews,
                        number_of_reviews=number_of_reviews, name_of_apt=name_of_apt, address=address_of_apt)

if len(list_of_reviews) == _number_of_reviews:
    log.info("SUCCESS - Captured all the reviews")
else:
    log.info("WARN - Some issue, was not able to capture all reviews")

log.info("Done, printing values")
for i in list_of_reviews:
    print(i)
log.info("All done")
