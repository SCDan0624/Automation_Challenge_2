class BasePage(object):

    url = None

    def __init__(self, driver):
        self.driver = driver

    def go(self):
        self.driver.get(self.url)

# Base Page
    # Will have all the things in general a page should
    # do that is not specific to my product
