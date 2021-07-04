import graphene
from graphene_django import DjangoObjectType
from myapp.models import UserModel, CategoryModel, ProductModel


class UserType(DjangoObjectType):
    class Meta:
        model = UserModel


# class CategoryType(DjangoObjectType):
#     class Meta:
#         model = CategoryModel


# class ProductType(DjangoObjectType):
#     class Meta:
#         model = ProductModel


class Query(graphene.ObjectType):
    users = graphene.List(UserType)

    def resolve_users(self, info):
        return UserModel.objects.all()


# class Query(graphene.ObjectType):
#     categorys = graphene.List(CategoryType)

#     def resolve_categorys(self, info):
#         return CategoryModel.objects.all()


# class Query(graphene.ObjectType):
#     products = graphene.List(ProductType)

#     def resolve_products(self, info):
#         return ProductModel.objects.all()


class CreateUser(graphene.Mutation):
    id = graphene.Int()
    first_name = graphene.String()
    last_name = graphene.String()
    mobile = graphene.String()
    email = graphene.String()
    password = graphene.String()

    class Arguments:
        first_name = graphene.String()
        last_name = graphene.String()
        mobile = graphene.String()
        email = graphene.String()
        password = graphene.String()

    def mutate(self, info, first_name, last_name, mobile,email , password):
        user = UserModel(first_name=first_name, last_name=last_name, mobile=mobile,email=email, password=password)
        user.save()

        return CreateUser(
            id=user.id,
            first_name=user.first_name,
            last_name=user.last_name,
            mobile=user.mobile,
            email=user.email,
            password=user.password,
        )        


# class CreateCategory(graphene.Mutation):
#     id = graphene.Int()
#     category_name = graphene.String()    

#     class Arguments:
#         category_name = graphene.String()
       
#     def mutate(self, info, category_name):
#         category = CategoryModel(category_name=category_name)
#         category.save()

#         return CreateCategory(
#             id=category.id,
#             category_name=category.category_name,
#         )        


# class CreateProduct(graphene.Mutation):
#     id = graphene.Int()
#     product_name = graphene.String()    

#     class Arguments:
#         product_name = graphene.String()
       
#     def mutate(self, info, product_name):
#         product = ProductModel(product_name=product_name)
#         product.save()

#         return CreateProduct(
#             id=product.id,
#             product_name=product.product_name,
#         )        


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    # create_category = CreateCategory.Field()
    # create_product = CreateProduct.Field()


schema = graphene.Schema(
    query=Query,
    mutation=Mutation
)