from graphene import relay, ObjectType, Schema, Int
from graphene_django.types import DjangoObjectType, ObjectType 
from graphene_django.filter import DjangoFilterConnectionField
from .models import User

# Create a GraphQL type for the User model
class UserType(DjangoObjectType):
  class Meta:
    model = User
    interfaces = (relay.Node, )
    filter_fields="__all__"
    fields = "__all__"
     
class Query(ObjectType):
  user = relay.Node.Field(UserType)
  users = DjangoFilterConnectionField(UserType)


schema = Schema(query=Query)