from api.serializers import WorkerSerializer, TradeMarkSerializer, VisitSerializer
from api.models import Worker, TradeMark, Visit
from rest_framework import viewsets
from rest_framework.response import Response


class MainViewset(viewsets.ModelViewSet):
	queryset = TradeMark.objects.all().select_related('worker')
	serializer_class = TradeMarkSerializer

	def list(self, request):
		print(self.queryset)
		phone = self.request.GET.get('phone', None)
		if phone is None:
			context = {
				'results': {
					'error': 'phone is required to access'
				}
			}
			return Response(context)
		queryset = self.queryset.filter(worker__phone=phone)
		serializer = self.serializer_class(queryset, many=True)
		context = {
			'results': {
				'data': serializer.data
			}
		}
		return Response(context)

	def create(self, request):
		latitude = self.request.data.get('latitude')
		longitude = self.request.data.get('longitude')
		trade_mark_id = self.request.data.get('trade_mark_id')
		phone = self.request.data.get('phone', None)
		print(phone)
		print(trade_mark_id, latitude, longitude)
		if phone is None:
			context = {
				'results': {
					'error': 'phone is required to access'
				}
			}
			return Response(context)
		if longitude is None or latitude is None or trade_mark_id is None:
			context = {
				'results': {
					'errors': "latitude/longitude/trade_mark_id are required"
				}
			}
			return Response(context)
		check_worker = self.queryset.filter(id=trade_mark_id, worker__phone=phone)
		if not check_worker:
			context = {
				'results': {
					'error': 'there is no trade mark found with the given phone number'
				}
			}
			return Response(context)
		visit = Visit.objects.create(
					trade_mark_id=trade_mark_id,
					latitude=latitude,
					longitude=longitude
				)
		visit_obj = Visit.objects.filter(id=visit.id)
		serializer = VisitSerializer(visit_obj, many=True)
		context = {
			'results': {
				'data': serializer.data
			}
		}
		return Response(context)