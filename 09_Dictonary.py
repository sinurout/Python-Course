mydict = {
    "nihar":"is a good boy",
    "biswa":"handsome boy",
    "marks":[34,55,87],
    "anotherdict":{'nehu':'good'}
}
print(mydict["nihar"])
# Change dictonary value
mydict['nihar']='bad boy'
print(mydict)

print(mydict["anotherdict"]['nehu'])