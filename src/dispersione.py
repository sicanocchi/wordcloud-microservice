import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io

# Dati
x = [1, 2, 1.5, 3, 2.5, 4, 4.5, 5, 2, 1, 1.2, 3.8, 4.2, 1.3, 0.8]  # Importanza
y = [0.5, 1, 1.5, 1.8, 2.5, 2.8, 3.5, 4, 1.2, 1.8, 0.7, 3.2, 3.8, 0.9, 0.4]  # Frequenza di scelta
labels = [
    "Utilità del lavoro", "Senso di appartenenza", "Rapporto con l'Azienda", 
    "Ambiente di lavoro", "Orario di lavoro", "Quantità di lavoro",
    "Pianificazione del lavoro", "Prospettive di carriera", "Relazioni colleghi",
    "Autonomia e responsabilità inadeguate", "Identificazione Luxury", 
    "Cultura organizzativa", "Equilibrio tra lavoro e vita privata", 
    "Scarsa chiarezza dei ruoli", "Valutazione"
]
def generate_dispersione(x, y, labels):
    # Creazione del grafico
    fig, ax = plt.subplots(figsize=(12, 6))

    # Aggiunta dei punti
    ax.scatter(x, y, color='red')

    # Aggiunta delle etichette ai punti
    for i, label in enumerate(labels):
        ax.text(x[i] + 0.1, y[i], label, fontsize=8)

    # Linee mediane
    ax.axhline(y=2, color='black', linestyle='--', linewidth=0.8)  # Linea orizzontale
    ax.axvline(x=2.5, color='black', linestyle='--', linewidth=0.8)  # Linea verticale

    # Personalizzazioni
    ax.set_xlim(0, 5.5)
    ax.set_ylim(0, 5)
    ax.set_xlabel("IMPORTANZA", fontsize=12, labelpad=10)
    ax.set_ylabel("FREQUENZA DI SCELTA", fontsize=12, labelpad=10)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('green')
    ax.spines['bottom'].set_color('green')
    ax.tick_params(axis='both', which='both', color='green')

    # Titolo
    plt.title("Distribuzione Importanza-Frequenza", fontsize=14, pad=15)

    # Salvataggio e visualizzazione
    plt.tight_layout()

    byte_io = io.BytesIO()
    plt.savefig(byte_io, format='PNG')
    plt.close()

    # Restituisce l'immagine come array di byte
    byte_io.seek(0)
    return byte_io.read()