#created by Lixtel Rubis 06/26/2023
#This step definition file will translate the gherkin languages in the feature file

from pytest_bdd import scenarios, given, parsers, when, then

scenarios("../features/check_details.feature") #connect to check_details.feature

@given(parsers.parse("the response from API call is recorded"))
def get_api_response(apitest_obj):
    apitest_obj.apitest_get_response() #call the apitest_get_response method
@when(parsers.parse("the record is transformed to json"))
def change_response_to_json(apitest_obj):
    apitest_obj.apitest_resp_to_json() #call the apitest_resp_to_json method

@then(parsers.parse("verify the primary field of {title} to be {value}"))
def check_api_resp_details(apitest_obj,title,value):
    apitest_obj.apitest_check_primary_fields(title,value) #call the apitest_check_primary_fields method

@when(parsers.parse("the details of {group} {field} as {name} is recorded"))
def get_record(apitest_obj,group,field,name):
    apitest_obj.apitest_get_record(group,field,name) #call the apitest_get_record method

@then(parsers.parse("verify the recorded value of {title} is {value}"))
def check_record_value(apitest_obj, title, value):
    apitest_obj.apitest_check_record_value(title,value) #call the apitest_check_record_value method

