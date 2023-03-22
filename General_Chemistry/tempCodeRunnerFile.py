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