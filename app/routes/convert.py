from fastapi import APIRouter, UploadFile, File
from fastapi.responses import FileResponse
from app.services.converter import PDFConverter
from app.config import UPLOAD_DIR
from app.utils.file_cleanup import delete_expired_files

router = APIRouter()


@router.post("/convert")
async def convert(file: UploadFile = File(...)):

    # Clean up old files
    delete_expired_files(UPLOAD_DIR, max_age_minutes=10)

    if not file.filename.endswith(".pdf"):
        return {"error": "Only PDF files are allowed."}

    pdf_path = UPLOAD_DIR / file.filename
    with open(pdf_path, "wb") as f:
        f.write(await file.read())

    docx_path = pdf_path.with_suffix(".docx")
    converter = PDFConverter(pdf_path)
    converter.convert_to_docx(docx_path)

    return FileResponse(path=docx_path, filename=docx_path.name)
