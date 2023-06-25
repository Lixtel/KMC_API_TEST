#created by Lixtel Rubis 06/26/2023
#this file contains the methods that can be called by the test framework

import requests

class ApiTestObj():

    response = {} #class variable for the response
    json_resp = {} #class variable for the json data
    record = {} #class variable for recorded data

    def apitest_get_response(self):

        url = "https://api.tmsandbox.co.nz/v1/Categories/6329/Details.json?catalogue=false" #url to the API

        self.response = requests.request('GET', url) #request method to initiate the API call and save the response to variable

        assert self.response.status_code == 200 #verify API status to successful


    def apitest_resp_to_json(self):
        self.json_resp = self.response.json() #transform response to Json data and save to variable

        assert self.json_resp != {} #verify Json record is not empty


    def apitest_check_primary_fields(self,title,value):
        result = str(self.json_resp[title]) #get value of json record for title then transform as string and save to variable

        assert result == value #verify the data is the same from expected

    def apitest_get_record(self,group,field,name):
        group_record = self.json_resp[group] #record the json data for the group

        for record_set in group_record: #loop for each group record
            if record_set[name] == field: #determine if record for name is same as field
                self.record = record_set #save record set as json data to a variable

    def apitest_check_record_value(self,title,value):
            assert self.record[title] == value #verify record data for a title is same as expected value