from fastapi import APIRouter

router = APIRouter(prefix="/explorer")


@router.get("/")
def start_explorer():
    return "start explorer"
