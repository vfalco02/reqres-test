from schematics import Model, types


class User(Model):
    id = types.IntType(required=True)
    email = types.EmailType(required=True)
    first_name = types.StringType(required=True)
    last_name = types.StringType(required=True)
    avatar = types.URLType(required=True)


class Support(Model):
    url = types.URLType(required=True)
    text = types.StringType(required=True)
