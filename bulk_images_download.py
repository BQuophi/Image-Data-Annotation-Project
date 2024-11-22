import os
from io import BytesIO
from pathlib import Path
from zipfile import ZipFile
import requests
from bs4 import BeautifulSoup
from fastapi.responses import FileResponse, StreamingResponse

google_image = "https://www.google.com/search?q=used+cars&sca_esv=b5b966a5f6140c86&udm=2&sxsrf=ADLYWILVbhZGHS8WUSfS6DjjVLnniMOCNA:1732231400053&source=lnt&tbs=isz:l&sa=X&ved=2ahUKEwjAj5PqyO6JAxUvaUEAHcpVM6kQpwV6BAgDEAc&biw=1366&bih=645&dpr=1"
user_agent = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
}
saved_folder = "images"


# Function to Download Images
def download_images(data: str, n_images: int):
    """Download images from Google based on search query and save them in a local folder."""

    print("Searching for images...")
    search_url = google_image + "q=" + data
    response = requests.get(search_url, headers=user_agent)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")

    # Attempt to find any 'img' tags, regardless of class
    results = soup.findAll("img")

    # Initialize counter and list for image links
    count = 1
    links = []

    # Loop through each 'img' tag found
    for result in results:
        try:
            # Try both 'data-src' and 'src' attributes for image URL
            link = result.get("data-src") or result.get("src")
            if link and link.startswith("http"):  # Filter out empty or invalid URLs
                links.append(link)
                count += 1

            if count > n_images:  # Stop when desired image count is reached
                break
        except KeyError:
            continue

    print(f"Downloading {len(links)} images...")

    # Download each image link
    for i, link in enumerate(links):
        response = requests.get(link)

        # Create the images folder if it doesn't already exist
        if not os.path.exists(saved_folder):
            os.mkdir(saved_folder)

        image_name = f"{saved_folder}/{data}{i+1}.jpg"
        with open(image_name, "wb") as fh:
            fh.write(response.content)

    return Path("images/")


download_images("used cars", 10)
