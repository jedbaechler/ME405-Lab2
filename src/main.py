'''
    @file main.py
    @author Jeremy Baechler
    @author Kendall Chappell
    @author Matthew Wimberley

'''

#Pull encoder data
#Run control loop with new data
#Take returned PWM duty and send that to the motor
#Store data in controller
#Print Data to serial port

#Input Kp, setpoint

import EncoderReader, controlloop
import motor_baechler_chappell_wimberley as motor_drv

ENA = pyb.Pin (pyb.Pin.board.PA10, pyb.Pin.OUT_PP)
IN1 = pyb.Pin (pyb.Pin.board.PB4, pyb.Pin.OUT_PP)
IN2 = pyb.Pin (pyb.Pin.board.PB5, pyb.Pin.OUT_PP) #motor port A pins
tim3 = pyb.Timer (3, freq=20000)


Kp = float(input('Please type in a proportional gain constant!: '))
setpoint = float(input('Please type in a position setpoint!: '))

mot1 = motor_drv.Motor_Driver(ENA, IN1, IN2, tim3)
enc1 = EncoderReader.EncoderReader(1)
controller = controlloop.ClosedLoop(Kp, setpoint)

while True:
    PWM = controller.run(enc1.read())
    controller.add_data()
    mot1.set_duty(PWM)
    utime.sleep_ms(10)
    


