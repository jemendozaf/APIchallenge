# -------Formula fibonacci

 
def fibonacci_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]

JsonResultItemCount = 16 #--Esta valor corresponde al total de elementos en nuestro diccionario de datos

Excel_Code= 'xyz'  #--Reemplaza valor de Code xyz que corresonde segun el excel APIChallengeFile.xlsx

Excel_Sequence= 0    #--Reemplaza el valor 0 por el Sequence que corresonde segun el excel APIChallengeFile.xlsx
 


#-------- Calcular el location integrando la formula de fibonacci

Location =  float(
        
        str(fibonacci_memo(JsonResultItemCount+Excel_Sequence)).replace(Excel_Code,'')
        
        )  -32.8608
 

print(Location)


#--------------------------------------------