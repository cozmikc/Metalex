from .models import Verifiable
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.decorators import api_view, parser_classes, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import VerifiableSerializer
# Create your views here.



@api_view(['GET'])
def getVerifiables(request):
    verifiable = Verifiable.objects.all()
    serializer = VerifiableSerializer(verifiable, many=True)
    return Response(serializer.data)

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
def memberVerification(request,pk):
    user = request.user
    data = request.data
    member = Verifiable.objects.get(chamberMember=pk)
    scanFile = str(data['file']).split(".")   
    if scanFile[1] == "pdf" or scanFile[1] == "doc":
        member.file = data['file']
        member.save()
        serializer = VerifiableSerializer(member, many=False)
        return Response(serializer.data)
    else:
        return Response({"details": "File type not supported!"})

