import requests
import time

def make_request(url, timeout=3, max_retries=1):
    """
    Requête HTTP GET avec mesure de latence et retry.
    """
    attempt = 0
    while attempt <= max_retries:
        start_time = time.time()
        try:
            # On tente la requête avec un timeout défini
            response = requests.get(url, timeout=timeout)
            
            # Calcul de la latence en millisecondes
            latency_ms = int((time.time() - start_time) * 1000)
            
            return response, latency_ms, None
            
        except requests.exceptions.Timeout:
            attempt += 1
            if attempt > max_retries:
                return None, 0, f"Timeout après {max_retries} retries"
                
        except requests.exceptions.RequestException as e:
            # Pour toute autre erreur de connexion (DNS, refusé, etc.)
            return None, 0, f"Erreur de connexion : {str(e)}"
            
    return None, 0, "Erreur inconnue"