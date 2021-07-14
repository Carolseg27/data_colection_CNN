import sqlite3
class BancoDados:

    # this stores the accelerometer data coming from the mpu 
    def create_table_acc():
        
        con = sqlite3.connect('acc_mpu.db') 
        cursor = con.cursor() 
        cursor.execute(
            
        ''' 
        CREATE TABLE IF NOT EXISTS acc_mpu( 
        Ax TEXT NOT NULL, 
        Ay TEXT NOT NULL, 
        Az TEXT NOT NULL,
        Time TEXT NOT NULL
        ); 
        '''
        )
        con.close()


    def insert_val_acc(ax, ay, az, time):
        
        con = sqlite3.connect('acc_mpu.db') 
        cursor = con.cursor()
        cursor.execute(

        """ 
        INSERT INTO acc_mpu (Ax,Ay,Az,Time) 
        VALUES (?,?,?,?) 
        """,(ax, ay, az, time))

        con.commit() 
        cursor.close()
        con.close()
        

    def get_value_acc():
        
        con = sqlite3.connect('acc_mpu.db') 
        cursor = con.cursor()
        cursor.execute(
        
        """
        SELECT * FROM acc_mpu;
        """)

        elements = cursor.fetchall()
        
        return elements

    # this stores the gyroscope data coming from the mpu  

    def create_table_gyr():
        
        con = sqlite3.connect('gyr_mpu.db') 
        cursor = con.cursor() 
        cursor.execute(
            
        ''' 
        CREATE TABLE IF NOT EXISTS gyr_mpu( 
        Ax TEXT NOT NULL, 
        Ay TEXT NOT NULL, 
        Az TEXT NOT NULL,
        Time TEXT NOT NULL
        ); 
        '''
        )
        con.close()


    def insert_val_gyr(ax, ay, az, time):
        
        con = sqlite3.connect('gyr_mpu.db') 
        cursor = con.cursor()
        cursor.execute(

        """ 
        INSERT INTO gyr_mpu (Ax,Ay,Az,Time) 
        VALUES (?,?,?,?) 
        """,(ax, ay, az, time))

        con.commit() 
        cursor.close()
        con.close()
        

    def get_value_gyr():
        
        con = sqlite3.connect('gyr_mpu.db') 
        cursor = con.cursor()
        cursor.execute(
        
        """
        SELECT * FROM gyr_mpu;
        """)

        elements = cursor.fetchall()
        
        return elements