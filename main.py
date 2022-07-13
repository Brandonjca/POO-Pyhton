from lib2to3.pgen2 import driver
from car import Car
from payment import pay
from rout import Rout
from user import User


if __name__ == "__main__":
    print ("Hola mundo")
    
    car =  Car()
    car.tipo            ="Datos del transporte"
    car.id              =5
    car.brand           ="Chevrolet"
    car.driver          ="Brandon"
    car.passager        =5
    
    print(vars(car))
    
    car2 = Car()
    car2.tipo           ="Datos del transporte"
    car2.id             =1754
    car2.brand          ="Toyota"
    car2.driver         ="Juan"
    car2.passager       =2
    
    print(vars(car2))
    
    pago = pay()
    pago.tipo          ="Pago"
    pago.id            =1
    pago.cantidad      =150
    pago.observacion   ="Pago realizado"
    
    print(vars(pago))
    
    user = User()
    user.tipo       ="Datos del usuario"
    user.id         =1725415143
    user.nombre     ="Maximiliam"
    user.apellido   ="Pegasus"
    
    print(vars(user))
    
    ruta = Rout()
    ruta.tipo       ="Datos de la ruta"
    ruta.id         =1235
    ruta.start      ="San Juan de Calderon"
    ruta.end        ="Instituto Yavirac"
    
    print(vars(ruta))
        