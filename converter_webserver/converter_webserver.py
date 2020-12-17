from sanic import Sanic
from sanic.response import json
from sanic_jwt import Initialize, exceptions
from sanic_jwt.decorators import protected
from utils import get_users, User

app = Sanic("Converter")


async def authenticate(request):
    username = request.json.get("username", None)
    password = request.json.get("password", None)

    if not username or not password:
        raise exceptions.AuthenticationFailed("Missing username or password.")

    username_table = get_users()
    user = username_table.get(username, None)

    if user is None:
        raise exceptions.AuthenticationFailed("User not found.")

    if password != user.password:
        raise exceptions.AuthenticationFailed("Password is incorrect.")

    return user


@app.route("/convert", methods=['POST'])
@protected()
async def convert(request):
    return json({x["name"]: x[[a for a in x.keys() if "val" in a.lower()][0]] for x in request.json})


def main():
    Initialize(app, authenticate=authenticate)
    app.run(host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
