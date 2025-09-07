import requests
import socket
import time

def test_network_connection():
    """Test network connectivity to Watson API"""
    
    host = 'sn-watson-emotion.labs.skills.network'
    port = 443
    
    print("Testing network connectivity...")
    print("=" * 50)
    
    # Test 1: Basic DNS resolution
    try:
        ip = socket.gethostbyname(host)
        print(f"✓ DNS Resolution successful: {host} -> {ip}")
    except socket.gaierror as e:
        print(f"✗ DNS Resolution failed: {e}")
        return False
    
    # Test 2: Port connectivity
    try:
        sock = socket.create_connection((host, port), timeout=10)
        sock.close()
        print(f"✓ Port {port} is accessible")
    except socket.error as e:
        print(f"✗ Port {port} connection failed: {e}")
        print("This might be a firewall or proxy issue")
        return False
    
    # Test 3: HTTP request with different timeout settings
    url = f'https://{host}/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    test_data = {"raw_document": {"text": "I am happy"}}
    
    timeout_values = [30, 60, 120]  # Try different timeout values
    
    for timeout in timeout_values:
        try:
            print(f"Testing API request with {timeout}s timeout...")
            response = requests.post(url, json=test_data, headers=headers, timeout=timeout)
            
            if response.status_code == 200:
                print(f"✓ API request successful with {timeout}s timeout")
                print(f"Response: {response.text[:100]}...")
                return True
            else:
                print(f"✗ API returned status code: {response.status_code}")
                
        except requests.exceptions.Timeout:
            print(f"✗ Request timed out after {timeout}s")
        except requests.exceptions.RequestException as e:
            print(f"✗ Request failed: {e}")
    
    return False

def test_alternative_endpoints():
    """Test alternative Watson endpoints"""
    
    alternative_urls = [
        'https://api.us-south.natural-language-understanding.watson.cloud.ibm.com',
        'https://gateway.watsonplatform.net/natural-language-understanding/api',
        'https://sn-watson-emotion.labs.skills.network'
    ]
    
    print("\nTesting alternative endpoints...")
    print("=" * 50)
    
    for url in alternative_urls:
        try:
            response = requests.get(f"{url}/", timeout=10)
            print(f"✓ {url} is accessible (status: {response.status_code})")
        except Exception as e:
            print(f"✗ {url} failed: {e}")

if __name__ == "__main__":
    if not test_network_connection():
        print("\nNetwork issues detected. Trying alternatives...")
        test_alternative_endpoints()
    
    print("\nRecommendations:")
    print("1. Check your internet connection")
    print("2. Try using VPN if you're behind a corporate firewall")
    print("3. Use the local emotion detector as fallback")
    print("4. Contact your network administrator if the issue persists")