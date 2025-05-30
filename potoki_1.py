import requests
import time
import threading

def download(url, results):
    response = requests.get(url, verify=False)
    results.append(f"{url}: {len(response.content)} байт загружено")
URLS=[
    "https://4kolesa.by/",
    "https://av.by/",
    "https://abw.by/",
    "https://avseven.by/contact/",
    "https://otoba.ru/",
    "https://wikimotors.ru/",
    "https://www.kinopoisk.ru/",
    "https://avtovelomoto.by/avto-i-moto/mototekhnika/mototsikly/",
    "https://mb.onliner.by/",
    "https://motoplanet.by/aksessuary"
]
def download(url, results):
    response = requests.get(url, verify=False)
    results.append(f"{url}: {len(response.content)} байт загружено")

def posled():
    start_time = time.time()
    results = []
    for url in URLS:
        download(url, results)
    end_time = time.time()
    print("Последовательное выполнение:")
    for result in results:
        print(result)
    print(f"Затрачено времени: {end_time - start_time:} секунд")
    return end_time - start_time

def potok():
    start_time = time.time()
    threads = []
    results = []

    for url in URLS:
        thread = threading.Thread(target=download, args=(url, results))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.time()
    print("Потоковое выполнение:")
    for result in results:
        print(result)
    print(f"Затрачено времени: {end_time - start_time:} секунд")
    return end_time - start_time