# ⏱️ CatanClock

Timer für Brettspiele mit individuellen Spieler-Zeiten und farbcodierter Anzeige.

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