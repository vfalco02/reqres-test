import pytest

pytestmark = pytest.mark.regression


class TestPutUser:
    @pytest.fixture(autouse=True)
    def setup(self, api):
        self.api = api
        self.new_name = "John Tester"
        self.new_job = "Tester"

    def test_valid_response(self):
        """Put a new name/job for user 1 and assert it updates.

        Note: This will not actually change the value of ID 1 due to this being a public API
        """
        response = self.api.put_user(1, self.new_name, self.new_job)
        response.validate()
        assert response.name == self.new_name
        assert response.job == self.new_job

    def test_valid_response_if_no_name(self):
        """Put a new job with no name for user 1 and assert it updates.

        Note: This will not actually change the value of ID 1 due to this being a public API
        """
        response = self.api.put_user(2, None, self.new_job)
        response.validate()
        assert response.name is None
        assert response.job == self.new_job

    def test_valid_response_if_no_job(self):
        """Put a new name with no job for user 1 and assert it updates.

        Note: This will not actually change the value of ID 1 due to this being a public API
        """
        response = self.api.put_user(3, self.new_name, None)
        response.validate()
        assert response.name == self.new_name
        assert response.job is None

    # TODO: Add tests for different parameter values (this particular API doesn't behave differently however)
