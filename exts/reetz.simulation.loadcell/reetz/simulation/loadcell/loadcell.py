
import serial

class LoadCell:
    def __init__(self, name=None, port=None):
        self.name = name
        self.port = port
        self.value = 0
        self.tare_offset = 0
        self.calibration_factor = 1

    def connect(self):
        self.ser = serial.Serial(self._com_port.model.get_value_as_string(), 115200)
        print(self.ser, self.ser.is_open)

    @property
    def is_ready(self):
        return self.ser and self.ser.is_open

    def tare(self):
        self.tare_offset = self._load_field.model.get_value_as_float()

    def calibrate(self):
        self.calibration_factor = (self._load_field.model.get_value_as_float() - self.tare_offset)

    def calculate_weight(self, value):
        return (float(value) - self.tare_offset) * self.calibration_factor
    
    def read_load(self):
        if self.is_ready:
            next_line = ''
            while(self.ser.in_waiting > 0):
                next_line = self.ser.readline().decode('utf-8')
            if 'Read' in next_line:
                load_value = next_line.split(' ')[1].replace("\r\n", '')
                load_value = self.calculate_weight(load_value)
            return load_value
        else:
            return False
    
    def shutdown_serial(self):
        if self.ser:
            self.ser.close()

    def flush(self):
        if self.ser:
            self.ser.flush()