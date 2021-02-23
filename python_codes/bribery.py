inital = [2,1,3,4,5,6,7,8]

final =  [1,2,5,3,7,8,6,4]

count = 0
chaos_counter = 0


for i in inital:
    inital_index = inital.index(i)
    if j in final:
        final_index = final.index(j)

    if inital_index == final_index or abs(inital_index-final_index) <= 2:
        if inital_index < final_index:
            count += abs(inital_index-final_index)
        #print(inital[inital_index])
        print(final[final_index])
        pass
    
    else:
        print("Too chaotic")
        chaos_counter += 1
        break

if chaos_counter == 0:
    print(count)
        