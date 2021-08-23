import math
import pytest


class TestGetUsers:
    @pytest.fixture(autouse=True)
    def setup(self, api):
        self.api = api

    def test_valid_response(self):
        """Make a request to /users and validate the response. Validation comes from the schematics models."""
        self.api.get_users()

    def test_page_info(self):
        """Validate the page information displayed aligns with the number of users."""
        response = self.api.get_users(per_page=1)
        expected_total = response.total
        assert response.total_pages == math.ceil(response.total / response.per_page)
        all_users = self.api.get_all_users()
        assert expected_total == len(all_users)

    def test_negative_page_number(self):
        """Test a negative page number. Will not throw an error, but will have a blank response"""
        response = self.api.get_users(page=-4)
        assert response.data == []

    def test_string_page_number(self):
        """Test a string page number. Will not throw an error and response will default to page 1"""
        response = self.api.get_users(page="abc", per_page=1)
        assert response.page == 1
        assert len(response.data) == 1

    # TODO: Add test for negative "per_page" parameter
    # TODO: Add test for string "per_page" parameter
