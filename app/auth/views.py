from app.auth import bp

@bp.route("/")
@bp.route("/login")
def login():
    return "login, baby!"
