import pytest
import requests


class TestGetUser:
    def test_valid_response(self, api):
        """Make a request to /users/2 and validate the response. Validation comes from the schematics models."""
        api.get_user(2)

    def test_response_for_user_not_found(self, api):
        """Validate the error and response when a user ID is not found"""
        with pytest.raises(requests.HTTPError) as exc:
            api.get_user(99999, expected_status_code=404)
        response = exc.value.response
        assert (
            exc.value.response.reason == "Not Found"
        ), f"Response reason was not 'Not Found'. Actual: {response.reason}"
        assert (
            exc.value.response.json() == {}
        ), f"Response body was not empty. Actual: {response.reason}"
