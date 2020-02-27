import time

def test_assert_basket(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    time.sleep(30)
    assert browser.find_elements_by_css_selector('.btn.btn-lg.btn-primary.btn-add-to-basket'), \
        'Nashol`'
