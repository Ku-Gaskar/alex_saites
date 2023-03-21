
from DB_Alex100 import DB_100
from Exel_Alex100 import Exel_100

PATH_EXEL_100='d:\\Work_AVERS\\Python\\alex_saites\\dbase\\Games_Product.xlsx'


def  main(): 
    dbase: DB_100 = DB_100()
    if not dbase:  return
    product : Exel_100 = Exel_100(PATH_EXEL_100)
    if not product: 
        dbase.close()
        return
    list_column : dict = product.readHeader('games')
    dbase.create_table('games',list_column)
    data=product.readData(list_column)
    if not data:
        dbase.close()
        product.close()
        return
    dbase.insertGames('games',data)
    dbase.close()
    product.close()
    print ("Ok")

if __name__ == '__main__' :
    main()
