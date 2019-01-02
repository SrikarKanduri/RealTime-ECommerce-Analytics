for (i = 1; i <= 30; i++) {
    db.products.insertOne(
        { 
            "pname": "product" + i, 
            "cname": "company" + i % 10, 
            "cost": 500 + i % 500, 
            "description": "description" + i 
        }
    )
}