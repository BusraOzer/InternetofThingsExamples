from hcsr04sensor import sensor
import time

while 1:
    trig_pin = 18
    echo_pin = 24

    # Default degerler
    # unit = 'metric'
    # temperature = 20
    # round_to = 1

    hole_depth = 10  # bardagin derinligi
    value = sensor.Measurement(trig_pin,
                               echo_pin
                               )
    #yuksek dogruluk icin sample_size ve sample_wait ayarla
    raw_measurement = value.raw_distance(sample_size=15,sample_wait=0.2)

    # Bardagin icinde bulunan cayin derinligini hesapla
    liquid_depth = value.depth_metric(raw_measurement, hole_depth)
    print("Bardaktaki cayin derinligi = {} cm".format(liquid_depth))
    time.sleep(1)
