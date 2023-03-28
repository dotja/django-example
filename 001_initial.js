db.createUser(
    {
        user: "user",
        pwd: "password",
        roles:[
            {
                role: "readWrite",
                db:   "flashcard_db"
            }
        ]
    }
);
db.createCollection('cards');