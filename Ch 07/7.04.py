import requests
import time
from concurrent.futures import ThreadPoolExecutor


def get_status_code(url: str) -> int:
    responce = requests.get(url)
    return responce.status_code


start = time.time()

with ThreadPoolExecutor() as pool:
    urls = ['https://www.example.com' for _ in range(1000)]
    results = pool.map(get_status_code, urls)
    for result in results:
        print(result, end="  ")

end = time.time()

print(f"Выполнение запросов завершено за {end - start:.4f} c")
