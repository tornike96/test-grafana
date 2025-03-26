from prometheus_client import Gauge, start_http_server
import time
import requests

# Define Prometheus metric
PRODUCT_ID_GAUGE = Gauge('first_product_id', 'ID of the first product from fakestoreapi')

def scrape_endpoint():
    try:
        response = requests.get("https://fakestoreapi.com/products")
        response.raise_for_status()  # Raise an exception for bad status codes
        first_product = response.json()[0]["id"]
        PRODUCT_ID_GAUGE.set(first_product)  # Set the metric value
        print(f"First product ID: {first_product}")
    except Exception as e:
        print(f"Error scraping endpoint: {e}")

if __name__ == "__main__":
    # Start the Prometheus metrics server on port 8000
    start_http_server(8000)
    print("Metrics server started on port 8000")
    while True:
        scrape_endpoint()
        time.sleep(10)