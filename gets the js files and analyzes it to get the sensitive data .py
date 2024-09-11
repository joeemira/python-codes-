import requests
from bs4 import BeautifulSoup
import os
import re
from urllib.parse import urljoin, urlparse

# Configuration
base_url = 'https://github.com/illsk1lls/ZipRipper'  # Replace with your target URL
output_dir = 'js_files'
results_file = 'sensitive_data_found.txt'
sensitive_patterns = [
    r'api[_\-\s]*key[\s\:=]*([\w\-]+)',  # Capture API key
    r'password[\s\:=]*([\w\-]+)',         # Capture password
    r'authorization[\s\:=]*([\w\-]+)',    # Capture Authorization headers
    r'secret[\s\:=]*([\w\-]+)',           # Capture secret
    r'csrf[_\-\s]*token[\s\:=]*([\w\-]+)',  # Capture CSRF tokens
    r'href[\s\:=]*[\'"]?([^\'"\s]+)[\'"]?',  # Capture href values
    r'api[_\-\s]*token[\s\:=]*([\w\-]+)',  # Capture API tokens
]

def get_js_files(url):
    print(f"Fetching JavaScript files from {url}...")
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    js_files = []
    print("HTML content:")
    print(soup.prettify())
    for script in soup.find_all('script'):
        src = script.get('src')
        if src:
            js_file_url = urljoin(url, src)
            js_files.append(js_file_url)
            print(f"Found JavaScript file: {js_file_url}")
    if not js_files:
        print("No JavaScript files found in the HTML.")
    return js_files

def download_file(url, directory):
    local_filename = os.path.join(directory, os.path.basename(urlparse(url).path))
    print(f"Downloading {url} to {local_filename}...")
    with requests.get(url) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            f.write(r.content)
    return local_filename

def search_sensitive_data(file_path, patterns, results_file):
    print(f"Scanning {file_path} for sensitive data...")
    with open(file_path, 'r', errors='ignore') as file:
        content = file.read()
        found = False
        with open(results_file, 'a') as result_file:
            for pattern in patterns:
                matches = re.findall(pattern, content, re.IGNORECASE)
                if matches:
                    found = True
                    for match in matches:
                        result_file.write(f"Sensitive data found in {file_path}: {match}\n")
            if found:
                result_file.write("\n")  # Add a newline for better readability between files

def main():
    os.makedirs(output_dir, exist_ok=True)
    if os.path.exists(results_file):
        os.remove(results_file)  # Remove the file if it already exists
    js_files = get_js_files(base_url)
    if not js_files:
        print("No JavaScript files to process.")
    for js_file in js_files:
        local_file = download_file(js_file, output_dir)
        search_sensitive_data(local_file, sensitive_patterns, results_file)
    print(f"Finished scanning all files. Results are stored in {results_file}.")

if __name__ == "__main__":
    main()
