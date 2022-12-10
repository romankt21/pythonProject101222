from  rest_framework.views import APIView
from  rest_framework.response import Response

# class UserView(APIView):
#     def get(self, *args, **kwargs):
#         return Response('hello from get')
#
#     def post(self, *args, **kwargs):
#         print(self.request.data)
#         print(self.request.query_params.dict())
#         return Response('hello from post')
#
#     def put(self, *args, **kwargs):
#         return Response('hello from put')
#
#     def patch(self, *args, **kwargs):
#         return Response('hello from patch')
#
#     def delete(self, *args, **kwargs):
#         return Response('hello from delete')
#
# class UserTestView(APIView):
#     def get(self, *args, **kwargs):
#         print(kwargs)
#         return Response('ok')


users = [
    {"name":"Max", "age":15},
    {"name":"Ira", "age":20},
    {"name":"Olha", "age":30},
    {"name":"Ivan", "age":25},

]

class UserListCreateView(APIView):
    def get(self, *args, **kwargs):
        return Response(users)
    def post(self, *args, **kwargs):
        user = self.request.data
        users.append(user)
        return Response(user)


class UserRetrieveUpdateDestroyView(APIView):
    def get(self, *args, **kwargs):
        pk = kwargs.get('pk')

        try:
            user = users[pk]
        except IndexError:
            return Response('Not found')

        return Response(users[pk])

    def put(self, *args, **kwargs):
        new_user = self.request.data
        pk = kwargs.get('pk')
        try:
            user = users[pk]
        except IndexError:
            return Response('Not found')
        user['name'] = new_user['name']
        user['age'] = new_user['age']
        return Response(new_user)

    def delete(self, *args, **kwargs):
        pk = kwargs.get('pk')

        try:
            del users[pk]
        except IndexError:
            return Response('Not found')
        return Response('deleted')
