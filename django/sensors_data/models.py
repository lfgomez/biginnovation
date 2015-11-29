from datetime import datetime as dt
from django.db import models

class SensorType(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False, unique=True)
    def __str__(self):
        return self.name

class Unit(models.Model):
    sensortype = models.ForeignKey(SensorType, blank=True, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=200, unique=True)
    def __str__(self):
        str_ret = ''
        if self.sensortype != None:
            str_ret += self.sensortype.name
        str_ret += '.' + self.name
        return str_ret

class Measure(models.Model):
    unit = models.ForeignKey(Unit, blank=False, null=False)
    unixtime = models.BigIntegerField(blank=False, null=False)
    def __str__(self):
        str_ret = ''
        if self.unit.sensortype != None:
            str_ret += self.sensortype.name
        else:
            str_ret += 'NULL'
        str_ret += '/' + self.unit.name
        str_ret += '/' + dt.fromtimestamp(self.unixtime).strftime('%Y-%m-%d_%H-%M-%S')
        str_ret += ':{'
        for data in self.data_set.all():
            str_ret += '\'' + data.datatype.name + '\': ' + str(data.value) + ', '
        str_ret += '}'
        return str_ret

class DataType(models.Model):
    # unit = models.ForeignKey(Unit, blank=False, null=False)
    # name = models.CharField(max_length=200, blank=False, null=False)#, unique=True)
    name = models.CharField(max_length=200, blank=False, null=False, unique=True)
    def __str__(self):
        return self.name

class Data(models.Model):
    datatype = models.ForeignKey(DataType, blank=False, null=False)
    measure = models.ForeignKey(Measure, blank=False, null=False)
    value = models.FloatField(blank=False, null=False)
    def __str__(self):
        return self.measure.__str__() + '.' + self.datatype.name + ':(' + str(self.value) + ')'
