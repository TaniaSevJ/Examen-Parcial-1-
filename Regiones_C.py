#En vez de Importar el framework fastapi, importamos APIRouter a nuestro entorno de trabajo
from fastapi import APIRouter, HTTPException, status
#Importamos pydantic para obtener una entidad que pueda definir usuarios
from pydantic import BaseModel

#Creamos un objeto a partir de la clase FastAPI
router= APIRouter()

#Levantamos el server Uvicorn
#-uvicorn 4_codigos_HTTP:app --reload-
#{"id":3,"Name":"Alfredo", "LastName":"Garcia", "Age":30}
#Definimos nuestra entidad: user

class Regiones_Contiemnetes(BaseModel):
    continent:str
    region:str
   
    
#Creamos un objeto en forma de lista con diferentes usuarios (Esto sería una base de datos)  
users_list=[Regiones_Contiemnetes(continent= "North America",region="Caribbean"),
            Regiones_Contiemnetes(continent= "North America",region="CentralAmerica"),
            Regiones_Contiemnetes(continent= "North America",region="NorthAmerica"),
            Regiones_Contiemnetes(continent= "Asia",region="Southern and central asia"),
            Regiones_Contiemnetes(continent= "Asia",region="Middle east"),
            Regiones_Contiemnetes(continent= "Asia",region="Southeast asia"),
            Regiones_Contiemnetes(continent= "Asia",region="Eastern asia"),
            Regiones_Contiemnetes(continent= "Africa",region="Central africa"),
            Regiones_Contiemnetes(continent= "Africa",region="Eastern africa"),
            Regiones_Contiemnetes(continent= "Africa",region="Western africa"),
            Regiones_Contiemnetes(continent= "Africa",region="Northern africa"),
            Regiones_Contiemnetes(continent= "Europe",region="Southern europe"),
            Regiones_Contiemnetes(continent= "Europe",region="Western europe"),
            Regiones_Contiemnetes(continent= "Europe",region="Eastern europe"),
            Regiones_Contiemnetes(continent= "Europe",region="Nordic countries"),
            Regiones_Contiemnetes(continent= "Europe",region="Baltic countries"),
            Regiones_Contiemnetes(continent= "Europe",region="British islands"),
            Regiones_Contiemnetes(continent= "Oceania",region="Polynesia"),
            Regiones_Contiemnetes(continent= "Oceania",region="Melanesia"),
            Regiones_Contiemnetes(continent= "Oceania",region="Australia and new zealand"),
            Regiones_Contiemnetes(continent= "Oceania",region="Micronesia"),
            Regiones_Contiemnetes(continent= "Oceania",region="Caribbean"),
            Regiones_Contiemnetes(continent= "Antartica",region="Antarctica"),
            Regiones_Contiemnetes(continent= "SouthAmerica",region="Southamerica")]
 
#***Get con Filtro Path
#Muestra toda la lista de contientes
@router.get("/continent/region")
async def continentregion():
        return (users_list)

#***Post
@router.post("/continent/region", response_model=Regiones_Contiemnetes, status_code=201)
async def continentregion(user:Regiones_Contiemnetes):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(users_list):
        if  saved_user.region == user.region:     #Si el code del usuario guardado es igual al code del usuario nuevo
         raise HTTPException(status_code=204,detail="La region ya existe")
    else:
            users_list.append(user)
            return user
    
   #Para actualizae, debemos borrar
   
    #***Put
@router.put("/continent/region", response_model=Regiones_Contiemnetes, status_code=status.HTTP_200_OK)
async def continentregion(user:Regiones_Contiemnetes):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 

    for index, saved_user in enumerate(users_list):
        if   saved_user.region== user.region:   
                users_list[index] = user  #accedemos al indice de la lista que hemos encontrado y actualizamos con el nuevo usuario
                found=True

    if not found:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail="No se ha actualizado la region")
    else:
         raise HTTPException(status_code= status.HTTP_302_FOUND,detail="La region ya se encuentra actualizada")

    
    
    
        #***Delete
@router.delete("/region/{region}", response_model=Regiones_Contiemnetes, status_code=status.HTTP_200_OK)
async def continentregion(user:Regiones_Contiemnetes):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(users_list):
        if saved_user.region == user.region:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           del users_list[index] #Eliminamos al indice de la lista que hemos encontrado 
           found=True
           raise HTTPException(status_code= status.HTTP_202_ACCEPTED,detail="Se ha eliminado la region")  
    if not found:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail="No se ha eliminado la región")
    #http://127.0.0.1:8000/continent/