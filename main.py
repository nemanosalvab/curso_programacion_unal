import json
import matplotlib.pyplot as plt



#with iteritems
# for i_key, i_value in d1.items():
#     print(f"{i_key}: {i_value} \n")
#     try:
#         for j_key, j_value in i_value.items():
#             print("\n")
#             print(f"{j_key}: {j_value} \n")
#             for k_key, k_value in j_value.items():
#                 print(f"{k_key}: {k_value} \n")
#     except Exception as e:
#         print(e)


# --------------------------1. Agrupar por genero a los personajes---------------------------------

def gender_groupby(data, generos):
    #Get all genders with set and dict comprenhension //https://michaeliscoding.com/how-to-create-a-list-of-unique-items-with-a-comprehension-in-python/

    #lista de personajes agrupados por generos
    generos = {genero : [] for genero in generos}
    for genero in generos:
        generos.update({genero : [value for key, value in data.items() if value['gender'] == genero]})
    
    print(generos)


#---------------------------2. Especies agrupadas por genero-----------------------------------------

def species_gender_groupby(data, generos, especies):
    #lista de personajes agrupados por especies
    especies_cantidad_genero = [] # {genero : 0 for genero in generos}
    for key , genero in enumerate(generos):
        tmp = []
        for especie in especies:
            tmp.append(len([value['species'] for key, value in data.items() if value['gender'] == genero and value['species'] == especie ]))
        especies_cantidad_genero.append(tmp)


    fig, ax_especies = plt.subplots()
    ax_especies.plot(especies, especies_cantidad_genero[0] , label="Female")
    ax_especies.plot(especies, especies_cantidad_genero[1] , label="Male")
    ax_especies.legend()
    plt.show()


#----------------------3 Diagrama pie, barras por especies en general (no agrupados)-------------------
# Creating plot
#---- TO DO ---------------------------------------
def diagram_species(data, generos, especies):
    fig = plt.figure(figsize =(10, 7))
    plt.bar(range(len(especies)), [len(value) for value in especies], tick_label=especies)
    plt.show()
    

#---------------------------------4 Edades agrupados por generos---------------------------------------

def gender_ages(data):
    #create list of two lists 0: ages, 1: gender
    edades_generos = tuple([(registro['gender'], registro['age']) for key, registro in data.items()])

    # Creating histogram -- flatten list :D
    fig, ax_mujeres_edades = plt.subplots(figsize =(10, 7))

    # Set title 
    ax_mujeres_edades.set_title("Distribucion edades hombres") 
    
    # adding labels 
    ax_mujeres_edades.set_xlabel('Edad') 
    ax_mujeres_edades.set_ylabel('Num. de Personajes') 


    hombres = [int(lis[-1]) for lis in edades_generos if lis[0] == 'Male' and lis[1] != 'Unknown']
    ax_mujeres_edades.hist(hombres, bins = range(min(hombres), max(hombres)+20, 5))


    fig, ax_hombres_edades = plt.subplots(figsize =(10, 7))
    # Set title 
    ax_hombres_edades.set_title("Distribucion edades mujeres") 
    
    # adding labels 
    ax_hombres_edades.set_xlabel('Edad') 
    ax_hombres_edades.set_ylabel('Num. de Personajes') 


    muejeres =  [int(lis[-1]) for lis in edades_generos if lis[0] == 'Female' and lis[1] != 'Unknown']
    ax_hombres_edades.hist(muejeres , bins = range(min(muejeres ), max(muejeres )+20, 5))
    plt.show()


#-----------------------------------5 Edades sin agrupacion---------------------------------------------
def ages_only(data, edades):
    edades = {edad : [] for edad in edades if edad != 'Unknown'}

    for edad in edades:
        edades.update({edad : [value['age'] for key, value in data.items() if value['age'] == edad]})

    # Creating histogram -- flatten list :D
    edades = [int(val) for item in edades.values() for val in item]

    fig, ax_edades = plt.subplots(figsize =(10, 7))

    # Set title 
    ax_edades.set_title("Distribucion edades") 
    
    # adding labels 
    ax_edades.set_xlabel('Edad') 
    ax_edades.set_ylabel('Num. de Personajes') 
    ax_edades.hist(edades, bins = range(min(edades), max(edades), 10))

    # show plot https://joserzapata.github.io/courses/python-ciencia-datos/visualizacion/
    plt.show()


def load_data():
    try:
        # Opening JSON file
        f = open('data.json')
        # returns JSON object as a dictionary
        data = json.load(f)
    except Exception as e:
        print(e)

    #If we want to convert the list into an iterable list of tuples 
    for key, value in enumerate(data):
        print(f"{key}: {value} \n")

    #Dict comprenhension
    return {key: data[key] for key in range(len(data))}


def main():
    data = load_data()

    #Set var type for unique values use
    generos = list({value['gender'] for key, value in data.items()})
    especies = list({value['species'] for key, value in data.items()})
    edades = list({value['age'] for key, value in data.items()})

    gender_groupby(data, generos)
    species_gender_groupby(data, generos, especies)
    diagram_species(data, generos, especies)
    gender_ages(data)
    ages_only(data, edades)


main()