# ⏱️ CatanClock

Timer für Brettspiele mit individuellen Spieler-Zeiten und farbcodierter Anzeige.


running at: https://catanclock-production.up.railway.app/settings

## Features

- 2-4 Spieler mit eigenen Timern (10-40 Min)
- Farbcodierte Fullscreen-Anzeige (Rot, Weiß, Blau, Gelb)
- Drag & Drop Spielerreihenfolge
- Undo-Funktion
- Zeit ablauf → +5 Min oder Elimination

## Installation

```bash
pip install flask
flask --app app run
```

## Screenshots
<p>
  <img src="https://github.com/user-attachments/assets/c38aedfe-d232-48e3-9040-5496a756930c" width="45%">
  <img src="https://github.com/user-attachments/assets/7b76299b-d913-49d1-beb3-2d7ccba0c79a" width="45%">
</p>

## Nutzung

1. Settings: Spieler, Zeit, Farben wählen
2. "Spiel starten"
3. Großer Button → Nächster Spieler
4. Pfeil links → Zurück
5. Zahnrad → Settings (Zeiten bleiben erhalten)

## Stack

- Flask + Session
- Tailwind CSS
- localStorage für Timer-State
