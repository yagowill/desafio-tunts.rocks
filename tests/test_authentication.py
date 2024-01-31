from authentication import auth
from google.oauth2.credentials import Credentials

def test_auth():
    assert isinstance(auth(), Credentials)