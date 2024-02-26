import time
from testpage import OperationsHelpers
import logging
import yaml

with open('testdata.yaml') as f:
    testdata = yaml.safe_load(f)


def test_step1(browser):
    logging.info("Test1")
    testpage = OperationsHelpers(browser)
    testpage.go_to_site()
    testpage.enter_login("test")
    testpage.enter_pass("test")
    testpage.click_login_button()
    assert testpage.get_error_text() == "401"
    testpage.driver.close()


def test_step2(browser):
    logging.info("Test2")
    testpage = OperationsHelpers(browser)
    testpage.go_to_site()
    testpage.enter_login("Totogogi")
    testpage.enter_pass("b235f795c2")
    testpage.click_login_button()
    assert testpage.get_user() == "Home"


def test_step3(browser):
    logging.info("Test3")
    testpage = OperationsHelpers(browser)
    testpage.go_to_site()
    testpage.enter_login("Totogogi")
    testpage.enter_pass("b235f795c2")
    testpage.click_login_button()
    testpage.click_new_post_btn()
    testpage.title_post("New")
    testpage.description_post("New post1")
    testpage.content_post("Page ready")
    time.sleep(testdata['sleep_time'])
    testpage.click_save_post_btn()
    assert testpage.success_save_post() == "Page ready"


def test_step4(browser):
    logging.info("Test4")
    testpage = OperationsHelpers(browser)
    testpage.go_to_site()
    testpage.enter_login("Totogogi")
    testpage.enter_pass("b235f795c2")
    testpage.click_login_button()
    testpage.click_contact_btn()
    testpage.contact_name("Aketo")
    testpage.contact_email("aketo13@gmail.com")
    testpage.contact_content("Nice work guys")
    testpage.click_contact_us_btn()
    time.sleep(testdata['sleep_time'])

    assert testpage.contact_alert() == "Form successfully submitted"