import os
import requests

API_KEY = os.getenv("VIRUSTOTAL_API_KEY")
BASE_URL = "https://www.virustotal.com/api/v3"


def lookup_indicator(indicator: str):
    """
    Looks up a domain or IP against VirusTotal's v3 API.
    Returns a normalized dict with reputation stats, or a graceful
    fallback if the API key is missing or the request fails.
    """
    if not API_KEY:
        return {
            "indicator": indicator,
            "reputation": "unknown",
            "error": "VIRUSTOTAL_API_KEY not set"
        }

    headers = {"x-apikey": API_KEY}
    url = f"{BASE_URL}/domains/{indicator}"

    try:
        response = requests.get(url, headers=headers, timeout=10)

        if response.status_code == 429:
            return {
                "indicator": indicator,
                "reputation": "unknown",
                "error": "rate_limited"
            }

        response.raise_for_status()
        stats = response.json()["data"]["attributes"]["last_analysis_stats"]

        if stats.get("malicious", 0) > 0:
            reputation = "malicious"
        elif stats.get("suspicious", 0) > 0:
            reputation = "suspicious"
        else:
            reputation = "harmless"

        return {
            "indicator": indicator,
            "reputation": reputation,
            "malicious": stats.get("malicious", 0),
            "suspicious": stats.get("suspicious", 0),
            "harmless": stats.get("harmless", 0),
        }

    except requests.RequestException as e:
        return {
            "indicator": indicator,
            "reputation": "unknown",
            "error": str(e)
        }
