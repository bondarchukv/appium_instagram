import time

class Page(object):

    def __init__(self, driver):
        self._driver = driver

    def open(self, url):
        self._driver.get(url)

    def find_element(self, loc):
        print loc
        return self._driver.find_element(*loc)

    def send_keys(self, loc, keys):
        self._driver.find_element(*loc).send_keys(keys)

    def click(self, loc):
        self._driver.find_element(*loc).click()

    def wait_for_element(self, loc, timeout_steps = 5, step_delay = 1):
        cur_step = 0
        while cur_step < timeout_steps:
            try:
                e = self._driver.find_element(*loc)
                return True
            except Exception, e:
                pass
            cur_step += 1
            time.sleep(step_delay)
        return False