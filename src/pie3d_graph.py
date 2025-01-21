import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io

def generate_pie3d(colors, labels, sizes, explode, title):
    """
    Genera un grafico a torta tridimensionale con colori personalizzati e restituisce l'immagine come array di byte.

    Args:
        colors (list): Lista di colori in formato "rgb(r, g, b)".
        labels (list): Etichette delle fette del grafico.
        sizes (list): Dimensioni delle fette del grafico.
        explode (list): Esplosione delle fette del grafico.
        title (str): Titolo del grafico.

    Returns:
        bytearray: L'immagine del grafico a torta tridimensionale come array di byte.
    """

    # Crea il grafico a torta tridimensionale
    fig, ax = plt.subplots()
    ax.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90, pctdistance=0.85)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle

    # Aggiungi il titolo al grafico
    plt.title(title)

    # Salva l'immagine in un buffer di memoria
    byte_io = io.BytesIO()
    plt.savefig(byte_io, format='PNG')
    plt.close()

    # Restituisce l'immagine come array di byte
    byte_io.seek(0)
    return byte_io.read()