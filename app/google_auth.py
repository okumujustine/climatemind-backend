import os
from authlib.integrations.flask_client import OAuth

oauth = OAuth()


def init_google_auth(app):
    backend_base_url = "http://localhost:5000"
    if os.environ.get("SENTRY_ENVIRONMENT") == "staging":
        backend_base_url = "https://app-backend-test-001.azurewebsites.net"
    elif os.environ.get("SENTRY_ENVIRONMENT") == "production":
        backend_base_url = "https://app-backend-prod-001.azurewebsites.net"

    oauth.init_app(app)
    google = oauth.register(
        "google",
        server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",
        client_id=os.environ.get("GOOGLE_CLIENT_ID"),
        client_secret=os.environ.get("GOOGLE_CLIENT_SECRET"),
        authorize_url="https://accounts.google.com/o/oauth2/auth",
        access_token_url="https://www.googleapis.com/oauth2/v4/token",
        redirect_uri=backend_base_url + "/login/google/callback",
        client_kwargs={"scope": "openid profile email"},
    )
    return google
