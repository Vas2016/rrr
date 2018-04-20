import threading
# import ev3dev.ev3 as ev3
stop = False
m0_speed = 0
m1_speed = 0
running = True
MAX_SPEED = 70
MIN_SPEED = 1
def send_command(command, val):
    print(command, val)

def scale(val, src, dst):
    return (float(val - src[0]) / (src[1] - src[0])) * (dst[1] - dst[0]) + dst[0]

def scale_stick(value):
    # global m0_speed, m1_speed, stop, MAX_SPEED, MIN_SPEED
    sc = scale(value,(0,255),(MAX_SPEED,-(MAX_SPEED)))
    if abs(sc) > MIN_SPEED:
            # stop = False
        return sc
    else:
        return 0
            # m0_speed = 0
            # m1_speed = 0
            # stop = True
    # 

    class Razg():
    def __init__(self):
        self.m_l = ev3.LargeMotor(ev3.OUTPUT_A)
        self.m_m = ev3.MediumMotor(ev3.OUTPUT_D)
    def run_makros_1(self):
        self.m_l.run_to_rel_pos(position_sp=90, duty_cycle_sp=30)
        self.m_m.run_to_rel_pos(position_sp=90, duty_cycle_sp=30)
    def run_makros_2(self):
        self.m_l.run_to_rel_pos(position_sp=-90, duty_cycle_sp=30)
        self.m_m.run_to_rel_pos(position_sp=-90, duty_cycle_sp=30)
razg = Razg()
    # class Zag():
        # def __init__(self):
        # def run_makros_1
            # threading.Thread.__init__(self)
    # def r_back():      
    #     if stop == False:

class MotorThread(threading.Thread):
    def __init__(self):
        self.m0 = ev3.LargeMotor(ev3.OUTPUT_B)
        self.m1 = ev3.LargeMotor(ev3.OUTPUT_C)
        threading.Thread.__init__(self)

    def run(self):
        print("Engine running!")
        while running:
            if stop == False:
                self.m0.run_direct(duty_cycle_sp=m0_speed)
                self.m1.run_direct(duty_cycle_sp=m1_speed)
            else:
                self.m0.stop()
                self.m1.stop()
        self.m0.stop()
        self.m1.stop()

motor_thread = MotorThread()
motor_thread.setDaemon(True)
motor_thread.start()

from inputs import get_gamepad
while running:
    evens = get_gamepad()
    for event in events:
            # 
        if event.ev_type == "Key":
            print('KEYKEY')
            print(event.code, event.state)
            if event.code == "BTN_BASE5" and event.state == 1:
                running = False
            if event.code == "BTN_TRIGGER" and event.state == 1:
                razg.run_makros_1()
            if event.code == "BTN_THUMB" and event.state == 1:
                razg.run_makros_2()
            if event.code == "BTN_THUMB2" and event.state == 1:
                send_command('c3')
                # razg.run_makros_2()
            if event.code == "BTN_TOP" and event.state == 1:
                send_command('c4')
            if event.code == "BTN_BASE" or event.code == "BTN_BASE2":
                if event.state  == 1 and stop == False:
                    stop = True
                elif event.state  == 0 and stop == True:
                    stop = False
            # elif 
        elif event.ev_type == "Absolute":
            print('ABSABS')
            if event.code == "ABS_Y":
                m0_speed = int(scale_stick(int(event.state)))
            elif event.code == "ABS_RY":
                m1_speed = int(scale_stick(int(event.state)))
        print(m0_speed, m1_speed, stop)