select T1.firstName, T1.lastName, T2.city, T2.state from Person as T1
Left Join Address as T2 
on T1.personID=T2.personID
