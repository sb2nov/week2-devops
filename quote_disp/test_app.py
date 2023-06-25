import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client

def test_get_quote(client):
    rv = client.get('/get_quote')
    assert b"The greatest glory in living lies not in never falling, but in rising every time we fall. -Nelson Mandela" in rv.data
    assert b"The way to get started is to quit talking and begin doing. -Walt Disney" in rv.data
    assert b"Your time is limited, so don't waste it living someone else's life. Don't be trapped by dogma – which is living with the results of other people's thinking. -Steve Jobs" in rv.data
    assert b"If life were predictable it would cease to be life, and be without flavor. -Eleanor Roosevelt" in rv.data
    assert b"If you look at what you have in life, you'll always have more. If you look at what you don't have in life, you'll never have enough. -Oprah Winfrey" in rv.data
    assert b"If you set your goals ridiculously high and it's a failure, you will fail above everyone else's success. -James Cameron" in rv.data