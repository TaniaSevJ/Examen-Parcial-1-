#En vez de Importar el framework fastapi, importamos APIRouter a nuestro entorno de trabajo
from fastapi import APIRouter, HTTPException, status
#Importamos pydantic para obtener una entidad que pueda definir usuarios
from pydantic import BaseModel

#Creamos un objeto a partir de la clase FastAPI
router= APIRouter()

#Levantamos el server Uvicorn
#-uvicorn Continentes_A:app --reload-
#{"id":3,"Name":"Alfredo", "LastName":"Garcia", "Age":30}
#Definimos nuestra entidad: user

class continentes(BaseModel):
    continent:str

continent_list=[continentes(continent="North America"),
                continentes(continent="Asia"),
                continentes(continent="Africa"),
                continentes(continent="Europe"),
                continentes(continent="Oceania"),
                continentes(continent="Antarctica"),
                continentes(continent="South America")]
#Creamos un objeto en forma de lista con diferentes usuarios (Esto sería una base de datos)  

#***Get
#Muestra toda la lista de contientes
@router.get("/continent/")
async def continent():
        return (continent_list)

 
#***Post
@router.post("/continent/", response_model=continentes, status_code=201)
async def continent(user:continentes):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(continent_list):
        if saved_user.continent == user.continent:  #Si el code del usuario guardado es igual al code del usuario nuevo
            raise HTTPException(status_code=204,detail="El continente ya existe")
        else:
            continent_list.append(user)
            return user
    
   
   
    #***Put
@router.put("/continent/", response_model=continentes, status_code=status.HTTP_200_OK)
async def continent(user:continentes):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(continent_list):
        #Si el Id del usuario guardado es igual al Id del usuario nuevo
        if  saved_user.continent == user.continent:  
           continent_list[index] = user  #accedemos al indice de la lista que hemos encontrado y actualizamos con el nuevo usuario
           found=True

        if not found:
         raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail="No se ha actualizado el contionente")
        else:
         raise HTTPException(status_code= status.HTTP_302_FOUND,detail="El continente ya se encuentra actualizado")
        #return user
    
   
    
        #***Delete
@router.delete("/continent/{continent}", response_model=continentes, status_code=status.HTTP_200_OK)
async def continent(continent:str):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(continent_list):
        if saved_user.continent == continent:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           del continent_list[index]  #Eliminamos al indice de la lista que hemos encontrado 
           found=True
           raise HTTPException(status_code= status.HTTP_202_ACCEPTED,detail="Se ha eliminado el contiente")
       
    if not found:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail="No se ha eliminado el contiente")
    
    #http://127.0.0.1:8000/Continent/