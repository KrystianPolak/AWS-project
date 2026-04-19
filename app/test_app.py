import pytest
from app import app, todos

@pytest.fixture
def client():
    # Uruchamiamy aplikację w specjalnym trybie testowym
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_homepage(client):
    """Test 1: Czy strona główna się ładuje i zwraca kod 200 (OK)"""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Moja Lista" in response.data # Sprawdzamy czy w HTML jest ten tekst

def test_add_task(client):
    """Test 2: Czy dodawanie zadania faktycznie powiększa listę"""
    initial_count = len(todos)
    
    # Symulujemy wysłanie formularza z nowym zadaniem
    response = client.post('/', data={'task': 'Zadanie testowe CI/CD'})
    
    # Po dodaniu aplikacja powinna nas przekierować (kod 302)
    assert response.status_code == 302 
    # Lista powinna być o 1 element dłuższa
    assert len(todos) == initial_count + 1
    # Nowe zadanie musi być na liście
    assert "Zadanie testowe CI/CD" in todos