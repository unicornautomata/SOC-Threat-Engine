# SOC Threat Engine

**Automated PCAP-based Threat Detection & SOC Analysis Platform**

SOC Threat Engine is a lightweight cybersecurity analysis platform that ingests packet captures (PCAP files), extracts network indicators (DNS, HTTP, TLS), enriches them with threat intelligence, and generates structured security alerts with risk scoring and MITRE ATT&CK mapping.

It is designed as a **commercializable SOC MVP** for small security teams, researchers, and blue-team automation workflows.

---

## 🚀 Key Features (MVP Scope)

- PCAP file ingestion and parsing
- DNS / HTTP / TLS extraction
- Host and domain normalization
- Threat intelligence enrichment (VirusTotal integration)
- Rule-based detection engine
- Basic risk scoring per host
- SQLite-based event storage
- FastAPI analysis endpoints
- CSV / JSON report export
- Alert generation system

---

## 🧠 System Overview

SOC Threat Engine processes network traffic through a modular pipeline:

```
PCAP Input
   ↓
Ingestion Layer (PCAP Parser)
   ↓
Normalization (Unified Event Format)
   ↓
Extraction (DNS / HTTP / TLS)
   ↓
Enrichment (VirusTotal, reputation data)
   ↓
Detection Engine (rules + heuristics)
   ↓
Risk Scoring + MITRE Mapping
   ↓
Storage (SQLite)
   ↓
API + Reporting Layer
```

---

## 📁 Project Structure

```
soc-threat-engine/
│
├── app/
│   ├── api/
│   ├── ingestion/
│   ├── pipeline/
│   ├── enrichment/
│   ├── detection/
│   ├── storage/
│   ├── reporting/
│   └── models/
│
├── dashboard/
├── tests/
├── data/
├── reports/
│
├── requirements.txt
├── .env.example
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-org/soc-threat-engine.git
cd soc-threat-engine
```

### 2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file:

```env
VIRUSTOTAL_API_KEY=your_api_key_here
DATABASE_URL=sqlite:///./soc.db
LOG_LEVEL=INFO
```

---

## ▶️ Running the API

```bash
uvicorn app.main:app --reload
```

---

## 📡 API Endpoints

### POST /analyze-pcap
Upload a PCAP file for analysis.

### GET /analysis/{id}
Retrieve analysis results.

### GET /alerts
Retrieve generated alerts.

---

## 📊 Output Example

```json
{
  "host": "192.168.1.10",
  "risk_score": 78,
  "alerts": [
    "Suspicious DNS query detected",
    "Known malicious domain contact"
  ],
  "mitre_techniques": [
    "T1071"
  ]
}
```

---

## 🛣️ Roadmap

### MVP Phase 1
- PCAP ingestion
- DNS/HTTP/TLS extraction
- VirusTotal enrichment
- SQLite storage
- FastAPI endpoints

### MVP Phase 2
- Streamlit dashboard
- Risk scoring engine
- MITRE mapping
- Alerts system

### MVP Phase 3
- Live capture
- Slack/Discord alerts
- GeoIP enrichment

### Commercial Phase
- Auth system
- RBAC
- Multi-tenancy
- Docker deployment

---

## 🔒 Security

- API keys stored in environment variables
- No raw PCAP exposure
- Minimal external dependencies

---

## 📄 License

Commercial license (proprietary MVP)
