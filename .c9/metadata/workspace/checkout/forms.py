{"filter":false,"title":"forms.py","tooltip":"/checkout/forms.py","undoManager":{"mark":4,"position":4,"stack":[[{"start":{"row":0,"column":0},"end":{"row":6,"column":53},"action":"insert","lines":["from django import forms","from .models import Post","","class BlogPostForm(forms.ModelForm):","    class Meta:","        model=Post","        fields = ('title', 'content', 'tag', 'image')"],"id":1}],[{"start":{"row":1,"column":23},"end":{"row":1,"column":24},"action":"remove","lines":["t"],"id":2},{"start":{"row":1,"column":22},"end":{"row":1,"column":23},"action":"remove","lines":["s"]},{"start":{"row":1,"column":21},"end":{"row":1,"column":22},"action":"remove","lines":["o"]},{"start":{"row":1,"column":20},"end":{"row":1,"column":21},"action":"remove","lines":["P"]}],[{"start":{"row":1,"column":20},"end":{"row":1,"column":21},"action":"insert","lines":["O"],"id":3},{"start":{"row":1,"column":21},"end":{"row":1,"column":22},"action":"insert","lines":["r"]},{"start":{"row":1,"column":22},"end":{"row":1,"column":23},"action":"insert","lines":["d"]},{"start":{"row":1,"column":23},"end":{"row":1,"column":24},"action":"insert","lines":["e"]},{"start":{"row":1,"column":24},"end":{"row":1,"column":25},"action":"insert","lines":["r"]}],[{"start":{"row":0,"column":0},"end":{"row":6,"column":53},"action":"remove","lines":["from django import forms","from .models import Order","","class BlogPostForm(forms.ModelForm):","    class Meta:","        model=Post","        fields = ('title', 'content', 'tag', 'image')"],"id":4},{"start":{"row":0,"column":0},"end":{"row":6,"column":143},"action":"insert","lines":["from django import forms","from .models import Order","","class OrderForm(forms.ModelForm):","    class Meta:","        model=Order","        fields = ('full_name', 'phone_number', 'country', 'postcode', 'town_or_city', 'street_address_1', 'street_address_2', 'county', 'date')"]}],[{"start":{"row":6,"column":141},"end":{"row":6,"column":142},"action":"remove","lines":["'"],"id":5},{"start":{"row":6,"column":140},"end":{"row":6,"column":141},"action":"remove","lines":["e"]},{"start":{"row":6,"column":139},"end":{"row":6,"column":140},"action":"remove","lines":["t"]},{"start":{"row":6,"column":138},"end":{"row":6,"column":139},"action":"remove","lines":["a"]},{"start":{"row":6,"column":137},"end":{"row":6,"column":138},"action":"remove","lines":["d"]},{"start":{"row":6,"column":136},"end":{"row":6,"column":137},"action":"remove","lines":["'"]},{"start":{"row":6,"column":135},"end":{"row":6,"column":136},"action":"remove","lines":[" "]},{"start":{"row":6,"column":134},"end":{"row":6,"column":135},"action":"remove","lines":[","]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":6,"column":134},"end":{"row":6,"column":134},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":true,"wrapToView":true},"firstLineState":0},"timestamp":1534945959282,"hash":"ac2195a3880c4aea06b3fba5ce23c5c5674dbfff"}