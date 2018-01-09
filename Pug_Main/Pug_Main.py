# -*- coding: utf-8 -*-
import smbus
import time
bus = smbus.SMBus(1)
address = 0x32
reg_buzzer = 41
servo_def_value = 90
servo_values = [150, 150, 150]
reg_servo_values = [52, 53, 54]
servo_inc_value = 10
x = 0
direction = 1

# 0 for dec and 1 for inc


def write_bytes(value, reg_val):
    bus.write_i2c_block_data(address, reg_val, value)
    return -1


def write_byte(value, reg_val):
    bus.write_byte_data(address, reg_val, value)
    return -1


def read_number(reg_val):
    number = bus.read_byte_data(address, reg_val)
    return number


def high_byte(num):
    hex_num = hex(num >> 8)
    dec_num = int(hex_num, 16)
    return dec_num


def low_byte(num):
    hex_num = hex(num & 0xFF)
    dec_num = int(hex_num, 16)
    return dec_num


def play_buzzer(freq):
    data = [high_byte(freq), low_byte(freq)]
    write_bytes(data, reg_buzzer)


while True:
    # Primary Duty Cycle
    time.sleep(1)
    play_buzzer(5000)
    time.sleep(1)
    play_buzzer(0)
    if direction == 1:
        servo_values[x % 3] = servo_values[x % 3] + servo_inc_value
    else:
        servo_values[x % 3] = servo_values[x % 3] - servo_inc_value
    if servo_values[2] >= 180:
        direction = 0
    elif servo_values[2] <= 1:
        direction = 1
        write_byte(servo_values[x % 3], reg_servo_values[x % 3])
    print(servo_values)
    x = x + 1