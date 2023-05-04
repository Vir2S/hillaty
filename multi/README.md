# Threading and Multiprocessing

```
import time
import requests

# CPU-bound task (heavy computation)
def encrypt_file(path: str):
    print(f"Processing image from {image_url} in process {os.getpid()}")
    # Simulate heavy computation by sleeping for a while
    _ = [i for i in range(100_000_000)]

# I/O-bound task (downloading image from URL)
def download_image(image_url):
    print(f"Downloading image from {image_url} in thread {threading.current_thread().name}")
    response = requests.get(image_url)
    with open("image.jpg", "wb") as f:
        f.write(response.content)

try:
    encrypt_file("rockyou.txt")
    download_image("https://picsum.photos/1000/1000")
    # print(f"Time taken for encryption task: {encryption_counter}, I/O-bound task: {download_counter}, Total: {total} seconds")
except Exception as e:
    print(f"Error occurred: {e}")
```

AC:

This code works pretty slowly. Change it using multithreading and multiprocessing as we did in the lesson

Add time counters and uncomment the print command in the try/except block. P.S. Use time.perf_counter.

The encryption could simulate the heavy task. No need to achieve the actual encryption

The image downloader should download the image for real.