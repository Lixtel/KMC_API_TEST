#created by Lixtel Rubis 06/26/2023
#this file is the feature file that uses gherkin language as steps for testing

@KMC_API_TEST
Feature: Check API Details
  This Feature File is an API Testing exam

  Scenario: Verify values of API response
    Given the response from API call is recorded
    When the record is transformed to json
    Then verify the primary field of Name to be Home & garden
    And verify the primary field of CanRelist to be True
    When the details of Promotions Feature as Name is recorded
    Then verify the recorded value of Description is Better position in category
