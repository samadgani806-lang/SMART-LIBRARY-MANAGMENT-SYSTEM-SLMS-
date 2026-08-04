def clearscreen ():
   import os
   os.system("cls"if os.name == "nt" else "clear")