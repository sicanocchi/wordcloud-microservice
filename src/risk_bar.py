import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io
import numpy as np

def create_risk_bar_chart(categories, values, groups, risk_zones, risk_colors, group_labels, legend_labels):
    """
    Crea un grafico a barre orizzontali con fasce di rischio sullo sfondo.

    :param categories: Lista di stringhe, nomi delle categorie.
    :param values: Lista di liste, ogni sottolista rappresenta i valori di un gruppo per categoria.
    :param groups: Lista di stringhe, nomi dei gruppi.
    :param risk_zones: Lista di tuple, ogni tuple rappresenta (inizio, fine) per una fascia di rischio.
    :param risk_colors: Lista di stringhe, colori delle fasce di rischio.
    :param group_labels: Lista di stringhe, etichette per i gruppi.
    :param legend_labels: Lista di stringhe, etichette della leggenda.
    """
    num_categories = len(categories)
    bar_height = 0.15
    fig, ax = plt.subplots(figsize=(12, 6))

    # Aggiungi le fasce di rischio come sfondo
    for i, (start, end) in enumerate(risk_zones):
        ax.axvspan(start, end, color=risk_colors[i], alpha=0.3, label=f"Rischio: {legend_labels[i]}")

    # Definizione delle posizioni per le barre
    y_positions = np.arange(num_categories)
    offsets = np.linspace(-bar_height * (len(groups) - 1) / 2, bar_height * (len(groups) - 1) / 2, len(groups))

    # Aggiungi le barre per ogni gruppo
    for i, (group, offset) in enumerate(zip(groups, offsets)):
        ax.barh(y_positions + offset, values[i], height=bar_height, label=group_labels[i], alpha=0.8)

    # Configura assi e legenda
    ax.set_yticks(y_positions)
    ax.set_yticklabels(categories)
    ax.set_xlabel("Valore")
    ax.legend(loc="upper right")
    ax.grid(axis="x", linestyle="--", alpha=0.5)

    # Mostra il grafico
    plt.tight_layout()
    byte_io = io.BytesIO()
    plt.savefig(byte_io, format='PNG')
    plt.close()

    # Restituisce l'immagine come array di byte
    byte_io.seek(0)
    return byte_io.read()


# # Esempio di utilizzo
# categories = ["Identificazione Luxury", "Carico di Lavoro", "Autonomia", "Ambiente", "Relazioni", "Equilibrio Casa-Lavoro"]
# values = [
#     [95, 96, 92, 94, 97, 93],  # Valori per Responsabili di Team
#     [101, 103, 98, 106, 100, 105],  # Valori per Uffici
#     [107, 110, 103, 102, 108, 101],  # Valori per Magazzino
# ]
# groups = ["Responsabili di Team", "Uffici", "Magazzino"]
# risk_zones = [(0, 80), (80, 95), (95, 105), (105, 120), (120, 160)]
# risk_colors = ["#4CAF50", "#8BC34A", "#FFEB3B", "#FFC107", "#F44336"]
# group_labels = ["Responsabili di Team", "Uffici", "Magazzino"]
# legend_labels = ["Basso <80", "Medio-basso 80-95", "Medio 95-105", "Medio-alto 105-120", "Alto >120"]

# create_risk_bar_chart(categories, values, groups, risk_zones, risk_colors, group_labels, legend_labels)