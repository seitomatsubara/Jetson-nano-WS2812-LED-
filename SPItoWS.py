import spidev
import sys
 
class SPItoWS():
    def __init__(self, ledc):
        self.led_count = ledc
        self.X = '' # X is signal of WS281x
        for i in range(self.led_count):
            self.X = self.X + "100100100100100100100100100100100100100100100100100100100100100100100100"
        self.spi = spidev.SpiDev()
        self.spi.open(0, 0)
        self.spi.max_speed_hz = 2400000

    def __del__(self):
        self.spi.close()
        
    def _Bytesto3Bytes(self, num, RGB): # num is number of signal, RGB is 8 bits (1 byte) str
        for i in range(8):
            if RGB[i] == '0':
                self.X = self.X[:num * 3 * 8 + i * 3] + '100' + self.X[num * 3 * 8 + i * 3 + 3:]
            elif RGB[i] == '1':
                self.X = self.X[:num * 3 * 8 + i * 3] + '110' + self.X[num * 3 * 8 + i * 3 + 3:]
    
    def _BytesToHex(self, Bytes):
        return ''.join(["0x%02X " % x for x in Bytes]).strip()
    
    def LED_show(self):
            Y = []
            for i in range(self.led_count * 9):
                Y.append(int(self.X[i*8:(i+1)*8],2))
            WS = self._BytesToHex(Y)
            self.spi.xfer3(Y, 2400000,0,8)

    def RGBto3Bytes(self, led_num, R, G, B):
        if (R > 255 or G > 255 or B > 255):
            print("Invalid Value: RGB is over 255\n")
            sys.exit(1)
        if (led_num > self.led_count - 1):
            print("Invalid Value: The number is over the number of LED")
            sys.exit(1)
        RR = format(R, '08b')
        GG = format(G, '08b')
        BB = format(B, '08b')
        self._Bytesto3Bytes(led_num * 3, GG)
        self._Bytesto3Bytes(led_num * 3 + 1, RR)
        self._Bytesto3Bytes(led_num * 3 + 2, BB)

    def LED_OFF_ALL(self):
        self.X = ''
        for i in range(self.led_count):
            self.X = self.X + "100100100100100100100100100100100100100100100100100100100100100100100100"
        self.LED_show()

if __name__ == "__main__":
    import time
    try:
        LED_COUNT = 600
        sig = SPItoWS(LED_COUNT)
        lux = 25
        while True:
            print("main menu\n")
            key = input()
            if key == 'q':
                print(key)
                break
            elif key == '1':
                i = 0
                try:
                    while True:
                        if (i != 0):
                            sig.RGBto3Bytes(i-1, 0, 1, 1)
                        else:
                            sig.RGBto3Bytes(LED_COUNT - 1, 0, 1, 1)
                        sig.RGBto3Bytes(i, 10, 0, 0)
                        sig.LED_show()
                        i = i + 1
                        if i == LED_COUNT:
                            i = 0
                        time.sleep(0.01)
                except KeyboardInterrupt:
                    sig.LED_OFF_ALL()
            elif key == '2':
                r = 255
                g = 0
                b = 0
                i = 0
                try:
                    while True:
                        sig.RGBto3Bytes(i, r, g, b)
                        sig.LED_show()
                        i = i + 1
                except KeyboardInterrupt:
                    sig.LED_OFF_ALL()
            elif key == '3':
                ii = [0,50,100,150,200,250, 300, 350, 400, 450, 500, 550]
                try:
                    while True:
                        sig.RGBto3Bytes(ii[0], 2, 0, 0)
                        sig.RGBto3Bytes(ii[1], 1, 1, 0)
                        sig.RGBto3Bytes(ii[2], 0, 2, 0)
                        sig.RGBto3Bytes(ii[3], 0, 1, 1)
                        sig.RGBto3Bytes(ii[4], 0, 0, 2)
                        sig.RGBto3Bytes(ii[5], 1, 0, 1)
                        sig.RGBto3Bytes(ii[6], 2, 0, 0)
                        sig.RGBto3Bytes(ii[7], 1, 1, 0)
                        sig.RGBto3Bytes(ii[8], 0, 2, 0)
                        sig.RGBto3Bytes(ii[9], 0, 1, 1)
                        sig.RGBto3Bytes(ii[10], 0, 0, 2)
                        sig.RGBto3Bytes(ii[11], 1, 0, 1)
                        sig.LED_show()
                        for i in range(6):
                            ii[i] = ii[i] + 1
                            if ii[i] == LED_COUNT: ii[i] = 0
                except KeyboardInterrupt:
                    sig.LED_OFF_ALL()
        sig.LED_OFF_ALL()
        del sig
        exit(0)
    except KeyboardInterrupt:
        sig.LED_OFF_ALL()
        del sig
        exit(0)
