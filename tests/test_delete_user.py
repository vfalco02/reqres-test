import pytest
import requests

pytestmark = pytest.mark.regression


class TestDeleteUser:
    @pytest.fixture(autouse=True)
    def setup(self, api):
        self.api = api
        user_setup = self.api.post_user("Test Delete", "Deleter")
        self.user_id = user_setup.id

    def test_delete_user(self):
        """Delete an existing user"""
        self.api.delete_user(self.user_id)

    @pytest.mark.xfail(reason="Non existent ID should throw a 404 error")
    def test_delete_non_existent_user(self):
        """Using this test to simulate an xfail for a scenario we would 'expect', but is not currently supported"""
        with pytest.raises(requests.HTTPError) as exc:
            self.api.delete_user(99999, expected_status_code=404)
        response = exc.value.response
        assert response.reason == "Not Found", f"Response reason was not 'Not Found'. Actual: {response.reason}"
        assert response.json() == {}, f"Response body was not empty. Actual: {response.reason}"
