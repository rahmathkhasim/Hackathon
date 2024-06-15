#we are storing places in the dictionary
dic={
    "hyderabad":["medilife","yashoda","sri"],
    "mancherial":["kims","healthcare","evya"],
    "khamam":["sunshine","medicare","agarwal"]
}
# hyderabad hospitals in the dic1
dic1={
    "medilife":{
    "name":"medilife",
    "type":"multispeciality",
    "noofbeds":30,
    "price":30000,
    "rating":4.5
},"yashoda":{
    "name":"yashoda",
    "type":"multispeciality",
    "noofbeds":25,
    "price":23000,
    "rating":4.1
},"sri":{
    "name":"sri",
    "type":"multispeciality",
    "noofbeds":33,
    "price":40000,
    "rating":3.5
}}
# macherial hospitals in the dic1
dic3={
"kims":{
    "name":"kims",
    "type":"multispeciality",
    "noofbeds":30,
    "price":30000,
    "rating":4.5
},"healthcare":{
    "name":"healthcare",
    "type":"multispeciality",
    "noofbeds":30,
    "price":30000,
    "rating":4.5
},"evya":{
    "name":"evya",
    "type":"multispeciality",
    "noofbeds":30,
    "price":30000,
    "rating":4.5
}}
# khammam hospitals in the dic1
dic4={
"sunshine":{
    "name":"sunshine",
    "type":"multispeciality",
    "noofbeds":30,
    "price":30000,
    "rating":4.5
},"medicare":{
    "name":"medicare",
    "type":"multispeciality",
    "noofbeds":30,
    "price":2000,
    "rating":4.5
},"agarwal":{
    "name":"agarwal",
    "type":"multispeciality",
    "noofbeds":10,
    "price":15000,
    "rating":3.8
}
}
#patient names for the specific hospital
dic2={
    "medilife":{
        "john":{
            "id":123,
            "name":"john",
            "age":20,
            "gender":"male",
            "bloodgroup":"A+"
            },
        "ram":{
            "id":124,
            "name":"ram",
            "age":20,
            "gender":"male",
            "bloodgroup":"A+"
            }
        },
    "yashoda":{
        "john":{
            "id":123,
            "name":"john",
            "age":20,
            "gender":"male",
            "bloodgroup":"A+"
            },
        "ram":{
            "id":124,
            "name":"ram",
            "age":20,
            "gender":"male",
            "bloodgroup":"A+"
            }
        },
    "sri":{
        "john":{
            "id":123,
            "name":"john",
            "age":20,
            "gender":"male",
            "bloodgroup":"A+"
            },
        "ram":{
            "id":124,
            "name":"ram",
            "age":20,
            "gender":"male",
            "bloodgroup":"A+"
            }
    },
    "kims":{
        "john":{
            "id":123,
            "name":"john",
            "age":20,
            "gender":"male",
            "bloodgroup":"A+"
            },
        "ram":{
            "id":124,
            "name":"ram",
            "age":20,
            "gender":"male",
            "bloodgroup":"A+"
            }
    },
    "healthcare":{
        "john":{
            "id":123,
            "name":"john",
            "age":20,
            "gender":"male",
            "bloodgroup":"A+"
            },
        "ram":{
            "id":124,
            "name":"ram",
            "age":20,
            "gender":"male",
            "bloodgroup":"A+"
            }
    },
    "evya":{
        "john":{
            "id":123,
            "name":"john",
            "age":20,
            "gender":"male",
            "bloodgroup":"A+"
            },
        "ram":{
            "id":124,
            "name":"ram",
            "age":20,
            "gender":"male",
            "bloodgroup":"A+"
            }
    },
    "sunshine":{
        "john":{
            "id":123,
            "name":"john",
            "age":20,
            "gender":"male",
            "bloodgroup":"A+"
            },
        "ram":{
            "id":124,
            "name":"ram",
            "age":20,
            "gender":"male",
            "bloodgroup":"A+"
            }
    },
    "medicare":{
        "john":{
            "id":123,
            "name":"john",
            "age":20,
            "gender":"male",
            "bloodgroup":"A+"
            },
        "ram":{
            "id":124,
            "name":"ram",
            "age":20,
            "gender":"male",
            "bloodgroup":"A+"
            }
    },
    "agarwal":{
        "john":{
            "id":123,
            "name":"john",
            "age":20,
            "gender":"male",
            "bloodgroup":"A+"
            },
        "ram":{
            "id":124,
            "name":"ram",
            "age":20,
            "gender":"male",
            "bloodgroup":"A+"
            }
    }
    
}

print("welcome",end=" ")
#we are taking 3 cities
city=["hyderabad","mancherial","khamam"]
print("the cities are:")
for ele in city:
    print(ele,end=" ")
print("")
x=input("enter the city name:")
for ele,val in dic.items():
    if ele ==x:
        print("the hospitals are:")
        for i in val:
            print(i)
#sorting acc to the user
if x=="hyderabad":
    p=input("you want sort anything type yes or no:")
    if p=="yes":
        m=input("do you sort by bed?")
        if m=="yes":
            z=dict(sorted(dic1.items(), key=lambda x:x[1]["noofbeds"],reverse=True))
            print(z)
        q=input("do you sort by price?")
        if q=="yes":
            z=dict(sorted(dic1.items(), key=lambda x:x[1]["price"]))
            print(z)
        n=input("do you sort by rating?")
        if n=="yes":
            z=dict(sorted(dic1.items(), key=lambda x:x[1]["rating"],reverse=True))
            print(z)
        e=input("do you sort by name?")
        if e=="yes":
            z=dict(sorted(dic1.items(), key=lambda x:x[1]["name"]))
            print(z)
               
elif x=="mancherial":
    p=input("you want sort anything type yes or no:")
    if p=="yes":
        m=input("do you sort by bed?")
        if m=="yes":
            z=dict(sorted(dic3.items(), key=lambda x:x[1]["noofbeds"],reverse=True))
            print(z)
        q=input("do you sort by price?")
        if q=="yes":
            z=dict(sorted(dic3.items(), key=lambda x:x[1]["price"]))
            print(z)
        n=input("do you sort by rating?")
        if n=="yes":
            z=dict(sorted(dic3.items(), key=lambda x:x[1]["rating"],reverse=True))
            print(z)
        e=input("do you sort by names?")
        if e=="yes":
            z=dict(sorted(dic3.items(), key=lambda x:x[1]["name"]))
            print(z)
           
else:
    p=input("you want sort anything type yes or no:")
    if p=="yes":
        m=input("do you sort by bed?")
        if m=="yes":
            z=dict(sorted(dic4.items(), key=lambda x:x[1]["noofbeds"],reverse=True))
            print(z)
        q=input("do you sort by price?")
        if q=="yes":
            z=dict(sorted(dic4.items(), key=lambda x:x[1]["price"]))
            print(z)
        n=input("do you sort by rating?")
        if n=="yes":
            z=dict(sorted(dic4.items(), key=lambda x:x[1]["rating"],reverse=True))
            print(z)
        e=input("do you sort by names?")
        if e=="yes":
            z=dict(sorted(dic4.items(), key=lambda x:x[1]["name"]))
            print(z)
x=input("enter the hospital:")
print()
for ele,val in dic1.items():
    if ele==x:
        for r,k in val.items():
            print(r,k)
want=input("do you want all patient details type yes or no:")
if want=="no":
    y=input("patient name")
    print("the patient details are:")
    for ele,val in dic2.items():
        if ele==x:
            for r,k in val.items():
                if r==y:
                    for s,l in k.items():
                        print(s,l)
else:
    for ele,val in dic2.items():
        if ele==x:
            for r,k in val.items():
                    print(r,k)

    