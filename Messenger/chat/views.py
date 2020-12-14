from django.shortcuts import render
from django.utils.safestring import mark_safe
import redis
import json
var = 5
pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
r = redis.Redis(connection_pool=pool)
r.set("site", "Flash")
r.set("Contacts", " ")
def chat_func(request):
    return render(request, 'chat/index.html')


def room(request, room_name):
    user = request.user.username
    contacts = str(r.get("Contacts")) + '|' + user + '|'
    r.set("Contacts", contacts)
    names = contacts.split('|')
    final_contacts = []
    forbidden = "'"
    for name in names:
        if len(name)>=1:
            if name[0].isalpha() and not(forbidden in name) and not(name in final_contacts) :
                final_contacts.append(name)
    print("Final contacts: ", final_contacts)
    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name)),
        'username' : mark_safe(json.dumps(request.user.username)),
        'array_history' : mark_safe(var),
        'user' : user,
        'contacts' : final_contacts,
    })
