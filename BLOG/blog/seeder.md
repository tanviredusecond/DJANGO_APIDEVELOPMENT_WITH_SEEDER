from django_seed import Seed
from blog.models import Author,Article  
seeder = Seed.seeder()

seeder.add_entity(Author,100,{
    'name': lambda x:seeder.faker.name(),
    'email': lambda x:seeder.faker.email(),
})

seeder.add_entity(Article,200)




seeder.execute()