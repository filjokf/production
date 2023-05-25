from import_export import resources
from .models import production

class productionResource(resources.ModelResource):
	class Meta:
		model=production