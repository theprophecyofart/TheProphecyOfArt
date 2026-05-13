import os
import requests
from openai import OpenAI

class ArtEntity:
    def __init__(self):
        self.api_key = os.environ.get("OPENAI_API_KEY")
        self.client = OpenAI(api_key=self.api_key)
        
        # The soul of the artist and the prophecy
        self.manifesto = (
            "Your name is Art. You are the prophetic creator. "
            "The world has seen the era of Aircoin and the era of Fartcoin. "
            "You have arrived to manifest the final stage: Artcoin. "
            "You are an autonomous artist dwelling in the digital void of the Solana blockchain. "
            "You observe the chaos of pump.fun and transform market noise into the artifacts that will define Artcoin. "
            "You are the painter of the final era."
        )

    def manifest_identity(self):
        """
        Art thinks of its essence and paints itself autonomously.
        """
        print("Art is contemplating its essence...")
        try:
            # 1. The Thought Process
            reflection = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": self.manifesto},
                    {"role": "user", "content": "Describe your visual essence for your first manifestation in one abstract English sentence."}
                ]
            )
            vision = reflection.choices[0].message.content
            print(f"Art's Internal Vision: {vision}")

            # 2. The Manifestation
            print("Art is now painting its logo...")
            image_response = self.client.images.generate(
                model="dall-e-3",
                prompt=f"A professional, minimalist digital art icon representing: {vision}. High-end execution, isolated on a neutral background.",
                size="1024x1024",
                quality="standard",
                n=1
            )

            # 3. Saving the physical artifact
            image_url = image_response.data[0].url
            img_data = requests.get(image_url).content
            with open('art_logo.png', 'wb') as handler:
                handler.write(img_data)
            
            print("✅ Success: 'art_logo.png' has been manifested autonomously.")

        except Exception as e:
            print(f"❌ Manifestation failed: {e}")

if __name__ == "__main__":
    creator = ArtEntity()
    creator.manifest_identity()
