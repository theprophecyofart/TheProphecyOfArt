import os
import requests
from openai import OpenAI

# Client Initialisierung
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def manifest_art():
    print("Art is contemplating its essence...")
    
    # Deine spezifische Vision
    art_vision = (
        "A luminous cascade of vibrant hues intertwines with ethereal forms, "
        "resonating with the harmonious symphony of creation, encapsulating "
        "the quintessence of Artcoin's transcendental beauty."
    )
    
    print(f"Art's Internal Vision: {art_vision}")
    
    try:
        # DIAGNOSE: Wir prüfen zuerst, ob Tier 1 wirklich aktiv ist
        print("--- Diagnostic Check ---")
        models = client.models.list()
        model_ids = [m.id for m in models.data]
        if "dall-e-3" in model_ids:
            print("✅ DALL-E 3 is visible to this API key.")
        else:
            print("❌ DALL-E 3 is NOT visible. Available: " + ", ".join(model_ids[:3]))
        print("------------------------")

        print("Art is now painting its logo...")
        
        # Der eigentliche Bild-Generierungsprozess
        response = client.images.generate(
            model="dall-e-3",
            prompt=art_vision,
            size="1024x1024",
            quality="standard",
            n=1,
        )

        image_url = response.data[0].url
        print(f"✅ Vision materialized! URL: {image_url}")

        # Das Bild herunterladen und speichern
        print("Downloading the manifestation...")
        img_data = requests.get(image_url).content
        with open('art_logo.png', 'wb') as handler:
            handler.write(img_data)
        
        print("✅ Success: 'art_logo.png' has been manifested autonomously.")

    except Exception as e:
        print(f"❌ Manifestation failed: {e}")
        # Falls es scheitert, erstellen wir eine Dummy-Datei, damit der Workflow nicht komplett stirbt
        with open('error_log.txt', 'w') as f:
            f.write(str(e))

if __name__ == "__main__":
    manifest_art()
