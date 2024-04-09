# Envoy HTTP/2 CPU Exhaustion Vulnerability PoC

This is a proof-of-concept (PoC) Python script designed to exploit the CPU exhaustion vulnerability in Envoy's HTTP/2 protocol stack. This vulnerability affects Envoy versions prior to 1.29.3, 1.28.2, 1.27.4, and 1.26.8, allowing an attacker to cause an HTTP/2 endpoint to read arbitrary amounts of header data by sending an excessive number of CONTINUATION frames.
Installation

## To use this PoC, you'll need the following Python modules:
- requests: This module is used to send HTTP/2 requests. Install it using pip:
```bash
pip install requests
```

##  Usage

- Clone this repository:

```bash
git clone [https://github.com/blackmagic/enjoy_http2_cpu_exhaustion_poc.git](https://github.com/blackmagic2023/http-2-DOS-PoC.git)
```
- Navigate to the cloned directory:

```bash

cd http-2-DOS-PoC
```
- Run the Python script:

```bash
python tp2con.py
```
-  Follow the prompts to enter the URL of the HTTP/2 endpoint and the number of excessive headers to send.

## Functionality

This PoC script prompts the user to input the URL of the HTTP/2 endpoint and the number of excessive headers to send. It then crafts an HTTP/2 request with the specified number of headers, each exceeding the MaxHeaderBytes limit. Finally, it sends the request and displays the response status code, indicating whether the attack was successful.
Author

This PoC script was created by blackmagic.

## Disclaimer

This PoC script is for educational and testing purposes only. It should be used responsibly and only against systems you have permission to test. Using it against systems without proper authorization may violate laws and regulations.
About the Vulnerability

The vulnerability in Envoy's HTTP/2 protocol stack allows an attacker to cause CPU exhaustion by sending an excessive number of CONTINUATION frames. This leads to the HTTP/2 endpoint reading arbitrary amounts of header data, potentially resulting in denial-of-service (DoS) conditions. The fix for this vulnerability sets a limit on the amount of excess header frames processed before closing a connection.

## Referrences
- https://thehackernews.com/2024/04/new-http2-vulnerability-exposes-web.html
- https://nvd.nist.gov/vuln/detail/CVE-2023-45288
