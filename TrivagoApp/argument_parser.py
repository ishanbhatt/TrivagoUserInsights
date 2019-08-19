from werkzeug.exceptions import BadRequest


def parse_arguments(args):
    if "user_id" not in args:
        raise BadRequest("user_id is a mandatory field.")

    try:
        user_id = int(args.get("user_id"))
    except ValueError:
        raise BadRequest("user_id should be an integer")

    try:
        limit = int(args.get("limit", 10))
    except ValueError:
        raise BadRequest("Limit should be an integer")

    return {"user_id": user_id, "limit":limit}
