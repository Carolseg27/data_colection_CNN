import sqlite3
class BancoDados:

    def create_table_mpu():
        
        con = sqlite3.connect('angles.db') 
        cursor = con.cursor() 
        cursor.execute(
            
        ''' 
        CREATE TABLE IF NOT EXISTS dados_mpu( 
        Ax TEXT NOT NULL, 
        Ay TEXT NOT NULL, 
        Az TEXT NOT NULL,
        Time TEXT NOT NULL
        ); 
        '''
        )
        con.close()


    def insert_val_mpu(ax, ay, az, time):
        
        con = sqlite3.connect('angles.db') 
        cursor = con.cursor()
        cursor.execute(

        """ 
        INSERT INTO dados_mpu (Ax,Ay,Az,Time) 
        VALUES (?,?,?,?) 
        """,(ax, ay, az, time))

        con.commit() 
        cursor.close()
        con.close()
        

    def get_value_mpu():
        
        con = sqlite3.connect('angles.db') 
        cursor = con.cursor()
        cursor.execute(
        
        """
        SELECT * FROM dados_mpu;
        """)

        elements = cursor.fetchall()
        
        return elements