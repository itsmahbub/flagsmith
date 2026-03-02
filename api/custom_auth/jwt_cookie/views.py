from djoser.views import TokenDestroyView  # type: ignore[import-untyped]
from drf_spectacular.utils import extend_schema
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import SlidingToken

from custom_auth.jwt_cookie.constants import JWT_SLIDING_COOKIE_KEY

import logging

logger = logging.getLogger(__name__)

class JWTSlidingTokenLogoutView(TokenDestroyView):  # type: ignore[misc]
    @extend_schema(request=None, responses={204: None})
    def post(self, request: Request) -> Response:
        logger.warning("LOGOUT called")
        logger.warning("request.auth = %s", request.auth)
        logger.warning("request.auth type = %s", type(request.auth))

        response = super().post(request)
        if isinstance(jwt_token := request.auth, SlidingToken):
            logger.warning("SlidingToken detected → blacklisting")
            jwt_token.blacklist()
            response.delete_cookie(JWT_SLIDING_COOKIE_KEY)
        else:
            logger.warning("NOT SlidingToken → blacklist skipped")
        return response  # type: ignore[no-any-return]
