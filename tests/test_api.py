import requests

def test_get():
    r = requests.get("http://localhost:5000/todos")
    assert r.status_code == 200

def test_post():
    r = requests.post("http://localhost:5000/todos", json={"task": "Test"})
    assert r.status_code == 201
