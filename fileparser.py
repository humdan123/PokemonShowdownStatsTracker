import messenger

def main(p1, p2):
    OPPOSING = "The opposing "
    f = open("input.txt", "r")

    lines = f.readlines()
    roster1 = False
    roster2 = False
    done1 = False
    done2 = False
    death = ""
    pokemon1 = ""
    pokemon2 = ""
    for line in lines:
        kill = ""
        oppose = False
        #print("iteration")
        if ("Go! " in line) and (not (":" in line)):
            if ("(" in line):
                mon1 = line.find("(")
                l = -3
            else:
                mon1 = line.find(" ")
                l = -2
            pokemon1 = line[mon1+1:l]
        elif ("sent out " in line) and (not (":" in line)):
            if ("(" in line):
                mon2 = line.find("(")
                l = -3
                r = 1
            else:
                mon2 = line.find("ut ")
                l = -2
                r = 3
            pokemon2 = line[mon2+r:l]

        if ("'s team:" in line) and ((not roster1) or (not roster2)):
            #print("reached")
            index = line.find("'s team:")
            name = line[:index]
            
            if name == p1:
                roster1 = True
            elif name == p2:
                roster2 = True
        
        elif (roster1 and (not done1)):
            roster = line
            j = roster.find(" / ")
            mons = []
            while j > 0:
                #print(j)
                mons.append(roster[:j])
                roster = roster[(j+3):]
                j = roster.find(" / ")
            mons.append(roster[:-1])
            for pokemon in mons:
                messenger.add_game(pokemon, p1)
            print(mons)
            done1 = True


        elif (roster2 and (not done2)):
            roster = line
            j = roster.find(" / ")
            mons = []
            while j > 0:
                mons.append(roster[:j])
                roster = roster[(j+3):]
                j = roster.find(" / ")
            mons.append(roster[:-1])
            for pokemon in mons:
                messenger.add_game(pokemon, p2)
            print(mons)
            done2 = True
            


        if ("fainted!" in line) and (not (":" in line)):
            death = line
            if line[0:len(OPPOSING)] == OPPOSING:
                death = line[len(OPPOSING):]
                oppose = True #opposing pokemon died, pokemonk1 got kill
            else:
                oppose = False #ally pokemon died, pokemonk2 got kill
        

            if oppose:
                kill = pokemon1
                death = pokemon2
                messenger.add_death(death, p2)
                messenger.add_kill(kill, p1)
            else:
                kill = pokemon2
                death = pokemon1
                messenger.add_death(death, p1)
                messenger.add_kill(kill, p2)
            
            
            print((death, kill))

    f.close()




