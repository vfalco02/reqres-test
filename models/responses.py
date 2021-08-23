from schematics import Model, types

from models import objects


class BaseResponse(Model):
    support = types.ModelType(objects.Support, required=True)


class GetUserResponse(BaseResponse):
    data = types.ModelType(objects.User, required=True)


class GetUsersResponse(BaseResponse):
    page = types.IntType(required=True)
    per_page = types.IntType(required=True)
    total = types.IntType(required=True)
    total_pages = types.IntType(required=True)
    data = types.ListType(types.ModelType(objects.User), required=True)
