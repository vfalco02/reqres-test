import requests

from models import responses


class API():
    def __init__(self, base_url="https://reqres.in/api"):
        self.base_url = base_url

    def base_api_call(self, method, partial_url, expected_status_code=200, **kwargs):
        full_url = f"{self.base_url}/{partial_url}"
        response = requests.request(method, full_url, **kwargs)
        assert response.status_code == expected_status_code, \
            f"Status code - {response.status_code} - did not match the exptected - {expected_status_code}"
        response.raise_for_status()
        return response.json()

    def get_user(self, user_id, expected_status_code=200):
        partial_url = f"users/{user_id}"
        response = self.base_api_call("GET", partial_url, expected_status_code=expected_status_code)
        return responses.GetUserResponse(response)

    def get_users(self, page=1, per_page=10, expected_status_code=200):
        partial_url = "users"
        params = {"page": page, "per_page": per_page}
        response = self.base_api_call("GET", partial_url, expected_status_code=expected_status_code, params=params)
        return responses.GetUsersResponse(response)

    def get_all_users(self, start=1, users=[]):
        resp = self.get_users(page=start, per_page=10)
        users.extend(resp.data)
        if resp.page < resp.total_pages:
            self.get_all_users(start=resp.page+1, users=users)
        return users