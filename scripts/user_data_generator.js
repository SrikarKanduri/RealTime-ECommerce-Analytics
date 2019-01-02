

for(i=1;i<11;i++){ 
    db.users.insertOne( 
        {
            "name": "user"+i,
            "gender": "male",     
            "emailid": "user"+i+"@dic.com",     
            "phoneno": (9193771031+i).toString(),     
            "DOB": "11/24/2019",     
            "password": "srinu"+i,     
            "address": i+"Avent Ferry RD 104 APT Raleigh NC"
        }
    )
}