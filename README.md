# Uttrekk og presentasjon av posisjonsdata
Dette er en oppgave som går ut på å arbeide med og presentere middels strukturerte posisjonsdata i [python](https://www.python.org/). Oppgaven kan løses hvordan du vil, men det kan være lurt å vurdere en form for Notebook. Enten [Jupyter Notebook](https://jupyter.org/) eller [ArcGIS Notebook](https://pro.arcgis.com/en/pro-app/latest/arcpy/get-started/pro-notebooks.htm). Det kan også være lurt å kikke på [pandas](https://pandas.pydata.org/) til databehandling, men du står helt fritt til å bruke andre datastrukturer når du arbeider med data.

## Oppgave
Ta for deg datasettene som ligger i mappen [data](/data). Ved hjelp av [python](https://www.python.org/) skal du automatisk generere et kart som presenterer datasettet. Lag et kart til hvert datasett.

## Data
Mappen [data](/data) inneholder en samling datasett med litt forskjellige utfordringer og egenskaper. Datasettene er autogenerert. Dersom du er nysgjerrig på hvordan de er laget eller ønsker å lage din egen variant ligger koden i mappen [datafabrikk](/datafabrikk). Her kommer det en kort beskrivelse av hvert enkelt datasett og noen små tips til hvordan de kan behandles:

### Referansepunkter
Filen [refpoints.xlsx](data/refpoints.xlsx) inneholder noen hundre referansepunkter som er lagret i et Excel-ark. Posisjonene er desverre ikke uniforme. De forekommer enten som desimalgrader, [MGRS](https://en.wikipedia.org/wiki/Military_Grid_Reference_System) eller [DMS](https://en.wikipedia.org/wiki/Decimal_degrees).

For å åpne filen er det greit å bruke [pandas.read_excel()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html#pandas.read_excel).

For å gjøre operasjoner på en hel kolonne i [pandas](https://pandas.pydata.org/) er det greit å bruke [pandas.DataFrame.apply()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.apply.html).

For å behandle [MGRS](https://en.wikipedia.org/wiki/Military_Grid_Reference_System) finnes det en egen pakke for det: [mgrs](https://pypi.org/project/mgrs/). Den kan også hjelpe deg med [DMS](https://en.wikipedia.org/wiki/Decimal_degrees). Eller så har sikkert [ESRI](https://www.esri.com) noe.

### Adresser
Filen [adresser.txt](data/adresser.txt) inneholder noen få adressser. Det er en vanlig tekstfil som enkelt kan åpnes med [open()](https://docs.python.org/3/library/functions.html#open). Deretter kan du bruke en geokoder for å få koordinater tilbake. [GeoPy](https://geopy.readthedocs.io/en/stable) er enkel og grei. Den geokoderen som heter [Nominatim](https://geopy.readthedocs.io/en/stable/#nominatim) er basert på [OpenStreetMap](https://www.openstreetmap.org) og krever ingen innlogging.

### Stridsmeldinger
Filen [stridsmelding.zip](data/stridsmelding.zip) inneholder 100 stridsmeldinger lagret i hver sin tekstfil.

Første steg er å hente ut tesksten slik at den kan prosesseres i [python](https://www.python.org/). Det er god støtte for zip-filer gjennom [zipfile](https://docs.python.org/3/library/zipfile.html) så det er ikke noe behov for å pakke ut dette manuelt. Her er to mulige fremgangsmåter:
* Den litt rotete måten er å pakke ut arkivet til en mappe med [ZipFile.extractall()](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile.extractall) for deretter å bla seg gjennom filene med [os.listdir()]() eller [os.scandir()]() og deretter åpne dem med [open()](https://docs.python.org/3/library/functions.html#open).
* Den litt mer elegante måten er å bruke [ZipFile.namelist()](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile.namelist) for å liste alt innholdet og deretter åpne filene direkte fra arkivet med [ZipFile.open()](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile.open).

For å hente posisjoner, dtg eller noe annet med et gitt mønster ut fra tekst er [regex](https://docs.python.org/3/howto/regex.html) et godt alternativ. Dette er et enkelt og kraftig verktøy som er veldig nyttig til mye rart.

For behandling av dato og tid er det [datetime](https://docs.python.org/3/library/datetime.html) som gjelder. For å gjøre om tekst til dato/tid kan du bruke [datetime.datetime.strptime()](https://docs.python.org/3/library/datetime.html#datetime.datetime.strptime). Hvis du er litt lat anbefaler jeg å ta en kikk på [dateutil](https://dateutil.readthedocs.io/en/stable/). Den kan gjøre livet ditt enklere.

## Presentasjon
Etter at data er trukket ut av filene og lagt i en ryddig struktur (f.eks [pandas](https://pandas.pydata.org/)) kan de rimelig enkelt plottes i et kart. Her er det mange alternativer. Her er noen:
* [ipyleaflet](https://ipyleaflet.readthedocs.io/en/latest/)
* [matplotlib](https://matplotlib.org/) / [cartopy](https://scitools.org.uk/cartopy/docs/latest/index.html)
* [plotly](https://plotly.com/)
* [seaborn](http://seaborn.pydata.org/)
* [deck.gl](https://deck.gl/)
* [kepler.gl](https://kepler.gl/)
* [Datashader](https://datashader.org/)
* [ArcGIS Notebooks in ArcGIS Pro](https://www.esri.com/arcgis-blog/products/arcgis-pro/analytics/introducing-arcgis-notebooks-in-arcgis-pro/)

Det aller enkleste er å eksportere kartet ditt til png/jpeg fra et av bibliotekene over.

Hvis du vil ta det et skritt lenger kan du legge kartet inn i et html-dokument slik at du kan legge inn mer informasjon som tekst eller noen annet for å lage et mer kompelett produkt. Da kan det også gjøres interaktivt ved å legge til litt javascript. Bilder kan legges inn i html-filer ved å bruke en kombinasjon av [io](https://docs.python.org/3/library/io.html) og [base64](https://docs.python.org/3/library/base64.html).

En annen mulighet er å skrive direkte til Word (f.eks [python-docx](https://python-docx.readthedocs.io/en/latest/)) eller Powerpoint (f.eks [python-pptx](https://python-pptx.readthedocs.io/en/latest/)).

Interaktive web-apper er også en mulighet. [Plotly Dash](https://plotly.com/dash/) gjør det ganske enkelt å lage en app.

## Installasjon
[Python](https://www.python.org/) er ofte en del av installasjonen til annen programvare som f.eks [ArcGIS Pro](https://www.esri.com/en-us/arcgis/products/arcgis-pro/overview). Hvis du ikke allerede har [python](https://www.python.org/) kan det lastes ned fra https://www.python.org/.

For å installere pakker utover det som finnes i [The Python Standard Library](https://docs.python.org/3/library/index.html#the-python-standard-library) kan du bruke enten [PyPI](https://pypi.org/) eller [Anaconda](https://anaconda.org/). Hvis du bruker Windows operativsystem er det ofte enklere å bruke [Anaconda](https://anaconda.org/) for å slippe kompilering. Hvis du uansett ønsker eller må bruke [PyPI](https://pypi.org/) på Windows kan det være mye hjelp i å hente ferdig kompilerte wheels fra [Christoph Gohlke](https://www.lfd.uci.edu/~gohlke/pythonlibs/).

Uansett hva du velger er det lurt å bruke mekanismer som isolerer hvert enkelt kjøremiljø. [Anaconda environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) for [conda](https://anaconda.org/) eller [virtualenv](https://virtualenv.pypa.io/) for [pip](https://pypi.org/).
