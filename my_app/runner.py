import datetime
import sys
import os

# Petite astuce pour pouvoir importer storage.py qui est dans le dossier parent
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import storage
from tester.tests import run_all_tests

def execute_run():
    """Lance les tests, calcule les métriques et sauvegarde le tout."""
    print("🚀 Début de la campagne de tests...")
    
    results = run_all_tests()
    
    # Calcul des statistiques
    passed = sum(1 for r in results if r["status"] == "PASS")
    failed = sum(1 for r in results if r["status"] == "FAIL")
    total = len(results)
    
    error_rate = failed / total if total > 0 else 0
    
    latencies = [r["latency_ms"] for r in results if r["latency_ms"] > 0]
    latency_avg = sum(latencies) / len(latencies) if latencies else 0
    latency_p95 = max(latencies) if latencies else 0 # Simplification du P95
    
    # Formatage de l'heure actuelle en format ISO
    timestamp = datetime.datetime.now(datetime.timezone.utc).isoformat()
    
    # Construction de la structure de données finale
    run_data = {
        "api": "Frankfurter",
        "timestamp": timestamp,
        "summary": {
            "passed": passed,
            "failed": failed,
            "error_rate": round(error_rate, 2),
            "latency_ms_avg": int(latency_avg),
            "latency_ms_p95": int(latency_p95)
        },
        "tests": results
    }
    
    # Sauvegarde dans la base de données
    storage.save_run(run_data)
    
    print(f"✅ Run terminé ! Succès: {passed} | Échecs: {failed} | Latence moy: {int(latency_avg)}ms")
    return run_data

# Si on exécute ce fichier directement dans le terminal
if __name__ == "__main__":
    execute_run()