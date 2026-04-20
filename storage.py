import sqlite3
import json

DB_FILE = "runs.db"

def init_db():
    """Initialise la base de données si elle n'existe pas."""
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS runs
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  timestamp TEXT,
                  data TEXT)''')
    conn.commit()
    conn.close()

def save_run(run_data):
    """Sauvegarde les résultats d'un run dans la base de données."""
    init_db()
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    # On convertit le dictionnaire python en texte JSON pour le stocker
    c.execute("INSERT INTO runs (timestamp, data) VALUES (?, ?)",
              (run_data["timestamp"], json.dumps(run_data)))
    conn.commit()
    conn.close()

def get_all_runs():
    """Récupère tout l'historique des runs, du plus récent au plus ancien."""
    init_db()
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT data FROM runs ORDER BY id DESC")
    rows = c.fetchall()
    conn.close()
    # On retransforme le texte JSON en dictionnaire python
    return [json.loads(row[0]) for row in rows]