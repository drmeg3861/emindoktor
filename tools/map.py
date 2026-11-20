# entry name -> (mono ATC codes, combo: (inn, prefix) or None)
M={}
def m(n,codes,inn=None,pre="C"): M[n]=(codes,(inn,pre) if inn else None)
ace=dict(Ramipril=("C09AA05","ramipril"),Perindopril=("C09AA04","perindopril"),Zofenopril=("C09AA15","zofenopril"),Silazapril=("C09AA08","cilazapril"),Lisinopril=("C09AA03","lisinopril"),Kinapril=("C09AA06","quinapril"),Benazepril=("C09AA07","benazepril"),Fosinopril=("C09AA09","fosinopril"),Trandolapril=("C09AA10","trandolapril"),Enalapril=("C09AA02","enalapril"),
 Losartan=("C09CA01","losartan"),Eprosartan=("C09CA02","eprosartan"),Valsartan=("C09CA03","valsartan"),Irbesartan=("C09CA04","irbesartan"),Kandesartan=("C09CA06","candesartan"),Telmisartan=("C09CA07","telmisartan"),Olmesartan=("C09CA08","olmesartan"),
 Amlodipin=("C08CA01","amlodipine"),Felodipin=("C08CA02","felodipine"),Nikardipin=("C08CA04","nicardipine"),Nifedipin=("C08CA05","nifedipine"),Nimodipin=("C08CA06","nimodipine"),Lasidipin=("C08CA09","lacidipine"),Lerkanidipin=("C08CA13","lercanidipine"),Benidipin=("C08CA15","benidipine"),
 Verapamil=("C08DA01","verapamil"),Diltiazem=("C08DB01","diltiazem"),Indapamid=("C03BA11","indapamide"),Furosemid=("C03CA01","furosemide"),Torasemid=("C03CA04","torasemide"),Spironolakton=("C03DA01","spironolactone"),
 Propranolol=("C07AA05","propranolol"),Sotalol=("C07AA07","sotalol"),Metoprolol=("C07AB02","metoprolol"),Atenolol=("C07AB03","atenolol"),Bisoprolol=("C07AB07","bisoprolol"),Nebivolol=("C07AB12","nebivolol"),Karvedilol=("C07AG02","carvedilol"))
for k,(c,i) in ace.items(): m(k,[c],i)
m("Triamteren+Hidroklorotiazid",["C03EA01"]); m("Atenolol+Klortalidon",["C07CB03","C07BB03"]); m("Eplerenon",["C03DA04"])
m("Metildopa",["C02AB01","C02AB02"]); m("Doksazosin",["C02CA04"]); m("Rilmenidin",["C02AC06"])
m("Pentoksifilin",["C04AD03"]); m("Digoksin",["C01AA05"]); m("Amiodaron",["C01BD01"]); m("Propafenon",["C01BC03"])
m("İzosorbid mononitrat",["C01DA14"]); m("Trimetazidin",["C01EB15"]); m("Diosmin+Hesperidin",["C05CA53","C05CA03"])
m("Kalsiyum dobesilat",["C05BX01"]); m("Rutosid / Okserutin",["C05CA01","C05CA04","C05CA51","C05CA54"]); m("Essin / Triterpen glikozid",["C05CX03","C05BX02"])
m("Atorvastatin",["C10AA05"]); m("Rosuvastatin",["C10AA07"]); m("Pitavastatin",["C10AA08"]); m("Pravastatin",["C10AA03"])
m("Fenofibrat",["C10AB05"]); m("Gemfibrozil",["C10AB04"]); m("Kolesevelam",["C10AC04"]); m("Ezetimib",["C10AX09"])
m("Asitretin",["D05BB02"]); m("İzotretinoin",["D10BA01"])
m("Kabergolin",["G02CB03"]); m("Bromokriptin",["G02CB01","N04BC01"]); m("Metilergonovin",["G02AB01"])
m("Estradiol+Noretisteron",["G03FA01","G03FB05"]); m("Estradiol+Drospirenon",["G03FA17"]); m("Estradiol",["G03CA03"])
m("Estradiol+Norgestrel",["G03FB01"]); m("Estradiol+Medroksiprogesteron",["G03FA12","G03FB06"]); m("Siproteron",["G03HA01"])
m("Etinilestradiol+Siproteron",["G03HB01"]); m("Estradiol+Siproteron",["G03HB01"])
m("Danazol",["G03XA01"]); m("Didrogesteron",["G03DB01"]); m("Klomifen sitrat",["G03GB02"]); m("Agnucaston",["G02CX03"])
for n,c in dict(Omeprazol="A02BC01",Pantoprazol="A02BC02",Lansoprazol="A02BC03",Rabeprazol="A02BC04",Esomeprazol="A02BC05",Deksrabeprazol="A02BC07",Famotidin="A02BA03",Nizatidin="A02BA04",Misoprostol="A02BB01",Ondansetron="A04AA01",Granisetron="A04AA02",Palonosetron="A04AA05").items(): m(n,[c])
m("Antasitler",["A02A*"])
m("Potasyum",["A12BA01","A12BA30","A12BA51","B05XA01"]); m("Potasyum sitrat",["A12BA02"]); m("Kalsitriol",["A11CC04"])
m("Kalsiyum asetat",["V03AE07"]); m("Kalsiyum karbonat",["A12AA04"]); m("Kalsiyum karbonat+Vitamin D3",["A12AX"])
m("Mesalazin",["A07EC02"]); m("Sülfasalazin",["A07EC01"])
m("İnsan (human) insülini",["A10AB01","A10AC01","A10AD01"]); m("Metformin",["A10BA02"]); m("Glimepirid",["A10BB12"]); m("Gliklazid",["A10BB09"])
m("Glibenklamid",["A10BB01"]); m("Glipizid",["A10BB07"]); m("Akarboz",["A10BF01"]); m("Nateglinid",["A10BX03"])
m("Asetilsalisilik asit",["B01AC06"]); m("Heparin",["B01AB01"]); m("Enoksaparin",["B01AB05"]); m("Bemiparin",["B01AB12"]); m("Varfarin",["B01AA03"])
m("Dipiridamol",["B01AC07"]); m("Tiklopidin",["B01AC05"]); m("Klopidogrel",["B01AC04"])
m("Fitomenadion (Vitamin K1)",["B02BA01"]); m("Traneksamik asit",["B02AA02"]); m("Desmopressin",["H01BA02"]); m("Kortikosteroidler",["H02AB*"])
m("Levotiroksin sodyum",["H03AA01"]); m("Liyotironin sodyum",["H03AA02"]); m("Liyotironin+Levotiroksin",["H03AA03"]); m("Propiltiyourasil",["H03BA02"])
m("Metimazol / Tiamazol",["H03BB02"]); m("İyot / Potasyum iyodür",["H03CA"])
for n,c in {"Anastrozol":"L02BG03","Eksemestan":"L02BG06","Megestrol asetat":"L02AB01","Bikalutamid":"L02BB03","Löprolid asetat":"L02AE02","Letrozol":"L02BG04","Goserelin":"L02AE03","Tamoksifen":"L02BA01",
 "Mikofenolat mofetil":"L04AA06","Mikofenolik asit":"L04AA06","Takrolimus":"L04AD02","Siklosporin":"L04AD01","Sirolimus":"L04AH01","Azatioprin":"L04AX01","Melfalan":"L01AA03","Busulfan":"L01AB01","Siklofosfamid":"L01AA01",
 "Klorambusil":"L01AA02","Merkaptopürin":"L01BB02","Kapesitabin":"L01BC06","5-Fluorourasil":"L01BC02","Vinorelbin":"L01CA04","Estramustin fosfat":"L01XX11","Hidroksiüre":"L01XX05",
 "Baklofen":"M03BX01","Tolperizon":"M03BX04","Kolşisin":"M04AC01","Allopurinol":"M04AA01","Zoledronik asit":"M05BA08","Alendronik asit":"M05BA04","Risedronat sodyum":"M05BA07","İbandronik asit":"M05BA06","Pamidronat disodyum":"M05BA03",
 "Petidin / Meperidin":"N02AB02","Tramadol":"N02AX02","Fentanil":"N02AB03","Morfin":"N02AA01","Oksikodon":"N02AA05","Fenobarbital":"N03AA02","Fenitoin":"N03AB02","Klonazepam":"N03AE01","Karbamazepin":"N03AF01","Okskarbazepin":"N03AF02",
 "Valproik asit":"N03AG01","Sodyum valproat":"N03AG01","Biperiden":"N04AA02","Amantadin":"N04BB01","Bornaprin":"N04AA11","Piribedil":"N04BC08","Zuklopentiksol":"N05AF05","Flupentiksol":"N05AF01","Sülpirid":"N05AL01",
 "Pimozid":"N05AG02","Trifluoperazin":"N05AB06","Flufenazin":"N05AB02","Lityum":"N05AN01","Haloperidol":"N05AD01","Klorpromazin":"N05AA01","Alprazolam":"N05BA12","Diazepam":"N05BA01","Lorazepam":"N05BA06","Buspiron":"N05BE01",
 "Zopiklon":"N05CF01","Trazodon":"N06AX05","Pirasetam":"N06BX03","Betahistin":"N07CA01","Neostigmin":"N07AA01","Piridostigmin":"N07AA02","Sinnarizin":"N07CA02","Flunarizin":"N07CA03",
 "Salbutamol":"R03AC02","Salbutamol+İpratropium":"R03AL02","Budesonid":"R03BA02","Siklesonid":"R03BA08","Flutikazon":"R03BA05","Terbutalin":"R03AC03","Teofilin":"R03DA04","Diprofilin":"R03DA01","Aminofilin":"R03DA05",
 "Asetazolamid":"S01EC01","Polistiren sülfonat kalsiyum":"V03AE01","Folinik asit / Kalsiyum folinat":"V03AF03","Mesna":"V03AF01","Gonadorelin asetat":"V04CM01","Hidroksiklorokin sülfat":"P01BA02"}.items(): m(n,[c])
m("Everolimus",["L04AH02","L04AA18"]); m("Metotreksat sodyum",["L04AX03","L01BA01"]); m("Metotreksat",["L01BA01","L04AX03"])
m("Levodopa+Benserazid",["N04BA02"]); m("Levodopa+Karbidopa",["N04BA02"])
m("Levosalbutamol+İpratropium",["R03AL"]); 
