

import time

def test_search(test_case):

    testcase = test_case
    testcase.go_to_url(testcase.url)
    testcase.click_search(testcase.search)
    testcase.search_product_name()
    testcase.add_to_cart()
    time.sleep(4)


