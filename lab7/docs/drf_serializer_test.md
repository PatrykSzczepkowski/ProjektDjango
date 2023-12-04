from polls.models import Team
from polls.serializers import TeamSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
 
team = Team(name='Awokado', country='Poland')
team.save() 
serializer = TeamSerializer(team)
serializer.data #{'name': 'Awokado', 'country': 'Poland'}
content = JSONRenderer().render(serializer.data)
content #b'{"name":"Awokado","country":"Poland"}'
import io
stream = io.BytesIO(content)
data = JSONParser().parse(stream)
deserializer = TeamSerializer(data=data) 
deserializer.is_valid() #True
deserializer.save() #<Team: Awokado>
deserializer.data #{'name': 'Awokado', 'country': 'Poland'}

#2 przyklad
from polls.models import Stanowisko
from polls.serializers import StanowiskoModelSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

st = Stanowisko(nazwa='Grafik') 
st #<Stanowisko: Grafik>
st.save()
serializer = StanowiskoModelSerializer(st) 
serializer.data #{'id': 3, 'nazwa': 'Grafik'}
content #b'{"id":3,"nazwa":"Grafik"}
stream = io.BytesIO(content)
data = JSONParser().parse(stream)
deserializer = StanowiskoModelSerializer(data=data) 
deserializer.is_valid() #True
deserializer.save() #<Team: Awokado>
deserializer.data #{'name': 'Awokado', 'country': 'Poland'}