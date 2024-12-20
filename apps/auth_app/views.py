from rest_framework.decorators import api_view
from rest_framework.response import Response
from firebase_admin import auth as firebase_auth
from rest_framework import status

# Vista para validar el token de Firebase
@api_view(['POST'])
def validate_token(request):
    """
    Valida un token de Firebase enviado desde el cliente.
    """
    token = request.data.get('token')
    if not token:
        return Response({'error': 'Token no proporcionado'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        # Decodifica y verifica el token usando Firebase Admin
        decoded_token = firebase_auth.verify_id_token(token)
        return Response({
            'message': 'Token válido',
            'user_id': decoded_token['uid'],
            'email': decoded_token['email'],
            'additional_info': decoded_token.get('name', 'No especificado')
        })
    except Exception as e:
        return Response({'error': 'Token inválido o expirado', 'details': str(e)}, status=status.HTTP_401_UNAUTHORIZED)
