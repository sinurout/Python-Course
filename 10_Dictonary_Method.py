mydict = {
    "nihar":"is a good boy",
    "biswa":"handsome boy",
    "marks":[34,55,87],
    "anotherdict":{'nehu':'good'},
    1:2
}
print(list(mydict.keys()))
print(list(mydict.values()))
print(list(mydict.items()))

update_dict ={
    "teju":"very good",
    "adi":"ver good",
    "nihar":"happy"

}
mydict.update(update_dict)
print(mydict)

print(mydict.get("nihar2"))