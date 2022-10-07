from decoracao.persistencia.db import connect_db

def valida_email(req):
    result = connect_db().cliente.find_one({
        "email": req['email']
    })

    return result



