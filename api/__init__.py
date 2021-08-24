import logging
import requests

from models import responses

LOGGER = logging.getLogger()


class API:
    def __init__(self, base_url="https://reqres.in/api"):
        self.base_url = base_url

    def base_api_call(self, method, partial_url, expected_status_code=200, skip_resp_log=False, **kwargs):
        full_url = f"{self.base_url}/{partial_url}"
        response = requests.request(method, full_url, **kwargs)
        LOGGER.info(f"'{method.upper()}' request to '{full_url}' returned a status code of '{response.status_code}'")
        assert (
            response.status_code == expected_status_code
        ), f"Status code - {response.status_code} - did not match the exptected - {expected_status_code}"
        response.raise_for_status()
        if response.content != b"":  # If there is no response body, don't return anything
            msg = f"Response body: {response.json()}"
            if len(msg) > 600:
                LOGGER.info("Response body too large. Not logging.")
            else:
                LOGGER.info(f"Response body: {response.json()}")
            return response.json()

    def get_user(self, user_id, expected_status_code=200):
        LOGGER.info(f"Getting user with ID '{user_id}' and expecting status code '{expected_status_code}'")
        partial_url = f"users/{user_id}"
        response = self.base_api_call("GET", partial_url, expected_status_code=expected_status_code)
        return responses.GetUserResponse(response)

    def get_users(self, page=1, per_page=10, expected_status_code=200):
        LOGGER.info(
            f"Getting users from page {page} with {per_page} users per page and expecting status code "
            f"'{expected_status_code}'"
        )
        partial_url = "users"
        params = {"page": page, "per_page": per_page}
        response = self.base_api_call("GET", partial_url, expected_status_code=expected_status_code, params=params)
        return responses.GetUsersResponse(response)

    def get_all_users(self, start=1, users=[]):
        LOGGER.info(f"Getting all users on page {start}")
        resp = self.get_users(page=start, per_page=10)
        users.extend(resp.data)
        if resp.page < resp.total_pages:
            self.get_all_users(start=resp.page + 1, users=users)
        return users

    def post_user(self, name, job, expected_status_code=201):
        LOGGER.info(
            f"Creating a user with name '{name}', job '{job}' and expecting status code '{expected_status_code}'"
        )
        partial_url = "users"
        body = {"name": name, "job": job}
        if name is None:
            body.pop("name")
        if job is None:
            body.pop("job")
        response = self.base_api_call(
            "POST", partial_url=partial_url, data=body, expected_status_code=expected_status_code
        )
        return responses.PostUserResponse(response)

    def put_user(self, user_id, name, job, expected_status_code=200):
        LOGGER.info(
            f"Updating user '{user_id}' with a PUT to name '{name}', job '{job}' and expected status code "
            f"{expected_status_code}"
        )
        response = self.put_or_patch_user("PUT", user_id, name, job, expected_status_code)
        return response

    def patch_user(self, user_id, name, job, expected_status_code=200):
        LOGGER.info(
            f"Updating user '{user_id}' with a PATCH to name '{name}', job '{job}' and expected status code "
            f"{expected_status_code}"
        )
        response = self.put_or_patch_user("PATCH", user_id, name, job, expected_status_code)
        return response

    def put_or_patch_user(self, verb, user_id, name, job, expected_status_code):
        partial_url = f"users/{user_id}"
        body = {"name": name, "job": job}
        if name is None:
            body.pop("name")
        if job is None:
            body.pop("job")
        response = self.base_api_call(
            verb, partial_url=partial_url, data=body, expected_status_code=expected_status_code
        )
        return responses.PutPatchUserResponse(response)

    def delete_user(self, user_id, expected_status_code=204):
        LOGGER.info(f"Deleting user '{user_id}' and expected status code {expected_status_code}")
        partial_url = f"users/{user_id}"
        self.base_api_call("DELETE", partial_url=partial_url, expected_status_code=expected_status_code)
