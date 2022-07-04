#Construye un programa que, al recibir como datos el costo de un artuculo vendido y la cantidad de dinero entregada por el cliente calcula

#1 el cambio que debe de entregar al cliente, si el pago efectuado es mayor al pproducto
#2 que pasa si el cliete paga exactamente lo qeu cale el producto
#la cantidad de dinero que falta por pafar, si el pago efectuado es menor que el precio del producto

art=float(input("Ingresa el total de la cuenta: "))
dinero=float(input("Dinero recibido: "))

    
if art > dinero:
    
    while art>dinero:
        print("Aun falta %s de dinero" %(round(abs(dinero-art) ,2)))
        dineroQueFalta = float(input("Dinero recibido: "))
        dinero+=dineroQueFalta

if art < dinero:
    print("Gracias por su compra, su cambio es %s" %(round(dinero-art ,2)))

elif art == dinero:
    print("Muchas gracias por haber comprado aqui, hasta pronto")

