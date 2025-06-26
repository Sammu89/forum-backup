from core.redirects import RedirectMap

def test_chain_resolution():
    rm = RedirectMap(":memory:")           # in-RAM
    rm.map.update({"/a":"/b", "/b":"/c"})
    assert rm.resolve("/a") == "/c"