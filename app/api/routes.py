from fastapi import APIRouter, UploadFile, File, HTTPException

from app.ingestion.pcap_parser import analyze_pcap
from app.storage.repository import (
    get_analysis,
    get_alerts
)

router = APIRouter()


@router.post("/analyze-pcap")
async def upload_pcap(file: UploadFile = File(...)):
    if not file.filename.lower().endswith((".pcap", ".pcapng")):
        raise HTTPException(
            status_code=400,
            detail="Only .pcap or .pcapng files are supported."
        )

    result = await analyze_pcap(file)
    return result


@router.get("/analysis/{analysis_id}")
def analysis(analysis_id: int):
    result = get_analysis(analysis_id)
    if result is None:
        raise HTTPException(status_code=404, detail="Analysis not found.")
    return result


@router.get("/alerts")
def alerts():
    return get_alerts()
