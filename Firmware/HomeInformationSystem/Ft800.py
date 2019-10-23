import Spi
import gpio





#class Spi(nss, drvname=SPI0, clock=12000000, bits=SPI_8_BITS, mode=SPI_MODE_LOW_FIRST)



class FT800:
    #definitions
    def __init__(self, power_down, spi_select, spi_chanel=SPI0):
        #isinstance
        self.power_down = gpio.mode(power_down, OUTPUT)
        self.spi_select = gpio.mode(spi_select, OUTPUT)
        self.ft00_spi = Spi(drvname=spi_chanel, clock=12000000, bits=Spi.SPI_8_BITS, mode=Spi.SPI_MODE_HIGH_FIRST)
        self.ChipOn = 1
        self.ChipOFF = 0
        
    # private method select slave
    def __Low_Byte(self, data):
        return (data & 0xFF)
        
    # private method select slave
    def __High_Byte(self, data):
        return ((data>>8) & 0xFF)
    
    # private method select slave
    def __SelectChipOnOff(self, ChipOnOff):         
        timeout=1000000
        if ChipOnOff == 1 :
           gpio.low(self.spi_select)
        #deselect chip after timout
        elif ChipOnOff == 0 :
            while timeout > 1 :
                timeout -= 1
            gpio.high(self.spi_select)
    
    # private method write
    def __SPI_WRITE (self, wert):
        self.ft00_spi.write(wert)
        self.ft00_spi.read(1)
        
    # private method write   
    def __SPI_READ(self):
        self.ft00_spi.write(0xff)
        return self.ft00_spi.read(1)
        
    # private method write 16bit   
    def __SPI2TransmitWord(self, wert):
        #Low byte first
        self.__SPI_WRITE(0xff&wert)
        self.__SPI_WRITE(0xFF&(wert>>8))
        
    # private method write 8bit   
    def __SPI2TransmitByte(self, wert):
        #Low byte first
        self.__SPI_WRITE(0xff&wert)
        
    # private method reveice Word 
    def __SPI2ReceiveByte(self):
        self.ft00_spi.write(0xff)
        return self.ft00_spi.read(1)
    
    # private method send command
    def __host_command(self, cmd):
        self.__SelectChipOnOff(self.ChipOn)
        self.__SPI_WRITE(cmd)
        self.__SPI_WRITE(0)
        self.__SPI_WRITE(0)
        self.__SelectChipOnOff(self.ChipOff)
        
    # private method write 32bit adress 8 Byte
    def __wr8(self, address, data):
        self.__SelectChipOnOff(self.ChipOn)
        self.__SPI_WRITE(0x80|(address>>16))
        self.__SPI_WRITE(address>>8)
        self.__SPI_WRITE(address)
        self.__SPI_WRITE(data)
        self.__SelectChipOnOff(self.ChipOff)    
    
    # private method write 32bit adress 16 Byte
    def __wr16(self, address, data):
        self.__SelectChipOnOff(self.ChipOn)
        self.__SPI_WRITE(0x80|(address>>16))
        self.__SPI_WRITE(address>>8)
        self.__SPI_WRITE(address)
        self.__SPI2TransmitWord(data)
        self.__SelectChipOnOff(self.ChipOff)    
        
    # private method write 32bit adress 32 Byte
    def __wr32(self, address, data):
        self.__SelectChipOnOff(self.ChipOn)
        self.__SPI_WRITE(0x80|(address>>16))
        self.__SPI_WRITE(address>>8)
        self.__SPI_WRITE(address)
        self.__SPI2TransmitWord(data)
        self.__SPI2TransmitWord(data>>16)
        self.__SelectChipOnOff(self.ChipOff)    
        
        
    # private methodread 32bit adress return 8 Byte
    def __rd8(self, address, data):   
        self.__SelectChipOnOff(self.ChipOn)
        self.__SPI_WRITE(0x80|(address>>16))
        self.__SPI_WRITE(address>>8)
        self.__SPI_WRITE(address)
        self.__SPI_WRITE(0x00)
        data=self.__SPI_READ()
        self.__SelectChipOnOff(self.ChipOff)   
        return data
        
    # private methodread 32bit adress return 16 Byte
    def __rd16(self, address, data):   
        self.__SelectChipOnOff(self.ChipOn)
        self.__SPI_WRITE(0x80|(address>>16))
        self.__SPI_WRITE(address>>8)
        self.__SPI_WRITE(address)
        self.__SPI_WRITE(0x00)
        data=self.__SPI_READ()
        data=data|(self.__SPI_READ()<<8)
        self.__SelectChipOnOff(self.ChipOff)   
        return data
 
    # private methodread 32bit adress return 32 Byte
    def __rd32(self, address, data):   
        self.__SelectChipOnOff(self.ChipOn)
        self.__SPI_WRITE(0x80|(address>>16))
        self.__SPI_WRITE(address>>8)
        self.__SPI_WRITE(address)
        self.__SPI_WRITE(0x00)
        data=self.__SPI_READ()
        data=data|(self.__SPI_READ()<<8)
        data=data|(self.__SPI_READ()<<16)
        data=data|(self.__SPI_READ()<<24)
        self.__SelectChipOnOff(self.ChipOff)   
        return data    
        
        
        
        