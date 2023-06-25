#created by Lixtel Rubis 06/26/2023
#this file is the constants for pytest-bdd framework

import pytest

@pytest.fixture()
def apitest_obj(): #create object for ApiTestObj class
    from api_test.page_object.api_test_objects import ApiTestObj
    return ApiTestObj()
