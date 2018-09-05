import hashlib
from urllib.parse import urlparse

from extensions import db
from models import URL


def shorten_url(url: str):
    if not (url.startswith('https://') or url.startswith('http://')):
        url = 'http://' + url
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    if not domain.startswith('www.'):
        domain = 'www.' + domain
    path = parsed_url.path
    sha_signature = hashlib.sha256((domain + path).encode()).hexdigest()

    existing_urls = URL.query.filter(URL.domain == domain, URL.path == path).all()
    if existing_urls:
        return 'localhost:5000/shorten/redirect/' + existing_urls[0].hash

    obj = URL(domain=domain, path=path, hash=sha_signature, original_url=url)
    db.session.add(obj)
    db.session.commit()

    return 'localhost:5000/shorten/redirect/' + obj.hash


def fetch_list():
    all_urls = URL.query.all()
    dict_list = []
    for i in all_urls:
        d = {'original_url' : i.original_url, 'shortened_url' : 'localhost:5000/shorten/redirect/'+i.hash}
        dict_list.append(d)
    return dict_list


def fetch_original(shortened_url):
    url_hash = shortened_url.rsplit('/', 1)[-1]
    original_url = URL.query.filter(URL.hash == url_hash).first().original_url
    return original_url


def delete_url(url_hash):
    URL.query.filter(URL.hash == url_hash).delete()
    db.session.commit()
