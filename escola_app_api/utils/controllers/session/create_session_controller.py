import jwt
import os
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.status import HTTP_201_CREATED
from ...assertions.assert_credentials_are_valid_and_get_user_id import (
    assertCredentialsAreValidAndGetUserId,
)
def createSessionController(request):
    print(f"Dados recebidos para criar sessão: {request.data}")
    email = request.data.get("email")
    password = request.data.get("senha")
    try:
        userId = assertCredentialsAreValidAndGetUserId(email, password)
    except Exception as e:
        return Response({"message": str(e)}, status=status.HTTP_401_UNAUTHORIZED)

    tokenPayload = {"sub": userId}
    token = jwt.encode(tokenPayload, os.environ.get("JWT_SECRET"), algorithm="HS256")

    response = Response({"message": "Sessão criada"})
    response.set_cookie(key="token", value=token, httponly=True)
    return response
