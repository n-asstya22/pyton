import requests
from classes import User
u1 = User()
u2 = User()
print(u1.posts,u1.subscriptions,u1.subscribers)
print(u2.posts,u2.subscriptions,u2.subscribers)
u1.sup(u2)
print(u1.posts,u1.subscriptions,u1.subscribers)
print(u2.posts,u2.subscriptions,u2.subscribers)




