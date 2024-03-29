
'''

#XXXXXX  PYTHON PANDAS TUTORIAL VIDEOS  XXXXXX

COREY SCHAFER - 11 VIDEOS

'''


'''
#VIDEO N1

csv import and visualization
'''

import pandas as pd
import numpy as np

df = pd.read_csv('/content/drive/MyDrive/Python_Files/Python_Import/stack-overflow-developer-survey-2019/survey_results_public.csv')
schema_df = pd.read_csv('/content/drive/MyDrive/Python_Files/Python_Import/stack-overflow-developer-survey-2019/survey_results_schema.csv')
#df = pd.read_csv('/content/drive/MyDrive/Python_Files/Python_Import/survey_results_public.csv', index_col = 'Respondent')
#posso aggiungere , index_col = 'nome colonna'

people = {
    'Name' : ['Fausto', 'Mavino', 'Saro'],
    'Last_Name' : ['Longo', 'Marino', 'Tedeschi'],
    'City' : ['Lucca', 'Catania', 'Genova']
}

df1 = pd.DataFrame(people)

people = {
    'Name' : ['Alessio', 'Davide'],
    'Last_Name' : ['Leli', 'Ortino'],
    'City' : ['Macerata' , 'Catania']
}

df2 = pd.DataFrame(people)

df1 = df1.append(df2, ignore_index = True)

df.shape
#codice per ottenere il numero di righe e di colonne del nostro df
#result:
#(88883, 85)

df.info()
#codice per ottenere info del mio df come nome colonne, righe e tipologia di dati

pd.set_option('display.max_columns', 85)
#codice importantissimo per visualizzare tutte le colonne del mio df
#usare il codice df.shape o df.info() per conoscere il numero esatto di colonne

pd.set_option('display.max_rows', 85)
#codice importantissimo per visualizzare tutte le righe del mio df
#usare il codice df.shape o df.info() per conoscere il numero esatto di righe

df.head(3)
#codice che ritorna le prime righe del mio df

df.tail(3)
#codice opposto a df.head(), ritorna le ultime righe del mio df


'''
#VIDEO N2

dataframe creation and properties
'''

#codice base per creare un dizionario da convertire a df
people = {
    'Name' : ['Fausto', 'Mavino', 'Saro'],
    'Last_Name' : ['Longo', 'Marino', 'Tedeschi'],
    'City' : ['Lucca', 'Catania', 'Genova']
}

df1 = pd.DataFrame(people)
df1
#codice per creare il df da un dizionario
#result:
# 	City	Name	Last_Name
#	0	Lucca	Fausto	Longo
#	1	Catania	Mavino	Marino
#	2	Genova	Saro	Tedeschi

df1['Name']
#codice per printare gli elementi di una specifica colonna
#result:
#0    Fausto
#1    Mavino
#2      Saro

df.columns[1]
#codice che ritorna la colonna di indice indicato

df1.loc[0]
df1.loc['Catania']
#codice che ritorna l'elemento in posizione label (indice)
#se assegno altro indice al mio df posso richiamare la riga con il nome assegnato

df.iloc[0]
#codice che ritorna la riga di indice indicato

df.iloc[0, 0]
#codice che ritorna l'elemento in posizione [riga, colonna]


'''
#VIDEO N3

indexing
'''

'''
#XXX INDICE DF XXX
'''

df1.set_index('City', inplace = True)
#codice per modificare l'indice automatico del mio df con una intera colonna

df1.reset_index(inplace = True)
#codice per resettare l'indice automatico di python

df1.sort_index(ascending = True, inplace = True)
#codice per filtrare l'indice in ordine ascendente 


'''
#VIDEO N4

filtering
'''

#codice per ricercare tramite boolean uno specifico elemnto in una specifica colonna
#leggo (indicami 'vero' quando una riga presenta 'Catania' nella colonna 'City')
filt = (df1['City'] == 'Catania')
#result:
#0    False
#1     True
#2    False
#Name: City, dtype: bool

df1.loc[filt] #modo corretto
df1[filt] #codice abbreviato
#result:
# Name	Last_Name	City
#1	Mavino	Marino	Catania

#inserendo la tilde (~) eseguiamo il comando inverso
#leggo (filtrami nel df tutti gli elementi opposti a Catania == City 'vero')
df1.loc[~filt]
df1[~filt] #codice abbreviato
#result:
#  Name	Last_Name	City
#0	Fausto	Longo	Lucca
#2	Saro	Tedeschi	Genova

high_salary = (df['ConvertedComp' ] > 70000)
#codice per filtrare il mio df per stipendio > 70000

df.loc[high_salary, ['Country', 'LanguageWorkedWith', 'ConvertedComp']]
#filtro per il salario definito sopra e chiedo di printare solamente le colonne indicate

filt = df['LanguageWorkedWith'].str.contains('Python', na = False)
#codice per filtrare il df per tipo di linguaggio e se questo contiene la str 'Python'


'''
#VIDEO N5

editing the df
'''

df1.columns = [x.lower() for x in df1.columns]
#codice per modificare in minuscolo i caratteri di tutte le colonne del df

df1.columns = [x.upper() for x in df1.columns]
#codice per modificare in maiuscolo i caratteri di tutte le colonne del df

df1.rename(columns = {'name': 'nome', 'last_name': 'cognome'}, inplace = True)
#codice per modificare solo specifiche colonne del mio df

df1.loc[1, 'Name'] = 'Fabio'
#codice per modificare un determinato elemento di una specifica riga [1] e colonna ('Name')
#in questo caso da 'Mavino' a 'Fabio'

df1.loc[1, ['Name', 'City']] = ['Fabio', 'Roma']
#codice per modificare più elementi di una specifica riga [1] e colonne ('Name', 'City')

df1['Last_Name'] = df1['Last_Name'].str.lower()
#codice per modificare in minuscolo tutti i caratteri di uan determinata colonna del mio df

df1['Last_Name'] = df1['Last_Name'].str.upper()
#codice per modificare in maiuscolo tutti i caratteri di uan determinata colonna del mio df

df1.apply(len)
#codice per ottenere il numero di elementi contenuti in ogni colonna del mio df
#result:
#Name         3
#Last_Name    3
#City         3
#dtype: int64

len(df1['Name'])
#codice per ottenere il numero di elementi contenuti in una specifica colonna del mio df
#result:
#3

df1.applymap(len)
#codice per applicare una determinata funzione (len) ad ogni elemento del mio df
#result:
#Name	Last_Name	City
#0	6	5	5
#1	6	6	7
#2	4	8	6

df1.applymap(str.lower)
#codice per applicare una determinata funzione (carattere minuscolo) ad ogni elemento del mio df

df1.applymap(str.upper)
#codice per applicare una determinata funzione (carattere maiuscolo) ad ogni elemento del mio df

df1['City'].replace({'Lucca' : 'Catania', 'Genova' : 'Catania'}, inplace = True)
#codice per modiificare specifici elementi di una specifica colonna del mio df

#codice per modificare tutti gli elementi di una specifica colonna del mio df
df1['City'].replace({ x : 'Picanello' for x in df1['City']}, inplace = True)
#result:
#Name	Last_Name	City
#0	Fausto	Longo	Picanello
#1	Mavino	Marino	Picanello
#2	Saro	Tedeschi	Picanello


'''
#VIDEO N6

add and removing rows and columns
'''

df1['Full_Name'] = df1['Name'] + ' ' + df1['Last_Name']
#codice per creare una nuova colonna che sia il risultato dell'unione di alre colonne del mio df
#result:
#   Name	Last_Name	City	Full_Name
#0	Fausto	Longo	Lucca	Fausto Longo
#1	Mavino	Marino	Catania	Mavino Marino
#2	Saro	Tedeschi	Genova	Saro Tedeschi

df1.drop(columns = ['Name', 'Last_Name'], inplace = True)
#codice per eliminare specifiche colonne del mio df

df1['Full_Name'].str.split(' ')
#codice per separare tutti gli elementi di una specifica colonna tramite virgola
#0     [Fausto, Longo]
#1    [Mavino, Marino]
#2    [Saro, Tedeschi]
#Name: Full_Name, dtype: object

df1['Full_Name'].str.split('')
#codice per separare tutti i caratteri degli gli elementi di una specifica colonna tramite virgola
#result:
#0       [, F, a, u, s, t, o,  , L, o, n, g, o, ]
#1    [, M, a, v, i, n, o,  , M, a, r, i, n, o, ]
#2    [, S, a, r, o,  , T, e, d, e, s, c, h, i, ]

df1['Full_Name'].str.split(' ', expand = True)
#inserendo il codice, expand = True, divido separo gli elementi e li dispongo su colonne diverse

df1[['Nome', 'Cognome']] = df1['Full_Name'].str.split(' ', expand = True)
#codice per separare elementi di una specifica colonna, disporli su nuove colonne da aggiungere al mio df
#result:
#     City	Full_Name	Nome	Cognome
#0	Lucca	Fausto Longo	Fausto	Longo
#1	Catania	Mavino Marino	Mavino	Marino
#2	Genova	Saro Tedeschi	Saro	Tedeschi

df1.append({'Name' : 'Alessio'}, ignore_index = True)
#codice per aggiungere una riga al mio df, inserisco un elemento in una specifica colonna del df
#result:
#   Name	Last_Name	City
#0	Fausto	Longo	Lucca
#1	Mavino	Marino	Catania
#2	Saro	Tedeschi	Genova
#3	Alessio	NaN	NaN

people = {
    'Name' : ['Alessio', 'Davide'],
    'Last_Name' : ['Leli', 'Ortino'],
    'City' : ['Macerata' , 'Catania']
}

df2 = pd.DataFrame(people)

df1 = df1.append(df2, ignore_index = True)
#codice per aggiungere come righe del mio df elementi di un altro df
#result:
#   Name	Last_Name	City
#0	Fausto	Longo	Lucca
#1	Mavino	Marino	Catania
#2	Saro	Tedeschi	Genova
#3	Alessio	Leli	Macerata
#4	Davide	Ortino	Catania

df1.drop(index = 3, inplace = True)
#codice per eliminare una specifica riga (indice) del mio df

filter = df1['City'] == 'Catania'
df1.drop(index = df1[filter].index, inplace = True)
#codice per eliminare tutte le righe contenenti uno specifico elemento in una specifica colonna del mio df
#result:
#   Name	Last_Name	City
#0	Fausto	Longo	Lucca
#2	Saro	Tedeschi	Genova
#3	Alessio	Leli	Macerata


'''
#VIDEO N7

sorting
'''

df1.sort_values(by = 'Last_Name', ascending = True)
#codice per ordinare gli elementi di una specifica colonna in ordine ascendente o discendente 'False'
#result:
#Name	Last_Name	City
#3	Alessio	Leli	Macerata
#0	Fausto	Longo	Lucca
#1	Mavino	Marino	Catania
#4	Davide	Ortino	Catania
#2	Saro	Tedeschi	Genova

df1.sort_values(by = ['Name', 'Last_Name'], ascending = True)
#codice per ordinare gli elementi di specifiche colonne in ordine ascendente o discendente 'False'
#result
#   Name	Last_Name	City
#3	Alessio	Leli	Macerata
#4	Davide	Ortino	Catania
#0	Fausto	Longo	Lucca
#1	Mavino	Marino	Catania
#2	Saro	Tedeschi	Genova

df1.sort_values(by = ['Name', 'Last_Name'], ascending = [False, True])
#codice per ordinare gli elementi di specifiche colonne in ordine ascendente e discendente 'False'
#result:
#   Name	Last_Name	City
#2	Saro	Tedeschi	Genova
#1	Mavino	Marino	Catania
#0	Fausto	Longo	Lucca
#4	Davide	Ortino	Catania
#3	Alessio	Leli	Macerata

df.sort_values(by = 'Country', inplace = True)
#codice veloce per sortare gli elementi di una specifica colonna del mio df

df.sort_values(by = ['Country', 'ConvertedComp'], ascending = [True, False], inplace = True)
#codice veloce per sortare gli elementi di specifiche colonne del mio df
#leggo (ordina il mio df per paesi e stipendio, paesi in ordine alfabetico e stipendio in ordine decrescente)

df[['Country', 'ConvertedComp']].head(50)
#codice per sortare velocemente solo le colonne del df che mi interessano

df['ConvertedComp'].nlargest(10)
#codice per ottenere solo gli elementi (i primi 10), di una specifica colonna, con valori piu alti

df.nlargest(10, 'ConvertedComp')
#codice per ottenere solo le righe (prime 10), di una specifica colonna, con valori piu alti

df['ConvertedComp'].nsmallest(10)
#codice per ottenere solo gli elementi (i primi 10), di una specifica colonna, con valori piu alti

df.nsmallest(10, 'ConvertedComp')
#codice per ottenere solo le righe (prime 10), di una specifica colonna, con valori piu bassi


'''
#VIDEO N8

grouping, counting and aggregating
'''

df['ConvertedComp'].median()
#codice veloce per calcolare la media di tutti i valori in una specifica colonna
#può essere sostituito da .count .std .mean

df.median()
#codice veloce che calcola la media di tutte le colonne del mio df contenenti numeri 
#può essere sostituito da .count .std .mean

df.describe()
#codice veloce che calcola diverse funzioni (media, std, count, ecc) di tutte le colonne del mio df contenenti numeri 

df['Hobbyist'].count()
#codice per contare tutti gli elementi di una specifica colonna del mio df
#result:
#88883

df['Hobbyist'].value_counts()
#codice per contare tutte i diversi elementi unici di una specifica colonna del mio df
#result:
#Yes    71257
#No     17626
#Name: Hobbyist, dtype: int64

df['Hobbyist'].value_counts(normalize = True)
#codice per conoscere la percentuale dei diversi elementi unici di una specifica colonna del mio df
#result:
#Yes    0.801694
#No     0.198306
#Name: Hobbyist, dtype: float64

country_grp = df.groupby(['Country'])
#codiceper raggruppare in nuovo df gli elementi parte di una specifica colonna del mio df

country_grp.get_group('United States')
country_grp.get_group('India')
#utilizzo il raggruppamento per ottenere solo specifici elementi della specifica colonna del df 

filt = df['Country'] == 'United States'
df.loc[filt]['SocialMedia'].value_counts()
#result: (solo prime 2 linee)
#Reddit                      5700
#Twitter                     3468
#Facebook                    2844

country_grp['SocialMedia'].value_counts()
#result: (solo prime 2 linee)
#Country      SocialMedia             
#Afghanistan  Facebook                    15
#             YouTube                      9
#             I don't use social media     6

country_grp['SocialMedia'].value_counts().loc['United States']
#con questa versione del codice posso modificare il paese per ottenere la lista dei social del paese
#result: (solo le prime linee)
#SocialMedia
#Reddit                      5700
#Twitter                     3468
#Facebook                    2844

country_grp['ConvertedComp'].median().loc['Germany']
#codice per utilizzare un`operazione su un determinato raggruppamento e colonna 
#result:
63016.0

country_grp['ConvertedComp'].agg(['median', 'mean']).loc['Italy']
#codice per utilizzare più operazioni .agg (in questo caso mediana e media)
#result:
#median    35518.000000
#mean      89535.843882
#Name: Italy, dtype: float64

filt = df['Country'] == 'India'
df.loc[filt]['LanguageWorkedWith'].str.contains('Python')
#codice per ottenere una lista in boolean degli utenti provenienti dall`India che hanno lavorato con Python
#imposto prima un filtro per la colonna 'LanguageWorkedWith' e chiedo di filtrare solo per gli elementi
#che contendono la parola 'Python' all`interno della stringa.
#result:
#7         True
#9         True
#14       False

filt = df['Country'] == 'India'
df.loc[filt]['LanguageWorkedWith'].str.contains('Python').sum()
#se aggiungo .sum() alla fine del codice ottengo il numero esatto delle persone che usano Python
#result:
#3105

country_grp['LanguageWorkedWith'].apply(lambda x: x.str.contains('Python').sum())
#codice per ottenere il raggroppamento degli utenti dei vari paesi che usano Python
#sul raggruppamento dobbiamo usare la funzione .apply()
#result:
#Country
#Afghanistan                              8
#Albania                                 23
#Algeria                                 40
#Andorra                                  0
#Angola                                   2
#                                        ..


'''
XXXX   ESERCIZIO   XXXX

come faccio ad ottenere la percentuale totale degli utenti che usano Python per diverso paese?
'''


country_respondents = df['Country'].value_counts()
country_respondents
#prima di tutto conto gli utenti totali per ogni singolo paese
#result:
#United States        20949
#India                 9061
#Germany               5866
#United Kingdom        5737
#Canada                3395
#                     ...  

country_uses_python = country_grp['LanguageWorkedWith'].apply(lambda x: x.str.contains('Python').sum())
country_uses_python
#riutilizzo il codice di prima per ottenere il numero dei soli utenti che usano Python
#result:
#Country
#Afghanistan                              8
#Albania                                 23
#Algeria                                 40
#Andorra                                  0
#Angola                                   2
#                                        ..

python_df = pd.concat([country_respondents, country_uses_python], axis = 'columns', sort = False)
python_df
#codice per concatenare piu' serie.
#Aggiungo axis = 'columns' per separarli in colonne altrimenti li unirebbe con le righe 
#Aggiungo sort = False perche` nelle nuove versioni il sort e` automatico
#result:
#	            Country  LanguageWorkedWith
#United States	20949	10083
#India        	9061	3105
#Germany      	5866	2451
#United Kingdom	5737	2384
#Canada	        3395	1558
#...	...	...

python_df.rename(columns = {'Country': 'NumRespondents', 'LanguageWorkedWith' : 'NumKnowsPython'}, inplace = True)
python_df
#codice per cambiare solo determinate colonne del mio df
#result:
#	          NumRespondents	NumKnowsPython
#United States	20949	      10083

python_df['PctKnowsPython'] = (python_df['NumKnowsPython'] / python_df['NumRespondents']) * 100
python_df
#per creare una nuova colonna nel mio df mi basta nominarla.
#per ottenere la percentuale eseguo la formula matematica inserendo le diverse colonne tra num e denom *100
#result:
#             NumRespondents	NumKnowsPython	PctKnowsPython
#United States	20949	           10083	       48.131176
#India	        9061            	3105	       34.267741
#Germany	      5866	            2451	       41.783157

python_df.sort_values(by = 'PctKnowsPython', ascending = False, inplace = True)
python_df
#codice per filtrare il mio database per % di persone che usano python per ogni paese
#result:
#                         NumRespondents	NumKnowsPython	PctKnowsPython
#Sao Tome and Principe	              1             	1   	100.000000
#Niger                               	1             	1   	100.000000
#Timor-Leste                        	1              	1	    100.000000
#Dominica	                            1	              1	    100.000000
#Turkmenistan                       	7	              6	    85.714286

python_df.loc['Italy']
#codice per ottenere le informazioni di un unico paese
#una volta creato il mio df con raggruppamento e percentuale, posso ricercare il singolo paese
#result:
#NumRespondents    1576.00000
#NumKnowsPython     625.00000
#PctKnowsPython      39.65736
#Name: Italy, dtype: float64


'''
#VIDEO N9

Cleaning Data - Casting Datatypes and Handling Missing Values
'''
#per iniziare creiamo un dizionario con informazioni di vario tipo
#fondamentale l`inserimento di valori nulli (None) e di valori numerici nulli (np.nan)

people = {
    'first': ['Corey', 'Jane', 'John', 'Chris', np.nan, None, 'NA'], 
    'last': ['Schafer', 'Doe', 'Doe', 'Schafer', np.nan, np.nan, 'Missing'], 
    'email': ['CoreyMSchafer@gmail.com', 'JaneDoe@email.com', 'JohnDoe@email.com', None, np.nan, 'Anonymous@email.com', 'NA'],
    'age': ['33', '55', '63', '36', None, None, 'Missing']
}

df = pd.DataFrame(people)
df
#codice per creare un dataframe da un dizionario
#result:
#    first	last	   email	                   age
#0	Corey	Schafer     	CoreyMSchafer@gmail.com	33
#1	Jane	Doe	          JaneDoe@email.com	      55
#2	John	Doe	          JohnDoe@email.com	      63
#3	Chris	Schafer	      None                  	36
#4	NaN	  NaN	          NaN	                  None
#5	None	NaN	          Anonymous@email.com	  None
#6	NA   	Missing	      NA	                 Missing

df.dropna(axis = 'index', how = 'any')
#codice per eliminare dal df tutte le righe contenenti almeno un valore nullo (amy)
#result:
#    first	last	   email	                   age
#0	Corey	Schafer     	CoreyMSchafer@gmail.com	33
#1	Jane	Doe	          JaneDoe@email.com	      55
#2	John	Doe	          JohnDoe@email.com	      63

df.dropna(axis = 'index', how = 'all') 
#codice per eliminare dal df tutte le righe contenenti solamente valori nulli (all)
#result:
#    first	last	   email	                   age
#0	Corey	Schafer     	CoreyMSchafer@gmail.com	33
#1	Jane	Doe	          JaneDoe@email.com	      55
#2	John	Doe	          JohnDoe@email.com	      63
#3	Chris	Schafer     	None	                  36
#5	None	NaN	          Anonymous@email.com	  None
#6	NA	  Missing     	NA	               Missing

df.dropna(axis = 'columns', how = 'any')
#codice per eliminare dal df tutte le colonne contenenti almeno un valore nullo (any)
#non otteniamo nulla perche` una riga del mio df presenta valori nulli per ogni colonna
#result:
#0

df.dropna(axis = 'columns', how = 'all')
#codice per eliminare dal df tutte le colonne contenenti solamente valori nulli (all)
#otteniamo l`intero df perche` nessuna colonna del mio df presenta solamente valori nulli
#result:
#    first	last	   email	                   age
#0	Corey	Schafer     	CoreyMSchafer@gmail.com	33
#1	Jane	Doe	          JaneDoe@email.com	      55
#2	John	Doe	          JohnDoe@email.com	      63
#3	Chris	Schafer	      None                  	36
#4	NaN	  NaN	          NaN	                  None
#5	None	NaN	          Anonymous@email.com	  None
#6	NA   	Missing	      NA	                 Missing

df.dropna(axis = 'index', how = 'any', subset = ['email'])
#codice per eliminare dal mio df tutte le righe che presentano valori nulli nella colonna 'email' (any)
#result:
#    first	last	   email	                   age
#0	Corey	Schafer     	CoreyMSchafer@gmail.com	33
#1	Jane	Doe	          JaneDoe@email.com	      55
#2	John	Doe	          JohnDoe@email.com	      63
#5	None	NaN	          Anonymous@email.com	  None
#6	NA   	Missing	      NA	                 Missing

df.dropna(axis = 'index', how = 'all', subset = ['last','email'])
#codice per eliminare dal mio df tutte le righe che presentano sia last che email nulli (all)
#result:
#    first	last	   email	                   age
#0	Corey	Schafer     	CoreyMSchafer@gmail.com	33
#1	Jane	Doe	          JaneDoe@email.com	      55
#2	John	Doe	          JohnDoe@email.com	      63
#3	Chris	Schafer	      None                  	36
#5	None	NaN	          Anonymous@email.com	  None
#6	NA   	Missing	      NA	                 Missing

df.dropna(axis = 'index', how = 'any', subset = ['last','email'])
#codice per eliminare dal mio df tutte le righe che presentano o last o email nulli (any)
#result:
#    first	last	   email	                   age
#0	Corey	Schafer     	CoreyMSchafer@gmail.com	33
#1	Jane	Doe	          JaneDoe@email.com	      55
#2	John	Doe	          JohnDoe@email.com	      63
#6	NA   	Missing	      NA	                 Missing

df.replace('NA', np.nan, inplace = True)
df.replace('Missing', np.nan, inplace = True)
#codice per sostituire tutti gli elementi del df contenenti 'xxx' con , 'yyy'
#in questo caso inserisco np.nan per ottenere dei valori numerici NaN
df
#result:
#    first	last	   email	                   age
#0	Corey	Schafer     	CoreyMSchafer@gmail.com	33
#1	Jane	Doe	          JaneDoe@email.com	      55
#2	John	Doe	          JohnDoe@email.com	      63
#3	Chris	Schafer	      None                  	36
#4	NaN	  NaN	          NaN	                  None
#5	None	NaN	          Anonymous@email.com	  None
#6	NaN  	Nan           NaN	                   Nan

df.dropna()
#codice per ottenere solo gli elementi del df che non contengono NaN. 
#va a droppare tutte le righe contenenti almeno un elemento Nan
#result:
#    first	last	   email	                   age
#0	Corey	Schafer     	CoreyMSchafer@gmail.com	33
#1	Jane	Doe	          JaneDoe@email.com	      55
#2	John	Doe	          JohnDoe@email.com	      63

df.isna()
#codice per ottenere boolean per ogni elemento del mio dataframe
#in questo caso mi da False se è presente un elemento, True se l'elemento è nullo
#result:
#   first	last	email	age
#0	False	False	False	False
#1	False	False	False	False
#2	False	False	False	False
#3	False	False	True	False
#4	True	True	True	True
#5	True	True	False	True
#6	True	True	True	True

df.fillna('MISSING')
df.fillna(0)
#codice per riempire tutte le celle del mio df contenenti Nan o null con un valore (o) o str ('MISSING)
#result:
#    first	last	   email	                   age
#0	Corey	Schafer     	CoreyMSchafer@gmail.com	33
#1	Jane	Doe	          JaneDoe@email.com	      55
#2	John	Doe	          JohnDoe@email.com	      63
#3	Chris	Schafer	      MISSING                 36
#4	MISSING	MISSING     MISSING	             MISSING
#5	MISSING	MISSING	    Anonymous@email.com  MISSING
#6	MISSING MISSING     MISSING	             MISSING

df.dtypes
#codice per conoscere le colonne del df e la natura degli elementi 
#result:
#first    object
#last     object
#email    object
#age      object
#dtype: object

df['age'] = df['age'].astype(float)
#codice per castare tutti gli elementi di una specifica colonna. Esempio in float
#il codice non funziona se vi sono missing data nella colonna
df.dtypes
#result:
#first    object
#last     object
#email    object
#age      float
#dtype: object

df['age'].mean()
#codice per calcolare la media di tutti i valori di una specifica colonna
#adesso posso farlo perchè tutte le str sono convertite a float
#result:
#46.75


'''
XXXX   ESERCIZIO   XXXX

calcolare in media da quanto tempo i soggetti programmano
'''

na_vals = ['NA', 'Missing']
df = pd.read_csv('/content/drive/MyDrive/Python_Files/Python_Import/stack-overflow-developer-survey-2019/survey_results_public.csv', na_values = na_vals)
schema_df = pd.read_csv('/content/drive/MyDrive/Python_Files/Python_Import/stack-overflow-developer-survey-2019/survey_results_schema.csv')
#se creo una lista di missing value, poi posso aggiungere na_values = lista creata
#per considerare tutti gli elementi della lista Nan.

df['YearsCode'].unique()
#codice per ottenere tutti gli elementi unici della colonna selezionata
#result:
#array(['4', nan, '3', '16', '13', '6', '8', '12', '2', '5', '17', '10',
#       '14', '35', '7', 'Less than 1 year', '30', '9', '26', '40', '19',
#       '15', '20', '28', '25', '1', '22', '11', '33', '50', '41', '18',
#       '34', '24', '23', '42', '27', '21', '36', '32', '39', '38', '31',
#       '37', 'More than 50 years', '29', '44', '45', '48', '46', '43',
#       '47', '49'], dtype=object)

df['YearsCode'].replace('Less than 1 year', 0, inplace = True)
df['YearsCode'].replace('More than 50 years', 51, inplace = True)
#uso il codice replace per sostituire le str con numeri

df['YearsCode'] = df['YearsCode'].astype(float)
#modifico tutti gli elementi della colonna in float
df['YearsCode'].mean()
#ora che tutti gli elementi della colonna sono float posso calcolare la media 
#result:
#11.662114216834588
df['YearsCode'].median()
#result:
#9


'''
XXXX   ESERCIZIO   XXXX

calcolare in media da quanto tempo gli italiani del sondaggio programmano
'''

country_grp = df.groupby(['Country'])
filt = df['Country'] == 'Italy'
df.loc[filt]['YearsCode'].mean()
#result:
#13.658785942492013


'''
#VIDEO N10

Working with Dates and Time Series Data

DATE TIME LIBRARY INFORMATION

https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior

https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#dateoffset-objects
'''

import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('/content/drive/MyDrive/Python_Files/Python_Import/ETH_1h.csv')

df.loc[0, 'Date']
#codice per selezionare solo il primo elemento della colonna 'Date' del mio df
#result:
#2020-03-13 08-PM

df['Date'] = pd.to_datetime(df['Date'])
#codice per cambiare il formato data str in formato data 

df['Date'] = pd.to_datetime(df['Date'], format = '%Y-%m-%d %I-%p')
#codice per cambiare il formato data da str a data secondo le nostre preferenze
#%Y = year, %m = month, %d = day, %I = 12h clock, %p = AM or PM
#controllare il link con la libreria per ulteriori formati

df.loc[0, 'Date'].day_name()
#codice per calcolare il giorno esatto partendo da una data in formato date time 
#result:
#Friday

d_parser = lambda x: pd.datetime.strptime(x, '%Y-%m-%d %I-%p' )
df = pd.read_csv('/content/drive/MyDrive/Python_Files/Python_Import/ETH_1h.csv', parse_dates = ['Date'], date_parser = d_parser)
#codice alternativo ridotto per modificare il formato della mia colonna data quando importo il file csv.

df['DayOfWeek'] = df['Date'].dt.day_name()
#codice per creare una colonna con il giorno esatto per tutte le date di una specifica colonna del df

df['Date'].min()
#codice per ottenere il valore minimo di una specifica colonna del df
#result:
#Timestamp('2017-07-01 11:00:00')

df['Date'].max()
#codice per ottenere il valore massimo di una specifica colonna del df
#result:
#Timestamp('2020-03-13 20:00:00')

df['Date'].max() - df['Date'].min()
#codice per calcolare il delta time, differenza tra due date espressa in giorni
#result:
#Timedelta('986 days 09:00:00')

filt = (df['Date'] >= '2020')
df.loc[filt]
#codice per creare un filtro e visualizzare solo gli elementi filtrati
#in questo caso creo un filtro per mostrare solo le date successive al 2019

filt = (df['Date'] >= '2019') & (df['Date'] < '2020')
df.loc[filt]
#codice per impostare un filtro con cap minimo e massimo

df.set_index('Date' , inplace = True)
#codice per impostare come index una specifica colonna del  mio df

df['2020-01':'2020-02']
#se imposto la colonna data come indice posso filtrare direttamente tramite le date
#funziona solo se inserisco inplace = True quando imposto il nuovo indice

df['2020-01':'2020-02']['Close'].mean()
#codice per ottenere la media di tutti i valori di una specifica colonna in un determinato arco di tempo
#result:
#195.1655902777778

df['2020-01-01']['High'].max()
#codice per ottenere il valore massimo in un determinato giorno 
#result:
#132.68

df['High'].resample('D').max()
#codice per ottenere solo i valori massimi per ogni giorno diverso del mio df
#usando la funzione .resample('unita` temporale) posso filtrare l`intera colonna per giorno, mese, anno, settimana ecc

highs = df['High'].resample('D').max()
highs['2020-01-01']
#codice per impostare il valore massimo per giorno e successivamente investigare un giorno specifico
#usare altre sigle per investigare anno, settimana, mese ecc
#132.68

df.resample('W').agg({'Close': 'mean', 'High': 'max', 'Low': 'min', 'Volume': 'sum' })
#codice per ottenere i valori settimanali con filtri specifici per le colonne desiderate

df['High'].plot()
#codice per plottare una determinata colonna dle mio df


'''
#VIDEO N11

Reading and Writing Data to Different Sources - Excel, JSON, SQL, Etc
'''

import pandas as pd

df = pd.read_csv('/content/drive/MyDrive/Python_Files/Python_Import/stack-overflow-developer-survey-2019/survey_results_public.csv', index_col = 'Respondent')
schema_df = pd.read_csv('/content/drive/MyDrive/Python_Files/Python_Import/stack-overflow-developer-survey-2019/survey_results_schema.csv', index_col = 'Column')
#posso aggiungere index_col ed altri elementi per modificare il mio df prima di importarlo


filt = (df['Country'] == 'India')
india_df = df.loc[filt]
india_df.head(3)
#codice per creare un df basato su un filtro paese
#nuovo df filtrato solo con le risposte dei soggetti provenienti dall' India
