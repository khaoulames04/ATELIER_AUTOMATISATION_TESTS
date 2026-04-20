from flask import Flask, render_template, jsonify
import storage
from my_app.runner import execute_run

app = Flask(__name__)

@app.route('/')
def home():
    # On garde la page d'accueil d'origine !
    return render_template('consignes.html')

@app.route('/run')
def trigger_run():
    """Déclenche l'exécution des tests manuellement via le web"""
    run_data = execute_run()
    return jsonify({
        "message": "Tests exécutés avec succès !",
        "data": run_data
    })

@app.route('/dashboard')
def show_dashboard():
    """Affiche l'interface web avec l'historique des tests"""
    # Récupère tous les historiques depuis la base SQLite
    all_runs = storage.get_all_runs()
    # Envoie les données au fichier HTML
    return render_template('dashboard.html', runs=all_runs)

if __name__ == "__main__":
    app.run(debug=True, port=8080)