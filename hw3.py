import data

#Part 1
def population_total(lista:list):
    sum = 0
    for county in lista:
        sum += county.population['2014 Population']
    return sum

#Part 2
def filter_by_state(lista:list,state:str):
    listb = []
    for county in lista:
        if county.state == state:
            listb.append(county)
    return listb

#Part 3

def population_by_education(lista:list, education:str)->float:
    population = 0
    for county in lista:
        if "2014 Population" in county.population and education in county.education:
            population += (county.population["2014 Population"] * (county.education[education]/100))
    return population

def population_by_ethnicity(lista:list, ethnicity:str)->float:
    population = 0
    for county in lista:
        if "2014 Population" in county.population and ethnicity in county.ethnicities:
            population += (county.population["2014 Population"] * (county.ethnicities[ethnicity] / 100))
    return population

def population_below_poverty_level(lista:list,poverty_lvl:str)->float:
    population = 0
    for county in lista:
        if "2014 Population" in county.population and poverty_lvl in county.income:
            population += (county.population["2014 Population"] * (county.income[poverty_lvl] / 100))
    return population

#Part 4
def percent_by_education(lista:list, education:str)->float:
    educated_pop = 0
    total_pop = 0
    for county in lista:
        if "2014 Population" in county.population and education in county.education:
            educated_pop += (county.population["2014 Population"] * (county.education[education] / 100))
            total_pop += county.population["2014 Population"]
    percent = (educated_pop / total_pop) * 100
    return percent

def percent_by_ethnicity(lista:list,ethnicity:str)->float:
    ethnic_pop = 0
    total_pop = 0
    for county in lista:
        if "2014 Population" in county.population and ethnicity in county.ethnicities:
            ethnic_pop += (county.population["2014 Population"] * (county.ethnicities[ethnicity] / 100))
            total_pop += county.population["2014 Population"]
    percent = (ethnic_pop / total_pop) * 100
    return percent

def percent_below_poverty_level(lista:list,poverty_lvl:str)->float:
    poverty_lvl_pop = 0
    total_pop = 0
    for county in lista:
        if "2014 Population" in county.population and poverty_lvl in county.income:
            poverty_lvl_pop += (county.population["2014 Population"] * (county.income[poverty_lvl] / 100))
            total_pop += county.population["2014 Population"]
    percent = (poverty_lvl_pop / total_pop) * 100
    return percent

#Part 5
def education_greater_than(lista:list, education:str, threshold:float)->list:
    listb = []
    for county in lista:
        if county.education[education] > threshold:
            listb.append(county)
    return listb

def education_less_than(lista:list, education:str, threshold:float)->list:
    listb = []
    for county in lista:
        if county.education[education] < threshold:
            listb.append(county)
    return listb

def ethnicity_greater_than(lista:list, ethnicity:str, threshold:float)->list:
    listb = []
    for county in lista:
        if county.ethnicities[ethnicity] > threshold:
            listb.append(county)
    return listb

def ethnicity_less_than(lista:list, ethnicity:str, threshold:float)->list:
    listb = []
    for county in lista:
        if county.ethnicities[ethnicity] < threshold:
            listb.append(county)
    return listb

def below_poverty_greater_than(lista:list, poverty_lvl:str, threshold:float)->list:
    listb = []
    for county in lista:
        if county.income[poverty_lvl] > threshold:
            listb.append(county)
    return listb

def below_poverty_less_than(lista:list, poverty_lvl:str, threshold:float)->list:
    listb = []
    for county in lista:
        if county.income[poverty_lvl] < threshold:
            listb.append(county)
    return listb


