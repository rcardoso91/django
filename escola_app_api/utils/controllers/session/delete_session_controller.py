from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework import status



def deleteSessionController(_: Request) -> Response:
    
    response = Response()

    response.delete_cookie("token")
    response.status_code = HTTP_204_NO_CONTENT
    return Response({"message": "Sessão deletada"}, status=status.HTTP_204_NO_CONTENT)
