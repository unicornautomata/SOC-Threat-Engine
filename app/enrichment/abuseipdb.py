import os
import requests

API_KEY = os.getenv("ABUSEIPDB_API_KEY")
BASE_URL = "https://api.abuseipdb.com/api/v2"


def lookup_ip(ip: str):
    """
    Looks up an IP address against AbuseIPDB's reputation database.
    Returns a normalized dict with abuse score, or a graceful fallback
    if the API key is missing or the request fails.
    """
    if not API_KEY:
        return {
            "ip": ip,
            "abuse_score": 0,
            "error": "ABUSEIPDB_API_KEY not set"
        }

    headers = {
        "Key": API_KEY,
        "Accept": "application/json"
    }
    params = {"ipAddress": ip, "maxAgeInDays": 90}

    try:
        response = requests.get(
            f"{BASE_URL}/check",
            headers=headers,
            params=params,
            timeout=10
        )
        response.raise_for_status()
        data = response.json()["data"]

        return {
            "ip": ip,
            "abuse_score": data.get("abuseConfidenceScore", 0),
            "total_reports": data.get("totalReports", 0),
            "country_code": data.get("countryCode"),
        }

    except requests.RequestException as e:
        return {
            "ip": ip,
            "abuse_score": 0,
            "error": str(e)
        }
