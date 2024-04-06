"""
List of data types
"""

'''
IMMUTABLE TYPES: After creating, We CAN'T modify(We CAN'T add/We CAN'T update/We CAN'T delete)

- Numbers

- strings: To keep Collection of characters, Example: name, email-id, address, words, sentences etc
    -- Here automatically index will be assigned to each character
    
- tuple: To keep Collection of values, like list of names, list of email-ids etc
    -- we can store duplicate values
    -- Here automatically index will be assigned to each values
    
- frozenset: To keep Collection of values, like list of names, list of email-ids etc
    -- we can store only UNIQUE values
    -- No Index to each value
    
- bytes: 
    -- Here automatically index will be assigned to each character
    
MUTABLE TYPES: After creating, We CAN modify(We CAN add/We CAN update/We CAN delete)

- list: To keep Collection of values, like list of names, list of email-ids etc
    -- we can store duplicate values
    -- immutable if we need then we can make use of 'tuple'
    -- Here automatically index will be assigned to each values

- set: To keep Collection of values, like list of names, list of email-ids etc
    -- we can store only UNIQUE values
    -- immutable if we need then we can make use of 'frozenset'
    -- No Index to each value
    
- bytearray:
    -- immutable if we need then we can make use of 'bytearray'
    -- Here automatically index will be assigned to each character
    
-dictionary: To keep Collection of values, like list of names, list of email-ids etc
    -- we can store duplicate values
    -- Here we can provide index to each value called KEY/VALUE PAIR
'''
