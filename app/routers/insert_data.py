from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.services.shared.operations import SharedOperationsService
from app.services.shared.http import HTTPService
from app.config.env import ENDPOINT_ENV, COLLECTION_ENV
import json

router = APIRouter(prefix="/insertion", tags=["Insertion"])


@router.post("/trees", summary="insérer les données des Arbres dans Mongo")
async def post_support():
    operations = SharedOperationsService()
    base_url = ENDPOINT_ENV['BASE_URL']
    req = await HTTPService.get(base_url + "/catalog/datasets/bruxelles_arbres_remarquables/records?limit=100&offset=100")
    trees = json.loads(req.text)
    response = await operations.insert_many_in_collection(COLLECTION_ENV['DATA_COLLECTION'], trees['results'])
    return JSONResponse(status_code=201, content={"data": response.acknowledged})