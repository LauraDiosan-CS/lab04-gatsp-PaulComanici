from PRB.GA import GA
from PRB.readData import readData2, readData1


def run():
    print("Fisier: \n")
    filename = input()
    if (filename != ""):
        print("Populatie = \n")
        populationSize = int(input())
        print("nr de generatii = \n")
        noGenerations = int(input())
        if filename == "hardE.txt":
            graph = readData2("Data/"+filename)
        else:
            graph = readData1("Data/"+filename)
        ga = GA(populationSize, graph)
        ga.initialization()
        contor = 0
        gen = contor + 1
        contor +=1
        best = ga.bestChromosome()
        print("generation " + str(gen) + " " + str(best.repres) + " fitness " + str(best.fitness))
        while (contor < noGenerations):
            ga.oneGenerationElitism()
            best = ga.bestChromosome()
            gen = contor + 1
            print("generation " + str(gen) + " " + str(best.repres) + " fitness "+str(best.fitness))
            contor += 1

run()