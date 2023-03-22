def components_str(components, key='dH'):
        return " + ".join(f"({coeff}*{data_dictionary[compound][key]})" for coeff, compound in components)