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

class Region_Paises(BaseModel):
    id:int
    name: str
    continent:str
    region:str
    
#Creamos un objeto en forma de lista con diferentes usuarios (Esto sería una base de datos)  
users_list=[Region_Paises(id=0, name="Aruba",continent= "North America",region="Caribbean"),
            Region_Paises( id=1,name="Anguilla",continent= "North America",region="Caribbean"), 
            Region_Paises(id=2,name="Netherlands Antilles",continent= "North America",region="Caribbean"),
            Region_Paises(id=3, name="Antigua and Barbuda",continent= "North America",region="Caribbean"),
            Region_Paises(id=4, name="Bahamas",continent= "North America",region="Caribbean"),
            Region_Paises(id=5, name="Barbados",continent= "North America",region="Caribbean"),
            Region_Paises(id=6, name="Cuba",continent= "North America",region="Caribbean"),
            Region_Paises(id=7, name="Cayman Islands",continent= "North America",region="Caribbean"),
            Region_Paises(id=8, name="Dominica",continent= "North America",region="Caribbean"),
            Region_Paises(id=9, name="Dominican Republic",continent= "North America",region="Caribbean"),
            Region_Paises(id=10, name="Guadeloupe",continent= "North America",region="Caribbean"),
            Region_Paises(id=11, name="Grenada",continent= "North America",region="Caribbean"),
            Region_Paises(id=12, name="Haiti",continent= "North America",region="Caribbean"),
            Region_Paises(id=13, name="Jamaica",continent= "North America",region="Caribbean"),
            Region_Paises(id=14, name="Saint Kitts and Nevis",continent= "North America",region="Caribbean"),
            Region_Paises(id=15, name="Saint Kitts and Nevis",continent= "North America",region="Caribbean"),
            Region_Paises(id=16, name="Saint Kitts and Nevis",continent= "North America",region="Caribbean"),
            Region_Paises(id=17, name="Saint Kitts and Nevis",continent= "North America",region="Caribbean"),
            Region_Paises(id=18, name="Saint Lucia",continent= "North America",region="Caribbean"),
            Region_Paises(id=19, name="Montserrat",continent= "North America",region="Caribbean"),
            Region_Paises(id=20, name="Martinique",continent= "North America",region="Caribbean"),
            Region_Paises(id=21, name="Puerto Rico",continent= "North America",region="Caribbean"),
            Region_Paises(id=22, name="Turks and Caicos Islands",continent= "North America",region="Caribbean"),
            Region_Paises(id=23, name="Trinidad and Tobago",continent= "North America",region="Caribbean"),
            Region_Paises(id=24, name="Saint Vincent and the Grenadines",continent= "North America",region="Caribbean"),
            Region_Paises(id=25, name="Virgin Islands British",continent= "North America",region="Caribbean"),
            Region_Paises(id=26, name="Virgin Islands",continent= "North America",region="Caribbean"),
            Region_Paises(id=27, name="U.S",continent= "North America",region="Caribbean"),
            Region_Paises(id=28, name="Belize",continent= "North America",region="CentralAmerica"),
            Region_Paises(id=29, name="Costa Rica",continent= "North America",region="CentralAmerica"),
            Region_Paises(id=30, name="Guatemala",continent= "North America",region="CentralAmerica"),
            Region_Paises(id=31, name="Honduras",continent= "North America",region="CentralAmerica"),
            Region_Paises(id=32, name="Mexico",continent= "North America",region="CentralAmerica"),
            Region_Paises(id=33, name="Nicaragua",continent= "North America",region="CentralAmerica"),
            Region_Paises(id=34, name="Panama",continent= "North America",region="CentralAmerica"),
            Region_Paises(id=35, name="El Salvador",continent= "North America",region="CentralAmerica"),
            Region_Paises(id=36, name="Bermuda",continent= "North America",region="NorthAmerica"),
            Region_Paises(id=37, name="Canada",continent= "North America",region="NorthAmerica"),
            Region_Paises(id=38, name="Greenland",continent= "North America",region="NorthAmerica"),
            Region_Paises(id=39, name="Saint pierre and Miguelon",continent= "North America",region="NorthAmerica"),
            Region_Paises(id=40, name="United States}",continent= "North America",region="NorthAmerica"),
            Region_Paises(id=41, name="Afghanistan",continent= "Asia",region="Southern and central asia"),
            Region_Paises(id=42, name="Bangladesh",continent= "Asia",region="Southern and central asia"),
            Region_Paises(id=42, name="Bhutan",continent= "Asia",region="Southern and central asia"),
            Region_Paises(id=43, name="India",continent= "Asia",region="Southern and central asia"),
            Region_Paises(id=44, name="Iran",continent= "Asia",region="Southern and central asia"),
            Region_Paises(id=45, name="Kazakstan",continent= "Asia",region="Southern and central asia"),
            Region_Paises(id=46, name="Kyrgyzstan",continent= "Asia",region="Southern and central asia"),
            Region_Paises(id=47, name="Sri Lanka",continent= "Asia",region="Southern and central asia"),
            Region_Paises(id=48, name="Maldives",continent= "Asia",region="Southern and central asia"),
            Region_Paises(id=49, name="Nepal",continent= "Asia",region="Southern and central asia"),
            Region_Paises(id=50, name="Pakistan",continent= "Asia",region="Southern and central asia"),
            Region_Paises(id=51, name="Tajikistan",continent= "Asia",region="Southern and central asia"),
            Region_Paises(id=52, name="Turkmenistan",continent= "Asia",region="Southern and central asia"),
            Region_Paises(id=53, name="Uzbekistan",continent= "Asia",region="Southern and central asia"),
            Region_Paises(id=54, name="United Arab Emirates",continent= "Asia",region="Middle east"),
            Region_Paises(id=55, name="Armenia",continent= "Asia",region="Middle east"),
            Region_Paises(id=56, name="Azerbaijan",continent= "Asia",region="Middle east"),
            Region_Paises(id=57, name="Bahrain",continent= "Asia",region="Middle east"),
            Region_Paises(id=58, name="Cyprus",continent= "Asia",region="Middle east"),
            Region_Paises(id=59, name="Georgia",continent= "Asia",region="Middle east"),
            Region_Paises(id=60, name="Iraq",continent= "Asia",region="Middle east"),
            Region_Paises(id=61, name="Israel",continent= "Asia",region="Middle east"),
            Region_Paises(id=62, name="Jordan",continent= "Asia",region="Middle east"),
            Region_Paises(id=63, name="Kuwait",continent= "Asia",region="Middle east"),
            Region_Paises(id=64, name="Lebanon",continent= "Asia",region="Middle east"),
            Region_Paises(id=65, name="Oman",continent= "Asia",region="Middle east"),
            Region_Paises(id=66, name="Palestine",continent= "Asia",region="Middle east"),
            Region_Paises(id=67, name="Qatar",continent= "Asia",region="Middle east"),
            Region_Paises(id=68,name="Saudi Arabia",continent= "Asia",region="Middle east"),
            Region_Paises(id=69, name="Syria",continent= "Asia",region="Middle east"),
            Region_Paises(id=70, name="Turkey",continent= "Asia",region="Middle east"),
            Region_Paises(id=71, name="Yemen",continent= "Asia",region="Middle east"),
            Region_Paises(id=72, name="Brunei Asia",continent= "Asia",region="Southeast asia"),
            Region_Paises(id=73, name="Cambodia",continent= "Asia",region="Southeast asia"),
            Region_Paises(id=74, name="Laos",continent= "Asia",region="Southeast asia"),
            Region_Paises(id=75, name="Myanmar",continent= "Asia",region="Southeast asia"),
            Region_Paises(id=76, name="Asia",continent= "Asia",region="Southeast asia"),
            Region_Paises(id=77, name="Malaysia",continent= "Asia",region="Southeast asia"),
            Region_Paises(id=78, name="Philippines",continent= "Asia",region="Southeast asia"),
            Region_Paises(id=79, name="Singapore",continent= "Asia",region="Southeast asia"),
            Region_Paises(id=80, name="Thailand",continent= "Asia",region="Southeast asia"),
            Region_Paises(id=81, name="East Timor",continent= "Asia",region="Southeast asia"),
            Region_Paises(id=82, name="China",continent= "Asia",region="Eastern asia"),
            Region_Paises(id=83, name="Hong Kong",continent= "Asia",region="Eastern asia"),
            Region_Paises(id=84, name="Japan",continent= "Asia",region="Eastern asia"),
            Region_Paises(id=85, name="South Korea",continent= "Asia",region="Eastern asia"),
            Region_Paises(id=86, name="Macao",continent= "Asia",region="Eastern asia"),
            Region_Paises(id=87, name="Mongolia",continent= "Asia",region="Eastern asia"),
            Region_Paises(id=88, name="North Korea",continent= "Asia",region="Eastern asia"),
            Region_Paises(id=89, name="Taiwan",continent= "Asia",region="Eastern asia"),
            Region_Paises(id=90, name="Angola",continent= "Africa",region="central africa"),
            Region_Paises(id=91, name="Central African Republic",continent= "Africa",region="central africa"),
            Region_Paises(id=92, name="Cameroon,Congo",continent= "Africa",region="central africa"),
            Region_Paises(id=93, name="The Democratic Republic of the Congo",continent= "Africa",region="central africa"),
            Region_Paises(id=94, name="Gabon",continent= "Africa",region="central africa"),
            Region_Paises(id=95, name="Equatorial Guinea",continent= "Africa",region="central africa"),
            Region_Paises(id=96, name="Sao Tome and Principe",continent= "Africa",region="central africa"),
            Region_Paises(id=97, name="Chad",continent= "Africa",region="central africa"),
            Region_Paises(id=98, name="Burundi",continent= "Africa",region="eastern africa"),
            Region_Paises(id=99, name="Comoros",continent= "Africa",region="eastern africa"),
            Region_Paises(id=100, name="Djibouti Eritrea",continent= "Africa",region="eastern africa"),
            Region_Paises(id=101, name="Ethiopia",continent= "Africa",region="eastern africa"),
            Region_Paises(id=102, name="British Indian Ocean Territory",continent= "Africa",region="eastern africa"),
            Region_Paises(id=103, name="Kenya Africa",continent= "Africa",region="eastern africa"),
            Region_Paises(id=104, name="Madagascar",continent= "Africa",region="eastern africa"),
            Region_Paises(id=105, name="Mozambique",continent= "Africa",region="eastern africa"),
            Region_Paises(id=106, name="Mauritius",continent= "Africa",region="eastern africa"),
            Region_Paises(id=107, name="Malawi",continent= "Africa",region="eastern africa"),
            Region_Paises(id=108, name="Mayotte",continent= "Africa",region="eastern africa"),
            Region_Paises(id=109, name="Reunion",continent= "Africa",region="eastern africa"),
            Region_Paises(id=110, name="Benin",continent= "Africa",region="western africa"),
            Region_Paises(id=111, name="Burkina Faso",continent= "Africa",region="western africa"),
            Region_Paises(id=112, name="Cote dIvoire",continent= "Africa",region="western africa"),
            Region_Paises(id=113, name="Cape Verde",continent= "Africa",region="western africa"),
            Region_Paises( id=114,name="Ghana",continent= "Africa",region="western africa"),
            Region_Paises(id=115, name="Ghana",continent= "Africa",region="western africa"),
            Region_Paises(id=116, name="Ghana",continent= "Africa",region="western africa"),
            Region_Paises(id=117, name="Guinea",continent= "Africa",region="western africa"),
            Region_Paises(id=118, name="Gambia",continent= "Africa",region="western africa"),
            Region_Paises(id=119, name="Guinea-Bissau",continent= "Africa",region="western africa"),
            Region_Paises(id=120, name="Liberia",continent= "Africa",region="western africa"),
            Region_Paises(id=121, name="Mali",continent= "Africa",region="western africa"),
            Region_Paises(id=122, name="Mauritania",continent= "Africa",region="western africa"),
            Region_Paises(id=123, name="Niger",continent= "Africa",region="western africa"),
            Region_Paises(id=124, name="Nigeria",continent= "Africa",region="western africa"),
            Region_Paises(id=125, name="Senegal",continent= "Africa",region="western africa"),
            Region_Paises(id=126, name="Saint Helena",continent= "Africa",region="western africa"),
            Region_Paises(id=127, name="Sierra Leone",continent= "Africa",region="western africa"),
            Region_Paises(id=128, name="Togo",continent= "Africa",region="western africa"),
            Region_Paises(id=129, name="Sierra Leone",continent= "Africa",region="western africa"),
            Region_Paises(id=130, name="Algeria",continent= "Africa",region="northern africa"),
            Region_Paises(id=131, name="Egypt",continent= "Africa",region="northern africa"),
            Region_Paises(id=132, name="Western Sahara",continent= "Africa",region="northern africa"),
            Region_Paises(id=133, name="Libyan Arab Jamahiriya",continent= "Africa",region="northern africa"),
            Region_Paises(id=134, name="Morocco",continent= "Africa",region="northern africa"),
            Region_Paises(id=135, name="Sudan",continent= "Africa",region="northern africa"),
            Region_Paises(id=136, name="Tunisia",continent= "Africa",region="northern africa"),
            Region_Paises(id=137, name="Albania",continent= "Europe",region="Southern europe"),
            Region_Paises(id=138, name="Andorra",continent= "Europe",region="Southern europe"),
            Region_Paises(id=139, name="Bosnia and Herzegovina",continent= "Europe",region="Southern europe"),
            Region_Paises(id=140, name="Spain",continent= "Europe",region="Southern europe"),
            Region_Paises(id=141, name="Gibraltar",continent= "Europe",region="Southern europe"),
            Region_Paises(id=142, name="Greece",continent= "Europe",region="Southern europe"),
            Region_Paises(id=143, name="Croatia",continent= "Europe",region="Southern europe"),
            Region_Paises(id=144, name="Italy",continent= "Europe",region="Southern europe"),
            Region_Paises(id=145, name="Macedonia",continent= "Europe",region="Southern europe"),
            Region_Paises(id=146, name="Malta",continent= "Europe",region="Southern europe"),
            Region_Paises(id=147, name="Portugal",continent= "Europe",region="Southern europe"),
            Region_Paises(id=148, name="San Marino",continent= "Europe",region="Southern europe"),
            Region_Paises(id=149, name="Slovenia",continent= "Europe",region="Southern europe"),
            Region_Paises(id=150, name="Holy See (Vatican City State)",continent= "Europe",region="Southern europe"),
            Region_Paises(id=151, name="Yugoslavia",continent= "Europe",region="Southern europe"),
            Region_Paises(id=152, name="Austria",continent= "Europe",region="Western europe"),
            Region_Paises(id=153, name="Belgium",continent= "Europe",region="Western europe"),
            Region_Paises(id=154, name="Switzerland",continent= "Europe",region="Western europe"),
            Region_Paises(id=155, name="Germany",continent= "Europe",region="Western europe"),
            Region_Paises(id=156, name="France",continent= "Europe",region="Western europe"),
            Region_Paises(id=157, name="Liechtenstein",continent= "Europe",region="Western europe"),
            Region_Paises(id=158, name="Luxembourg",continent= "Europe",region="Western europe"),
            Region_Paises(id=159, name="Monaco",continent= "Europe",region="Western europe"),
            Region_Paises(id=160, name="Netherlands",continent= "Europe",region="Western europe"),
            Region_Paises(id=161, name="Denmark",continent= "Europe",region="Nordic countries"),
            Region_Paises(id=162, name="Finland",continent= "Europe",region="Nordic countries"),
            Region_Paises(id=163, name="Faroe Islands",continent= "Europe",region="Nordic countries"),
            Region_Paises(id=164, name="Iceland",continent= "Europe",region="Nordic countries"),
            Region_Paises(id=165, name="Norway",continent= "Europe",region="Nordic countries"),
            Region_Paises(id=166, name="Svalbard and Jan Mayen",continent= "Europe",region="Nordic countries"),
            Region_Paises(id=167, name="Sweden",continent= "Europe",region="Nordic countries"),
            Region_Paises(id=168, name="Norway",continent= "Europe",region="Nordic countries"),
            Region_Paises(id=169, name="Estonia",continent= "Europe",region="Baltic countries"),
            Region_Paises(id=170, name="Lithuania",continent= "Europe",region="Baltic countries"),
            Region_Paises(id=171, name="Latvia",continent= "Europe",region="Baltic countries"),
            Region_Paises(id=172, name="united Kingdom",continent= "Europe",region="British islands"),
            Region_Paises(id=173, name="Ireland",continent= "Europe",region="Baltic countries"),
            Region_Paises(id=174, name="American Samoa",continent= "Oceania",region="Polynesia"),
            Region_Paises(id=175, name="Cook Islands",continent= "Oceania",region="Polynesia"),
            Region_Paises(id=176, name="Niue",continent= "Oceania",region="Polynesia"),
            Region_Paises(id=177, name="Pitcairn",continent= "Oceania",region="Polynesia"),
            Region_Paises(id=178, name="French Polynesia",continent= "Oceania",region="Polynesia"),
            Region_Paises(id=179, name="Tokelau",continent= "Oceania",region="Polynesia"),
            Region_Paises(id=180, name="Tonga",continent= "Oceania",region="Polynesia"),
            Region_Paises(id=181, name="Tuvalu",continent= "Oceania",region="Polynesia"),
            Region_Paises(id=182, name="Wallis and Futuna",continent= "Oceania",region="Polynesia"),
            Region_Paises(id=183, name="Samoa",continent= "Oceania",region="Polynesia"),
            Region_Paises(id=184, name="Fiji Islands",continent= "Oceania",region="Melanesia"),
            Region_Paises(id=185, name="New Caledonia",continent= "Oceania",region="Melanesia"),
            Region_Paises(id=186, name="Papua New Guinea",continent= "Oceania",region="Melanesia"),
            Region_Paises(id=187, name="Solomon Islandss",continent= "Oceania",region="Melanesia"),
            Region_Paises(id=188, name="Vanuatu",continent= "Oceania",region="Melanesia"),
            Region_Paises(id=189, name="Australia",continent= "Oceania",region="Australia and new zealand"),
            Region_Paises(id=190, name="Cocos (Keeling) Islands",continent= "Oceania",region="Australia and new zealand"),
            Region_Paises(id=191, name="Christmas Island",continent= "Oceania",region="Australia and new zealand"), 
            Region_Paises(id=191, name="Norfolk Island",continent= "Oceania",region="Australia and new zealand"),
            Region_Paises(id=192, name="New Zealand",continent= "Oceania",region="Australia and new zealand"),
            Region_Paises(id=193, name="Micronesia",continent= "Oceania",region="Micronesia"),
            Region_Paises(id=194, name="Guam",continent= "Oceania",region="Micronesia"),
            Region_Paises(id=195, name="Kiribati",continent= "Oceania",region="Micronesia"),
            Region_Paises(id=196, name="Marshall Islands",continent= "Oceania",region="Micronesia"),
            Region_Paises(id=197, name="Northern Mariana Islands",continent= "Oceania",region="Micronesia"),
            Region_Paises(id=198, name="Nauru",continent= "Oceania",region="Micronesia"),
            Region_Paises(id=199, name="Palau",continent= "Oceania",region="Micronesia"),
            Region_Paises(id=200, name="united States Minor Outlying Islands",continent= "Oceania",region="Micronesia"),
            Region_Paises(id=201, name="united States Minor Outlying Islands",continent= "Oceania",region="Micronesia"),
            Region_Paises(id=202, name="united States Minor Outlying Islands",continent= "Oceania",region="Caribbean"),
            Region_Paises(id=203, name="Antarctica",continent= "Antartica",region="Antarctica"),
            Region_Paises(id=204, name="French Southern territories",continent= "Antartica",region="Antarctica"),
            Region_Paises(id=205, name="Bouvet Island",continent= "Antartica",region="Antarctica"),
            Region_Paises(id=206, name="Heard Island and McDonald Islands",continent= "Antartica",region="Antarctica"),
            Region_Paises(id=207, name="South Georgia and the South Sandwich Islands",continent= "Antartica",region="Antarctica"),
            Region_Paises(id=208, name="Argentina",continent= "SouthAmerica",region="southamerica"),
            Region_Paises(id=209, name="Bolivia",continent= "SouthAmerica",region="southamerica"),
            Region_Paises(id=210, name="Brazil",continent= "SouthAmerica",region="southamerica"),
            Region_Paises(id=211, name="Chile",continent= "SouthAmerica",region="southamerica"),
            Region_Paises(id=212, name="Colombia",continent= "SouthAmerica",region="southamerica"),
            Region_Paises(id=213, name="Ecuador",continent= "SouthAmerica",region="southamerica"),
            Region_Paises(id=214, name="Falkland Islands",continent= "SouthAmerica",region="southamerica"),
            Region_Paises(id=215, name="French Guiana",continent= "SouthAmerica",region="southamerica"),
            Region_Paises(id=216, name="Guyana",continent= "SouthAmerica",region="southamerica"),
            Region_Paises(id=217, name="Peru",continent= "SouthAmerica",region="southamerica"),
            Region_Paises(id=218, name="Paraguay",continent= "SouthAmerica",region="southamerica"),
            Region_Paises(id=219, name="Suriname",continent= "SouthAmerica",region="southamerica"),
            Region_Paises(id=220, name="uruguay",continent= "SouthAmerica",region="southamerica"),
            Region_Paises(id=221, name="Venezuela",continent= "SouthAmerica",region="southamerica")]
              


#***Get con Filtro Path
@router.get("/region/country/{id}/", response_model=Region_Paises, status_code=status.HTTP_200_OK)
async def usersclass(id:int):
    users=filter (lambda user: user.id == id, users_list)  #Función de orden superior
    try:
        return list(users)[0]
    except:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail="No se han encontrado los paises por region")
        #return{"error":"No se ha encontrado el usuario"}
    
     # En el explorador colocamos la raiz de la ip: http://127.0.0.1:8000/usersclass/1

 #***Post
@router.post("/region/country/", response_model=Region_Paises, status_code=status.HTTP_201_CREATED)
async def usersclass(user:Region_Paises):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
            #return {"error":"el usuario ya existe"}
            raise HTTPException(status_code= status.HTTP_401_UNAUTHORIZED,detail="los paises por region ya existe")
    else:
        users_list.append(user)
        raise HTTPException(status_code= status.HTTP_200_OK,detail="los paises por region ya se encuentra agregado")
    
    #http://127.0.0.1:8000/usersclass/
      #***Put
@router.put("/region/country/", response_model=Region_Paises, status_code=status.HTTP_200_OK)
async def usersclass(user:Region_Paises):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           users_list[index] = user  #accedemos al indice de la lista que hemos encontrado y actualizamos con el nuevo usuario
           found=True
           
    if not found:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail="No se ha actualizado los paises por region")
        #return {"error":"No se ha actualizado el usuario"}
    else:
        raise HTTPException(status_code= status.HTTP_302_FOUND,detail="los paises por region ya se encuentra agregado")
    
    #http://127.0.0.1:8000/usersclass/
    
    
        #***Delete
@router.delete("/region/country/{id}/", response_model=Region_Paises, status_code=status.HTTP_200_OK)
async def usersclass(id:int):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(users_list):
        if saved_user.id ==id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           del users_list[index]  #Eliminamos al indice de la lista que hemos encontrado 
           found=True
           raise HTTPException(status_code= status.HTTP_202_ACCEPTED,detail="los paises por region se ha eliminado")
           #return "El registro se ha eliminado"
       
    if not found:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail="No se ha eliminado los paises por region")
        #return {"error":"No se ha eliminado el usuario"}
    
    #http://127.0.0.1:8000/usersclass/1