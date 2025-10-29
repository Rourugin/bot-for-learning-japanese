from aiogram import Router

from app.handlers.main_h.py import main_r
from app.handlers.verbs_h.py import verbs_r
from app.handlers.constructions_h.py import constructions_r

def setup_routers() -> Router:
    router = Router()
    router.include_routers(main_r)
    router.include_routers(verbs_r)
    router.include_routers(constructions_r)
    return router
