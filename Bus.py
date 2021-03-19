import mysql.connector 
class Bus:
    def __init__(self):
        self.mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="brs"
        
       )
        if self.mydb.is_connected():
            print("Connection Successful")

            
    def admin(self):
            print("\t\t\t\t*****************************************************************")
            print("\t\t\t\t***************** Bus Reservation System Database ***************")
            print("\t\t\t\t*****************************************************************")
            print("\t\t\t\t----------------------      ADMIN  LOGIN   --------------------- ")
            while(True):
                  try:
                        print("")
                        self.uname=input("\t\t\tUsername : ")
                        self.passwd=input("\t\t\tPassword : ")
                        if(self.uname=="Admin") & (self.passwd=="Admin@123"):
                              print("\t\t\t================================")
                              print("\t\t\t\tLogin Successful")
                              break
                        raise ValueError
                  except ValueError:
                        print("\t\t\tRe - enter Username & Password ")

    def Add(self):
       print("\t\t\t************************************************************")
       self.id=int(input("Enter Id:"))
       self.name=input("Enter Name:")
       self.number=input("Enter Number:")
       self.type=input("Enter Type:")
       self.route=input("Enter Route:")
       self.date=input("Enter Date:")
       self.time=input("Enter Time:")
       self.source=input("Enter Source:")
       self.destination=input("Enter Destination:")
       query="INSERT into bus(id,name,number,type,route,date,time,source,destination)values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
       val=(self.id,self.name,self.number,self.type,self.route,self.date,self.time,self.source,self.destination)
       cur=self.mydb.cursor()
       try:
           cur.execute(query,val)
           self.mydb.commit()
           print("Data Entered Successfully")
       except:
               print("Query Error")
           
    def Update(self):
       print("\t\t\t************************************************************")
       self.id=input("\t\t Enter Bus id for UPDATE:")
       print("\t\t 1.Update Type \t\t\t 2.Update Route \n\t\t 3.Update Time \n\t\t 4.Update Source \n\t\t 5.Update Destination \n\t\t 6.Exit")
       while(True):
                  print("\t\t\t=====================================")
                  ch=int(input("\t\t Enter your Choice for Updation   : "))
                  print("\t\t\t=====================================")
                  if(ch==1):
                        self.type=input("\t\t\t Enter New Type:")
                        query="update Bus  set Type=%s where ID=%s"
                        cur=self.mydb.cursor()
                        val=(self.type,self.id)
                        try:
                              cur.execute(query,val)
                              self.mydb.commit()
                              print("\t\t\t -- New Type is Updated -- ")
                        except:
                              print("\t\t\t Oops ,Record Not Found !")

                              
                  if(ch==2):
                        self.rout=input("\t\t\t Enter New Rout:")
                        query="update Bus  set Route=%s where ID=%s"
                        cur=self.mydb.cursor()
                        val=(self.rout,self.id)
                        try:
                              cur.execute(query,val)
                              self.mydb.commit()
                              print("\t\t\t -- New Route is Updated -- ")
                        except:
                              print("\t\t\t Oops ,Record Not Found !")
      
        
                  if(ch==3):
                        self.time=input("\t\t\t Enter New Time for Bus: ")
                        query="update Bus set TIME=%s where ID=%s"
                        cur=self.mydb.cursor()
                        val=(self.time,self.id)
                        try:
                              cur.execute(query,val)
                              self.mydb.commit()
                              print(" \t\t\t-- New TimeName  is Updated --")                              
                        except:
                              print(" \t\t\tOops ,Record Not Found !")

                  if(ch==4):
                        self.source=input("\t\t\t Enter New Source for Bus: ")
                        query="update Bus set SOURCE=%s where ID=%s"
                        cur=self.mydb.cursor()
                        val=(self.source,self.id)
                        try:
                              cur.execute(query,val)
                              self.mydb.commit()
                              print(" \t\t\t-- New Source is Updated --")                              
                        except:
                              print(" \t\t\tOops ,Record Not Found !")


                  if(ch==5):
                        self.destination=input("\t\t\t Enter New Destination for Bus: ")
                        query="update Bus set DESTINATION=%s where ID=%s"
                        cur=self.mydb.cursor()
                        val=(self.destination,self.id)
                        try:
                              cur.execute(query,val)
                              self.mydb.commit()
                              print(" \t\t\t-- New Destination is Updated --")                              
                        except:
                              print(" \t\t\tOops ,Record Not Found !")

                  if(ch==6):
                        break 
            


    def show(self):
        query="SELECT * FROM Bus"
        try:
            cur=self.mydb.cursor()
            cur.execute(query)
        except:
            print("\t\t\tError in Query ")
        else:
            result=cur.fetchall()
            for row in result:
                print("\t\t\t",row)                      

 
    def delete(self):
        print("\t\t\t******************************************************************************************")
        self.id=input("\t\t\t Enter Bus Id for DELETE:")
        query="DELETE from Bus where Id=%s"
        cur=self.mydb.cursor()
        try:
            cur.execute(query,self.id)
        except:
              print("\t\t\t Record Not Found")
        else:
            self.mydb.commit()
            print("\t\t\tRecord Deleted Successfully")
    
   

     

b=Bus()
b.admin()
b.show()
b.delete()
b.show()
b.Update()
b.show()




         
        
       
