from fastapi import APIRouter, HTTPException
from backend.models.schemas import ConvertRequest, ConvertResponse
from backend.services.tone_converter import converter

router = APIRouter()

@router.post("/convert", response_model=ConvertResponse)
async def convert_tone(request: ConvertRequest):
    try:
        converted_text = await converter.convert(request.text, request.target_audience)
        return ConvertResponse(
            converted_text=converted_text,
            target_audience=request.target_audience,
            original_text=request.text
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
