from django.test import TestCase
import markdown

# Create your tests here.

html = markdown.markdown("**![image](https://i.pinimg.com/280x280_RS/cb/b2/80/cbb280fa8c687cf3b137df878bf82d08.jpg)**")
print(html)