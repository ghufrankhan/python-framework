#noinspection CucumberUndefinedStep
Feature: Motorway Test
"""
  The aim is to extract data from a text file, populate additional information via motorway.co.uk and then compare
  it with the output data and ensure the expected data exists.
"""


  Scenario: Extract data and add additional info and then compare with the output data
    Given I extract the registration numbers from the text file 'car_input - V5.txt' located in the input_files folder
    And I navigate to the motorway website
    When I enter each of the extracted registration numbers and populate the results data
    And I extract the data from the text file 'car_output - V5.txt' located in the output_files folder
    Then I check to see if the expected data matches the actual data