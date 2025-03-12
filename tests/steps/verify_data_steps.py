from behave import Step
from hamcrest import assert_that, equal_to


@Step("I check to see if the expected data matches the actual data")
def verify_data_matches(context):
    expected_data = context.car_details
    actual_data = set(context.output_data)

    # Check each expected record is in the actual data
    for expected_record in expected_data:
        assert_that(expected_record in actual_data, equal_to(True),
                    f"The following expected data is not in the actual data: {expected_record}")
