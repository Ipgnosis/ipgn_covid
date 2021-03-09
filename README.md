Overview

The source of this data is Our World in Data (http://www.ourworldindata.org) which is a project based at the Oxford Martin School at the University of Oxford, UK.

The full data can be downloaded from https://ourworldindata.org/coronavirus-source-data in either .json, .csv or .xlsx format.


Data Structure

Dict - dict - list - dict

{
    "iso-code" : {
        key: value  (see 'Level 1' list below - up to 17 pairs, plus "data")
        "data": [
            {
                "date": string, iso format (YYYY-MM-DD),
                key: value  (see 'Level 2' list below - up to 41 pairs, including "date")
            }
        ]
    }
}


Level 0 data:

A set of key:value pairs.  The key is iso_code: a 3 letter, uppercase string (see below) corresponding to a country.


Level 1 data:

For each iso_code (country) key that exists, the values are contained in a dictionary.  The dict contains key:values that *may* be available:

    continent
    location
    population
    population_density
    median_age
    aged_65_older
    aged_70_older
    gdp_per_capita
    extreme_poverty
    cardiovasc_death_rate
    diabetes_prevalence
    female_smokers
    male_smokers
    handwashing_facilities
    hospital_beds_per_thousand
    life_expectancy
    human_development_index
    data
    
    
Level 2 data:

The Level 1 key 'data' has a value which is a list of dictionaries.  Each dictionary contains data for a given date for which data exists - not all dates have data in all countries.  Each date dictionary *may* contain the attributes listed below:

The attribute 'date' is a string in iso format (YYYY-MM-DD).
    
    date
    total_cases
    new_cases
    new_cases_smoothed
    total_deaths
    new_deaths
    new_deaths_smoothed
    total_cases_per_million
    new_cases_per_million
    new_cases_smoothed_per_million
    total_deaths_per_million
    new_deaths_per_million
    new_deaths_smoothed_per_million
    reproduction_rate
    icu_patients
    icu_patients_per_million
    hosp_patients
    hosp_patients_per_million
    weekly_icu_admissions
    weekly_icu_admissions_per_million
    weekly_hosp_admissions
    weekly_hosp_admissions_per_million
    total_tests
    new_tests
    total_tests_per_thousand
    new_tests_per_thousand
    new_tests_smoothed
    new_tests_smoothed_per_thousand
    positive_rate
    tests_per_case
    tests_units
    total_vaccinations
    people_vaccinated
    people_fully_vaccinated
    new_vaccinations
    new_vaccinations_smoothed
    total_vaccinations_per_hundred
    people_vaccinated_per_hundred
    people_fully_vaccinated_per_hundred
    new_vaccinations_smoothed_per_million
    stringency_index

ISO Country codes with corresponding attributes of continent and location:

iso_code    continent	    location

AFG	        Asia	        Afghanistan
AGO	        Africa	        Angola
ALB	        Europe	        Albania
AND	        Europe	        Andorra
ARE	        Asia	        United Arab Emirates
ARG	        South America	Argentina
ARM	        Asia	        Armenia
ATG	        North America	Antigua and Barbuda
AUS	        Oceania	        Australia
AUT	        Europe	        Austria
AZE	        Asia	        Azerbaijan
BDI	        Africa	        Burundi
BEL	        Europe	        Belgium
BEN	        Africa	        Benin
BFA	        Africa	        Burkina Faso
BGD	        Asia	        Bangladesh
BGR	        Europe	        Bulgaria
BHR	        Asia	        Bahrain
BHS	        North America	Bahamas
BIH	        Europe	        Bosnia and Herzegovina
BLR	        Europe	        Belarus
BLZ	        North America	Belize
BOL	        South America	Bolivia
BRA	        South America	Brazil
BRB	        North America	Barbados
BRN	        Asia	        Brunei
BTN	        Asia	        Bhutan
BWA	        Africa	        Botswana
CAF	        Africa	        Central African Republic
CAN	        North America	Canada
CHE	        Europe	        Switzerland
CHL	        South America	Chile
CHN	        Asia	        China
CIV	        Africa	        Cote d'Ivoire
CMR	        Africa	        Cameroon
COD	        Africa	        Democratic Republic of Congo
COG	        Africa	        Congo
COL	        South America	Colombia
COM	        Africa	        Comoros
CPV	        Africa	        Cape Verde
CRI	        North America	Costa Rica
CUB	        North America	Cuba
CYP	        Europe	        Cyprus
CZE	        Europe	        Czechia
DEU	        Europe	        Germany
DJI	        Africa	        Djibouti
DMA	        North America	Dominica
DNK	        Europe	        Denmark
DOM	        North America	Dominican Republic
DZA	        Africa	        Algeria
ECU	        South America	Ecuador
EGY	        Africa	        Egypt
ERI	        Africa	        Eritrea
ESP	        Europe	        Spain
EST	        Europe	        Estonia
ETH	        Africa	        Ethiopia
FIN	        Europe	        Finland
FJI	        Oceania	        Fiji
FRA	        Europe	        France
FSM	        Oceania	        Micronesia (country)
GAB	        Africa	        Gabon
GBR	        Europe	        United Kingdom
GEO	        Asia	        Georgia
GHA	        Africa	        Ghana
GIN	        Africa	        Guinea
GMB	        Africa	        Gambia
GNB	        Africa	        Guinea-Bissau
GNQ	        Africa	        Equatorial Guinea
GRC	        Europe	        Greece
GRD	        North America	Grenada
GTM	        North America	Guatemala
GUY	        South America	Guyana
HND	        North America	Honduras
HRV	        Europe	        Croatia
HTI	        North America	Haiti
HUN	        Europe	        Hungary
IDN	        Asia	        Indonesia
IND	        Asia	        India
IRL	        Europe	        Ireland
IRN	        Asia	        Iran
IRQ	        Asia	        Iraq
ISL	        Europe	        Iceland
ISR	        Asia	        Israel
ITA	        Europe	        Italy
JAM	        North America	Jamaica
JOR	        Asia	        Jordan
JPN	        Asia	        Japan
KAZ	        Asia	        Kazakhstan
KEN	        Africa	        Kenya
KGZ	        Asia	        Kyrgyzstan
KHM	        Asia	        Cambodia
KNA	        North America	Saint Kitts and Nevis
KOR	        Asia	        South Korea
KOS	        Europe	        Kosovo  (artificial iso_code - see note below)
KWT	        Asia	        Kuwait
LAO	        Asia	        Laos
LBN	        Asia	        Lebanon
LBR	        Africa	        Liberia
LBY	        Africa	        Libya
LCA	        North America	Saint Lucia
LIE	        Europe	        Liechtenstein
LKA	        Asia	        Sri Lanka
LSO	        Africa	        Lesotho
LTU	        Europe	        Lithuania
LUX	        Europe	        Luxembourg
LVA	        Europe	        Latvia
MAR	        Africa	        Morocco
MCO	        Europe	        Monaco
MDA	        Europe	        Moldova
MDG	        Africa	        Madagascar
MDV	        Asia	        Maldives
MEX	        North America	Mexico
MHL	        Oceania	        Marshall Islands
MKD	        Europe	        North Macedonia
MLI	        Africa	        Mali
MLT	        Europe      	Malta
MMR	        Asia	        Myanmar
MNE	        Europe	        Montenegro
MNG	        Asia	        Mongolia
MOZ	        Africa	        Mozambique
MRT	        Africa	        Mauritania
MUS	        Africa	        Mauritius
MWI	        Africa	        Malawi
MYS	        Asia	        Malaysia
NAM	        Africa	        Namibia
NER	        Africa	        Niger
NGA	        Africa	        Nigeria
NIC	        North America	Nicaragua
NLD	        Europe	        Netherlands
NOR	        Europe	        Norway
NPL	        Asia	        Nepal
NZL	        Oceania	        New Zealand
OMN	        Asia	        Oman
OWID_WRL	World           None    (exluded from data - see note below)
PAK	        Asia	        Pakistan
PAN	        North America	Panama
PER	        South America	Peru
PHL	        Asia	        Philippines
PNG	        Oceania	        Papua New Guinea
POL	        Europe	        Poland
PRT	        Europe	        Portugal
PRY	        South America	Paraguay
PSE	        Asia	        Palestine
QAT	        Asia	        Qatar
ROU         Europe	        Romania
RUS	        Europe	        Russia
RWA	        Africa	        Rwanda
SAU	        Asia	        Saudi Arabia
SDN	        Africa	        Sudan
SEN	        Africa	        Senegal
SGP	        Asia	        Singapore
SLB	        Oceania	        Solomon Islands
SLE	        Africa	        Sierra Leone
SLV	        North America	El Salvador
SMR	        Europe	        San Marino
SOM	        Africa	        Somalia
SRB	        Europe	        Serbia
SSD	        Africa	        South Sudan
STP	        Africa	        Sao Tome and Principe
SUR	        South America	Suriname
SVK	        Europe	        Slovakia
SVN	        Europe	        Slovenia
SWE	        Europe	        Sweden
SWZ	        Africa	        Eswatini
SYC	        Africa	        Seychelles
SYR	        Asia	        Syria
TCD	        Africa	        Chad
TGO	        Africa	        Togo
THA	        Asia	        Thailand
TJK	        Asia	        Tajikistan
TLS	        Asia	        Timor
TTO	        North America	Trinidad and Tobago
TUN	        Africa	        Tunisia
TUR	        Asia	        Turkey
TWN	        Asia	        Taiwan
TZA	        Africa	        Tanzania
UGA	        Africa	        Uganda
UKR	        Europe	        Ukraine
URY	        South America	Uruguay
USA	        North America	United States
UZB	        Asia	        Uzbekistan
VAT	        Europe	        Vatican
VCT	        North America	Saint Vincent and the Grenadines
VEN	        South America	Venezuela
VNM	        Asia	        Vietnam
VUT	        Oceania	        Vanuatu
WSM	        Oceania	        Samoa
YEM	        Asia	        Yemen
ZAF	        Africa	        South Africa
ZMB	        Africa	        Zambia
ZWE	        Africa	        Zimbabwe
None        None            International

The last country (International) is a catch-all bucket for cases that are not assignable to a specific country.  Note that the 'iso_code' and 'continent' are None.

Note that in the OWID data, Kosovo has a special iso_code (below).  So for consistency (see above), an artificial iso_code = KOS has been assigned to this data.

OWID_KOS	Europe	        Kosovo

Note also that the iso_code for 'the World' that will be exluded from the api for the time being, but can be aggregated if required:

OWID_WRL	World           None
