from tester.khaoula import make_request

BASE_URL = "https://api.frankfurter.app"

def test_latest_endpoint():
    """Teste le endpoint principal et la structure du JSON (Contrat)"""
    url = f"{BASE_URL}/latest"
    response, latency, error = make_request(url)

    # 1. Vérification de la robustesse (pas de timeout/erreur)
    if error:
        return {"name": "GET /latest", "status": "FAIL", "latency_ms": latency, "details": error}

    # 2. Vérification du code HTTP
    if response.status_code != 200:
        return {"name": "GET /latest", "status": "FAIL", "latency_ms": latency, "details": f"Erreur HTTP {response.status_code}"}

    # 3. Vérification du format JSON et des champs obligatoires
    try:
        data = response.json()
        if "amount" not in data or "base" not in data or "rates" not in data:
            return {"name": "GET /latest", "status": "FAIL", "latency_ms": latency, "details": "Champs obligatoires manquants"}
    except ValueError:
        return {"name": "GET /latest", "status": "FAIL", "latency_ms": latency, "details": "Le contenu n'est pas un JSON valide"}

    # Si tout passe :
    return {"name": "GET /latest", "status": "PASS", "latency_ms": latency, "details": ""}


def test_conversion_endpoint():
    """Teste le endpoint avec des paramètres (from=USD)"""
    url = f"{BASE_URL}/latest?from=USD&to=EUR"
    response, latency, error = make_request(url)

    if error or response.status_code != 200:
        return {"name": "GET /latest?from=USD", "status": "FAIL", "latency_ms": latency, "details": "Échec de la requête de conversion"}

    data = response.json()
    if data.get("base") != "USD":
        return {"name": "GET /latest?from=USD", "status": "FAIL", "latency_ms": latency, "details": "La devise de base retournée n'est pas l'USD"}

    return {"name": "GET /latest?from=USD", "status": "PASS", "latency_ms": latency, "details": ""}


def run_all_tests():
    """Exécute tous les tests et retourne une liste de résultats"""
    return [
        test_latest_endpoint(),
        test_conversion_endpoint()
    ]