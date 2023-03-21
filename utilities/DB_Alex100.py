import psycopg2.extensions
import psycopg2 
from psycopg2 import Error

class   DB_100:
    def __init__(self):
        self.__db : psycopg2.extensions.connection = None
        try:
            self.__db = psycopg2.connect(user="postgres",
                                 password="postgress",
                                     dbname = "alex_100",
                                     host = "localhost",
                                     port = "5432")


        except (Exception, Error) as error:
            print("Ошибка соединения с DB  :", error)
            if self.__db:
               self.__db.close()
               print("Соединение с PostgreSQL закрыто")
            # return None

    def __update_execute(self,_sql_query:str,return_data=False):
        try:            
            cursor=self.__db.cursor()
            cursor.execute(_sql_query)
            self.__db.commit()
            if return_data:
                return cursor.fetchone()
            return True
        except (Exception,Error) as error:
            print("Ошибка при обновлении БД:", error)
            return False


    def close(self):
        self.__db.close()
        

    def create_table(self, name_table:str, list_column:dict):
        SQL_query = f"""CREATE TABLE IF NOT EXISTS public.{name_table} ("""
        SQL_query += ",\n ".join(f"""{col.replace(':',' ')} {'COLLATE pg_catalog."default"' if 'character varying' in col else ''}"""  for col in list_column.values()) 
        SQL_query +=f""",\n  CONSTRAINT {name_table}_pkey PRIMARY KEY ({list(list_column.values())[0].split(':')[0]})
                        USING INDEX TABLESPACE azad
                        );  """        

        self.__update_execute("DROP TABLE IF EXISTS public.games;")
        return self.__update_execute(SQL_query) 


    def insertGames(self,name_table,data:list[dict]):
        for recordGame in data:
            if 'available' in recordGame:
                recordGame['available'] = True if recordGame['available'] == 'есть' else False
            headerGame=tuple(recordGame.keys())
            str_nameColumn=','.join(item for item in headerGame)
            dataGame=tuple(recordGame.values())
            SQL_query =f"""INSERT INTO public.{name_table} AS t({str_nameColumn}) 
                            SELECT * FROM (values {dataGame}) v({str_nameColumn}) 
                            WHERE NOT EXISTS  (SELECT FROM public.{name_table} AS d where d.{headerGame[0]} = v.{headerGame[0]}) 
                            on conflict do nothing returning {headerGame[0]};"""
            
            print (self.__update_execute(SQL_query,return_data=True))
            


    