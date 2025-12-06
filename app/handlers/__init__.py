from aiogram import Router

from app.handlers.main_h import main_r
from app.handlers.verbs_h import verbs_r
from app.handlers.constructions_h import constructions_r

def setup_routers() -> Router:
    router = Router()
    router.include_routers(main_r)
    router.include_routers(constructions_r)
    router.include_routers(verbs_r)
    return router
