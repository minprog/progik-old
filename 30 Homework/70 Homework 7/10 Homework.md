
# Investigating the World Development Indicators

For this weeks homework we'll be working with data from the world bank,
listing many different development indicators for many countries. This means
you can find anything from CO2 emissions to the number of internet connections, 
listed per country from 1960 until 2015. The description from the the world
bank reads:

*The primary World Bank collection of development indicators, compiled from
officially-recognized international sources. It presents the most current and
accurate global development data available, and includes national, regional and
global estimates.*

And the list of topics they give includes:

* Agriculture & Rural Development
* Aid Effectiveness
* Climate Change
* Economy & Growth
* Education
* Energy & Mining
* Environment
* External Debt
* Financial Sector
* Gender
* Health
* Infrastructure
* Labor & Social Protection
* Poverty
* Private Sector
* Public Sector
* Science & Technology
* Social Development
* Trade
* Urban Development

So a very interesting and diverse set of data to work it. Your job this week
will be to investigate, combine and plot a part of that data!

## Getting started

The datafile can be found on the world bank site, follow the link below.

[Data file](http://databank.worldbank.org/data/download/WDI_csv.zip)

Make sure to unpack the zip. You will only need the `WDI_Data.csv` file.

We wrote a small python program to extract information from the `WDI_Data`
file. The program will do some simple conversions, fill in missing values and
can filter what parts of the data you want specifically. The new data will then
be written to a seperate file.

The program can be downloaded [here](wdi_data.py).

*The program should be stored in the same folder as `WDI_Data.csv` in order for
it to work.*

There are several commands you can use with this program. First we will try
and select an interesting topic to investigate. For this we will use the `-k`
option, which allows you to enter keywords on which to search the data
descriptions. For example, if we wanted to search all data containing the term
**CO2**, we would try

    python wdi_data.py -k CO2
    
    EN.ATM.CO2E.EG.ZS       CO2 intensity (kg per kg of oil equivalent energy use)
    EN.ATM.CO2E.GF.KT       CO2 emissions from gaseous fuel consumption (kt)
    EN.ATM.CO2E.GF.ZS       CO2 emissions from gaseous fuel consumption (% of total)
    EN.ATM.CO2E.KD.GD       CO2 emissions (kg per 2010 US$ of GDP) 
    ...

and get a list of all the relevant datacodes. Now say we wanted the "CO2
emissions form gaseous fuel consumption (kilotons)" then we would use the `-c`
option to select the code to write to a new file. In this case that would be

    python wdi_data.py -c EN.ATM.CO2E.GF.KT

which would produce a new file called EN.ATM.CO2E.GF.KT.csv (feel free to
rename it to something a little more clear) containing the emission data from
all the countries from 1960 to 2015.

Each line in this file will be the data for a country. The first column will be
the country-code for that country. If you want to know what all the country-codes
are, you can use the `-s` command, as in

    python wdi_data.py -s
    
    ABW     Aruba
    ADO     Andorra
    AFG     Afghanistan
    AGO     Angola
    ALB     Albania
    ...

So if you wanted to compare the emissions for Aruba and Angola, you would look
at the lines containing the codes *ABW* and *AGO*.

Start the homework this week by searching through the data file using `-k` and
creating some smaller files using `-c` for parts of the data you think are
interesting.

## Working with the data

Work in a notebook called `hw7.ipynb`. Each function you write should be a
separate cell.

### Function 1

Reading file into a dictionary

### Function 2

Average value for several countries

### Function 3

Creating a new subset of countries dict

### Function 4

Slicing all data from a certain year until a certain year

### Function 5

Computing the growth / difference between each year for all the data

## Starting the investigation

Write a research question. Plot some data. Write a conclusion in markdown. Go.

