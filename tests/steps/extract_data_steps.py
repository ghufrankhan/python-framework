import re
from behave import Step
from common.common_functions import add_space_after_numbers
from hamcrest import assert_that, is_not


@Step("I extract the registration numbers from the text file '{file_name}' located in the input_files folder")
def extract_data_from_input_text_file(context, file_name):
    # Reads the text file located in the input_files folder
    file_path = f"input_files/{file_name}"
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()

    # Regex pattern for reg nums
    pattern = r"[A-Z]{2}[0-9]{2}\s?[A-Z]{3}"

    # Finds all the reg nums that match pattern and adds to a list
    registration_plates = re.findall(pattern, text)

    # Adds a space if needed after nums and save to context
    context.registration_plates = [
        add_space_after_numbers(reg) for reg in registration_plates
    ]

    # Fails the test if no reg nums found
    assert_that(context.registration_plates, is_not([]), "No registration plates found")


@Step("I extract the data from the text file '{file_name}' located in the output_files folder")
def extract_data_from_output_text_file(context, file_name):
    # Reads the text file located in the output_files folder
    file_path = f"output_files/{file_name}"
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    # Strips whitespace from each line, adds each line to a list and saves to context
    context.output_data = [line.strip() for line in lines]

    # Fails the test if no data found
    assert_that(context.output_data, is_not([]), "Output file is empty")
