from django.contrib import admin
from api.models import Worker, TradeMark, Visit


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
	search_fields = ('name',)
	list_display = 'name', 'phone'


@admin.register(TradeMark)
class TradeMarkAdmin(admin.ModelAdmin):
	search_fields = ('name',)
	list_display = 'name', 'worker'


@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
	search_fields = ('trade_mark__worker__name', 'trade_mark__name')
	list_display = 'visit_date', 'latitude', 'longitude', 'trade_mark'