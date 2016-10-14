
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

Create a new notebook called `hw7.ipynb`. In the first cell write a short intro
about your data file(s) using markdown.

For this next part you are asked to write several functions, each function you
write should be a separate notebook cell. Make sure to add a short markdown
explanation beneath each one and add some comments in the function aswell. The
whole notebook should be understandable without knowledge of the exact
assignment.

### Function 1: `read_data(filename)`

The first function you should write is `read_data(filename)`. It should take
one argument, the filename you want to read, and return the data in the file
as a dictionary.

Reading a file in *Python* is easy, we also used it in the Lab last week to 
write the `load_words()` function. If you don't remember how to do it, take a
quick look at [Lab 6](https://progik.mprog.nl/labs/lab-6).

If you open up one of the `.csv` files or print the result of reading the lines,
you can see the structure of each file. You should notice that there are a lot
of values on each line, separated by commas, in fact that is exactly what
**CSV** stands for *Comma Separated Values*.

In order to actually use this data, we need to split each line into a list of
separate values. Fortunately *Python* has a built-in function for just that, 
unsuprisingly called `split()`. The documentation can be found
[here](https://docs.python.org/2/library/stdtypes.html#str.split).
Look at the examples listed there and see if you can figure out how it works.

The final dictionary you return should contain the country-codes as the *keys*
and the *values* should be the complete list of values for that country. Each
value in the list should be converted to a float, so it can be used to compute
with.

Make sure to add a call to your function at bottom the cell and print the result,
so you can see it actually works. Also add a new markdown cell and add a short 
explanation of what you did.

### Function 2: `subset_countries(data, country_list)`

Create a new code cell for the next function; `subset_countries(data, country_list)`.
This function should take 2 arguments; the dictionary containing the
data and and a list of country-codes. It should then return a new dictinoary,
containing only the data for the countries in the country-code list. The
structure of the dictionary should be exactly the same as the input dictionary,
only the number of key-value pairs should change. 

Don't forget to add a test at the bottom of the cell, where you print the
result. Try and see if the values you get are what you would expect. Also, don't
forget to add a short markdown description in a separate cell below.

### Function 3: `average_data(data)`

In the next code cell write a function called `average_data(data)`.
This function should take only one argument; the dictionary containing the data.
It should then return a single list, containing the average values for all
the country-code in the dictionary, computed separately for each year in the
data.

Again, add a test at the bottom and print the result. Make sure to verify that
the produced result is correct. If everything works, add a short description
in markdown.

### Function 4: `year_slice(data, start, end)`

This next function is called `year_slice(data, start, end)`. It should take
3 arguments; the dictionary containing the data, the starting year for the data
and the end year for the data. It should then cut the data for each
country-code to only start at the start year and end at the end year. Remember
that the default starting year is 1960 and the default end year is 2015. So for
instance, if you called the function like so
    
    year_slice(data, 1970, 2015)

you would expect the first 10 years to be removed from the data for each country.

Include a similar test in your code cell and print the result. Is it as you
expected? Add another short description in markdown below.

### Function 5: `compute_growth(data)`

The last function to write will be `compute_growth(data)`. It should take one
argument, the dictionary containing the data and compute the 
difference (or growth) of the data between each year, for all countries. If
the value of the data increases from one year to the next, the growth will be
postive for that year and the larger the value, the bigger the increase.
Conversely if the  value drops from one year to the next, the growth will be
negative. 

Also test this function, include a print and a short description in markdown.

## Starting the investigation

For the last part of this assignment you are asked to investigate the data
for yourself. Start by writing a short introduction to the part of the data
you are investigating and add a research question you would like to try and
answer using the data.

Plot your data in a graph using matplotlib and write down your findings in
markdown. Include at least 2 graphs and separate conclusions.

Zip the notebook folder, including any images you might want to add and the 
data files you created together in a single zip called `hw7.zip`. **Do not** add
the orginal `WDI_Data.csv`.


