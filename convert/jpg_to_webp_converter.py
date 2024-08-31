from PIL import Image
import requests
from io import BytesIO
import os

def jpg_to_webp(urls, output_dir):
    try:
        os.makedirs(output_dir, exist_ok=True)  

        for i, url in enumerate(urls):
            try:
                response = requests.get(url)
                img = Image.open(BytesIO(response.content))

                output_path = os.path.join(output_dir, f"converted_image_{i+1}.webp")

                img.save(output_path, 'WEBP')
                print(f"Conversion successful. WebP image saved at {output_path}")

            except Exception as e:
                print(f"Error converting image from {url}: {e}")

    except Exception as e:
        print(f"Error creating output directory {output_dir}: {e}")