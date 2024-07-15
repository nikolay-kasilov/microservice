from fastapi import APIRouter
from services import create_post, get_posts

router = APIRouter()

router.add_api_route("/", create_post, methods=["POST"])
router.add_api_route("/", get_posts, methods=["GET"])
