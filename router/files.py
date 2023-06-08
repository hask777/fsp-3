from fastapi import APIRouter, File

router = APIRouter(
    prefix='/file',
    tags=['file'],
)

@router.post('/file')
def get_file(files: bytes = File(...)):
    content = files.decode('utf-8')
    lines = content.split('\n')
    return {'lines': lines}
