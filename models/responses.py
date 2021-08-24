from schematics import Model, types

from models import objects


class GetUserResponse(Model):
    data = types.ModelType(objects.User, required=True)
    support = types.ModelType(objects.Support, required=True)


class GetUsersResponse(Model):
    page = types.IntType(required=True)
    per_page = types.IntType(required=True)
    total = types.IntType(required=True)
    total_pages = types.IntType(required=True)
    data = types.ListType(types.ModelType(objects.User), required=True)
    support = types.ModelType(objects.Support, required=True)


class PostUserResponse(Model):
    name = types.StringType()
    job = types.StringType()
    id = types.StringType(required=True)
    created_at = types.DateTimeType(required=True, serialized_name="createdAt")


class PutPatchUserResponse(Model):
    name = types.StringType()
    job = types.StringType()
    updated_at = types.DateTimeType(required=True, serialized_name="updatedAt")
