from django.db import models


class Worker(models.Model):
	name = models.CharField(max_length=255, verbose_name='имя')
	phone = models.CharField(max_length=255, verbose_name="номер телефона")

	def __str__(self):
		return f"{self.name} | {self.phone}"

	class Meta:
		verbose_name = "Работник"
		verbose_name_plural = "Работник"


class TradeMark(models.Model):
	name = models.CharField(max_length=255, verbose_name='название')
	worker = models.ForeignKey('api.Worker', verbose_name="Работник",
												 on_delete=models.PROTECT)

	def __str__(self):
		return f"{self.name} | {self.worker}"

	class Meta:
		verbose_name = "Торговая точка"
		verbose_name_plural = "Торговая точка"


class Visit(models.Model):
	visit_date = models.DateTimeField(auto_now_add=True, verbose_name="дата/время")
	latitude = models.FloatField(verbose_name='широта', blank=True, null=True)
	longitude = models.FloatField(verbose_name='долгота', blank=True, null=True)
	trade_mark = models.ForeignKey('api.TradeMark', verbose_name="Торговая точка",
												on_delete=models.PROTECT)

	def __str__(self):
		return f"{self.visit_date} | {self.trade_mark}"

	class Meta:
		verbose_name = "Посещение"
		verbose_name_plural = "Посещение"