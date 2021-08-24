import pytest
import requests

pytestmark = pytest.mark.regression


class TestGetUser:
    @pytest.fixture(autouse=True)
    def setup(self, api):
        self.api = api

    def test_valid_response(self):
        """Make a request to /users/2 and validate the response. Validation comes from the schematics models."""
        response = self.api.get_user(2)
        response.validate()

    def test_response_for_user_not_found(self):
        """Validate the error and response when a user ID is not found"""
        with pytest.raises(requests.HTTPError) as exc:
            self.api.get_user(99999, expected_status_code=404)
        response = exc.value.response
        assert response.reason == "Not Found", f"Response reason was not 'Not Found'. Actual: {response.reason}"
        assert response.json() == {}, f"Response body was not empty. Actual: {response.reason}"
