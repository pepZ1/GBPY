import yaml
import time

with open('testdata.yaml') as f:
    testdata = yaml.safe_load(f)


def test_1(site, path_login, path_passwd, button, element2, result2):
    input1 = site.find_element("xpath", path_login)
    input1.send_keys(testdata['login'])
    input2 = site.find_element("xpath", path_passwd)
    input2.send_keys(testdata['passwd'])
    btn = site.find_element("xpath", button)
    btn.click()
    label = site.find_element("xpath", element2)
    assert label.text == result2


def test_2(site, path_login, path_passwd, button,
               create_post, title, description, content,
               create_post_finish, post, title_post):
    input1 = site.find_element("xpath", path_login)
    input1.send_keys(testdata['login'])
    input2 = site.find_element("xpath", path_passwd)
    input2.send_keys(testdata['passwd'])
    btn = site.find_element("xpath", button)
    btn.click()
    time.sleep(testdata['sleep_time'])
    new_post = site.find_element("xpath", create_post)
    new_post.click()
    input3 = site.find_element("xpath", title)
    input3.send_keys(testdata['title'])
    input4 = site.find_element("xpath", description)
    input4.send_keys(testdata['description'])
    input5 = site.find_element("xpath", content)
    input5.send_keys(testdata['content'])
    save = site.find_element("xpath", create_post_finish)
    save.click()
    post1 = site.find_element("xpath", post)
    assert post1.text == title_post