# test_api.py
import requests
import pytest

API_KEY = "4343_mYV3VmC2QKax6JUmsv196I4gIu9hRGijsVDXqdYwX_lCmkB0kyJ_oWYNSfF8EN8x"
BASE_URL = "https://demo.reportportal.io/api/v1/default_personal"  # Добавлен project name

def test_create_dashboard():
    response = requests.post(
        f"{BASE_URL}/dashboard",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "name": "MyTestDashboard",
            "description": "Test dashboard"
        }
    )
    print(response.text)
    assert response.status_code == 201, f"Ожидался 201, получен {response.status_code}. Ответ: {response.text}"

def test_negative_create():
    response = requests.post(
        f"{BASE_URL}/dashboard",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json={"invalid": "data"}  # Неправильные данные вместо пустого объекта
    )
    print(response.text)
    assert response.status_code == 400, f"Ожидался 400, получен {response.status_code}. Ответ: {response.text}"