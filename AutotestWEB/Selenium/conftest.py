import pytest
from module import Site
import yaml

with open('testdata.yaml') as f:
    testdata = yaml.safe_load(f)


@pytest.fixture
def path_login():
    x_selector1 = """//*[@id="login"]/div[1]/label/input"""
    return x_selector1


@pytest.fixture
def path_passwd():
    x_selector2 = """//*[@id="login"]/div[2]/label/input"""
    return x_selector2


@pytest.fixture
def button():
    btn_selector = """//*[@id="login"]/div[3]/button"""
    return btn_selector


@pytest.fixture
def element1():
    x_selector3 = """//*[@id="app"]/main/div/div/div[2]/h2"""
    return x_selector3


@pytest.fixture
def result1():
    return "401"


@pytest.fixture
def site(scope='session'):
    site_instance = Site(testdata['address'])
    yield site_instance
    site_instance.close()


@pytest.fixture
def element2():
    x_selector3 = """//*[@id="app"]/main/nav/a/span"""
    return x_selector3


@pytest.fixture
def result2():
    return "Home"


@pytest.fixture
def create_post():
    return """//*[@id="create-btn"]"""


@pytest.fixture
def title():
    return """//*[@id="create-item"]/div/div/div[1]/div/label/input"""


@pytest.fixture
def description():
    return """//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea"""


@pytest.fixture
def content():
    return """//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea"""


@pytest.fixture
def create_post_finish():
    return """//*[@id="create-item"]/div/div/div[7]/div/button"""


@pytest.fixture
def post():
    return """//*[@id="app"]/main/div/div[1]/div/div[3]"""


@pytest.fixture
def title_post():
    return "New post"