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

class User(BaseModel):
    code:str
    population:int
    life_expectancy:int
    local_name:str
    government_form:str
    head_of_state:str

#Creamos un objeto en forma de lista con diferentes usuarios (Esto sería una base de datos)  
users_list=[User(code= "ABW",population=103000,life_expectancy=78.4,gnp=828,gnp_old=793,local_name="Aruba",government_form="Nonmetropolitan Territory of The Netherlands",head_of_state= "Willem-Alexander"),
                User(code= "AFG",population=22720000,life_expectancy=45.9,gnp=5976,gnp_old=0,local_name="Afganistan/Afqanestan",government_form="Islamic Emirate",head_of_state= "Mohammad Omar"),
                User(code= "AGO",population=12878000,life_expectancy=38.3,gnp=6648,gnp_old=7984,local_name="Angola",government_form="Republic",head_of_state= "Jose Eduardo dos Santos"),
                User(code= "AIA",population=8000,life_expectancy=76.1,gnp=63.2,gnp_old=0,local_name="Anguilla",government_form="Dependent Territory of the uK",head_of_state= "Elisabeth II"),
                User(code= "ALB",population=3401200,life_expectancy=71.6,gnp=3205,gnp_old=2500,local_name="Shqiperia",government_form="Republic",head_of_state= "Rexhep Mejdani"),
                User(code= "AND",population=78000,life_expectancy=83.5,gnp=1630,gnp_old=0,local_name="Andorra",government_form="Parliamentary Coprincipality",head_of_state= ""),
                User(code= "ANT",population=217000,life_expectancy=74.7,gnp=1941,gnp_old=0,local_name="Nederlandse Antillen",government_form="Nonmetropolitan Territory of The Netherlands",head_of_state= "Willem-Alexander"),
                User(code= "ARE",population=2441000,life_expectancy=74.1,gnp=37966,gnp_old=36846,local_name="Al-Imarat al- Arabiya al-Muttahida",government_form="Emirate Federation",head_of_state= "Zayid bin Sultan al-Nahayan"),
                User(code= "ARG",population=37032000,life_expectancy=75.1,gnp=340238,gnp_old=323310,local_name="Argentina",government_form="Federal Republic",head_of_state= "Fernando de la Rua"),
                User(code= "ARM",population=3520000,life_expectancy=66.4,gnp=1813,gnp_old=1627,local_name="Hajastan",government_form="Republic",head_of_state= "Robert KotSarjan"),
                User(code= "ASM",population=68000,life_expectancy=75.1,gnp=334,gnp_old=0,local_name="Amerika Samoa",government_form="uS Territory",head_of_state= "George W. Bush"),
                User(code= "ATA",population=0,life_expectancy=0,gnp=0,gnp_old=0,local_name="N/A",government_form="Co-administrated",head_of_state= ""),
                User(code= "ATF",population=0,life_expectancy=0,gnp=0,gnp_old=0,local_name="Terres australes francaises",government_form="Nonmetropolitan Territory of France",head_of_state= "Jacques Chirac"),
                User(code= "ATG",population=68000,life_expectancy=70.5,gnp=612,gnp_old=584,local_name="Antigua and Barbuda",government_form="Constitutional Monarchy",head_of_state= "Elisabeth II"),
                User(code= "AuS",population=18886000,life_expectancy=79.8,gnp=351182,gnp_old=392911,local_name="Australia",government_form="Constitutional Monarchy",head_of_state= " Federation,Elisabeth II"),
                User(code= "AuT",population=8091800,life_expectancy=77.7,gnp=211860,gnp_old=206025,local_name="osterreich",government_form="Federal Republic",head_of_state= "Thomas Klestil"),
                User(code= "AZE",population=7734000,life_expectancy=62.9,gnp=4127,gnp_old=4100,local_name="Azarbaycan",government_form="Federal Republic",head_of_state= "Heydar aliyev"),
                User(code= "BDI",population=6695000,life_expectancy=46.2,gnp=903,gnp_old=982,local_name="Burundi/uburundi",government_form="Republic",head_of_state= "Pierre Buyoya"),
                User(code= "BEL",population=10239000,life_expectancy=77.8,gnp=249704,gnp_old=243948,local_name="Belgie/Belgique",government_form="Constitutional Monarchy",head_of_state= " Federation,Albert II"),
                User(code= "BEN",population=6097000,life_expectancy=50.2,gnp=2357,gnp_old=2141,local_name="Benin",government_form="Republic",head_of_state= "Mathieu Kerekou"),
                User(code= "FA",population=11937000,life_expectancy=46.7,gnp=2425,gnp_old=2201,local_name="Burkina Faso",government_form="Republic",head_of_state= "Blaise Compaore"),
                User(code= "BGD",population=129155000,life_expectancy=60.2,gnp=32852,gnp_old=31966,local_name="Bangladesh",government_form="Republic",head_of_state= "Shahabuddin Ahmad"),
                User(code= "BGR",population=8190900,life_expectancy=70.9,gnp=12178,gnp_old=10169,local_name="Balgarija",government_form="Republic",head_of_state= "Petar Stojanov"),
                User(code= "BHR",population=617000,life_expectancy=73,gnp=6366,gnp_old=6097,local_name="Al Bahrayn",government_form="Monarchy (Emirate)",head_of_state= "Hamad ibn Isa al-Khalifa"),
                User(code= "BHS",population=307000,life_expectancy=71.1,gnp=3527,gnp_old=3347,local_name="he Bahamas",government_form="Constitutional Monarchy",head_of_state= "Elisabeth II"),
                User(code= "BIH",population=3972000,life_expectancy=71.5,gnp=2841,gnp_old=0,local_name="Bosna i Hercegovina",government_form="Federal Republic",head_of_state= "Ante Jelavic"),
                User(code= "BLR",population=10236000,life_expectancy=68,gnp=13714,gnp_old=0,local_name="Belarus",government_form="Republic",head_of_state= "Aljaksandr LukaSenka"),
                User(code= "BLZ",population=241000,life_expectancy=70.9,gnp=630,gnp_old=616,local_name="Belize",government_form="Constitutional Monarchy",head_of_state= "Elisabeth II"),
                User(code= "BMu",population=65000,life_expectancy=76.9,gnp=2328,gnp_old=2190,local_name="Bermuda",government_form="Dependent Territory of the uK",head_of_state= "Elisabeth II"),
                User(code= "BOL",population=8329000,life_expectancy=63.7,gnp=8571,gnp_old=7967,local_name="Bolivia",government_form="Republic",head_of_state= "Hugo Banzer Suarez"),
                User(code= "BRA",population=170115000,life_expectancy=62.9,gnp=776739,gnp_old=804108,local_name="Brasil",government_form="Federal Republic",head_of_state= "Fernando Henrique Cardoso"),
                User(code= "BRB",population=270000,life_expectancy=73,gnp=2223,gnp_old=2186,local_name="Barbados",government_form="Constitutional Monarchy",head_of_state= "Elisabeth II"),
                User(code= "BRN",population=328000,life_expectancy=73.6,gnp=11705,gnp_old=12460,local_name="Brunei Darussalam",government_form="Monarchy (Sultanate)",head_of_state= "Haji Hassan al-Bolkiah"),
                User(code= "BTN",population=2124000,life_expectancy=52.4,gnp=372,gnp_old=383,local_name="Druk-Yul",government_form="Monarchy",head_of_state= "Jigme Singye Wangchuk"),
                User(code= "BVT",population=0,life_expectancy=0,gnp=0,gnp_old=0,local_name="Bouvetoya",government_form="Dependent Territory of Norway",head_of_state= "Harald V"),
                User(code= "BWA",population=1622000,life_expectancy=39.3,gnp=4834,gnp_old=4935,local_name="Botswana",government_form="Republic",head_of_state= "Festus G. Mogae"),
                User(code= "CAF",population=3615000,life_expectancy=44,gnp=1054,gnp_old=993,local_name="Centrafrique/Be-Afrika",government_form="Republic",head_of_state= "Ange-Felix Patasse"),
                User(code= "CAN",population=31147000,life_expectancy=79.4,gnp=598862,gnp_old=625626,local_name="Canada",government_form="Constitutional Monarchy",head_of_state= " Federation, Elisabeth II"),
                User(code= "CCK",population=600,life_expectancy=0,gnp=0,gnp_old=0,local_name="Cocos (Keeling) Islands",government_form="Territory of Australia",head_of_state="Elisabeth II"),
                User(code= "CHE",population=7160400,life_expectancy=79.6,gnp=264478,gnp_old=256092,local_name="Schweiz/Suisse/Svizzera/Svizra",government_form="Federation",head_of_state= "Adolf Ogi"),
                User(code= "CHL",population=15211000,life_expectancy=75.7,gnp=72949,gnp_old=75780,local_name="Chile",government_form="Republic",head_of_state= "Ricardo Lagos Escobar"),
                User(code= "CHN",population=1277558000,life_expectancy=71.4,gnp=982268,gnp_old=917719,local_name="Zhongquo",government_form="PeoplesRepublic",head_of_state= "Jiang Zemin"),
                User(code= "CIV",population=14786000,life_expectancy=45.2,gnp=11345,gnp_old=10285,local_name="Cote dIvoire",government_form="Republic",head_of_state= "Laurent Gbagbo"),
                User(code= "CMR",population=15085000,life_expectancy=54.8,gnp=9174,gnp_old=8596,local_name="Cameroun/Cameroon",government_form="Republic",head_of_state= "Paul Biya"),
                User(code= "COD",population=51654000,life_expectancy=48.8,gnp=6964,gnp_old=2474,local_name="Republique Democratique du Congo",government_form="Republic",head_of_state= "Joseph Kabila"),
                User(code= "COG",population=2943000,life_expectancy=47.4,gnp=2108,gnp_old=2287,local_name="Congo",government_form="Republic",head_of_state= "Denis Sassou-Nguesso"),
                User(code= "COK",population=20000,life_expectancy=71.1,gnp=100,gnp_old=0,local_name="The Cook Islands",government_form="Nonmetropolitan Territory of New Zealand",head_of_state= "Elisabeth II"),
                User(code= "COL",population=42321000,life_expectancy=70.3,gnp=102896,gnp_old=105116,local_name="Colombia",government_form="Republic",head_of_state= "Andres Pastrana Arango"),
                User(code= "COM",population=578000,life_expectancy=60,gnp=4401,gnp_old=4361,local_name="Komori/Comores",government_form="Republic",head_of_state= "Azali Assoumani"),
                User(code= "CPV",population=428000,life_expectancy=68.9,gnp=435,gnp_old=420,local_name="Cabo Verde",government_form="Republic",head_of_state= "Antonio Mascarenhas Monteiro"),
                User(code= "CRI",population=4023000,life_expectancy=75.8,gnp=10226,gnp_old=9757,local_name="Costa Rica",government_form="Republic",head_of_state= "Miguel angel RodrIguez EcheverrIa"),
                User(code= "CuB",population=11201000,life_expectancy=76.2,gnp=17843,gnp_old=18862,local_name="Cuba",government_form="Socialistic Republic",head_of_state= "Fidel Castro Ruz"),
                User(code= "CXR",population=2500,life_expectancy=0,gnp=0,gnp_old=0,local_name="Christmas Island",government_form="Territory of Australia",head_of_state= "Elisabeth II"),
                User(code= "CYM",population=38000,life_expectancy=78.9,gnp=1263,gnp_old=1186,local_name="Cayman Islands",government_form="Dependent Territory of the uK",head_of_state= "Elisabeth II"),
                User(code= "CYP",population=754700,life_expectancy=76.7,gnp=9333,gnp_old=8246,local_name="Kypros/Kibris",government_form="Republic",head_of_state= "Glafkos Klerides"),
                User(code= "CZE",population=10278100,life_expectancy=74.5,gnp=55017,gnp_old=52037,local_name="esko",government_form="Republic",head_of_state= "Vaclav Havel"),
                User(code= "DEu",population=82164700,life_expectancy=77.4,gnp=2133367,gnp_old=2102826,local_name="Deutschland",government_form="Federal Republic",head_of_state= "Johannes Rau"),
                User(code= "DJI",population=638000,life_expectancy=50.8,gnp=382,gnp_old=373,local_name="Djibouti/Jibuti",government_form="Republic",head_of_state= "Ismail Omar Guelleh"),
                User(code= "DMA",population=71000,life_expectancy=73.4,gnp=256,gnp_old=243,local_name="Dominica",government_form="Republic",head_of_state= "Vernon Shaw"),
                User(code= "DNK",population=5330000,life_expectancy=76.5,gnp=174099,gnp_old=169264,local_name="Danmark",government_form="Constitutional Monarchy",head_of_state= "Margrethe II"),
                User(code= "DOM",population=8495000,life_expectancy=73.2,gnp=15846,gnp_old=15076,local_name="Republica Dominicana",government_form="Republic",head_of_state= "Hipolito MejIa DomInguez"),
                User(code= "DZA",population=31471000,life_expectancy=69.7,gnp=49982,gnp_old=46966,local_name="Al-Jazair/Algerie",government_form="Republic",head_of_state= "Abdelaziz Bouteflika"),
                User(code= "ECu",population=12646000,life_expectancy=71.1,gnp=19770,gnp_old=19769,local_name="Ecuador",government_form="Republic",head_of_state= "Gustavo Noboa Bejarano"),
                User(code= "EGY",population=68470000,life_expectancy=63.3,gnp=82710,gnp_old=75617,local_name="Misr",government_form="Republic",head_of_state= "Hosni Mubarak"),
                User(code= "ERI",population=3850000,life_expectancy=55.8,gnp=650,gnp_old=755,local_name="Ertra",government_form="Republic",head_of_state= "Isayas Afewerki [Isaias Afwerki]"),
                User(code= "ESH",population=293000,life_expectancy=49.8,gnp=60,gnp_old=0,local_name="As-Sahrawiya",government_form="Occupied by Marocco",head_of_state= "Mohammed Abdel Aziz"),
                User(code= "ESP",population=39441700,life_expectancy=78.8,gnp=553233,gnp_old=532031,local_name="Espana",government_form="Constitutional Monarchy",head_of_state= "Juan Carlos I"),
                User(code= "EST",population=1439200,life_expectancy=69.5,gnp=5328,gnp_old=3371,local_name="Eesti",government_form="Republic",head_of_state= "Lennart Meri"),
                User(code= "ETH",population=62565000,life_expectancy=45.2,gnp=6353,gnp_old=6180,local_name="YeItyop iya",government_form="Republic",head_of_state= "Negasso Gidada"),
                User(code= "FIN",population=5171300,life_expectancy=77.4,gnp=121914,gnp_old=119833,local_name="Suomi",government_form="Republic",head_of_state= "Tarja Halonen"),
                User(code= "FJI",population=817000,life_expectancy=67.9,gnp=1536,gnp_old=2149,local_name="Fiji Islands",government_form="Republic",head_of_state= "Josefa Iloilo"),
                User(code= "FLK",population=2000,life_expectancy=0,gnp=0,gnp_old=0,local_name="Falkland Islands",government_form="Dependent Territory of the uK",head_of_state= "Elisabeth II"),
                User(code= "FRA",population=59225700,life_expectancy=78.8,gnp=1424285,gnp_old=1392448,local_name="France",government_form="Republic",head_of_state= "Jacques Chirac"),
                User(code= "FRO",population=43000,life_expectancy=78.4,gnp=0,gnp_old=0,local_name="Foroyar",government_form="Part of Denmark",head_of_state= "Margrethe II"),
                User(code= "FSM",population=119000,life_expectancy=68.6,gnp=212,gnp_old=0,local_name="Micronesia",government_form="Federal Republic",head_of_state= "Leo A. Falcam"),
                User(code= "GAB",population=1226000,life_expectancy=50.1,gnp=5493,gnp_old=5279,local_name="Le Gabon",government_form="Republic",head_of_state= "Omar Bongo"),
                User(code= "GBR",population=59623400,life_expectancy=77.7,gnp=1378330,gnp_old=1296830,local_name="united Kingdom",government_form="Constitutional Monarchy",head_of_state= "Elisabeth II"),
                User(code= "GEO",population=4968000,life_expectancy=64.5,gnp=6064,gnp_old=5924,local_name="Sakartvelo",government_form="Republic",head_of_state= "Eduard Sevardnadze"),
                User(code= "GHA",population=20212000,life_expectancy=57.4,gnp=7137,gnp_old=6884,local_name="Ghana",government_form="Republic",head_of_state="John Kufuor"),
                User(code= "GIB",population=25000,life_expectancy=79,gnp=258,gnp_old=0,local_name="Gibraltar",government_form="Dependent Territory of the uK",head_of_state= "Elisabeth II"),
                User(code= "GIN",population=7430000,life_expectancy=45.6,gnp=2352,gnp_old=2383,local_name="Guinee",government_form="Republic",head_of_state= "Lansana Conte"),
                User(code= "GLP",population=456000,life_expectancy=77,gnp=3501,gnp_old=0,local_name="Guadeloupe",government_form="Overseas Department of France",head_of_state= "Jacques Chirac"),
                User(code= "GMB",population=1305000,life_expectancy=53.2,gnp=320,gnp_old=325,local_name="The Gambia",government_form="Republic",head_of_state= "Yahya Jammeh"),
                User(code= "GNB",population=1213000,life_expectancy=49,gnp=293,gnp_old=272,local_name="Guine-Bissau",government_form="Republic",head_of_state= "Kumba Iala"),
                User(code= "GNQ",population=453000,life_expectancy=53.6,gnp=283,gnp_old=542,local_name="Guinea Ecuatorial",government_form="Republic",head_of_state= "Teodoro Obiang Nguema Mbasogo"),
                User(code= "GRC",population=10545700,life_expectancy=78.4,gnp=120724,gnp_old=119946,local_name="Ellada",government_form="Republic",head_of_state= "Kostis Stefanopoulos"),
                User(code= "GRD",population=94000,life_expectancy=64.5,gnp=318,gnp_old=0,local_name="Grenada",government_form="Constitutional Monarchy",head_of_state= "Elisabeth II"),
                User(code= "GRL",population=56000,life_expectancy=68.1,gnp=0,gnp_old=0,local_name="Kalaallit Nunaat/Gronland",government_form="Part of Denmark",head_of_state= "Margrethe II"),
                User(code= "GTM",population=11385000,life_expectancy=66.2,gnp=19008,gnp_old=17797,local_name="Guatemala",government_form="Republic",head_of_state= "Alfonso Portillo Cabrera"),
                User(code= "GuF",population=181000,life_expectancy=76.1,gnp=681,gnp_old=0,local_name="Guyane francaise",government_form="Overseas Department of France",head_of_state= "Jacques Chirac"),
                User(code= "GuM",population=168000,life_expectancy=77.8,gnp=1197,gnp_old=1136,local_name="Guam",government_form="uS Territory",head_of_state= "George W. Bush"),
                User(code= "GuY",population=861000,life_expectancy=64,gnp=722,gnp_old=743,local_name="Guyana",government_form="Republic",head_of_state= "Bharrat Jagdeo"),
                User(code= "HKG",population=6782000,life_expectancy=79.5,gnp=166448,gnp_old=173610,local_name="Xianggang/Hong Kong",government_form="Special Administrative Region of China",head_of_state= "Jiang Zemin"),
                User(code= "HMD",population=0,life_expectancy=0,gnp=0,gnp_old=0,local_name="Heard and McDonald Islands",government_form="Territory of Australia",head_of_state= "Elisabeth II",capital="NULL",code2= "HM"),
                User(code= "HND",population=6485000,life_expectancy=69.9,gnp=5333,gnp_old=4697,local_name="Honduras",government_form="Republic",head_of_state= "Carlos Roberto Flores Facusse"),
                User(code= "HRV",population=4473000,life_expectancy=73.7,gnp=20208,gnp_old=19300,local_name="Hrvatska",government_form="Republic",head_of_state= "Stipe Mesic"),
                User(code= "HTI",population=8222000,life_expectancy=49.2,gnp=3459,gnp_old=3107,local_name="Haiti/Dayti",government_form="Republic",head_of_state= "Jean-Bertrand Aristide"),
                User(code= "HuN",population=10043200,life_expectancy=71.4,gnp=48267,gnp_old=45914,local_name="Magyarorszag",government_form="Republic",head_of_state= "Ferenc Madl"),
                User(code= "IDN",population=212107000,life_expectancy=68,gnp=84982,gnp_old=215002,local_name="Indonesia",government_form="Republic",head_of_state= "Abdurrahman Wahid"),
                User(code= "IND",population=1013662000,life_expectancy=62.5,gnp=447114,gnp_old=430572,local_name="Bharat/India",government_form="Federal Republic",head_of_state= "Kocheril Raman Narayanan"),
                User(code= "IOT",population=0,life_expectancy=0,gnp=0,gnp_old=0,local_name="British Indian Ocean Territory",government_form="Dependent Territory of the uK",head_of_state= "Elisabeth II"),
                User(code= "IRL",population=3775100,life_expectancy=76.8,gnp=75921,gnp_old=73132,local_name="Ireland/eire",government_form="Republic",head_of_state= "Mary McAleese"),
                User(code= "IRN",population=67702000,life_expectancy=69.7,gnp=195746,gnp_old=160151,local_name="Iran",government_form="Islamic Republic",head_of_state= "Ali Mohammad Khatami-Ardakani"),
                User(code= "IRQ",population=23115000,life_expectancy=66.5,gnp=11500,gnp_old=0,local_name="Al- Iraq",government_form="Republic",head_of_state= "Saddam Hussein al-Takriti"),
                User(code= "ISL",population=279000,life_expectancy=79.4,gnp=8255,gnp_old=7474,local_name="Island",government_form="Republic",head_of_state= "olafur Ragnar GrImsson"),
                User(code= "ISR",population=6217000,life_expectancy=78.6,gnp=97477,gnp_old=98577,local_name="Yisrael/Israil",government_form="Republic",head_of_state= "Moshe Katzav"),
                User(code= "ITA",population=57680000,life_expectancy=79,gnp=1161755,gnp_old=1145372,local_name="Italia",government_form="Republic",head_of_state= "Carlo Azeglio Ciampi"),
                User(code= "JAM",population=2583000,life_expectancy=75.2,gnp=6871,gnp_old=6722,local_name="Jamaica",government_form="Constitutional Monarchy",head_of_state= "Elisabeth II"),
                User(code= "JOR",population=5083000,life_expectancy=77.4,gnp=7526,gnp_old=7051,local_name="Al-urdunn",government_form="Constitutional Monarchy",head_of_state= "Abdullah II"),
                User(code= "JPN",population=126714000,life_expectancy=80.7,gnp=3787042,gnp_old=4192638,local_name="Nihon/Nippon",government_form="Constitutional Monarchy",head_of_state= "Akihito"),
                User(code= "KAZ",population=16223000,life_expectancy=63.2,gnp=24375,gnp_old=23383,local_name="Qazaqstan",government_form="Republic",head_of_state= "Nursultan Nazarbajev"),
                User(code= "KEN",population=30080000,life_expectancy=48,gnp=9217,gnp_old=10241,local_name="Kenya",government_form="Republic",head_of_state="Daniel arap Moi"),
                User(code= "KGZ",population=4699000,life_expectancy=63.4,gnp=1626,gnp_old=1767,local_name="Kyrgyzstan",government_form="Republic",head_of_state= "Askar Akajev"),
                User(code= "KHM",population=11168000,life_expectancy=56.5,gnp=5121,gnp_old=5670,local_name="Kampuchea",government_form="Constitutional Monarchy",head_of_state= "Norodom Sihanouk"),
                User(code= "KIR",population=83000,life_expectancy=59.8,gnp=40.7,gnp_old=0,local_name="Kiribati",government_form="Republic",head_of_state= "Teburoro Tito"),
                User(code= "KNA",population=38000,life_expectancy=70.7,gnp=299,gnp_old=0,local_name="Saint Kitts and Nevis",government_form="Constitutional Monarchy",head_of_state= "Elisabeth II"),
                User(code= "KOR",population=46844000,life_expectancy=74.4,gnp=320749,gnp_old=442544,local_name="Taehan Minguk (Namhan)",government_form="Republic",head_of_state= "Kim Dae-jung"),
                User(code= "KWT",population=1972000,life_expectancy=76.1,gnp=27037,gnp_old=30373,local_name="Al-Kuwayt",government_form="Constitutional Monarchy (Emirate)",head_of_state= "Jabir al-Ahmad al-Jabir al-Sabah"),
                User(code= "LAO",population=5433000,life_expectancy=53.1,gnp=1292,gnp_old=1746,local_name="Lao",government_form="Republic",head_of_state= "Khamtay Siphandone"),
                User(code= "LBN",population=3282000,life_expectancy=71.3,gnp=17121,gnp_old=15129,local_name="Lubnan",government_form="Republic",head_of_state= "emile Lahoud"),
                User(code= "LBR",population=3154000,life_expectancy=51,gnp=2012,gnp_old=0,local_name="Liberia",government_form="Republic",head_of_state= "Charles Taylor"),
                User(code= "LBY",population=5605000,life_expectancy=75.5,gnp=44806,gnp_old=40562,local_name="Libiya",government_form="Socialistic State",head_of_state= "Muammar al-Qadhafi"),
                User(code= "LCA",population=154000,life_expectancy=72.3,gnp=571,gnp_old=0,local_name="Saint Lucia",government_form="Constitutional Monarchy",head_of_state= "Elisabeth II"),
                User(code= "LIE",population=32300,life_expectancy=78.8,gnp=1119,gnp_old=1084,local_name="Liechtenstein",government_form="Constitutional Monarchy",head_of_state= "Hans-Adam II"),
                User(code= "LKA",population=18827000,life_expectancy=71.8,gnp=15706,gnp_old=15091,local_name="Sri Lanka/Ilankai",government_form="Republic",head_of_state= "Chandrika Kumaratunga"),
                User(code= "LSO",population=2153000,life_expectancy=50.8,gnp=1061,gnp_old=1161,local_name="Lesotho",government_form="Constitutional Monarchy",head_of_state= "Letsie III"),
                User(code= "LTu",population=3698500,life_expectancy=69.1,gnp=10692,gnp_old=9585,local_name="Lietuva",government_form="Republic",head_of_state= "Valdas Adamkus"),
                User(code= "LuX",population=435700,life_expectancy=77.1,gnp=16321,gnp_old=15519,local_name="Luxembourg/Letzebuerg",government_form="Constitutional Monarchy",head_of_state= "Henri"),
                User(code= "LVA",population=2424200,life_expectancy=68.4,gnp=6398,gnp_old=5639,local_name="Latvija",government_form="Republic",head_of_state= "Vaira Vike-Freiberga"),
                User(code= "MAC",population=473000,life_expectancy=81.6,gnp=5749,gnp_old=5940,local_name="Macau/Aomen",government_form="Special Administrative Region of China",head_of_state= "Jiang Zemin"),
                User(code= "MAR",population=28351000,life_expectancy=69.1,gnp=36124,gnp_old=33514,local_name="Al-Maghrib",government_form="Constitutional Monarchy",head_of_state= "Mohammed VI"),
                User(code= "MCO",population=34000,life_expectancy=78.8,gnp=776,gnp_old=0,local_name="Monaco",government_form="Constitutional Monarchy",head_of_state= "Rainier III"),
                User(code= "MDA",population=4380000,life_expectancy=64.5,gnp=1579,gnp_old=1872,local_name="Moldova",government_form="Republic",head_of_state= "Vladimir Voronin"),
                User(code= "MDG",population=15942000,life_expectancy=55,gnp=3750,gnp_old=3545,local_name="Madagasikara/Madagascar",government_form="Federal Republic",head_of_state= "Didier Ratsiraka"),
                User(code= "MDV",population=286000,life_expectancy=62.2,gnp=199,gnp_old=0,local_name="Dhivehi Raajje/Maldives",government_form="Republic",head_of_state= "Maumoon Abdul Gayoom"),
                User(code= "MEX",population=98881000,life_expectancy=71.5,gnp=414972,gnp_old=401461,local_name="Mexico",government_form="Federal Republic",head_of_state= "Vicente Fox Quesada"),
                User(code= "MHL",population=64000,life_expectancy=65.5,gnp=97,gnp_old=0,local_name="Marshall Islands/Majol",government_form="Republic",head_of_state= "Kessai Note"),
                User(code= "MKD",population=2024000,life_expectancy=73.8,gnp=1694,gnp_old=1915,local_name="Makedonija",government_form="Republic",head_of_state= "Boris Trajkovski"),
                User(code= "MLI",population=11234000,life_expectancy=46.7,gnp=2642,gnp_old=2453,local_name="Mali",government_form="Republic",head_of_state= "Alpha Oumar Konare"),
                User(code= "MLT",population=380200,life_expectancy=77.9,gnp=3512,gnp_old=3338,local_name="Malta",government_form="Republic",head_of_state= "Guido de Marco"),
                User(code= "MMR",population=45611000,life_expectancy=54.9,gnp=180375,gnp_old=171028,local_name="Myanma Pye",government_form="Republic",head_of_state= "kenraali Than Shwe"),
                User(code= "MNG",population=2662000,life_expectancy=67.3,gnp=1043,gnp_old=933,local_name="Mongol uls",government_form="Republic",head_of_state= "Natsagiin Bagabandi"),
                User(code= "MNP",population=78000,life_expectancy=75.5,gnp=0,gnp_old=0,local_name="Northern Mariana Islands",government_form="Commonwealth of the uS",head_of_state= "George W. Bush"),
                User(code= "MOZ",population=19680000,life_expectancy=37.5,gnp=2891,gnp_old=2711,local_name="Mocambique",government_form="Republic",head_of_state= "JoaquIm A. Chissano"),
                User(code= "MRT",population=2670000,life_expectancy=50.8,gnp=998,gnp_old=1081,local_name="Muritaniya/Mauritanie",government_form="Republic",head_of_state= "Maaouiya Ould Sid Ahmad Taya"),
                User(code= "MSR",population=11000,life_expectancy=78,gnp=109,gnp_old=0,local_name="Montserrat",government_form="Dependent Territory of the uK",head_of_state= "Elisabeth II"),
                User(code= "MTQ",population=395000,life_expectancy=78.3,gnp=2731,gnp_old=2559,local_name="Martinique",government_form="Overseas Department of France",head_of_state= "Jacques Chirac"),
                User(code= "MuS",population=1158000,life_expectancy=71,gnp=4251,gnp_old=4186,local_name="Mauritius",government_form="Republic",head_of_state= "Cassam uteem"),
                User(code= "MWI",population=10925000,life_expectancy=37.6,gnp=1687,gnp_old=2527,local_name="Malawi",government_form="Republic",head_of_state= "Bakili Muluzi"),
                User(code= "MYS",population=22244000,life_expectancy=70.8,gnp=69213,gnp_old=97884,local_name="Malaysia",government_form="Constitutional Monarchy",head_of_state= " Federation,Salahuddin Abdul Aziz Shah Alhaj"),
                User(code= "MYT",population=149000,life_expectancy=59.5,gnp=0,gnp_old=0,local_name="Mayotte",government_form="Territorial Collectivity of France",head_of_state= "Jacques Chirac"),
                User(code= "NAM",population=1726000,life_expectancy=42.5,gnp=3101,gnp_old=3384,local_name="Namibia",government_form="Republic",head_of_state= "Sam Nujoma"),
                User(code= "NCL",population=214000,life_expectancy=72.8,gnp=3563,gnp_old=0,local_name="Nouvelle-Caledonie",government_form="Nonmetropolitan Territory of France",head_of_state= "Jacques Chirac"),
                User(code= "NER",population=10730000,life_expectancy=41.3,gnp=1706,gnp_old=1580,local_name="Niger",government_form="Republic",head_of_state= "Mamadou Tandja"),
                User(code= "NFK",population=2000,life_expectancy=0,gnp=0,gnp_old=0,local_name="Norfolk Island",government_form="Territory of Australia",head_of_state= "Elisabeth II"),
                User(code= "NGA",population=111506000,life_expectancy=51.6,gnp=65707,gnp_old=58623,local_name="Nigeria",government_form="Federal Republic",head_of_state= "Olusegun Obasanjo"),
                User(code= "NIC",population=5074000,life_expectancy=68.7,gnp=1988,gnp_old=2023,local_name="Nicaragua",government_form="Republic",head_of_state= "Arnoldo Aleman Lacayo"),
                User(code= "NIu",population=2000,life_expectancy=0,gnp=0,gnp_old=0,local_name="Niue",government_form="Nonmetropolitan Territory of New Zealand",head_of_state= "Elisabeth II"),
                User(code= "NLD",population=15864000,life_expectancy=78.3,gnp=371362,gnp_old=360478,local_name="Nederland",government_form="Constitutional Monarchy",head_of_state= "Willem-Alexander"),
                User(code= "NOR",population=4478500,life_expectancy=78.7,gnp=145895,gnp_old=153370,local_name="Norge",government_form="Constitutional Monarchy",head_of_state= "Harald V"),
                User(code= "NPL",population=23930000,life_expectancy=57.8,gnp=4768,gnp_old=4837,local_name="Nepal",government_form="Constitutional Monarchy",head_of_state= "Gyanendra Bir Bikram"),
                User(code= "NRu",population=12000,life_expectancy=60.8,gnp=197,gnp_old=0,local_name="Naoero/Nauru",government_form="Republic",head_of_state= "Bernard Dowiyogo"),
                User(code= "NZL",population=3862000,life_expectancy=77.8,gnp=54669,gnp_old=64960,local_name="New Zealand/Aotearoa",government_form="Constitutional Monarchy",head_of_state= "Elisabeth II"),
                User(code= "OMN",population=2542000,life_expectancy=71.8,gnp=16904,gnp_old=16153, local_name="uman",government_form="Monarchy (Sultanate)",head_of_state="Qabus ibn Sa id"),
                User(code= "PAK",population=156483000,life_expectancy=61.1,gnp=61289,gnp_old=58549,local_name="Pakistan",government_form="Republic",head_of_state= "Mohammad Rafiq Tarar"),
                User(code= "PAN",population=2856000,life_expectancy=75.5,gnp=9131,gnp_old=8700,local_name="Panama",government_form="Republic",head_of_state= "Mireya Elisa Moscoso RodrIguez"),
                User(code= "PCN",population=50,life_expectancy=0,gnp=0,gnp_old=0,local_name="Pitcairn",government_form="Dependent Territory of the uK",head_of_state= "Elisabeth II",capital=2912,code2= "PN"),
                User(code= "PER",population=25662000,life_expectancy=70,gnp=64140,gnp_old=65186,local_name="Peru/Piruw",government_form="Republic",head_of_state= "Valentin Paniagua Corazao",capital=2890,code2= "PE"),
                User(code= "PHL",population=75967000,life_expectancy=67.5,gnp=65107,gnp_old=82239,local_name="Pilipinas",government_form="Republic",head_of_state= "Gloria Macapagal-Arroyo",capital=766,code2= "PH"),
                User(code= "PLW",population=19000,life_expectancy=68.6,gnp=105,gnp_old=0,local_name="Belau/Palau",government_form="Republic",head_of_state= "Kuniwo Nakamura"),
                User(code= "PNG",population=4807000,life_expectancy=63.1,gnp=4988,gnp_old=6328,local_name="Papua New Guinea/Papua Niugini",government_form="Constitutional Monarchy",head_of_state= "Elisabeth II"),
                User(code= "POL",population=38653600,life_expectancy=73.2,gnp=151697,gnp_old=135636,local_name="Polska",government_form="Republic",head_of_state= "Aleksander Kwasniewski",capital=2928,code2= "PL"),
                User(code= "PRI",population=3869000,life_expectancy=75.6,gnp=34100,gnp_old=32100,local_name="Puerto Rico",government_form="Commonwealth of the uS",head_of_state= "George W. Bush"),
                User(code= "PRK",population=24039000,life_expectancy=70.7,gnp=5332,gnp_old=0,local_name="Choson Minjujuui In min Konghwaguk (Bukhan)",government_form="Socialistic Republic",head_of_state= "Kim Jong-il"),
                User(code= "PRT",population=9997600,life_expectancy=75.8,gnp=105954,gnp_old=102133,local_name="Portugal",government_form="Republic",head_of_state= "Jorge Sampaio"),
                User(code= "PRY",population=5496000,life_expectancy=73.7,gnp=8444,gnp_old=9555,local_name="Paraguay",government_form="Republic",head_of_state= "Luis angel Gonzalez Macchi"),
                User(code= "PSE",population=3101000,life_expectancy=71.4,gnp=4173,gnp_old=0,local_name="Filastin",government_form="Autonomous Area",head_of_state= "Yasser (Yasir) Arafat"),
                User(code= "PYF",population=235000,life_expectancy=74.8,gnp=818,gnp_old=781,local_name="Polynesie francaise",government_form="Nonmetropolitan Territory of France",head_of_state= "Jacques Chirac"),
                User(code= "QAT",population=599000,life_expectancy=72.4,gnp=9472,gnp_old=8920,local_name="Qatar",government_form="Monarchy",head_of_state= "Hamad ibn Khalifa al-Thani"),
                User(code= "REu",population=699000,life_expectancy=72.7,gnp=8287,gnp_old=7988,local_name="Reunion",government_form="Overseas Department of France",head_of_state= "Jacques Chirac"),
                User(code= "ROM",population=22455500,life_expectancy=69.9,gnp=38158,gnp_old=34843,local_name="Romania",government_form="Republic",head_of_state= "Ion Iliescu"),
                User(code= "RuS",population=146934000,life_expectancy=67.2,gnp=276608,gnp_old=442989,local_name="Rossija",government_form="Federal Republic",head_of_state= "Vladimir Putin"),
                User(code= "RWA",population=7733000,life_expectancy=39.3,gnp=2036,gnp_old=1863,local_name="Rwanda/urwanda",government_form="Republic",head_of_state= "Paul Kagame"),
                User(code= "SAu",population=21607000,life_expectancy=67.8,gnp=137635,gnp_old=146171,local_name="Al- Arabiya as-Sa udiya",government_form="Monarchy",head_of_state= "Fahd ibn Abdul-Aziz al-Sa ud"),
                User(code= "SDN",population=29490000,life_expectancy=56.6,gnp=10162,gnp_old=0,local_name="As-Sudan",government_form="Islamic Republic",head_of_state= "Omar Hassan Ahmad al-Bashir"),
                User(code= "SEN",population=9481000,life_expectancy=62.2,gnp=4787,gnp_old=4542,local_name="Senegal/Sounougal",government_form="Republic",head_of_state= "Abdoulaye Wade"),
                User(code= "SGP",population=3567000,life_expectancy=80.1,gnp=86503,gnp_old=96318,local_name="Singapore/Singapura/Xinjiapo/Singapur",government_form="Republic",head_of_state= "Sellapan Rama Nathan"),
                User(code= "SGS",population=0,life_expectancy=0,gnp=0,gnp_old=0,local_name="South Georgia and the South Sandwich Islands",government_form="Dependent Territory of the uK",head_of_state= "Dependent Territory of the uK,Elisabeth II"),
                User(code= "SHN",population=6000,life_expectancy=76.8,gnp=0,gnp_old=0,local_name="Saint Helena",government_form="Dependent Territory of the uK",head_of_state="Elisabeth II"),
                User(code= "SJM",population=3200,life_expectancy=0,gnp=0,gnp_old=0,local_name="Svalbard og Jan Mayen",government_form="Dependent Territory of Norway",head_of_state="Harald V"),
                User(code= "SLB",population=444000,life_expectancy=71.3,gnp=182,gnp_old=220,local_name="Solomon Islands",government_form="Constitutional Monarchy",head_of_state="Elisabeth II"),
                User(code= "SLE",population=4854000,life_expectancy=45.3,gnp=746,gnp_old=858,local_name="Sierra Leone",government_form="Republic",head_of_state="Ahmed Tejan Kabbah"),
                User(code= "SLV",population=6276000,life_expectancy=69.7,gnp=11863,gnp_old=11203,local_name="El Salvador",government_form="Republic",head_of_state="Francisco Guillermo Flores Perez"),
                User(code= "SMR",population=27000,life_expectancy=81.1,gnp=510,gnp_old=0,local_name="San Marino",government_form="Republic",head_of_state="NuLL",capital=3171,code2= "SM"),
                User(code= "SOM",population=10097000,life_expectancy=46.2,gnp=935,gnp_old=0,local_name="Soomaaliya",government_form="Republic",head_of_state="Abdiqassim Salad Hassan"),
                User(code= "SPM",population=7000,life_expectancy=77.6,gnp=0,gnp_old=0,local_name="Saint-Pierre-et-Miquelon",government_form="Territorial Collectivity of France",head_of_state="Jacques Chirac"),
                User(code= "STP",population=147000,life_expectancy=65.3,gnp=6,gnp_old=0,local_name="Sao Tome e PrIncipe",government_form="Republic",head_of_state="Miguel Trovoada"),
                User(code= "SuR",population=417000,life_expectancy=71.4,gnp=870,gnp_old=706,local_name="Suriname",government_form="Republic",head_of_state="Ronald Venetiaan"),
                User(code= "SVK",population=5398700,life_expectancy=73.7,gnp=20594,gnp_old=19452,local_name="Slovensko",government_form="Republic",head_of_state="Rudolf Schuster"),
                User(code= "SVN",population=1987800,life_expectancy=74.9,gnp=19756,gnp_old=18202,local_name="Slovenija",government_form="Republic",head_of_state="Milan Kucan"),
                User(code= "SWE",population=8861400,life_expectancy=79.6,gnp=226492,gnp_old=227757,local_name="Sverige",government_form="Constitutional Monarchy",head_of_state="Carl XVI Gustaf"),
                User(code= "SWZ",population=1008000,life_expectancy=40.4,gnp=1206,gnp_old=1312,local_name="kaNgwane",government_form="Monarchy",head_of_state="Mswati III"),
                User(code= "SYC",population=77000,life_expectancy=70.4,gnp=536,gnp_old=539,local_name="Sesel/Seychelles",government_form="Republic",head_of_state="France-Albert Rene"),
                User(code= "SYR",population=16125000,life_expectancy=68.5,gnp=65984,gnp_old=64926,local_name="Suriya",government_form="Republic",head_of_state="Bashar al-Assad"),
                User(code= "TCA",population=17000,life_expectancy=73.3,gnp=96,gnp_old=0,local_name="The Turks and Caicos Islands",government_form="Dependent Territory of the uK",head_of_state="Elisabeth II"),
                User(code= "TCD",population=7651000,life_expectancy=50.5,gnp=1208,gnp_old=1102,local_name="Tchad/Tshad",government_form="Republic",head_of_state="Idriss Deby"),
                User(code= "TGO",population=4629000,life_expectancy=54.7,gnp=1449,gnp_old=1400,local_name="Togo",government_form="Republic",head_of_state="Gnassingbe Eyadema"),
                User(code= "THA",population=61399000,life_expectancy=68.6,gnp=116416,gnp_old=153907,local_name="Prathet Thai",government_form="Constitutional Monarchy",head_of_state="Bhumibol Adulyadej"),
                User(code= "TJK",population=6188000,life_expectancy=64.1,gnp=1990,gnp_old=1056,local_name="Tocikiston",government_form="Republic",head_of_state="Emomali Rahmonov"),
                User(code= "TKL",population=2000,life_expectancy=0,gnp=0,gnp_old=0,local_name="Tokelau",government_form="Nonmetropolitan Territory of New Zealand",head_of_state="Elisabeth II"),
                User(code= "TKM",population=4459000,life_expectancy=60.9,gnp=4397,gnp_old=2000,local_name="Turkmenostan",government_form="Republic",head_of_state="Saparmurad Nijazov"),
                User(code= "TMP",population=885000,life_expectancy=46,gnp=0,gnp_old=0,local_name="Timor Timur",government_form="Administrated by the uN",head_of_state="Jose Alexandre Gusmao"),
                User(code= "TON",population=99000,life_expectancy=67.9,gnp=146,gnp_old=170,local_name="Tonga",government_form="Monarchy",head_of_state="Taufa ahau Tupou IV"),
                User(code= "TTO",population=1295000,life_expectancy=68,gnp=6232,gnp_old=5867,local_name="Trinidad and Tobago",government_form="Republic",head_of_state="Arthur N. R. Robinson"),
                User(code= "TuN",population=9586000,life_expectancy=73.7,gnp=20026,gnp_old=18898,local_name="Tunis/Tunisie",government_form="Republic",head_of_state="Zine al-Abidine Ben Ali"),
                User(code= "TuR",population=66591000,life_expectancy=71,gnp=210721,gnp_old=189122,local_name="Turkiye",government_form="Republic",head_of_state="Ahmet Necdet Sezer"),
                User(code= "TuV",population=12000,life_expectancy=66.3,gnp=6,gnp_old=0,local_name="Tuvalu",government_form="Constitutional Monarchy",head_of_state="Elisabeth II"),
                User(code= "TWN",population=22256000,life_expectancy=76.4,gnp=256254,gnp_old=263451,local_name="Tai-wan",government_form="Republic",head_of_state="Chen Shui-bian"),
                User(code= "TZA",population=33517000,life_expectancy=52.3,gnp=8005,gnp_old=7388,local_name="Tanzania",government_form="Republic",head_of_state="Benjamin William Mkapa"),
                User(code= "uGA",population=21778000,life_expectancy=42.9,gnp=6313,gnp_old=6887,local_name="uganda",government_form="Republic",head_of_state="Yoweri Museveni"),
                User(code= "uKR",population=50456000,life_expectancy=66,gnp=42168,gnp_old=49677,local_name="ukrajina",government_form="Republic",head_of_state="Leonid KutSma"),
                User(code= "uMI",population=0,life_expectancy=0,gnp=0,gnp_old=0,local_name="united States Minor Outlying Islands",government_form="Dependent Territory of the uS",head_of_state="George W. Bush"),
                User(code= "uRY",population=3337000,life_expectancy=75.2,gnp=20831,gnp_old=19967,local_name="uruguay",government_form="Republic",head_of_state="Jorge Batlle Ibanez"),
                User(code= "uSA",population=278357000,life_expectancy=77.1,gnp=8510700,gnp_old=8110900,local_name="united States",government_form="Federal Republic",head_of_state="George W. Bush"),
                User(code= "uZB",population=24318000,life_expectancy=63.7,gnp=14194,gnp_old=21300,local_name="uzbekiston",government_form="Republic",head_of_state="Islam Karimov"),
                User(code= "VAT",population=1000,life_expectancy=0,gnp=9,gnp_old=0,local_name="Santa Sede/Citta del Vaticano",government_form="Independent Church State",head_of_state="Johannes Paavali II"),
                User(code= "VCT",population=114000,life_expectancy=72.3,gnp=285,gnp_old=0,local_name="Saint Vincent and the Grenadines",government_form="Constitutional Monarchy",head_of_state="Elisabeth II"),
                User(code= "VEN",population=24170000,life_expectancy=73.1,gnp=95023,gnp_old=88434,local_name="Venezuela",government_form="Federal Republic",head_of_state="Hugo Chavez FrIas"),
                User(code= "VGB",population=21000,life_expectancy=75.4,gnp=612,gnp_old=573,local_name="British Virgin Islands",government_form="Dependent Territory of the uK",head_of_state="Elisabeth II"),
                User(code= "VIR",population=93000,life_expectancy=78.1,gnp=0,gnp_old=0,local_name="Virgin Islands of the united States",government_form="uS Territory",head_of_state="George W. Bush"),
                User(code= "VNM",population=79832000,life_expectancy=69.3,gnp=21929,gnp_old=22834,local_name="Viet Nam",government_form="Socialistic Republic",head_of_state="Tran Duc Luong"),
                User(code= "VuT",population=190000,life_expectancy=60.6,gnp=261,gnp_old=246,local_name="Vanuatu",government_form="Republic",head_of_state="John Bani"),
                User(code= "WLF",population=15000,life_expectancy=0,gnp=0,gnp_old=0,local_name="Wallis-et-Futuna",government_form="Nonmetropolitan Territory of France",head_of_state="Jacques Chirac"),
                User(code= "WSM",population=180000,life_expectancy=69.2,gnp=141,gnp_old=157,local_name="Samoa",government_form="Parlementary Monarchy",head_of_state="Malietoa Tanumafili II"),
                User(code= "YEM",population=18112000,life_expectancy=59.8,gnp=6041,gnp_old=5729,local_name="Al-Yaman",government_form="Republic",head_of_state="Ali Abdallah Salih"),
                User(code= "YuG",population=10640000,life_expectancy=72.4,gnp=17000,gnp_old=00,local_name="Jugoslavija",government_form="Federal Republic",head_of_state="Vojislav KoStunica"),
                User(code= "ZAF",population=40377000,life_expectancy=51.1,gnp=116729,gnp_old=129092,local_name="South Africa",government_form="Republic",head_of_state="Thabo Mbeki"),
                User(code= "ZMB",population=9169000,life_expectancy=37.2,gnp=3377,gnp_old=3922,local_name="Zambia",government_form="Republic",head_of_state="Frederick Chiluba"),
                User(code="ZWE",population=11669000,life_expectancy=37.8,gnp=5951,gnp_old=8670,local_name="Zimbabwe",government_form="Republic",head_of_state="Robert G. Mugabe")]



@router.get("/continent/region/country/")
async def continent():
        return (users_list)

 
#***Post
@router.post("/continent/region/country/", response_model=User, status_code=201)

async def routerPais(user:User):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(users_list):
        if saved_user.code == user.code:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           raise HTTPException(status_code=204,detail="El país ya existe")
    else:
        users_list.append(user)
        return user
    
    #http://127.0.0.1:8000/usersclass/
   
   
    #***Put
@router.put("/continent/region/country/", response_model=User, status_code=status.HTTP_200_OK)
async def routerPais(user:User):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(users_list):
        if saved_user.code == user.code:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           users_list[index] = user  #accedemos al indice de la lista que hemos encontrado y actualizamos con el nuevo usuario
           found=True
           
    if not found:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail="No se ha actualizado el país")
    else:
        raise HTTPException(status_code= status.HTTP_302_FOUND,detail="el país ya se encuentra agregado")
        #return user
    
    #http://127.0.0.1:8000/usersclass/
    
    
        #***Delete
@router.delete("/continent/region/country/{code}", response_model=User, status_code=status.HTTP_200_OK)
async def usersclassRouter(user:User):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(users_list):
        if saved_user.code == user.code : #Si el Id del usuario guardado es igual al Id del usuario nuevo
           del users_list[index]  #Eliminamos al indice de la lista que hemos encontrado 
           found=True
           raise HTTPException(status_code= status.HTTP_202_ACCEPTED,detail="Se ha eliminado el país")
       
    if not found:
      raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail="No se ha eliminado el país")


