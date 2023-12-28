import pandas as pd

# Einlesen der Daten
data = pd.read_csv('DuneMaster.csv')

# Berechnung des Gesamteinsatzes pro Runde
total_deposit_per_round = data.groupby(['roundid', 'block_number'])['deposit_eth'].sum()

# Hinzufügen des Gesamteinsatzes pro Runde zu den ursprünglichen Daten
data = data.join(total_deposit_per_round, on=['roundid', 'block_number'], rsuffix='_total')

# Berechnung der Gewinnwahrscheinlichkeit für jede Transaktion
data['win_probability'] = data['deposit_eth'] / data['deposit_eth_total']

# Überprüfung, ob ein Spieler immer mit der gleichen Gewinnwahrscheinlichkeit spielt
consistent_win_probability = data.groupby('depositor')['win_probability'].nunique() == 1
probability_consistent_win_probability = consistent_win_probability.mean()

# Ausgabe der Wahrscheinlichkeit
print("Wahrscheinlichkeit, dass ein Spieler immer mit der gleichen Gewinnwahrscheinlichkeit spielt:", probability_consistent_win_probability)
