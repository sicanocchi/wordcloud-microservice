import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io

def generate_barre_in_pila(colors, labels, sizes):
    """
    Genera un grafico a barre in pila con colori personalizzati e restituisce l'immagine come array di byte.

    Args:
        colors (list): Lista di colori in formato "rgb(r, g, b)".
        labels (list): Etichette delle fette del grafico.
        sizes (list): Dimensioni delle fette del grafico.

    Returns:
        bytearray: L'immagine del grafico a barre in pila come array di byte.
    """

    # Crea il grafico a barre in pila
    fig, ax = plt.subplots()
    ax.bar(labels, sizes, color=colors)

    # Salva l'immagine in un buffer di memoria
    byte_io = io.BytesIO()
    plt.savefig(byte_io, format='PNG')
    plt.close()

    # Restituisce l'immagine come array di byte
    byte_io.seek(0)
    # Aggiungi la legenda in basso
    ax.legend(labels, loc='lower center', bbox_to_anchor=(0.5, -0.05), ncol=len(labels))

    return byte_io.read()