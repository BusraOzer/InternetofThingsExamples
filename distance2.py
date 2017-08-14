from hcsr04sensor import sensor
import time
'''Eger github'da verilen ornek kodu kullanacak iseniz 
trigger pin ve echo pin'i duzenlemeniz gerekebilir'''
trig_pin = 18
echo_pin = 24

# Default degerler
# unit = 'metric'
# temperature = 20
# round_to = 1
# Default degerler uzerine override yapiliyor
value = sensor.Measurement(trig_pin, echo_pin,
			   temperature=25,
			   unit='imperial',
                           round_to=2
                           )
while 1:
    raw_measurement = value.raw_distance(sample_size=10)

    # Uzaklik inch turunden hesaplaniyor.
    #imperial measurement dedikleri Ingiltere'nin kullandigi olcu birimleridir.
    #metric measurement ise uluslararasi kabul gormus olcu sistemidir
    imperial_distance = value.distance_imperial(raw_measurement)
    metric_distance = value.distance_metric(raw_measurement)
    print("Olculen uzaklik ={} cm {} inch").format(metric_distance,imperial_distance)
    time.sleep(1)
