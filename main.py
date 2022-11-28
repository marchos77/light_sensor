#!/usr/bin/python3

import RPi.GPIO as GPIO
import pymysql

GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.IN)


def database():
    conn = pymysql.connect(
        host='xx.xx.xx.xx',
        user='username',
        password='password',
        db='pi_projects',
    )
    return conn


def read_light():
	light = GPIO.input(4)
	if light == 1:
		out = "off"
		print("Lights off")
	elif light == 0:
		out = "on"
		print("Lights on")
	return out


def insert_db(output):
    connection = database()
    cursor = connection.cursor()
    sensor = "Pi3 Light Sensor"
    try:
        cursor.execute("""INSERT INTO light(light_output) VALUES(%s)""", [output])
    except:
        connection.rollback()
        print("Rolling Back")
    else:
        connection.commit()
        connection.close()
    return "Complete!"


output = read_light()
add_output = insert_db(output)
print(add_output)
