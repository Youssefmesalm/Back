import graphene
from graphene_django.types import DjangoObjectType, ObjectType 
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.forms.mutation import DjangoModelFormMutation
from .models import User
from .forms import UserCreationForm, UserEditForm

# Create a GraphQL type for the User model
class CustomNode(graphene.relay.Node):
  class Meta:
    name ="Node"
  @staticmethod
  def to_global_id(self,type,id):
    return id
  @staticmethod
  def get_node_from_global_id(self,context,info,global_id, only_type=None):
    node = super().get_node_from_global_id(global_id, context, info, only_type)
    
    if node:
     return node
    get_node = getattr(only_type, "get_node", None)
    
    if get_node:
      return get_node(global_id,context, info)

class UserType(DjangoObjectType):
  class Meta:
    model = User
    interfaces = (CustomNode, )
    filter_fields="__all__"
    fields = "__all__"
  @classmethod
  def get_node(self,info,id): 
    user = User.objects.get(id=id)
    return user
     
class UserQuery(ObjectType):
  user = graphene.relay.Node.Field(UserType)
  users = DjangoFilterConnectionField(UserType)

class UserEdit(DjangoModelFormMutation):
  user = graphene.Field(UserType)
  class Meta:
    form_class = UserEditForm
    input_field_name = "data"
    
class UserCreate(DjangoModelFormMutation):
  class Meta:
    form_class= UserCreationForm
  user= graphene.Field(UserType)
  
    
class Mutation(graphene.ObjectType):
  UserCreate = UserCreate.Field()
  UserEdit = UserEdit.Field()
schema = graphene.Schema(query=UserQuery, mutation=Mutation)