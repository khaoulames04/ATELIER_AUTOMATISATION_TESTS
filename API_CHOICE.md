# API Choice

- Étudiant : **Khaoula MESBAHI**
- API choisie : **Frankfurter**
- URL base : `https://api.frankfurter.app`
- Documentation officielle / README : `https://www.frankfurter.app/docs/`
- Auth : **None**
- Endpoints testés :
  - GET `/latest` (Récupère les taux de change les plus récents)
  - GET `/latest?from=USD&to=EUR` (Convertit une devise spécifique)
- Hypothèses de contrat (champs attendus, types, codes) :
  - Code HTTP attendu : 200 OK
  - Format attendu : JSON
  - Le JSON doit contenir une clé `amount` (float/int), une clé `base` (string) et un objet `rates`.
- Limites / rate limiting connu : Pas de limite stricte bloquante indiquée, mais usage raisonnable attendu.
- Risques (instabilité, downtime, CORS, etc.) : API publique maintenue par un tiers, risque de timeout si le serveur est surchargé.