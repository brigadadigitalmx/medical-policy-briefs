
Bienvenido al Banco de datos médicos de la Brigada Digital MX. Nuestro objetivo es facilitar el acceso a datos médicos.

Estaremos procesando datos y subiéndolos diariamente para facililar su uso. El código que usamos para procesar los datos está disponible en nuestro repositorio en caso de que quieras reproducir o modificar el procedimiento.

# Literature tables

The Kaggle community is mining COVID-19 related papers and consolidating tables for several medical variables.

[Click here for details](kaggle-tables/README.md)

# Secretaría de Salud (México)

La Secretaría de Salud en México reporta diariamente el número de casos confirmados y sospechosos en formato PDF. Nosotros descargamos dicho archivo, extraemos las tablas y y las convertirmos a CSV. [Click aquí para ver el código.](https://github.com/brigadadigitalmx/policy-briefs-medical/tree/master/pipelines/mx-health-ministry)

Actualizado el 10 de abril de 2020.

 
* Casos confirmados (CSV). [Click para descargar](https://mx-covid-data.s3-us-west-1.amazonaws.com/mx-health-ministry/2020.04.10/confirmed.csv)
* Casos sospechosos (CSV). [Click para descargar](https://mx-covid-data.s3-us-west-1.amazonaws.com/mx-health-ministry/2020.04.10/suspected.csv)
* Datos agregados (confirmados y sospechosos) por estado con tasa de mortalidad. [Click para descargar](https://mx-covid-data.s3-us-west-1.amazonaws.com/mx-health-ministry/2020.04.10/cases_pop.csv)

Para obtener datos historicos, cambia la fecha en la URL. Los datos empezaron a ser capturados el 8 de abril de 2020.

## Fuentes originales

* [Secretaría de Salud (archivos en PDF)](https://www.gob.mx/salud/documentos/coronavirus-covid-19-comunicado-tecnico-diario-238449)


# Tasa de mortalidad por país

Tasa de mortalidad por país (por cada 100,000 habitantes). [Click aquí para ver el código.](https://github.com/brigadadigitalmx/policy-briefs-medical/tree/master/pipelines/mortality)

* [Click para descargar.](https://mx-covid-data.s3-us-west-1.amazonaws.com/mortality_rate.csv)

## Fuentes originales

* [Banco Mundial (población)](https://data.worldbank.org/indicator/sp.pop.totl)
* [JHU CSSE (Número de casos por país)](https://github.com/CSSEGISandData/COVID-19)

# Hospitalizaciones

* [California, EE.UU.](https://data.chhs.ca.gov/dataset/california-covid-19-hospital-data-and-case-statistics/resource/6cd8d424-dfaa-4bdd-9410-a3d656e1176e)


# Reporta un error

Si encontraste un error en los datos o en esta página. [Click aquí para reportarlo.](https://github.com/brigadadigitalmx/policy-briefs-medical/issues/new)

