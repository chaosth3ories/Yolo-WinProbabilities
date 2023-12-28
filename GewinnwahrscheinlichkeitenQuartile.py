import pandas as pd

# Einlesen der Daten
data = pd.read_csv('DuneMaster.csv')

# Berechnung der durchschnittlichen Gewinnwahrscheinlichkeit pro Spieler
average_win_probability_per_player = data.groupby('depositor')['win_probability'].mean()

# Berechnung der Quartile und der Varianz
probability_quartiles = average_win_probability_per_player.quantile([0.25, 0.5, 0.75])
probability_variance = average_win_probability_per_player.var()

# Ausgabe der Quartile und Varianz
print("Quartile der Gewinnwahrscheinlichkeiten:")
print(probability_quartiles)
print("\nVarianz der Gewinnwahrscheinlichkeiten:", probability_variance)
