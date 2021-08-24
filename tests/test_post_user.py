import pytest

pytestmark = pytest.mark.regression


class TestPostUser:
    @pytest.fixture(autouse=True)
    def setup(self, api):
        self.api = api
        self.name = "John Tester"
        self.job = "Tester"

    def test_valid_response(self):
        response = self.api.post_user(self.name, self.job)
        response.validate()
        assert response.name == self.name
        assert response.job == self.job
        assert False

    def test_valid_response_if_no_name(self):
        response = self.api.post_user(None, self.job)
        response.validate()
        assert response.name is None
        assert response.job == self.job

    def test_valid_response_if_no_job(self):
        response = self.api.post_user(self.name, None)
        response.validate()
        assert response.name == self.name
        assert response.job is None

    # TODO: Add tests for different parameter values (this particular API doesn't behave differently however)
