from decoracao.persistencia.cliente_persistencia import check_user, add_user
from fastapi import Response, status
from fastapi.responses import JSONResponse

def create_new_user(req, response: Response):
    if check_user(req) is not None:
        response.status_code = status.HTTP_409_CONFLICT
    else:
        add_user(req)




