def weighted_ordered_greedy(objectsList,maxW):

    
    #trier les objets dans l'ordre croissant de leur poids(volume)
    objectsList.sort(key=weight_ordered)
    
    
    #On intialise la liste des solutions 
    solutions = []
    objectsList[0].append(0)
    solutions.append(objectsList[0])
    
    
    #intialise current weight
    cur_w = 0
    i = 0
    aprox_p = 0
    stop = False
    
    #tant qu'il y a de l'espace(volume) dans le sac a dos 
    #--> on met à chaque fois un exemplaire de l'objet du poids minimum dans le sac
    while (cur_w < maxW) and not(stop):
        
        if(cur_w + objectsList[i][1] <= maxW ):  # possible to add Object
            
            solutions[i][3]+=1              #on incremente le nombre d'exemplaire
            cur_w += objectsList[i][1]      #we update the current weight
            aprox_p += objectsList[i][2]    #we update the approximate solution
              

        else:
            stop = True
            
    
    return solutions,aprox_p
