from fastapi import FastAPI, UploadFile, File, HTTPException, status
import os
import aiofiles

app = FastAPI()

if not os.path.exists("validated_files"):
    os.makedirs("validated_files")

MAX_FILE_SIZE_MB = 5
MAX_FILE_SIZE_BYTES = MAX_FILE_SIZE_MB * 1024 * 1024

@app.post("/upload_validate_size/")
async def upload_file_validate_size(file: UploadFile = File(...)):
    file_location = os.path.join("validated_files", file.filename)
    file_size = getattr(file, "size", None)
    if file_size is not None and file_size > MAX_FILE_SIZE_BYTES:
        raise HTTPException(
            status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
            detail=f"File too large. Max size is {MAX_FILE_SIZE_MB}MB."
        )

    current_size = 0
    chunk_size = 1024 * 1024

    try:
        async with aiofiles.open(file_location, "wb") as out_file:
            while True:
                content = await file.read(chunk_size)
                if not content:
                    break

                current_size += len(content)

                if current_size > MAX_FILE_SIZE_BYTES:
                    raise HTTPException(
                        status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
                        detail=f"File too large. Max size is {MAX_FILE_SIZE_MB}MB."
                    )

                await out_file.write(content)
        
        return {
            "filename": file.filename,
            "content_type": file.content_type,
            "size_bytes": current_size,
            "message": "File uploaded and size validated successfully."
        }

    except HTTPException:
        if os.path.exists(file_location):
            os.remove(file_location)
        raise

    except Exception as e:
        if os.path.exists(file_location):
            os.remove(file_location)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An unexpected error occurred during file upload: {e}"
        )