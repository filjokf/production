
from django.http import HttpResponse , JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect  
from webapp.forms import productionForm 
from webapp.models import production 
from tablib import Dataset
from .resources import productionResource
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from webapp.serializers import productionSerializers
from rest_framework import viewsets
from .serializers import productionSerializers
from .models import production

def importexl(request):
	if request.method=='POST':
		production_resource=productionResource
		datasets=Dataset()
		new_file=request.FILES['myfile']
		imported_data=datasets.load(new_file.read(), format='xlsx')
		for data in imported_data:
			value=production(
				data[0],
				data[1],
				data[2],
				data[3],
				data[4]
				)
			value.save()

	return render(request, 'index.html')
 

class productionViewSet(viewsets.ModelViewSet):
	queryset=production.objects.all()
	serializer_class=productionSerializers

		#return Response(serializer.data)

