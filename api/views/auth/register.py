import uuid

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.request import Request
from rest_framework.views import APIView

from api.models import InvitationToken
from note.responses import NotAuthenticatedResponse, OKResponse, BadRequestResponse


class __RequestToken(APIView):
    @staticmethod
    def get(request: Request):
        if (r_user := request.user).is_authenticated:
            try:
                inv_token = InvitationToken.objects.get(user=r_user)
            except:
                t = uuid.uuid4().__str__().lower()
                inv_token = InvitationToken.objects.create(token=t, user=r_user)
            return OKResponse(data={"token": inv_token.token})
        else:
            return NotAuthenticatedResponse()


class __RegisterAPIView(APIView):
    @staticmethod
    def post(request: Request):
        try:
            inv_token: str = request.data.get('inv_code')
            errors = []
            if not inv_token:
                errors.append("invitation token not valid")

            username: str = request.data.get('username')
            if not username:
                errors.append("username not valid")

            password: str = request.data.get('password')
            if not password:
                errors.append("password not valid")
            conf_password: str = request.data.get('password_confirmation')
            if not conf_password:
                errors.append("confirmation password not valid")
            else:
                if conf_password != password:
                    errors.append("two passwords don't match")
            email: str = request.data.get('email')
            if not email:
                errors.append("email not valid")
            if errors:
                return BadRequestResponse(errors)

            t = InvitationToken.objects.get(token=inv_token)
            if t:
                user = User.objects.create(username=username, password=password, email=email)
                if user:
                    tok, _ = Token.objects.get_or_create(user=user)
                    InvitationToken.delete(t)
                    return OKResponse({"message": f"user {username} created successfully",
                                       "token": tok.key})
                else:
                    return BadRequestResponse(['user not created'])
            else:
                return BadRequestResponse(['token not found'])
        except Exception as eee:
            return BadRequestResponse(["invalid or missing token", eee.__str__()])


request_token = __RequestToken.as_view()
register_user = __RegisterAPIView.as_view()
