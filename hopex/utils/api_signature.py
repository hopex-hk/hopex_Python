import datetime
import base64
import hashlib
from hashlib import sha256
import hmac
import json
from hopex.constant.system import HttpMethod


def create_signature(api_key, secret_key, request_method, request_path, builder):
    payload = dict()
    if request_method == HttpMethod.GET:
        payload = json.dumps(builder.param_map, indent=4, ensure_ascii=False)
    elif request_method == HttpMethod.POST:
        payload = json.dumps(builder.post_map, indent=4, ensure_ascii=False)

    date = utc_now()
    # print(date)
    sha256_hash = hashlib.sha256()
    sha256_hash.update(payload.encode('utf-8'))
    digest = sha256_hash.hexdigest()

    text_to_sign = "date: " + date + "\n"
    text_to_sign += request_method + " " + request_path + " HTTP/1.1" + "\n"
    text_to_sign += "digest: " + "SHA-256=" + digest

    # print(text_to_sign)
    signature = base64.b64encode(
        hmac.new(secret_key.encode('utf-8'), text_to_sign.encode('utf-8'), digestmod=sha256).digest())

    head_auth = "hmac apikey=\"" + api_key + "\", algorithm=\"hmac-sha256\", headers=\"date request-line digest\", " \
                                             "signature=\"" + signature.decode("utf-8") + "\""

    headers = {
        'Date': date,
        'Digest': 'SHA-256={}'.format(digest),
        'Authorization': head_auth,
        'Content-Type': 'application/json',
        'User-Agent': 'hopex'  # Please Specified Your Exchange Name
    }
    # print(json.dumps(headers, indent=4))
    builder.put_header(headers)


def utc_now():
    return datetime.datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')
