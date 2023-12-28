import pandas as pd

# Einlesen der Daten
data = pd.read_csv('DuneMaster.csv')

# Berechnung der durchschnittlichen Gewinnwahrscheinlichkeit pro Spieler
average_win_probability_per_player = data.groupby('depositor')['win_probability'].mean()

# Definition von Klassen für die Gewinnwahrscheinlichkeiten
probability_bins = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
probability_labels = ['0-0.1', '0.1-0.2', '0.2-0.3', '0.3-0.4', '0.4-0.5', '0.5-0.6', '0.6-0.7', '0.7-0.8', '0.8-0.9', '0.9-1']

# Zuordnung der Spieler zu Klassen
player_probability_class = pd.cut(average_win_probability_per_player, probability_bins, labels=probability_labels, right=False)

# Ausgabe der Spieleranzahl pro Klasse
print("Spieleranzahl pro Gewinnwahrscheinlichkeitsklasse:")
print(player_probability_class.value_counts().sort_index())
