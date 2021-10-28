myData = [
[50.065703299999996,19.918958667058632, 'AGH University of Science and Technology, Akademicka, Czarna Wieś, Krowodrza, Krakow, Lesser Poland Voivodeship, 30-054, Poland'],
[52.2394966,21.015693129786936, 'Academy of Fine Arts in Warsaw, 5, Krakowskie Przedmieście, Centrum, Śródmieście Północne, Śródmieście, Warsaw, Masovian Voivodeship, 00-068, Poland'],
[30.042767599999998,31.236599299797163, 'American University in Cairo, Al Qasr Al Eini Street, El Dawadin, Bab al Luq, Cairo, Cairo Governorate, 11519, Egypt'],
[33.42152185,-111.93316158417922, 'Arizona State University, East Apache Boulevard, Tempe Junction, Tempe, Maricopa County, Arizona, 85287, United States'],
[37.9425172,23.8706149, 'Athens Information Technology, Μαρκόπουλου, Karellas, Municipality of Kropia, Regional Unit of East Attica, Attica, 19400, Greece'],
[17.547231,78.5725623, 'bits pilani, Lovers Lane, Kapra mandal, Medchal–Malkajgiri, Telangana, 500087, India'],
[6.89041435,3.722404914587505, 'Babcock University, Benin-Sagamu Expressway, Ilishan, Ikenne, Ogun, Nigeria'],
[25.2662887,82.9927969, 'Banaras Hindu University, Semi Circle Road 2, Karbirdas Colony, Varanasi, Uttar Pradesh, 221005, India'],
[12.944172049999999,77.5091485894286, 'Bangalore University, Kenchenahalli Main Road, Pantarapalya, Rajarajeshwari Nagar, Rajarajeshwari Nagar Zone, Bengaluru, Bangalore South, Bangalore Urban, Karnataka, 560111, India'],
[31.55043405,-97.1102905567766, 'Baylor University, 1301, South University Parks Drive, Waco, McLennan County, Texas, 76706, United States'],
[39.96014155,116.35970438026524, 'Beijing Normal University (BNU), 19, 新街口外大街, Haidian District, Beijing, 100875, China'],
[53.83806745,27.476155257195504, 'Belarusian State University, Kastrychnitski District, Minsk, Belarus'],
[44.8061452,20.47476551568353, 'Svetozar Marković University Library, 71, King Alexander Boulevard, Vracar, Vracar Urban Municipality, Belgrade, City of Belgrade, Central Serbia, 11000, Serbia'],
[42.5009819,-89.0157777411969, 'Beloit College, Emerson Street, Beloit, Rock County, Wisconsin, 53511, United States'],
[32.9620656,35.49778161569644, 'Faculty of Medicine in the Galilee, 8, Henrietta Szold, Shikma, Zefat, Safed Subdistrict, North District, 1311502, Israel'],
[42.35031725,-71.10122725124097, 'Boston University, Brighton Avenue, North Brighton, Allston, Boston, Suffolk County, Massachusetts, 02134, United States'],
[35.3074623,-120.66464833678835, 'California Polytechnic State University, North Santa Rosa Street, San Luis Obispo, San Luis Obispo County, California, 93407-0283, United States'],
[34.18191745,-117.32174391836504, 'California State University, San Bernardino, 5500, University Parkway, Serrano Village, San Bernardino, San Bernardino County, California, 92407, United States'],
[51.5213399,-0.17489614009105153, 'City of Westminster College, 25, Paddington Green, Paddington, Westminster, London, Greater London, England, W2 1NB, United Kingdom'],
[40.8079488,-73.96179735692117, 'Columbia University, Reunion Plaza, Morningside Heights, Manhattan Community Board 9, Manhattan, New York County, New York, United States'],
[52.070415350000005,-0.6287932053178253, 'Cranfield University, Moulsoe Road, Cranfield, Central Bedfordshire, East of England, England, MK43 0TR, United Kingdom'],
[50.0763407,14.417571110089021, 'Czech Technical University in Prague, Na Zderaze, New Town, Prague, 11121, Czechia'],
[50.3514839,-3.583844, 'Dartmouth, South Hams, Devon, South West England, England, TQ6 9ES, United Kingdom'],
[37.31770065,-122.04455706238198, 'De Anza College, 21250, Stevens Creek Boulevard, Cupertino, Santa Clara County, California, 95014, United States'],
[48.4348076,35.03780903602534, 'Dnipro National University, Олександра Рейнгарда вулиця, Dnipro Municipality, Sobornyi district, Dnipro, Дніпровський район, Dnipropetrovsk Oblast, 49600, Ukraine'],
[38.4794593,-94.6085663, 'Drexel, Cass County, Missouri, United States'],
[30.2852198,-97.73389272663796, 'University of Texas at Austin, 1, Austin, Travis County, Texas, 78712, United States'],
[36.00015569999999,-78.94422972195878, 'Duke University, 15th Street, 9th Street District, Durham, Durham County, North Carolina, 27705, United States'],
[45.7859567,4.763955690376829, 'EM Lyon Business School - Lyon-Écully Campus, Avenue Guy de Collongue, Écully, Lyon, Métropole de Lyon, Departemental constituency of Rhône, Auvergne-Rhône-Alpes, Metropolitan France, 69130, France'],
[57.0388522,34.9546925, 'Paris, 6, Кузнечная улица, Torzhok, Tver Oblast, Central Federal District, 172002, Russia'],
[36.10652745,-79.50282572055133, 'Elon University, University Drive, Glen Raven, Elon, Alamance County, North Carolina, 27216, United States'],
[55.48841555,8.447026487581917, 'Erhvervsakademi Sydvest, Spangsbjerg Kirkevej, Spangsbjerg, Esbjerg, Esbjerg Municipality, Region of Southern Denmark, 6700, Denmark'],
[-2.1848338,-79.8768655, 'ESCUELA SUPERIOR POLITECNICA DEL LITORAL, Simón Bolívar, Rocafuerte, Carbo-Concepción, Guayaquil, 090313, Ecuador'],
[51.24812155,6.79124852501046, 'Düsseldorf University of Applied Science, 156, Münsterstraße, Derendorf, Stadtbezirk 1, Dusseldorf, North Rhine-Westphalia, 40476, Germany'],
[47.72360745,13.086718915696402, 'Fachhochschule Salzburg, Urstein Süd, Puch bei Hallein, Bezirk Hallein, Salzburg, 5412, Austria'],
[45.2464728,19.851704147473647, 'Faculty of Technical Sciences, Трг Доситеја Обрадовића, Liman, Нови Сад, Novi Sad, Novi Sad City, South Backa Administrative District, Vojvodina, 21101, Serbia'],
[40.74894575,-73.43165564683342, 'Nold Atletic Complex, Dr Frank A Cipriani Dr, Suffolk County, New York, 11735, United States'],
[26.119403650000002,-80.14169191096471, 'Florida Atlantic University, 111, East Las Olas Boulevard, Fort Lauderdale, Broward County, Florida, 33301, United States'],
[43.2125814,-71.4947929, 'Franklin Pierce College, Chenell Drive, Concord, Merrimack County, New Hampshire, 03301, United States'],
[26.153410700000002,91.6657647108439, 'Gauhati University, Gopinath Bardoloi Nagar, NH17, Guwahati, Kamrup Metropolitan, 781014, India'],
[38.83133325,-77.30798838879116, 'George Mason University, Cleveland Street, Maple Hills, Halemhurst, Fairfax, Fairfax (city), Virginia, 22030, United States'],
[38.8972714,-77.01291794240097, 'Georgetown University Law Center, New Jersey Avenue Northwest, Washington, Washington, D.C., 20001, United States'],
[33.754761349999995,-84.38819218475689, 'Georgia State University, 33, Gilmer Street Southeast, Five Points, Atlanta, Fulton County, Georgia, 30303, United States'],
[48.5956451,4.2319159, 'Grandville, Troyes, Aube, Grand Est, Metropolitan France, 10700, France'],
[59.85758525,17.629521017894447, 'Universitetshuset, 3, Biskopsgatan, Fjärdingen, Uppsala, Uppsala kommun, Uppsala County, 753 10, Sweden'],
[21.0042964,105.84372341443063, 'Hanoi University of Science and Technology, 1, Đại Cồ Việt, Phường Bách Khoa, Hai Ba Trung District, Hanoi, 10999, Vietnam'],
[39.13757895,-84.52132079870667, 'Hebrew Union College, Clifton Avenue, Fairview, Clifton Heights–University Heights–Fairview, Cincinnati, Hamilton County, Ohio, 45220-3027, United States'],
[17.4454957,78.34854697544472, 'International Institute of Information Technology, Hyderabad, ISB Road, Anjaiah Nagar, Ward 105 Gachibowli, Hyderabad, Serilingampalle mandal, Rangareddy, Telangana, 500032, India'],
[26.5119015,80.2458787, 'IIT Kanpur, NH34, Kanpur, Kanpur Nagar, Uttar Pradesh, 208012, India'],
[29.3063535,120.0702682, 'Yiwu, Jinhua, Zhejiang, China'],
[45.43185925,12.31706562464495, 'Iuav - Sede Magazzino 6, Fossa Capara, Dorsoduro, Venezia-Murano-Burano, Mestre, Venice, Venezia, Veneto, 30170, Italy'],
[41.8361963,-87.62655912742909, 'Illinois Institute of Technology, East 30th Street, Douglas, Chicago, Cook County, Illinois, 60616, United States'],
[28.5444176,77.1893001, 'Indian Institute Of Technology, IIT Delhi Main Road, Mehrauli Tehsil, South Delhi, Delhi, 110 067, India'],
[22.31442745,87.3104488017961, 'Indian Institute of Technology Kharagpur, Residential, Kharagpur, Kharagpur-I, Paschim Medinipur, West Bengal, 721302, India'],
[39.170121800000004,-86.52609779880657, 'William H. Mathers Museum of World Cultures, 601, East 8th Street, Bloomington, Monroe County, Indiana, 47408, United States'],
[39.170121800000004,-86.52609779880657, 'William H. Mathers Museum of World Cultures, 601, East 8th Street, Bloomington, Monroe County, Indiana, 47408, United States'],
[14.7168914,-17.4556123, 'Institut Supérieur de Technologies, Rue LIB-223, Liberté, Dakar, 00000, Senegal'],
[18.48770705,-69.96213326009398, 'Instituto Tecnológico de Santo Domingo, Calle Yanquimur, Constelacion, Los Jardines, Santo Domingo, 10602, Dominican Republic'],
[17.4454957,78.34854697544472, 'International Institute of Information Technology, Hyderabad, ISB Road, Anjaiah Nagar, Ward 105 Gachibowli, Hyderabad, Serilingampalle mandal, Rangareddy, Telangana, 500032, India'],
[52.2807365,104.28305934551582, 'Baikal University, 11 к2, улица Ленина, Irkutsk, Правобережный административный округ, Irkutsk, городской округ Иркутск, Irkutsk Oblast, Siberian Federal District, 664003, Russia'],
[22.5611537,88.4131019353334, 'Jadavpur University, Chingrighata Flyover, Basani Devi Colony, Kolkata, Bhangar - II, South 24 Parganas, West Bengal, 700098, India'],
[17.49306445,78.39140794729656, 'Jawaharlal Nehru Technological University, Hyderabad, Shortcut from CRC to temple, Vasanth Nagar, Ward 114 KPHB Colony, Hyderabad, Kukatpally mandal, Medchal–Malkajgiri, Telangana, 500071, India'],
[28.540166749999997,77.16456005394733, 'Jawaharlal Nehru University, Bhagwan Mahavir Marg, Vasant Kunj, Vasant Vihar Tehsil, New Delhi, Delhi, 110067, India'],
[32.49566485,35.99160717192832, 'Jordan University of Science and Technology, Betra St, Irbid, Jordan'],
[46.6228162,14.3079604, 'Klagenfurt, Carinthia, Austria'],
[3.1526589,101.7022205, 'Federal Territory of Kuala Lumpur, Malaysia'],
[42.2907304,-85.59937672047477, 'Kalamazoo College, West South Street, Kalamazoo, Kalamazoo County, Michigan, 49007, United States'],
[54.9037711,23.9596397, 'Gymnasium of Kaunas University of Technology, 65, Studentų g., Gričiupis, Gričiupio seniūnija, Kaunas, Kauno miesto savivaldybė, Kaunas County, 51368, Lithuania'],
[54.898778449999995,23.912636540834075, 'Kaunas University of Technology, 73, K. Donelaičio g., New Town, Centro seniūnija, Kaunas, Kauno miesto savivaldybė, Kaunas County, 44029, Lithuania'],
[55.79069515,49.12192908363142, 'Kazan Federal University, 18, Kremlyovskaya Street, Вахитовский район, Kazan, Tatarstan, Volga Federal District, 420008, Russia'],
[41.1443525,-81.33982832845717, 'Kent State University, Health Center Drive, Kent, Portage County, Ohio, 44242-0001, United States'],
[13.651800049999999,100.4944222992759, 'King Mongkuts University of Technology, Thonburi, Phutthabucha Road, Bang Mot Subdistrict, Thung Khru District, Bangkok, 10140, Thailand'],
[50.44922055,30.45773968731175, 'National Technical University of Ukraine “Igor Sikorsky Kyiv Polytechnic Institute”, Polovyi Lane, Казенні дачі, Solomianskyi district, Kyiv, Київська міська громада, 03057, Ukraine'],
[46.4666416,-80.9738711, 'Laurentian University, University Road, Greater Sudbury, Sudbury District, Northeastern Ontario, Ontario, P3E 2C6, Canada'],
[10.4763211,-66.8902923, 'Lisandro Alvarado, Ciudad Universitaria de Caracas, Caracas, Parroquia San Pedro, Municipio Libertador, Capital District, 1040, Venezuela'],
[49.704941,24.571054, 'Univ, Peremyshliany Urban Hromada, Lviv Raion, Lviv Oblast, 81216, Ukraine'],
[45.66381885,-111.07930568352012, 'Montana State University, West College Street, Bozeman, Gallatin County, Montana, 59715, United States'],
[13.0116753,80.24000774361667, 'Madras University, Ward 171, Zone 13 Adyar, Chennai, Chennai District, Tamil Nadu, India'],
[34.30368705,48.850726699999996, 'Artificial turf Azad University, کوچه نادری, ازناو, Kuh Sardeh, Central District, Malayer County, Hamadan Province, 6571614616, Iran'],
[39.416095049999996,-81.44842058753335, 'Marietta College, Foster Lane, Marietta Historic District, Harmar, Marietta, Washington County, Ohio, 45750, United States'],
[24.4348507,54.6167989, 'Masdar Institute, Pedestrian Zone Masdar, Masdar City, Abu Dhabi, Abu Dhabi Emirate, 46450, United Arab Emirates'],
[44.8000034,20.4848369, 'Faculty of Mathematics, 5, Vatroslava Jagica, Црвени крст, Vracar, Vracar Urban Municipality, Belgrade, City of Belgrade, Central Serbia, 11000, Serbia'],
[42.7192043,-84.47791987346606, 'Michigan State University, Short Street, Bailey, East Lansing, Ingham County, Michigan, 48823, United States'],
[39.875496749999996,32.78553505584672, 'Middle East Technical University, 1, 1580. Sokak, Çiğdem Mahallesi, Ankara, Çankaya, Ankara, Central Anatolia Region, 06800, Turkey'],
[37.95289395,-91.77385800554143, 'Missouri University of Science and Technology, North Walker Avenue, Rolla, Phelps County, Missouri, 65409, United States'],
[-26.0840525,27.87762537852294, 'Monash, Monash Boulevard, Johannesburg Ward 97, Roodepoort, City of Johannesburg Metropolitan Municipality, Gauteng, South Africa'],
[-37.783974549999996,144.95867432609305, 'Monash University, Mile Lane, Parkville, City of Melbourne, Victoria, 3052, Australia'],
[55.60460415,38.10651526217077, 'Moscow Institute of Physics and Technology, 16, Str. Gagarina, Gagarina, Zhukovsky, Moscow Oblast, Central Federal District, 140187, Russia'],
[55.7036683,37.5320492, '1, Moscow State University, Ramenki District, Moscow, Central Federal District, 119991, Russia'],
[22.2501589,84.90668556980866, 'NIT Rourkela, Gulmohar street, Rourkela, Sundargarh, Odisha, 769042, India'],
[40.72925325,-73.99625393609625, 'New York University, Waverly Place, Greenwich Village, Manhattan Community Board 2, Manhattan, New York County, New York, 10003, United States'],
[51.7520849,-1.2516646208312259, 'University College, Logic Lane, St Ebbes, City Centre, Oxford, Oxfordshire, South East, England, OX1 4EX, United Kingdom'],
[1.3484104000000001,103.68293320728537, 'Nanyang Technological University, Nanyang Green, Western Water Catchment, Southwest, 639667, Singapore'],
[31.39571075,75.5357675438753, 'National Institute of Technology, GT road, Jalandhar II Tahsil, Jalandhar, Punjab, 144044, India'],
[25.01682835,121.53846923577314, 'National Taiwan University, 1, Section 4, Roosevelt Road, Wencheng Village, Zhongzheng District, Gongguan, Taipei, 10617, Taiwan'],
[-12.02037945,-77.04816939032196, 'National University of Engineering, 18 de Enero, San Martín de Porres, Province of Lima, Lima, 15028, Peru'],
[41.774365450000005,-88.14274924248255, 'North Central College, South Ellsworth Street, Naperville, DuPage County, Illinois, 60540, United States'],
[42.3390301,-71.08791294953176, 'Northeastern University, Ruggles Street, Roxbury Crossing, Roxbury, Boston, Suffolk County, Massachusetts, 02120, United States']
];