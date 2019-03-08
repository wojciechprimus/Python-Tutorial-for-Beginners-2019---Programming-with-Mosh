import emoji
e=emoji.emojize


message=input("write a sentence in english using emoji(fire, thumbsup, thumbsdown) ")
words=message.split(' ')

emojis = {
    "fire" : '🔥',
    "thumbsup" : "👍",
    "thumbsdown" : "👎",
}

output=""

for i in words:
    output +=emojis.get(i,i) + " "

print(output)
