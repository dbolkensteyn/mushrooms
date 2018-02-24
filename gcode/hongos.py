import serial
import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)            #selecciona numero de pines del conector
GPIO.setup(38,GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Open grbl serial port
s = serial.Serial('/dev/ttyACM0', 115200)
# Open g-code file
f = open('busca_hongo.txt','r');
f1 = open('deja_hongo.txt','r');

# Wake up grbl
s.write("\r\n\r\n")
time.sleep(2)   # Wait for grbl to initialize
s.flushInput()  # Flush startup text in serial input

# Manda comandos para buscar el hongo
for line in f:
    l = line.strip() # Strip all EOL characters for consistency
    print 'Sending: ' + l,
    s.write(l + '\n') # Send g-code block to grbl
    grbl_out = s.readline() # Wait for grbl response with carriage return
    print ' : ' + grbl_out.strip()

#...............................................................
#baja eze Z de a poco hasta detectar el hongo por vacio.
z0 = 0	#valor inicial
dz = 5	#incremento por cada bajada buscando el hongo
zmax = 80	#limite inferior para evitar que golpee la mesa por si no detecta el hongo
status = True

while status:
    z0=z0+dz	#baja eje Z un paso (5mm)
    c='z ' + str(z0)    #arma comando de movimiento z con una coordenada cada vez mas alta para ir acercandose al hongo
    s.write(c + '\n') # Send g-code Z movement to grbl
    grbl_out = s.readline() # Wait for grbl response with carriage return
    print ' : ' + grbl_out.strip()
    print c
    time.sleep(.5)
    if z0 == zmax:
      print 'Llego al maximo y NO detecto el hongo' + '\n'
      break
    status = GPIO.input(38)
    if status == False:
        print "hongo agarrado"
#...............................................................
# Manda comandos para dejar el hongo
for line in f1:
    l = line.strip() # Strip all EOL characters for consistency
    print 'Sending: ' + l,
    s.write(l + '\n') # Send g-code block to grbl
    grbl_out = s.readline() # Wait for grbl response with carriage return
    print ' : ' + grbl_out.strip()

# Wait here until grbl is finished to close serial port and file.
raw_input("  Press <Enter> to exit and disable grbl.") 

# Close file and serial port
f.close()
s.close()    
