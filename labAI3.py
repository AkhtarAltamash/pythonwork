import json

# x = '{"Name":"Altamash", "Age":22}'
# y = json.loads(x)
# print(y["Name"])
#
# d = {"Name":"Altamash", "Age":22}
# print(json.dumps(d))
############################################

# d = {"Name":"Altamash", "Age":22}
# print(json.dumps(d))

data = {
"Human Name":"ALI",
"Human CNIC":4250194750253,
"Human Blood Group":"A+",
"Human Region":"Muslim",
"Human Country":"Pakistan",

    "part":[
        {"hand":2,"left":"!!","right":"??"}
        {"Face":"Mouth""eyes""nose"}
    ]
}

print(json.dumps(data,indent=2,sort_keys=True))