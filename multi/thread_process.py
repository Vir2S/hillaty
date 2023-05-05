import os
import threading
import multiprocessing
import time
import requests


# CPU-bound task (heavy computation)
def encrypt_file(path: str):
    print(f"Processing file from {path} in process {os.getpid()}")
    # Simulate heavy computation by sleeping for a while
    _ = [i for i in range(100_000_000)]


# I/O-bound task (downloading image from URL)
def download_image(image_url):
    print(
        f"Downloading image from {image_url} in thread {threading.current_thread().name}"
    )
    response = requests.get(image_url)
    with open("image.jpg", "wb") as f:
        f.write(response.content)


if __name__ == "__main__":
    start = time.perf_counter()

    encryption_process_1 = multiprocessing.Process(
        target=encrypt_file, args=("rockyou.txt",)
    )
    encryption_process_2 = multiprocessing.Process(
        target=encrypt_file, args=("rockyou.txt",)
    )

    encryption_process_1.start()
    encryption_process_2.start()

    encryption_process_1.join()
    encryption_process_2.join()

    encryption_counter = time.perf_counter() - start

    start = time.perf_counter()

    download_thread = threading.Thread(
        target=download_image, args=("https://picsum.photos/1000/1000",)
    )
    download_thread.start()

    download_thread.join()

    download_counter = time.perf_counter() - start

    total_time = encryption_counter + download_counter
    print(
        f"Time taken for encryption task: {encryption_counter} seconds\nI/O-bound task: {download_counter} seconds\nTotal time taken: {total_time} seconds"
    )
