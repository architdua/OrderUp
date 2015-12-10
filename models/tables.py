db.define_table('request',
                Field('name', 'text', label="What's your name?"),
                Field('toName', 'text', label="Your friend's name?"),
                Field('toNumber', 'text', label="Your friend's number?"),
                Field('meal', requires=IS_IN_SET(['Burrito','Bowl','Taco','Salad']), label="Choose your meal!"),
                Field('rice',requires=IS_IN_SET(['white rice','brown rice','both white & brown rice','no rice']),
                      label="How about some rice?"),
                Field('beans',requires=IS_IN_SET(['black','pinto','both black & pinto','no beans']),
                      label="Fancy some beans?"),
                Field('meat',requires=IS_IN_SET(['chicken','steak','barbacoa', 'carnitas', 'fajitas (veggies)', 'no meat or veggies']),
                      label="Meat or veggies?"),
                Field('salsa',requires=IS_IN_SET(['mild','medium','hot','no salsa']),
                      label="ToMeto or ToMato salsa?"),
                Field('guac',requires=IS_IN_SET(['guac', 'no guac']),
                      label="Guacamole?"),
                Field('corn',requires=IS_IN_SET(['corn', 'no corn']),
                      label="Corn?"),
                Field('sourcream',requires=IS_IN_SET(['sour cream','no sour cream']),
                      label="Sour Cream?"),
                Field('cheese',requires=IS_IN_SET(['jack & white cheddar','no cheese']),
                      label="Cheese?"),
                Field('lettuce',requires=IS_IN_SET(['lettuce','no lettuce']),
                      label="Lettuce?"),
                Field('drink',requires=IS_IN_SET(['small soda', 'medium soda', 'large soda', 'Snapple','no drink']),
                      label="Any drinks?"),
                Field('chips',requires=IS_IN_SET(['chips','no chips']),
                      label="Chips on the side?"),
                Field('author', db.auth_user, default=auth.user_id),
                Field('additional_comments', 'text', label="Anything else?"),

            )

db.define_table('contacts',
                Field('name', 'text', label="Enter Name and Number"),
                Field('contact_id'),
                Field('user_id')
                )



db.request.author.readable = False;
db.request.author.writable = False;
