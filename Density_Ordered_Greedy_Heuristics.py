def Density_ordered_greedy(objectsList,maxW):
    
    #Trier les objets dans l'ordre décroissant de leur rapport bénéfice/volume (Bi/Vi)
    objectsList.sort(key=ratio_b_over_v, reverse=True)
    
    #Initialise solution list
    solutions = []
    
    #newObject : boolean to check if an object "i" is added to the solution's list
    #Initial value = true 
    newObject=True
    
    
    #total_aprox_p = le bénéfice total des objets choisis comme solution 
    #C'est la solution approximative
    total_aprox_p = 0

    
    # i :  index in ObjetsList table
    i=0
    
    # j : index in solutions table
    j=-1
    
    # cur_w : le volume total des objets choisis comme solution 
    cur_w = 0
    
    
    
    #On parcourt le tableau des objets triés selon l'ordre décroissant de leur rapport bi/vi.
    #Pour chaque objet du tableau, on ajoute autant d'exemplaires que possible.
    
    while (cur_w < maxW) and (i<len(objectsList)):
        
        # S'il est possible d'ajouter l'objet avec l'index i dans la table "objectsList" (la table triée selon Bi/vi dans l'ordre décroissant) au sac
        if(cur_w + objectsList[i][1] <= maxW):
            
            #Si l'objet "i" est ajouté à la liste des solutions, On incrémente le nombre d'exemplaires de cet objet
            if not (newObject):
                solutions[j][3]+=1
                cur_w += objectsList[i][1]
                total_aprox_p += objectsList[i][2]
                
            # Sinon, nous ajoutons l'objet à la liste des solutions, avec le nombre d'exemplaires = 1.
            else:
                objectsList[i].append(1)
                solutions.append(objectsList[i])
                newObject=False
                j+=1
                cur_w += objectsList[i][1]
                total_aprox_p += objectsList[i][2]
            
               
                
        #S'il est pas possible de l'ajouter, on passe a l'objet suivant dans la table "objectsList"        
        else:
            i+=1
            newObject=True

    return solutions,total_aprox_p
