#!/usr/bin/python3

import sys, os, numpy as np

import django
sys.path.append(os.path.abspath('/home/hackathon/sensors_django/'))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sensors_django.settings")
django.setup()
from sensors_data import models

def main():
    unit_preexisting = models.Unit.objects.filter(name='temp1')[0]
    unit, flag_new = models.Unit.objects.get_or_create(name='y4k_temp1_noised')
    list_data = [data for measure in unit_preexisting.measure_set.all() for data in measure.data_set.all()]
    std_data = np.array([data.value for data in list_data]).std()
    for data in list_data:
        unixtime = data.measure.unixtime + np.random.randint(low=-1, high=2)
        value = np.absolute(data.value + np.random.random() * 7. * std_data)

        datatype, flag_newdatatype = models.DataType.objects.get_or_create(name=data.datatype.name)
        measure, flag_newmeasure = models.Measure.objects.get_or_create(unit=unit, unixtime=unixtime)

        data = models.Data.objects.create(datatype=datatype, measure=measure, value=value)


if __name__ == '__main__':
    main()
