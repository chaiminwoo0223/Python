pokemon = { 
    "name": "리자몽",
    "level": 50,
    "elements": ["불꽃", "비행"],
    "skills": {"공격": "플레어드라이브", "특수공격": "화염방사"}
    }

for key in pokemon:
    if type(pokemon[key]) == list:
        for element in pokemon[key]:
            print(key, ":", element)
    elif type(pokemon[key]) == dict:
        for skill in pokemon[key]:
            print(key, ":", pokemon[key][skill])
    else:
        print(key, ":", pokemon[key])