#!/usr/bin/python3

import sys, os

import django
sys.path.append(os.path.abspath('/home/hackathon/sensors_django/'))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sensors_django.settings")
django.setup()
from sensors_data import models

def main():
    # print('SensorType:', models.SensorType.objects.all())
    # print('Unit:', models.Unit.objects.all())
    # print('Measure:', models.Measure.objects.all())
    # print('DataType:', models.DataType.objects.all())
    # print('Data:', models.Data.objects.all())
    # models.SensorType.objects.all().delete()
    # models.Unit.objects.all().delete()
    # models.Measure.objects.all().delete()
    # models.DataType.objects.all().delete()
    # models.Data.objects.all().delete()
    # print('SensorType:', models.SensorType.objects.all())
    # print('Unit:', models.Unit.objects.all())
    # print('Measure:', models.Measure.objects.all())
    # print('DataType:', models.DataType.objects.all())
    # print('Data:', models.Data.objects.all())

    list_typedata = []
    list_paramValue = [tuple(s.split('=')) for s in sys.argv[1:]]
    for param, value in list_paramValue:
        if param == 'unit':
            unit_name = value
        elif param == 'unixtime':
            unixtime = int(value)
        else:
            list_typedata.append((param, float(value),))
    unit, flag_new = models.Unit.objects.get_or_create(name=unit_name)
    measure = models.Measure.objects.create(unit=unit, unixtime=unixtime)
    for datatype_name, data_value in list_typedata:
        datatype, flag_new = models.DataType.objects.get_or_create(name=datatype_name)
        data = models.Data.objects.create(datatype=datatype, measure=measure, value=data_value)
    # print(measure.data_set.all())

    # models.SensorType.objects.all().delete()
    # models.Unit.objects.all().delete()
    # models.Measure.objects.all().delete()
    # models.DataType.objects.all().delete()
    # models.Data.objects.all().delete()


if __name__ == '__main__':
    main()
