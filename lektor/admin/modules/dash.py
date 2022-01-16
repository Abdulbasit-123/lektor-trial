from flask import Blueprint
from flask import render_template


bp = Blueprint("dash", __name__, url_prefix="/admin")


@bp.route("/<any(edit, delete, preview, add-child, upload):view>", endpoint="app")
def app_view(**kwargs):
    """Render the React admin GUI app."""
    return render_template("dash.html")
