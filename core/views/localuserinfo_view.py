from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.utils.encoding import force_text

from core.models import User
#from backend_utils.logs import log_params

import logging
log = logging.getLogger(__name__)


class UserInfoSerializer(ModelSerializer):

    class Meta:
        model = User
        exclude = ('password', )


class LocalUserInfoView(APIView):
    """
    View to list all users in the system.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        user = self.request.user
        serializer = UserInfoSerializer(user)
        if not self.request.user:
            return Response(
                {'detail': 'AUTHENTICATION IS REQUIRED'},
                status=status.HTTP_511_NETWORK_AUTHENTICATION_REQUIRED
            )
        if self.request.user.is_authenticated:
            # log.info(force_text('User is authenticated'),
            #         extra=log_params(self.request))
            log.info(('User is authenticated'), extra={
                'path': self.request.get_full_path(),
                'ip': self.request.META['REMOTE_ADDR'],
                'user': self.request.user,
                'method': self.request.method
            })
            return Response(serializer.data)
        else:
            # log.warning(force_text('User is anonymous'),
            #            extra=log_params(self.request))
            log.warning(('User is anonymous'), extra={
                'path': self.request.get_full_path(),
                'ip': self.request.META['REMOTE_ADDR'],
                'user': self.request.user,
                'method': self.request.method
            })
        return Response({'detail': 'AUTHENTICATION IS REQUIRED'},
                        status=status.HTTP_511_NETWORK_AUTHENTICATION_REQUIRED)
