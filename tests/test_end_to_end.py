import pytest
import requests

pytestmark = pytest.mark.e2e


class TestEndToEnd:
    @pytest.fixture(autouse=True)
    def setup(self, api):
        self.api = api

    def test_create_update_delete_user(self):
        self.create_user()
        self.update_user_with_put()
        self.update_user_with_patch()
        self.delete_user()
        self.validate_user_deleted()

    def create_user(self):
        post_response = self.api.post_user("John Tester", "Tester")
        self.validate_response(post_response, "John Tester", "Tester")
        self.user_id = post_response.id

    def update_user_with_put(self):
        put_response = self.api.put_user(self.user_id, "Put John Tester", "Put Tester")
        self.validate_response(put_response, "Put John Tester", "Put Tester")

    def update_user_with_patch(self):
        put_response = self.api.patch_user(self.user_id, "Patch John Tester", "Patch Tester")
        self.validate_response(put_response, "Patch John Tester", "Patch Tester")

    def delete_user(self):
        self.api.delete_user(self.user_id)

    def validate_user_deleted(self):
        """Validate the user was deleted.

        Note since this API doesn't actually create/delete data, a non-existent ID was specified to simulate the
        expectation of this test
        """
        with pytest.raises(requests.HTTPError):
            self.api.get_user(999, expected_status_code=404)  # In a real test the ID would be self.user_id

    @staticmethod
    def validate_response(response, name, job):
        response.validate()
        assert response.name == name
        assert response.job == job
