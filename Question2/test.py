import service as serv

def test_shorten_url():
    retrieved = serv.shorten_url("www.test123.com")
    assert retrieved == "localhost:5000/shorten/redirect/ecda499d6cd507269abae21d8f2d82447ea11be5a8bce9cb7237938ee3c4f111"

def test_fetch_list():
    retrieved = serv.fetch_list()
    assert retrieved

def test_fetch_original():
    retrieved = serv.fetch_original("localhost:5000/shorten/redirect/ecda499d6cd507269abae21d8f2d82447ea11be5a8bce9cb7237938ee3c4f111")
    assert retrieved == "www.test123.com"