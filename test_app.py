import pytest

from app import app

client = app.test_client()


def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.get_json() == {"status": "ok"}


@pytest.mark.parametrize(
    "yol, a, b, beklenen",
    [
        ("topla", 2, 3, 5),
        ("cikar", 5, 3, 2),
        ("carp", 4, 3, 12),
        ("bol", 10, 4, 2.5),
    ],
)
def test_islemler(yol, a, b, beklenen):
    r = client.get(f"/{yol}?a={a}&b={b}")
    assert r.status_code == 200
    assert r.get_json()["sonuc"] == beklenen


def test_bol_sifira():
    r = client.get("/bol?a=1&b=0")
    assert r.status_code == 400


@pytest.mark.parametrize("yol", ["topla", "cikar", "carp", "bol"])
def test_gecersiz_parametre(yol):
    r = client.get(f"/{yol}?a=x&b=3")
    assert r.status_code == 400


def test_eksik_parametre():
    r = client.get("/topla?a=2")
    assert r.status_code == 400