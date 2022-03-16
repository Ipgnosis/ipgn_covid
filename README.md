# National Covid Data API
## Overview

The source of this data is Our World in Data (http://www.ourworldindata.org) which is a project based at the Oxford Martin School at the University of Oxford, UK.

The full data can be downloaded from https://ourworldindata.org/coronavirus-source-data in either .json, .csv or .xlsx format.


## Data Structure

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


## Level 0 data:

A set of key:value pairs.  The key is iso_code: a 3 letter, uppercase string (see below) corresponding to a country.


## Level 1 data:

For each iso_code (country) key that exists, the values are contained in a dictionary.  The dict contains key:values that *may* be available:

<table>
<tr>
<th>resource</th><th>data type</th>
</tr>
<tr>
<td>continent</td><td>string</td>
</tr>
<tr>
<td>location</td><td>string</td>
</tr>
<tr>
<td>population</td><td>float</td>
</tr>
<tr>
<td>population_density</td><td>float</td>
</tr>
<tr>
<td>median_age</td><td>float</td>
</tr>
<tr>
<td>aged_65_older</td><td>float</td>
</tr>
<tr>
<td>aged_70_older</td><td>float</td>
</tr>
<tr>
<td>gdp_per_capita</td><td>float</td>
</tr>
<tr>
<td>extreme_poverty</td><td>float</td>
</tr>
<tr>
<td>cardiovasc_death_rate</td><td>float</td>
</tr>
<tr>
<td>diabetes_prevalence</td><td>float</td>
</tr>
<tr>
<td>handwashing_facilities</td><td>float</td>
</tr>
<tr>
<td>hospital_beds_per_thousand</td><td>float</td>
</tr>
<tr>
<td>life_expectancy</td><td>float</td>
</tr>
<tr>
<td>human_development_index</td><td>float</td>
</tr>
<tr>
<td>female_smokers</td><td>float</td>
</tr>
<tr>
<td>male_smokers</td><td>float</td>
</tr>
<tr>
<td>data</td><td>list (see below)</td>
</tr>
</table>


## Level 2 data:

The value of the last Level 1 key: **'data'** is a list of dictionaries.  Each dictionary contains data for a given date for which data exists - not all dates have data in all countries.  Each date dictionary *may* contain the attributes listed below:

The attribute 'date' is a string in iso format (YYYY-MM-DD).

<table>
<tr>
<th>resource</th><th>data type</th>
</tr>
<tr>
<td>date</td><td>string</td>
</tr>
<tr>
<td>total_cases</td><td>float</td>
</tr>
<tr>
<td>new_cases</td><td>float</td>
</tr>
<tr>
<td>new_cases_smoothed</td><td>float</td>
</tr>
<tr>
<td>total_deaths</td><td>float</td>
</tr>
<tr>
<td>new_deaths</td><td>float</td>
</tr>
<tr>
<td>new_deaths_smoothed</td><td>float</td>
</tr>
<tr>
<td>total_cases_per_million</td><td>float</td>
</tr>
<tr>
<td>new_cases_per_million</td><td>float</td>
</tr>
<tr>
<td>new_cases_smoothed_per_million</td><td>float</td>
</tr>
<tr>
<td>total_deaths_per_million</td><td>float</td>
</tr>
<tr>
<td>new_deaths_per_million</td><td>float</td>
</tr>
<tr>
<td>new_deaths_smoothed_per_million</td><td>float</td>
</tr>
<tr>
<td>reproduction_rate</td><td>float</td>
</tr>
<tr>
<td>icu_patients</td><td>float</td>
</tr>
<tr>
<td>icu_patients_per_million</td><td>float</td>
</tr>
<tr>
<td>hosp_patients</td><td>float</td>
</tr>
<tr>
<td>hosp_patients_per_million</td><td>float</td>
</tr>
<tr>
<td>weekly_icu_admissions</td><td>float</td>
</tr>
<tr>
<td>weekly_icu_admissions_per_million</td><td>float</td>
</tr>
<tr>
<td>weekly_hosp_admissions</td><td>float</td>
</tr>
<tr>
<td>weekly_hosp_admissions_per_million</td><td>float</td>
</tr>
<tr>
<td>total_tests</td><td>float</td>
</tr>
<tr>
<td>new_tests</td><td>float</td>
</tr>
<tr>
<td>total_tests_per_thousand</td><td>float</td>
</tr>
<tr>
<td>new_tests_per_thousand</td><td>float</td>
</tr>
<tr>
<td>new_tests_smoothed</td><td>float</td>
</tr>
<tr>
<td>new_tests_smoothed_per_thousand</td><td>float</td>
</tr>
<tr>
<td>positive_rate</td><td>float</td>
</tr>
<tr>
<td>tests_per_case</td><td>float</td>
</tr>
<tr>
<td>tests_units</td><td>string</td>
</tr>
<tr>
<td>total_vaccinations</td><td>float</td>
</tr>
<tr>
<td>people_vaccinated</td><td>float</td>
</tr>
<tr>
<td>people_fully_vaccinated</td><td>float</td>
</tr>
<tr>
<td>new_vaccinations</td><td>float</td>
</tr>
<tr>
<td>new_vaccinations_smoothed</td><td>float</td>
</tr>
<tr>
<td>total_vaccinations_per_hundred</td><td>float</td>
</tr>
<tr>
<td>people_vaccinated_per_hundred</td><td>float</td>
</tr>
<tr>
<td>people_fully_vaccinated_per_hundred</td><td>float</td>
</tr>
<tr>
<td>new_vaccinations_smoothed_per_million</td><td>float</td>
</tr>
<tr>
<td>stringency_index</td><td>float</td>
</tr>
</table>


## ISO Country codes

With corresponding attributes of continent and location:

<table>
<tr>
<th>iso_code</th><th>continent</th><th>location</th>
</tr>
<tr>
<td>AFG</td><td>Asia</td><td>Afghanistan</td>
</tr>
<tr>
<td>AGO</td><td>Africa</td><td>Angola</td>
</tr>
<tr>
<td>ALB</td><td>Europe</td><td>Albania</td>
</tr>
<tr>
<td>AND</td><td>Europe</td><td>Andorra</td>
</tr>
<tr>
<td>ARE</td><td>Asia</td><td>United Arab Emirates</td>
</tr>
<tr>
<td>ARG</td><td>South America</td><td>Argentina</td>
</tr>
<tr>
<td>ARM</td><td>Asia</td><td>Armenia</td>
</tr>
<tr>
<td>ATG</td><td>North America</td><td>Antigua and Barbuda</td>
</tr>
<tr>
<td>AUS</td><td>Oceania</td><td>Australia</td>
</tr>
<tr>
<td>AUT</td><td>Europe</td><td>Austria</td>
</tr>
<tr>
<td>AZE</td><td>Asia</td><td>Azerbaijan</td>
</tr>
<tr>
<td>BDI</td><td>Africa</td><td>Burundi</td>
</tr>
<tr>
<td>BEL</td><td>Europe</td><td>Belgium</td>
</tr>
<tr>
<tr><td>BEN</td><td>Africa</td><td>Benin</td>
</tr>
<tr>
<td>BFA</td><td>Africa</td><td>Burkina Faso</td>
</tr>
<tr>
<td>BGD</td><td>Asia</td><td>Bangladesh</td>
</tr>
<tr>
<td>BGR</td><td>Europe</td><td>Bulgaria</td>
</tr>
<tr>
<td>BHR</td><td>Asia</td><td>Bahrain</td>
</tr>
<tr>
<td>BHS</td><td>North America</td><td>Bahamas</td>
</tr>
<tr>
<td>BIH</td><td>Europe</td><td>Bosnia and Herzegovina</td>
</tr>
<tr>
<td>BLR</td><td>Europe</td><td>Belarus</td>
</tr>
<tr>
<td>BLZ</td><td>North America</td><td>Belize</td>
</tr>
<tr>
<td>BOL</td><td>South America</td><td>Bolivia</td>
</tr>
<tr>
<td>BRA</td><td>South America</td><td>Brazil</td>
</tr>
<tr>
<td>BRB</td><td>North America</td><td>Barbados</td>
</tr>
<tr>
<td>BRN</td><td>Asia</td><td>Brunei</td>
</tr>
<tr>
<td>BTN</td><td>Asia</td><td>Bhutan</td>
</tr>
<tr>
<td>BWA</td><td>Africa</td><td>Botswana</td>
</tr>
<tr>
<td>CAF</td><td>Africa</td><td>Central African Republic</td>
</tr>
<tr>
<td>CAN</td><td>North America</td><td>Canada</td>
</tr>
<tr>
<td>CHE</td><td>Europe</td><td>Switzerland</td>
</tr>
<tr>
<td>CHL</td><td>South America</td><td>Chile</td>
</tr>
<tr>
<td>CHN</td><td>Asia</td><td>China</td>
</tr>
<tr>
<td>CIV</td><td>Africa</td><td>Cote d'Ivoire</td>
</tr>
<tr>
<td>CMR</td><td>Africa</td><td>Cameroon</td>
</tr>
<tr>
<td>COD</td><td>Africa</td><td>Democratic Republic of Congo</td>
</tr>
<tr>
<td>COG</td><td>Africa</td><td>Congo</td>
</tr>
<tr>
<td>COL</td><td>South America</td><td>Colombia</td>
</tr>
<tr>
<td>COM</td><td>Africa</td><td>Comoros</td>
</tr>
<tr>
<td>CPV</td><td>Africa</td><td>Cape Verde</td>
</tr>
<tr>
<td>CRI</td><td>North America</td><td>Costa Rica</td>
</tr>
<tr>
<td>CUB</td><td>North America</td><td>Cuba</td>
</tr>
<tr>
<td>CYP</td><td>Europe</td><td>Cyprus</td>
</tr>
<tr>
<td>CZE</td><td>Europe</td><td>Czechia</td>
</tr>
<tr>
<td>DEU</td><td>Europe</td><td>Germany</td>
</tr>
<tr>
<td>DJI</td><td>Africa</td><td>Djibouti</td>
</tr>
<tr>
<td>DMA</td><td>North America</td><td>Dominica</td>
</tr>
<tr>
<td>DNK</td><td>Europe</td><td>Denmark</td>
</tr>
<tr>
<td>DOM</td><td>North America</td><td>Dominican Republic</td>
</tr>
<tr>
<td>DZA</td><td>Africa</td><td>Algeria</td>
</tr>
<tr>
<td>ECU</td><td>South America</td><td>Ecuador</td>
</tr>
<tr>
<td>EGY</td><td>Africa</td><td>Egypt</td>
</tr>
<tr>
<td>ERI</td><td>Africa</td><td>Eritrea</td>
</tr>
<tr>
<td>ESP</td><td>Europe</td><td>Spain</td>
</tr>
<tr>
<td>EST</td><td>Europe</td><td>Estonia</td>
</tr>
<tr>
<td>ETH</td><td>Africa</td><td>Ethiopia</td>
</tr>
<tr>
<td>FIN</td><td>Europe</td><td>Finland</td>
</tr>
<tr>
<td>FJI</td><td>Oceania</td><td>Fiji</td>
</tr>
<tr>
<td>FRA</td><td>Europe</td><td>France</td>
</tr>
<tr>
<td>FSM</td><td>Oceania</td><td>Micronesia</td>
</tr>
<tr>
<td>GAB</td><td>Africa</td><td>Gabon</td>
</tr>
<tr>
<td>GBR</td><td>Europe</td><td>United Kingdom</td>
</tr>
<tr>
<td>GEO</td><td>Asia</td><td>Georgia</td>
</tr>
<tr>
<td>GHA</td><td>Africa</td><td>Ghana</td>
</tr>
<tr>
<td>GIN</td><td>Africa</td><td>Guinea</td>
</tr>
<tr>
<td>GMB</td><td>Africa</td><td>Gambia</td>
</tr>
<tr>
<td>GNB</td><td>Africa</td><td>Guinea-Bissau</td>
</tr>
<tr>
<td>GNQ</td><td>Africa</td><td>Equatorial Guinea</td>
</tr>
<tr>
<td>GRC</td><td>Europe</td><td>Greece</td>
</tr>
<tr>
<td>GRD</td><td>North America</td><td>Grenada</td>
</tr>
<tr>
<td>GUY</td><td>South America</td><td>Guyana</td>
</tr>
<tr>
<td>HND</td><td>North America</td><td>Honduras</td>
</tr>
<tr>
<td>HRV</td><td>Europe</td><td>Croatia</td>
</tr>
<tr>
<td>HTI</td><td>North America</td><td>Haiti</td>
</tr>
<tr>
<td>HUN</td><td>Europe</td><td>Hungary</td>
</tr>
<tr>
<td>IDN</td><td>Asia</td><td>Indonesia</td>
</tr>
<tr>
<td>IND</td><td>Asia</td><td>India</td>
</tr>
<tr>
<td>IRL</td><td>Europe</td><td>Ireland</td>
</tr>
<tr>
<td>IRN</td><td>Asia</td><td>Iran</td>
</tr>
<tr>
<td>IRQ</td><td>Asia</td><td>Iraq</td>
</tr>
<tr>
<td>ISL</td><td>Europe</td><td>Iceland</td>
</tr>
<tr>
<td>ISR</td><td>Asia</td><td>Israel</td>
</tr>
<tr>
<td>ITA</td><td>Europe</td><td>Italy</td>
</tr>
<tr>
<td>JAM</td><td>North America</td><td>Jamaica</td>
</tr>
<tr>
<td>JOR</td><td>Asia</td><td>Jordan</td>
</tr>
<tr>
<td>JPN</td><td>Asia</td><td>Japan</td>
</tr>
<tr>
<td>KAZ</td><td>Asia</td><td>Kazakhstan</td>
</tr>
<tr>
<td>KEN</td><td>Africa</td><td>Kenya</td>
</tr>
<tr>
<td>KGZ</td><td>Asia</td><td>Kyrgyzstan</td>
</tr>
<tr>
<td>KHM</td><td>Asia</td><td>Cambodia</td>
</tr>
<tr>
<td>KNA</td><td>North America</td><td>Saint Kitts and Nevis</td>
</tr>
<tr>
<td>KOR</td><td>Asia</td><td>South Korea</td>
</tr>
<tr>
<td>KOS</td><td>Europe</td><td>Kosovo (see note below)</td>
</tr>
<tr>
<td>KWT</td><td>Asia</td><td>Kuwait</td>
</tr>
<tr>
<td>LAO</td><td>Asia</td><td>Laos</td>
</tr>
<tr>
<td>LBN</td><td>Asia</td><td>Lebanon</td>
</tr>
<tr>
<td>LBR</td><td>Africa</td><td>Liberia</td>
</tr>
<tr>
<td>LBY</td><td>Africa</td><td>Libya</td>
</tr>
<tr>
<td>LCA</td><td>North America</td><td>Saint Lucia</td>
</tr>
<tr>
<td>LIE</td><td>Europe</td><td>Liechtenstein</td>
</tr>
<tr>
<td>LKA</td><td>Asia</td><td>Sri Lanka</td>
</tr>
<tr>
<td>LSO</td><td>Africa</td><td>Lesotho</td>
</tr>
<tr>
<td>LTU</td><td>Europe</td><td>Lithuania</td>
</tr>
<tr>
<td>LUX</td><td>Europe</td><td>Luxembourg</td>
</tr>
<tr>
<td>LVA</td><td>Europe</td><td>Latvia</td>
</tr>
<tr>
<td>MAR</td><td>Africa</td><td>Morocco</td>
</tr>
<tr>
<td>MCO</td><td>Europe</td><td>Monaco</td>
</tr>
<tr>
<td>MDA</td><td>Europe</td><td>Moldova</td>
</tr>
<tr>
<td>MDG</td><td>Africa</td><td>Madagascar</td>
</tr>
<tr>
<td>MDV</td><td>Asia</td><td>Maldives</td>
</tr>
<tr>
<td>MEX</td><td>North America</td><td>Mexico</td>
</tr>
<tr>
<td>MHL</td><td>Oceania</td><td>Marshall Islands</td>
</tr>
<tr>
<td>MKD</td><td>Europe</td><td>North Macedonia</td>
</tr>
<tr>
<td>MLI</td><td>Africa</td><td>Mali</td>
</tr>
<tr>
<td>MLT</td><td>Europe</td><td>Malta</td>
</tr>
<tr>
<td>MMR</td><td>Asia</td><td>Myanmar</td>
</tr>
<tr>
<td>MNE</td><td>Europe</td><td>Montenegro</td>
</tr>
<tr>
<td>MNG</td><td>Asia</td><td>Mongolia</td>
</tr>
<tr>
<td>MOZ</td><td>Africa</td><td>Mozambique</td>
</tr>
<tr>
<td>MRT</td><td>Africa</td><td>Mauritania</td>
</tr>
<tr>
<td>MUS</td><td>Africa</td><td>Mauritius</td>
</tr>
<tr>
<td>MWI</td><td>Africa</td><td>Malawi</td>
</tr>
<tr>
<td>MYS</td><td>Asia</td><td>Malaysia</td>
</tr>
<tr>
<td>NAM</td><td>Africa</td><td>Namibia</td>
</tr>
<tr>
<td>NER</td><td>Africa</td><td>Niger</td>
</tr>
<tr>
<td>NGA</td><td>Africa</td><td>Nigeria</td>
</tr>
<tr>
<td>NIC</td><td>North America</td><td>Nicaragua</td>
</tr>
<tr>
<td>NLD</td><td>Europe</td><td>Netherlands</td>
</tr>
<tr>
<td>NOR</td><td>Europe</td><td>Norway</td>
</tr>
<tr>
<td>NPL</td><td>Asia</td><td>Nepal</td>
</tr>
<tr>
<td>NZL</td><td>Oceania</td><td>New Zealand</td>
</tr>
<tr>
<td>OMN</td><td>Asia</td><td>Oman</td>
</tr>
<tr>
<td>PAK</td><td>Asia</td><td>Pakistan</td>
</tr>
<tr>
<td>PAN</td><td>North America</td><td>Panama</td>
</tr>
<tr>
<td>PER</td><td>South America</td><td>Peru</td>
</tr>
<tr>
<td>PHL</td><td>Asia</td><td>Philippines</td>
</tr>
<tr>
<td>PNG</td><td>Oceania</td><td>Papua New Guinea</td>
</tr>
<tr>
<td>POL</td><td>Europe</td><td>Poland</td>
</tr>
<tr>
<td>PRT</td><td>Europe</td><td>Portugal</td>
</tr>
<tr>
<td>PRY</td><td>South America</td><td>Paraguay</td>
</tr>
<tr>
<td>PSE</td><td>Asia</td><td>Palestine</td>
</tr>
<tr>
<td>QAT</td><td>Asia</td><td>Qatar</td>
</tr>
<tr>
<td>ROU</td><td>Europe</td><td>Romania</td>
</tr>
<tr>
<td>RUS</td><td>Europe</td><td>Russia</td>
</tr>
<tr>
<td>RWA</td><td>Africa</td><td>Rwanda</td>
</tr>
<tr>
<td>SAU</td><td>Asia</td><td>Saudi Arabia</td>
</tr>
<tr>
<td>SDN</td><td>Africa</td><td>Sudan</td>
</tr>
<tr>
<td>SEN</td><td>Africa</td><td>Senegal</td>
</tr>
<tr>
<td>SGP</td><td>Asia</td><td>Singapore</td>
</tr>
<tr>
<td>SLB</td><td>Oceania</td><td>Solomon Islands</td>
</tr>
<tr>
<td>SLE</td><td>Africa</td><td>Sierra Leone</td>
</tr>
<tr>
<td>SLV</td><td>North America</td><td>El Salvador</td>
</tr>
<tr>
<td>SMR</td><td>Europe</td><td>San Marino</td>
</tr>
<tr>
<td>SOM</td><td>Africa</td><td>Somalia</td>
</tr>
<tr>
<td>SRB</td><td>Europe</td><td>Serbia</td>
</tr>
<tr>
<td>SSD</td><td>Africa</td><td>South Sudan</td>
</tr>
<tr>
<td>STP</td><td>Africa</td><td>Sao Tome and Principe</td>
</tr>
<tr>
<td>SUR</td><td>South America</td><td>Suriname</td>
</tr>
<tr>
<td>SVK</td><td>Europe</td><td>Slovakia</td>
</tr>
<tr>
<td>SVN</td><td>Europe</td><td>Slovenia</td>
</tr>
<tr>
<td>SWE</td><td>Europe</td><td>Sweden</td>
</tr>
<tr>
<td>SWZ</td><td>Africa</td><td>Eswatini</td>
</tr>
<tr>
<td>SYC</td><td>Africa</td><td>Seychelles</td>
</tr>
<tr>
<td>SYR</td><td>Asia</td><td>Syria</td>
</tr>
<tr>
<td>TCD</td><td>Africa</td><td>Chad</td>
</tr>
<tr>
<td>TGO</td><td>Africa</td><td>Togo</td>
</tr>
<tr>
<td>THA</td><td>Asia</td><td>Thailand</td>
</tr>
<tr>
<td>TJK</td><td>Asia</td><td>Tajikistan</td>
</tr>
<tr>
<td>TLS</td><td>Asia</td><td>Timor</td>
</tr>
<tr>
<td>TTO</td><td>North America</td><td>Trinidad and Tobago</td>
</tr>
<tr>
<td>TUN</td><td>Africa</td><td>Tunisia</td>
</tr>
<tr>
<td>TUR</td><td>Asia</td><td>Turkey</td>
</tr>
<tr>
<td>TWN</td><td>Asia</td><td>Taiwan</td>
</tr>
<tr>
<td>TZA</td><td>Africa</td><td>Tanzania</td>
</tr>
<tr>
<td>UGA</td><td>Africa</td><td>Uganda</td>
</tr>
<tr>
<td>UKR</td><td>Europe</td><td>Ukraine</td>
</tr>
<tr>
<td>URY</td><td>South America</td><td>Uruguay</td>
</tr>
<tr>
<td>USA</td><td>North America</td><td>United States</td>
</tr>
<tr>
<td>UZB</td><td>Asia</td><td>Uzbekistan</td>
</tr>
<tr>
<td>VAT</td><td>Europe</td><td>Vatican</td>
</tr>
<tr>
<td>VCT</td><td>North America</td><td>Saint Vincent and the Grenadines</td>
</tr>
<tr>
<td>VEN</td><td>South America</td><td>Venezuela</td>
</tr>
<tr>
<td>VNM</td><td>Asia</td><td>Vietnam</td>
</tr>
<tr>
<td>VUT</td><td>Oceania</td><td>Vanuatu</td>
</tr>
<tr>
<td>WSM</td><td>Oceania</td><td>Samoa</td>
</tr>
<tr>
<td>YEM</td><td>Asia</td><td>Yemen</td>
</tr>
<tr>
<td>ZAF</td><td>Africa</td><td>South Africa</td>
</tr>
<tr>
<td>ZMB</td><td>Africa</td><td>Zambia</td>
</tr>
<tr>
<td>ZWE</td><td>Africa</td><td>Zimbabwe</td>
</tr>
</table>

There also exists a synthetic 'country' (International) as a catch-all bucket for cases that are not assignable to a specific country.

<table>
<tr>
<th>iso_code</th>
<th>continent</th>
<th>location</th>
</tr>
<tr>
<td>None</td>
<td>None</td>
<td>International</td>
</tr>
</table>

Since 'iso_code' is None (Null), this data has been exluded for the time being.  The data currently comprises:
* total_cases < 1,000
* total_deaths < 20.

Note that in the OWID data, Kosovo has a special iso_code (below).  So for consistency (see above), an artificial iso_code = KOS has been assigned to this data.

<table>
<tr>
<th>iso_code</th>
<th>continent</th>
<th>location</th>
</tr>
<tr>
<td>OWID_KOS</td>
<td>Europe</td>
<td>Kosovo</td>
</tr>
</table>

Note also that the iso_code for 'the World' that will be exluded from the api for the time being, but can be aggregated if required:

<table>
<tr>
<th>iso_code</th>
<th>continent</th>
<th>location</th>
</tr>
<tr>
<td>OWID_WRL</td>
<td>World</td>
<td>None</td>
</tr>
</table>
