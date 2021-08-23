import pytest
import requests


class TestGetUser():
    def test_valid_response(self, api):
        api.get_user(2)

    def test_response_for_user_not_found(self, api):
        with pytest.raises(requests.HTTPError) as exc:
            api.get_user(99999, expected_status_code=404)
        response = exc.value.response
        assert exc.value.response.reason == "Not Found", f"Response reason was not 'Not Found'. Actual: {response.reason}"
        assert exc.value.response.json() == {}, f"Response body was not empty. Actual: {response.reason}"
