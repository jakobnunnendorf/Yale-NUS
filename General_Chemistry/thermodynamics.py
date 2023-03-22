from datascience import *

path = "appendix_g.csv"

data_table = Table().read_table(path)

data_dictionary = {}

def to_float(value):
    value = value.replace(",", "")
    if value == "—":
        return None
    return float(value)

for row in data_table.rows:
    data_dictionary[row[0]] = {'dH': to_float(row[1]), 'dG': to_float(row[2]), 'dS': to_float(row[3])}

def parse_reaction(reaction):
    reactants, products = reaction.split("->")
    reactants = reactants.split("+")
    products = products.split("+")
    
    def parse_species(species_list):
        parsed_species = []
        for species in species_list:
            species = species.strip()
            coeff = 1
            compound = species
            if species[0].isdigit():
                for i, char in enumerate(species):
                    if not char.isdigit():
                        coeff = int(species[:i])
                        compound = species[i:]
                        break
            parsed_species.append((coeff, compound))
        return parsed_species

    reactants = parse_species(reactants)
    products = parse_species(products)
    
    return reactants, products

def get_dH(reaction):
    reactants, products = parse_reaction(reaction)
    dH = 0
    for coeff, reactant in reactants:
        dH -= coeff * data_dictionary[reactant]['dH']
    for coeff, product in products:
        dH += coeff * data_dictionary[product]['dH']
    print(f"dH: {dH}")
    return dH

def get_dG(reaction):
    reactants, products = parse_reaction(reaction)
    dG = 0
    for coeff, reactant in reactants:
        dG -= coeff * data_dictionary[reactant]['dG']
    for coeff, product in products:
        dG += coeff * data_dictionary[product]['dG']
    print(f"dG: {dG}")
    return dG

def get_dS(reaction):
    reactants, products = parse_reaction(reaction)
    dS = 0
    for coeff, reactant in reactants:
        dS -= coeff * data_dictionary[reactant]['dS']
    for coeff, product in products:
        dS += coeff * data_dictionary[product]['dS']
    print(f"dS: {dS}")
    return dS

def get_all_values(reaction):
    reactants, products = parse_reaction(reaction)
    
    dH_reactants = sum(coeff * data_dictionary[reactant]['dH'] for coeff, reactant in reactants)
    dH_products = sum(coeff * data_dictionary[product]['dH'] for coeff, product in products)
    dH = dH_products - dH_reactants

    dG_reactants = sum(coeff * data_dictionary[reactant]['dG'] for coeff, reactant in reactants)
    dG_products = sum(coeff * data_dictionary[product]['dG'] for coeff, product in products)
    dG = dG_products - dG_reactants

    dS_reactants = sum(coeff * data_dictionary[reactant]['dS'] for coeff, reactant in reactants)
    dS_products = sum(coeff * data_dictionary[product]['dS'] for coeff, product in products)
    dS = dS_products - dS_reactants

    def components_str(components, key='dH'):
        return " + ".join(f"({coeff}*{data_dictionary[compound][key]})" for coeff, compound in components)

    print("\n" + reaction + "\nStandard Thermodynamic Properties")
    print(f"Δ𝐻∘f(kJ mol^–1) = ({components_str(products, 'dH')} - {components_str(reactants, 'dH')})")
    print(f"Δ𝐻∘): {dH} kJ/mol"  + "\n")
    print(f"Δ𝐺∘f(kJ mol^–1) = ({components_str(products, 'dG')} - {components_str(reactants, 'dG')})")
    print(f"Δ𝐺∘): {dG} kJ/mol"  + "\n")
    print(f"𝑆°(J K^–1 mol^–1) = ({components_str(products, 'dS')} - {components_str(reactants, 'dS')})")
    print(f"𝑆°: {dS} J/(mol*K)" + "\n")
    print()
    return dH, dG, dS

def user_input_values():
    user_reaction = input("Please enter a reaction (e.g., I2(s) + Br2(l) -> 2IBr(g)): ")
    get_all_values(user_reaction)

def calculate_dG_with_temperature():
    user_reaction = input("Please enter a reaction (e.g., I2(s) + Br2(l) -> 2IBr(g)): ")
    temperature_C = float(input("Please enter the temperature in Celsius: "))
    temperature_K = temperature_C + 273.15
    
    dH, dG, dS = get_all_values(user_reaction)

    dG_temperature = dH - temperature_K * dS / 1000
    print(f"ΔG = ΔH° − TΔS°")
    print(f"ΔG = {dH} kJ/mol - ({temperature_K} K) * ({dS} J/(mol*K)) / 1000")
    print(f"ΔG: {dG_temperature} kJ/mol")

import math

def calculate_keq():
    user_reaction = input("Please enter a reaction (e.g., I2(s) + Br2(l) -> 2IBr(g)): ")
    temperature_C = float(input("Please enter the temperature in Celsius: "))
    temperature_K = temperature_C + 273.15

    dH, dG, dS = get_all_values(user_reaction)
    
    dG_temperature = dH - temperature_K * dS / 1000

    print(f"ΔG at {temperature_C}°C = ΔH° − TΔS°")
    print(f"ΔG = {dH} kJ/mol - ({temperature_K} K * {dS / 1000} kJ/(mol*K))")
    print(f"ΔG: {dG_temperature} kJ/mol\n")
    
    R = 8.31446261815324 # J/(mol*K)
    keq = math.exp(-dG_temperature * 1000 / (R * temperature_K))

    print(f"Keq = e^(-ΔG/RT)")
    print(f"Keq = e^(-({dG_temperature} kJ/mol * 1000) / ({R} J/(mol*K) * {temperature_K} K))")
    print(f"Keq: {keq}")

calculate_keq()




