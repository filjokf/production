from rest_framework import serializers
from webapp.models import production

class productionSerializers(serializers.HyperlinkedModelSerializer):
	class Meta:
		model=production
		fields="__all__"
