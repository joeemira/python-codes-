import requests

def check_clickjacking(url):
    try:
        # Send a request to the URL
        response = requests.get(url)
        
        # Check for X-Frame-Options header
        x_frame_options = response.headers.get('X-Frame-Options', None)
        if x_frame_options:
            print(f"X-Frame-Options: {x_frame_options}")
        else:
            print("X-Frame-Options header is missing.")
        
        # Check for Content-Security-Policy header
        csp = response.headers.get('Content-Security-Policy', None)
        if csp:
            frame_ancestors = [directive for directive in csp.split(';') if 'frame-ancestors' in directive]
            if frame_ancestors:
                print(f"Content-Security-Policy: {csp}")
            else:
                print("Content-Security-Policy does not include 'frame-ancestors'.")
        else:
            print("Content-Security-Policy header is missing.")
    
    except requests.RequestException as e:
        print(f"Error checking {url}: {e}")

if __name__ == "__main__":
    target_url = input("Enter the URL to check for clickjacking: ")
    check_clickjacking(target_url)
