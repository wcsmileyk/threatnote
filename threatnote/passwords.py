import hashlib
import hmac

from werkzeug.security import generate_password_hash, check_password_hash

# Werkzeug < 2.3 stored salted hashes as "sha256$<salt>$<hmac hexdigest>".
# Werkzeug 3 refuses to verify them, so we check those ourselves.
LEGACY_METHOD = 'sha256'


def is_legacy_hash(pwhash):
    return bool(pwhash) and pwhash.split('$', 1)[0] == LEGACY_METHOD


def verify_password(pwhash, password):
    if not pwhash or password is None:
        return False
    if is_legacy_hash(pwhash):
        try:
            _, salt, hashval = pwhash.split('$', 2)
        except ValueError:
            return False
        digest = hmac.new(salt.encode(), password.encode(), hashlib.sha256).hexdigest()
        return hmac.compare_digest(digest, hashval)
    return check_password_hash(pwhash, password)


def hash_password(password):
    return generate_password_hash(password)
