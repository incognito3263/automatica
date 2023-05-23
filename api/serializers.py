from rest_framework import serializers
from api.models import Worker, TradeMark, Visit


class WorkerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Worker
		fields = '__all__'


class TradeMarkSerializer(serializers.ModelSerializer):
	# worker_obj = WorkerSerializer(many=False, read_only=True, source='worker')

	class Meta:
		model = TradeMark
		fields = 'id', 'name'


class VisitSerializer(serializers.ModelSerializer):
	class Meta:
		model = Visit
		fields = 'id', 'visit_date',