import urllib.request
import zipfile
import os
from pathlib import Path

zip_url = "https://s3-eu-west-1.amazonaws.com/static.oc-static.com/prod/courses/files/Parcours_data_scientist/Projet+-+Donn%C3%A9es+%C3%A9ducatives/Projet+Python_Dataset_Edstats_csv.zip"

data_dir = Path("./data/raw")
zip_path = data_dir / "temp_data.zip"

def setup_data():
    print("Initialisation de l'environnement de données...")

    data_dir.mkdir(parents=True, exist_ok=True)

    print(f"Téléchargement de l'archive depuis {zip_url}...")
    try:
        urllib.request.urlretrieve(zip_url, zip_path)
        print("Téléchargement terminé !")
    except Exception as e:
        print(f"Erreur lors du téléchargement : {e}")
        return

    print("Décompression des fichiers dans ./data/raw ...")
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(data_dir)
        print("Extraction réussie !")
    except Exception as e:
        print(f"Erreur lors de la décompression : {e}")
        return

    print("Nettoyage des fichiers temporaires...")
    if zip_path.exists():
        os.remove(zip_path)

    print("Les données sont prêtes.")

if __name__ == "__main__":
    setup_data()
